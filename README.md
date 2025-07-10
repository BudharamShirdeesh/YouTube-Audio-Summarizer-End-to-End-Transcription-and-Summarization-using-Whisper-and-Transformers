YouTube Audio Transcriber & Summarizer

This project is a complete pipeline for automatically downloading audio from a YouTube video, transcribing the speech using OpenAI's Whisper model, and summarizing the transcription using Hugging Face's `facebook/bart-large-cnn` summarizer.

---

##  Features

-  **YouTube Integration** – Download audio from any YouTube video.
-  **Automatic Transcription** – Use Whisper (open-source ASR model) to transcribe spoken content.
-  **Summarization** – Generate concise summaries using BART transformer model.
-  **Save Outputs** – Store both the transcription and summary in `.txt` files.
-  **NLTK Sentence Chunking** – Ensures cleaner, chunked input for better summaries.

---

##  Getting Started

###  Prerequisites

Make sure you have Python 3.8+ and `ffmpeg` installed on your system.

###  Installation

Clone the repository and install dependencies.
## Usage
video_url = " PLACE URL IN THE SCRIPT "
run_pipeline(video_url) 



