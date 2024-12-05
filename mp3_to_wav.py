from pydub import AudioSegment


def convert_mp3_to_wav(mp3_file_path, wav_file_path):
    # Load the MP3 file
    audio = AudioSegment.from_mp3(mp3_file_path)

    # Export the audio as WAV
    audio.export(wav_file_path, format="wav")


# Example usage
mp3_file_path = "sunflower.mp3"
wav_file_path = "output.wav"
convert_mp3_to_wav(mp3_file_path, wav_file_path)
