🧵 LoreWeaver

LoreWeaver is a simple terminal-based AI assistant using the Llama 4 Maverick AI model that answers your questions using custom documents and chat history. It can not access the internet.

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
