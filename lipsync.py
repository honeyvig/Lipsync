from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt
import os

# Load audio file
def load_audio(file_path):
    audio = AudioSegment.from_file(file_path)
    return audio

# Simple function to visualize audio wave
def plot_audio_wave(audio):
    samples = np.array(audio.get_array_of_samples())
    plt.figure(figsize=(10, 4))
    plt.plot(samples)
    plt.title("Audio Waveform")
    plt.xlabel("Sample")
    plt.ylabel("Amplitude")
    plt.show()

# Phoneme to viseme mapping
phoneme_to_viseme = {
    'a': 'Mouth Open',
    'b': 'Closed Mouth',
    'p': 'Closed Mouth',
    'f': 'Teeth Apart',
    'm': 'Closed Mouth',
    'o': 'Mouth Open',
    's': 'Teeth Apart',
    't': 'Closed Mouth',
    'k': 'Closed Mouth',
    # Add more phonemes and their corresponding visemes
}

# Function to extract phonemes (simplified)
def extract_phonemes(audio):
    # In a real implementation, you would use a speech recognition library or API
    # Here we just simulate phoneme extraction
    phonemes = ['a', 'b', 'o', 's', 't']  # Example phoneme sequence
    return phonemes

# Generate viseme sequence from phonemes
def generate_viseme_sequence(phonemes):
    viseme_sequence = [phoneme_to_viseme.get(p, 'Unknown') for p in phonemes]
    return viseme_sequence

# Main function
def main(audio_file):
    audio = load_audio(audio_file)
    plot_audio_wave(audio)
    
    phonemes = extract_phonemes(audio)
    viseme_sequence = generate_viseme_sequence(phonemes)

    print("Phoneme Sequence:", phonemes)
    print("Viseme Sequence:", viseme_sequence)

# Example usage
if __name__ == "__main__":
    audio_file_path = "path_to_your_audio_file.wav"  # Change to your audio file
    main(audio_file_path)
