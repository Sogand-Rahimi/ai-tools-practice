# audio_dsp_processing.py
# Raw Audio Signal Processing, Amplification, and Visualization

import wave
import matplotlib.pyplot as plt
import numpy as np
import pyaudio


def record_and_process_audio():
    # Audio Configuration Constants
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 10000  # 10,000 samples per second
    CHUNK = 1024  # Buffer size per read pass
    NUM_CHUNKS = 50  # Total recording cycles (~5.12 seconds)

    audio_driver = pyaudio.PyAudio()

    # 1. Capture Raw Audio from Microphone
    print("Recording audio from microphone...")
    stream_in = audio_driver.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK,
    )

    raw_frames = []
    audio_signal = np.array([], dtype=np.int16)

    for _ in range(NUM_CHUNKS):
        binary_data = stream_in.read(CHUNK)
        raw_frames.append(binary_data)

        # Convert raw byte string to 16-bit integer array
        numpy_chunk = np.frombuffer(binary_data, dtype=np.int16)
        audio_signal = np.append(audio_signal, numpy_chunk)

    # Clean up input stream
    stream_in.stop_stream()
    stream_in.close()
    print("Recording complete.")

    # 2. Plot Original Audio Waveform
    plt.figure(figsize=(10, 4))
    plt.plot(audio_signal, color="blue", alpha=0.7)
    plt.title("Original Audio Signal Waveform")
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude (16-bit)")
    plt.grid(True)
    plt.savefig("original_waveform.png")
    plt.show()

    # 3. Playback Original Audio
    print("Playing back original audio...")
    stream_out = audio_driver.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        output=True,
        frames_per_buffer=CHUNK,
    )

    original_bytes = audio_signal.tobytes()
    stream_out.write(original_bytes)

    # 4. Amplify Audio Signal (Mathematical Manipulation)
    print("Amplifying audio signal (5x)...")
    amplified_signal = np.clip(audio_signal * 5, -32768, 32767).astype(np.int16)

    # Plot Amplified Waveform
    plt.figure(figsize=(10, 4))
    plt.plot(amplified_signal, color="red", alpha=0.7)
    plt.title("Amplified Audio Signal Waveform (5x Boost)")
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude (16-bit)")
    plt.grid(True)
    plt.savefig("amplified_waveform.png")
    plt.show()

    # Playback Amplified Audio
    stream_out.write(amplified_signal.tobytes())

    # Clean up output stream
    stream_out.stop_stream()
    stream_out.close()

    # 5. Save Raw Recording to WAV File
    output_filename = "recorded_audio.wav"
    sample_width = audio_driver.get_sample_size(FORMAT)

    with wave.open(output_filename, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(sample_width)
        wf.setframerate(RATE)
        wf.writeframes(b"".join(raw_frames))

    print(f"Audio saved successfully to '{output_filename}'.")

    # Terminate PyAudio Engine
    audio_driver.terminate()


if __name__ == "__main__":
    record_and_process_audio()
