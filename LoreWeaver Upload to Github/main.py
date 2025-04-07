import os
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader, PyMuPDFLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings 
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
api_base = "https://openrouter.ai/api/v1"

# Load documents from folder
def load_documents(folder_path):
    documents = []
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)

        if filename.endswith(".txt"):
            loader = TextLoader(filepath)
        elif filename.endswith(".pdf"):
            loader = PyMuPDFLoader(filepath)
        else:
            continue  # Skip unknown files

        try:
            documents.extend(loader.load())
        except Exception as e:
            print(f"❌ Error loading {filename}: {e}")
    return documents

# Run the full question-answering system
def run_qa():
    print("📚 Loading documents...")
    docs = load_documents("reference_files")

    if not docs:
        print("❌ No documents loaded. Make sure the folder has valid .txt or .pdf files.")
        return  # Exit before trying anything else

    print("🧠 Creating embeddings...")
    embeddings = HuggingFaceEmbeddings()

    vectorstore = FAISS.from_documents(docs, embeddings)
    # rest of code...

    retriever = vectorstore.as_retriever()

    llm = ChatOpenAI(
        openai_api_key=api_key,
        openai_api_base=api_base,
        model_name="gpt-3.5-turbo"  # or "mistral", "gpt-4", etc.
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    print("🤖 Ask me anything about your reference files!\n")

    while True:
        query = input("📝 You: ")
        if query.lower() in ["exit", "quit", "bye"]:
            print("👋 Goodbye!")
            break

        result = qa_chain(query)
        print("\n📖 Answer:")
        print(result["result"])
        print("\n🔎 Source(s):")
        for doc in result["source_documents"]:
            print(f"- {doc.metadata.get('source', 'Unknown')}")

if __name__ == "__main__":
    run_qa()
