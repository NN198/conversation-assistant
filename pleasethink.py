import whisper
import ollama
import os

# Set this to the name of your manual file
FILENAME = "test_convo.wav"

# Explicit client so it always hits the correct host/port
client = ollama.Client(host='http://localhost:11434')

def process_existing_file():
    # Check if the file actually exists so it doesn't crash
    if not os.path.exists(FILENAME):
        return f"Error: I couldn't find '{FILENAME}' in this folder."

    # 1. Transcribe Audio file
    print(f"✍️ Transcribing {FILENAME}...")
    model = whisper.load_model("base")
    result = model.transcribe(FILENAME)
    transcript = result["text"]

    print(f"📝 Raw Transcript: {transcript}\n")

    if not transcript.strip():
        return "No speech detected in the file."

    # 2. Summarize transcribed text
    print("🧠 Asking Gemma 3 to summarize...")

    full_prompt = (
        "I zoned out during a conversation. Based on this transcript, "
        "give me a brief summary and list any action items or dates mentioned:\n\n"
        f"{transcript}"
    )

    # Use client.generate instead of ollama.generate
    response = client.generate(
        model='gemma3',
        prompt=full_prompt
    )
    return response['response']

if __name__ == "__main__":
    summary = process_existing_file()
    print("\nWHAT YOU MISSED")
    print(summary)