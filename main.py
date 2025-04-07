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
            loader = TextLoader(filepath, encoding="utf-8")
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
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        openai_api_base=api_base,
        model_name="meta-llama/llama-4-maverick:free"  # or the correct DeepSeek model identifier
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    chat_history_file = os.path.join("reference_files", "chat_history.txt")

    print("🤖 Ask me anything about your reference files!\n")

    while True:
        query = input("📝 You: ")
        if query.lower() in ["exit", "quit", "bye"]:
            print("👋 Goodbye! Thanks a lot for using this program -Rxzy")
            break

        # Read chat history from file
        try:
            with open(chat_history_file, "r") as file:
                chat_history = file.readlines()[-10:]  # Keep the last 10 lines
                chat_history = "".join(chat_history)
        except FileNotFoundError:
            chat_history = ""

        # Create a prompt template with conversation history
        prompt = f"""
        Conversation History:
        {chat_history}
        
        Query: {query}
        
        Answer:
        """

        # Get the response from the LLM
        result = qa_chain(prompt)

        # Write the conversation to the file
        with open(chat_history_file, "a") as file:
            file.write(f"You: {query}\n")
            file.write(f"Model: {result['result']}\n")

        print("\n📖 Answer:")
        print(result["result"])
        print("\n🔎 Source(s):")
        for doc in result["source_documents"]:
            print(f"- {doc.metadata.get('source', 'Unknown')}")

if __name__ == "__main__":
    run_qa()
