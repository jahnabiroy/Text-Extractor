import moviepy.editor as mp
import speech_recognition as sr


def extract_audio_from_video(file_path):
    # to extract audio from video
    video = mp.VideoFileClip(file_path)
    audio_file_path = "output.wav"
    video.audio.write_audiofile(audio_file_path)
    return audio_file_path
