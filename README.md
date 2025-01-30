# GenAIWebUI Ollama
Lightweight, customizable, local web interface for Deepseek and other GenAI models.

--- 

This project provides a **local web-based UI** to interact with **DeepSeek and other AI models** using Ollama. Thanks to **distilled models**, it is now feasible to run generative AI models on regular laptops without relying on cloud services.

## Features

- **Offline & Private** – No data is leaked online. Everything runs locally.
- **Faster Responses** – No internet lag; AI runs directly on your machine.
- **Easily Customizable** – Modify the UI, model, or processing logic as needed.
- **Supports Markdown** – AI responses render with proper formatting.
- **Chat History Management** – View, scroll, and clear past chats.

## Installation & Setup

### 1. Install Ollama and DeepSeek

Ensure you have [Ollama](https://ollama.com/) installed. Then, download the DeepSeek model:

```sh
ollama pull deepseek-r1:1.5b
```
### 2. Clone this Repository
```sh
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 3. Install Dependencies
```sh
pip install flask requests
```


### 4. Run the Server!
```python
python app.py
```

This will start a Flask server at `http://localhost:5000`.

## Usage

1. Type a prompt into the input box.
2. Press "Send" or use `Ctrl + Enter` to submit.
3. View AI responses in the chat area.
4. Chat history is stored and can be cleared using the "Clear Chat History" button.

## Customization

### Changing the AI Model

By default, the project uses **DeepSeek (deepseek-r1:1.5b)**, but you can switch models by modifying `app.py`:

```python
payload = {
    "model": "your-model-name-here", # Change this to another model
    "prompt": user_input,
    "stream": False
}
```

### Modifying the User Interface
The UI is in `templates/index.html`. You can:

- Change the layout (CSS modifications in `<style>` section).
- Edit response formatting (uses marked.js for Markdown rendering).
- Change chat history behavior in `updateChatHistory()` inside `<script>`.

# License
This project is open-source under the MIT License.