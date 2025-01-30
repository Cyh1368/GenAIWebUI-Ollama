from flask import Flask, request, jsonify, render_template
import requests
import json
import os

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"
CHAT_HISTORY_FILE = "chat_history.json"

def load_chat_history():
    """Load chat history from file"""
    if os.path.exists(CHAT_HISTORY_FILE):
        with open(CHAT_HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def save_chat_history(chat_history):
    """Save chat history to file"""
    with open(CHAT_HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(chat_history, file, indent=4)

@app.route("/")
def index():
    chat_history = load_chat_history()
    return render_template("index.html", chat_history=chat_history)

@app.route("/chat-history")
def get_chat_history():
    chat_history = load_chat_history()
    return jsonify({"chat_history": chat_history})

@app.route("/clear-chat-history", methods=["POST"])
def clear_chat_history():
    """Clears the chat history file"""
    with open(CHAT_HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump([], file)  # Save an empty list to reset history
    return jsonify({"message": "Chat history cleared!"})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    # Send request to Ollama API
    payload = {
        "model": "deepseek-r1:1.5b",
        "prompt": user_input,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    output = response.json()
    print(output)
    ai_response = output.get("response", "Error")

    # Load existing chat history
    chat_history = load_chat_history()

    # Append new chat entry
    chat_history.append({"prompt": user_input, "response": ai_response})

    # Save updated chat history
    save_chat_history(chat_history)

    return jsonify({"response": ai_response, "chat_history": chat_history})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
