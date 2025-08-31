# 🧑‍🤝‍🧑 MultiPersona Chat (CLI)

A lightweight **Command Line Interface (CLI) chatbot** that allows users to interact with multiple personas such as **Doctor**, **Teacher**, or **Friend**.  
Built using **Python** and **OpenAI API**, this project demonstrates how conversational AI can adapt to different contexts and personalities.

---

## ✨ Features
- 🔄 **Switch personas** dynamically (Doctor, Teacher, Friend, etc.)
- 💬 **Conversation memory** maintained per persona
- ⚡ **Simple CLI interface** – no extra setup needed
- 🛠️ **Easily extendable** by adding new personas
- 🔑 Secure API key handling with `.env`

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Taqadus814/MultiPersona-Chat.git
cd MultiPersona-Chat
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

```
### 3. Install Dependencies
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

```
### 4. Set up Environment Variables
Create a .env file in the root directory and add:

```bash
OPENAI_API_KEY=your_api_key_here

```
### 5. Run the Chat CLI
```bash
python chat_cli.py

```
