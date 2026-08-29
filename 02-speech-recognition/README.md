# Speech & Audio Processing

This module covers both high-level Speech-to-Text conversion and low-level Digital Signal Processing (DSP) of live audio streams.

---

## Included Scripts

1. **`speech_to_text.py`**: Interactive Speech Recognition CLI supporting `.wav` audio files and live microphone input in English (`en-US`) and Persian (`fa-IR`).
2. **`audio_dsp_processing.py`**: Raw audio signal processing engine — records PCM audio buffers, converts byte streams into NumPy arrays, plots signal waveforms via Matplotlib, performs volume amplification, and exports `.wav` files.

---

## Prerequisites

Install the required dependencies:

```bash
pip install SpeechRecognition pyaudio numpy matplotlib
