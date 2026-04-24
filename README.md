Conversation Recovery Assistant (Offline AI)

A lightweight local AI system that helps you recover what you missed in a conversation when your attention drops.

Instead of replaying audio, it extracts meaning:

🗣️ What was said
📌 What matters
✅ What you need to do next
🚀 Demo (Concept)
🎤 audio → 📝 transcription → 🧠 summary → 📄 action items

Output:
• Buy groceries  
• Call uncle  
• Dinner at 8 PM  
💡 Why This Exists

Sometimes, in the middle of a conversation, attention slips.

Not intentionally. Not out of disinterest.

Just cognitive overload.

This project explores:

“Can AI reconstruct meaning from conversations I partially missed?”

⚙️ Features
🎤 Processes recorded .wav files
📝 Speech-to-text using Whisper
🧠 Summarization using Gemma 3 via Ollama
🔒 Fully offline after setup
💸 No API costs
🧰 Tech Stack
Python 3.x
openai-whisper
ollama
FFmpeg
💻 Hardware (Tested On)
Scarlett Studio microphone (audio input)
RTX 50-series GPU
16 GB RAM
Standard consumer CPU

This is not a high-end setup — the goal is accessibility.

📦 Installation
1. Clone repository
git clone <your-repo-url>
cd convo-project
2. Create virtual environment
python -m venv venv

Activate:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3. Install dependencies
pip install openai-whisper ollama
4. Install FFmpeg

Download from: https://ffmpeg.org/download.html

Add to PATH

Verify:

ffmpeg -version
5. Install Ollama + model

Download Ollama:
👉 https://ollama.com/download

Then pull model:

ollama pull gemma3:latest
▶️ Usage
Add your audio file:
test_convo.wav
Run:
python pleasethink.py
🧠 Core Logic
result = model.transcribe(FILENAME)
transcript = result["text"]

response = client.generate(
    model='gemma3:latest',
    prompt=full_prompt
)
🔐 Local vs Cloud AI

Tools like Granola and Fireflies.ai are powerful — but cloud-dependent.

This project shows a different path:

Feature	Cloud Tools	This Project
Internet	Required	Not required
Privacy	External	Local
Cost	Subscription/API	Free
Control	Limited	Full

AI becomes something you run, not something you call.

⚠️ Limitations
Not real-time (yet)
Accuracy depends on audio quality
CPU inference can be slow
🔮 Roadmap
⏱️ Real-time “last 30 seconds” recall
🌍 Multilingual summaries
🎯 Structured outputs (tasks, deadlines)
⌨️ Hotkey-triggered capture