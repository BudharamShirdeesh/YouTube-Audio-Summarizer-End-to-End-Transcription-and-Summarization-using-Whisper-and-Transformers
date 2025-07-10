import os
import yt_dlp
import whisper
from transformers import pipeline
import nltk

nltk.download('punkt')
from nltk.tokenize import sent_tokenize

# Download YouTube Audio
def download_audio(url: str, filename: str = "audio"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{filename}.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
    }

    if os.path.exists("audio.mp3"):
        os.remove("audio.mp3")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return "audio.mp3"

# Transcribe with Whisper
def transcribe_audio(file_path: str):
    print("🔊 Transcribing audio...")
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result["text"]

# Summarization
def summarize_text(text: str):
    print("📄 Summarizing transcription...")
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    sentences = sent_tokenize(text)
    chunks = []
    chunk = ""
    for sentence in sentences:
        if len(chunk) + len(sentence) <= 1000:
            chunk += sentence + " "
        else:
            chunks.append(chunk.strip())
            chunk = sentence + " "
    if chunk:
        chunks.append(chunk.strip())

    summary = ''
    for chunk in chunks:
        result = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
        summary += result[0]['summary_text'] + '\n'

    return summary.strip()

# Run Pipeline and Save Files
def run_pipeline(youtube_url: str):
    print("🔗 Downloading audio...")
    audio_path = download_audio(youtube_url)

    print("🧠 Running transcription + summarization...")
    transcription = transcribe_audio(audio_path)
    summary = summarize_text(transcription)

    # Save transcription and summary to files
    with open("transcription.txt", "w", encoding="utf-8") as f:
        f.write(transcription)

    with open("summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)

    print("\n📝 Transcription Preview:\n", transcription[:300], "...\n")
    print("✅ Final Summary:\n", summary)

# YouTube Video URL
video_url = "https://www.youtube.com/watch?v=aNbY1XyuEPI"
run_pipeline(video_url)