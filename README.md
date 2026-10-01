# 👁️ AI Vision Chatbot

An AI-powered chatbot that allows users to upload an image and ask questions about it. The application uses OpenAI's vision capabilities to understand the uploaded image and generate answers.

## 🚀 Features

- 📷 Upload JPG, JPEG, PNG, or WEBP images
- 💬 Ask questions about the uploaded image
- 🤖 AI-powered image understanding
- 🔐 Secure API key management using Streamlit Secrets
- 🌐 Deployed using Streamlit Community Cloud

## 🛠️ Technologies Used

- Python
- Streamlit
- OpenAI API
- GitHub
- Streamlit Community Cloud

## ⚙️ How It Works

1. User uploads an image.
2. User enters a question about the image.
3. The image is encoded and sent to the OpenAI API.
4. The AI analyzes the image.
5. The chatbot displays the generated response.

## 📁 Project Structure

```text
ai-vision-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .streamlit/
    └── secrets.toml
