🧵 Weavyrn 

Weavyrn is a simple terminal-based AI assistant using OpenRouter to connect with Llama 4 Maverick AI model that answers your questions using custom documents and chat history. It can not access the internet.

📦 Features
Load your own .txt or .pdf files

Ask natural-language questions

Answers are printed directly to the terminal

Source files used for answers are also shown

🚀 Installation
Clone the repository:

```
git clone https://github.com/RazaYgPrnhAd/Weavyrn.git
cd LoreWeaver
```

Install required packages:

```
pip install -r requirements.txt 
```

🧠 How to Use
Add your reference files into the reference_files folder.

Add your Openrouter API Key inside the .env file:

```
OPENROUTER_API_KEY=your_openrouter_api_key_here
SAME_API_KEY=your_openrouter_api_key_here

```

Run the script:

```
python main.py
```

Type your question in the terminal.

Get the answer and see which documents were used to generate it.
