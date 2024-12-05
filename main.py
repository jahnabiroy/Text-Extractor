import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub import AudioSegment, silence
import fitz
import moviepy.editor as mp
import sys
import shutil

from extract_text_from_video import extract_audio_from_video
from extract_text_from_audio import segmenting_audio
from extract_text_from_pdf import extract_text_from_pdf
from write_to_file import write_to_file


def main():
    multimedia = sys.argv[1]
    file_name = sys.argv[2]
    if multimedia == "VIDEO":
        audio_path = extract_audio_from_video(file_name)
        transcription = segmenting_audio(audio_path, "audio_segments")
        write_to_file(transcription, multimedia)
        shutil.rmtree(f"audio_segments")
    elif multimedia == "AUDIO":
        transcription = segmenting_audio(file_name, "audio_segments")
        write_to_file(transcription, multimedia)
        shutil.rmtree(f"audio_segments")
    elif multimedia == "PDF":
        transcription = extract_text_from_pdf(file_name)
        write_to_file(transcription, multimedia)


if __name__ == "__main__":
    main()
