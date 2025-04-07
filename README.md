🧵 LoreWeaver

LoreWeaver is a simple terminal-based AI assistant that answers your questions using custom documents. It uses LangChain, FAISS for vector search, and HuggingFace Transformers for generating answers.

📦 Features
Load your own .txt or .pdf files

Ask natural-language questions

Answers are printed directly to the terminal

Source files used for answers are also shown

🚀 Installation
Clone the repository:


```
git clone https://github.com/yourusername/LoreWeaver.git
cd LoreWeaver
```

Install required packages:

```
pip install -r requirements.txt 
```

⚙️ Environment Setup
Create a .env file in the root directory with your Openrouter API:
```
OPENROUTER_API_KEY=your_openrouter_api_here
OPENAI_API_KEY=your_openrouter_api_here
```

📂 Folder Structure
LoreWeaver/
├── reference_files/        ← Put your `.txt` or `.pdf` files here
├── main.py                 ← Main script
├── .env                    ← API token
├── requirements.txt        ← Dependency list
└── README.md
🧠 How to Use
Add your reference files into the reference_files folder.

Run the script:

```
python main.py
```

Type your question in the terminal.

Get the answer and see which documents were used to generate it.
