# 🧠 Conversation Recovery Assistant (Offline AI)

A lightweight local AI system that helps you **recover what you missed in a conversation** when your attention drops.

Instead of replaying audio, it extracts meaning:

- 🗣️ What was said  
- 📌 What matters  
- ✅ What you need to do next  

---

## 🚀 Demo (Concept)

---

## 💡 Why This Exists

Sometimes, in the middle of a conversation, attention slips.

Not intentionally. Not out of disinterest.

Just cognitive overload.

This project explores:

> “Can AI reconstruct meaning from conversations I partially missed?”

---

## ⚙️ Features

- 🎤 Processes recorded `.wav` files  
- 📝 Speech-to-text using Whisper  
- 🧠 Summarization using Gemma 3 via Ollama  
- 🔒 Fully offline after setup  
- 💸 No API costs  

---

## 🧰 Tech Stack

- Python 3.x  
- `openai-whisper`  
- `ollama`  
- FFmpeg  

---

## 💻 Hardware (Tested On)

- Scarlett Studio microphone (audio input)  
- RTX 50-series GPU  
- 16 GB RAM  
- Standard consumer CPU  

> This is not a high-end setup — the goal is accessibility.

---

## 📦 Installation

### 1. Clone repository

```bash
git clone <your-repo-url>
cd convo-project