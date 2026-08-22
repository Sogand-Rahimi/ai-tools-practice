# Speech to Text Converter

An interactive Python CLI application for Speech-to-Text (STT) conversion supporting both pre-recorded audio files (`.wav`) and live microphone input in multiple languages (English and Persian).

---

## Key Features

* **Dual Input Modes:** Process audio from local files or record live via microphone.
* **Multi-Language Support:** Easily toggle between English (`en-US`) and Persian (`fa-IR`).
* **Noise Adjustment:** Automatic calibration for background ambient noise prior to recording.
* **Error Handling:** Robust exception management for missing files, audio glitches, and hardware driver issues.

---

## Prerequisites

```bash
pip install SpeechRecognition pyaudio
