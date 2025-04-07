🧵 LoreWeaver
LoreWeaver is a simple terminal-based AI assistant that answers your questions using custom documents. It uses LangChain, FAISS for vector search, and HuggingFace Transformers for generating answers.

📦 Features
Load your own .txt or .pdf files

Ask natural-language questions

Answers are printed directly to the terminal

Source files used for answers are also shown

🚀 Installation
Clone the repository:


```git clone https://github.com/yourusername/LoreWeaver.git
cd LoreWeaver```
Install required packages:

bash
Copy
Edit
pip install -r requirements.txt
(Optional) Use a virtual environment:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
⚙️ Environment Setup
Create a .env file in the root directory with your Hugging Face API token:

ini
Copy
Edit
HUGGINGFACEHUB_API_TOKEN=your_token_here
Get your token at huggingface.co/settings/tokens

📂 Folder Structure
css
Copy
Edit
LoreWeaver/
├── reference_files/        ← Put your `.txt` or `.pdf` files here
├── main.py                 ← Main script
├── .env                    ← API token
├── requirements.txt        ← Dependency list
└── README.md
🧠 How to Use
Add your reference files into the reference_files folder.

Run the script:

bash
python main.py
Type your question in the terminal.

Get the answer and see which documents were used to generate it.
