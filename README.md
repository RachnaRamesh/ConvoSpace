# ConvoSpace 💬

ConvoSpace is a high-performance, full-stack chat application designed for real-time interactions with Large Language Models (LLMs). It features a sleek **Streamlit** frontend, a robust **Python** backend, and persistent storage using **MongoDB**. The core of the application leverages the **Groq API** for ultra-fast inference, enabling a smooth and responsive user experience.

---

## 🚀 Key Features

- **Real-time Chat**: Interactive interface powered by Streamlit for a seamless user experience.
- **Ultra-fast Inference**: Leverages Groq API for near-instant responses from cutting-edge models (Llama 3.1, 3.3, etc.).
- **Chat Persistence**: Full history of conversations stored in MongoDB, allowing users to resume previous chats.
- **Auto-Title Generation**: Automatically generates relevant, concise titles for new chat sessions using LLMs.
- **Model Selection**: Switch between different LLMs on-the-fly via a user-friendly dropdown.
- **Session Management**: Easily create new chats or delete old ones from the sidebar.

---

## 🛠️ Technology Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: [Python 3.x](https://www.python.org/)
- **Database**: [MongoDB](https://www.mongodb.com/)
- **LLM Inference**: [Groq](https://groq.com/)
- **Configuration**: [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- **Environment Management**: [python-dotenv](https://github.com/theskumar/python-dotenv)

---

## 📂 Project Structure

- `main.py`: The entry point of the application, managing the UI and orchestration.
- `config/`: Configuration layer using Pydantic for environment variable management.
- `db/`: Database layer handling MongoDB connections and CRUD operations for conversations.
- `llm_factory/`: Factory pattern implementation for managing Groq client initialization.
- `services/`: Business logic including chat utilities, model listing, and title generation.
- `requirements.txt`: List of Python dependencies.
- `env_template.txt`: Template for required environment variables.

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone <repository-url>
cd ConvoSpace
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory based on `env_template.txt`:
```env
MONGO_DB_URL=your_mongodb_connection_string
MONGO_DB_NAME=ConvoSpace
GROQ_API_KEY=your_groq_api_key
```

### 5. Run the Application
```bash
streamlit run main.py
```

---

## 📖 Core Workflows

### Initializing a Chat
1. User sends the first message.
2. `get_chat_title()` uses the LLM to generate a summary title.
3. A new conversation document is created in MongoDB.
4. The message and its response are stored with timestamps.

### Generating a Response
1. The app retrieves the full chat history from the session state.
2. `get_answer()` calls the Groq API with the history and a system prompt.
3. The response is displayed and appended to the MongoDB record.

---

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License
This project is licensed under the MIT License.
