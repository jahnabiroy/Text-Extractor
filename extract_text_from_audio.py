import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub import AudioSegment, silence


# segmenting audio since google speech to text cannot handle processing of audio duration more than 120 seconds.
def segmenting_audio(
    path, folder, interval=115000, min_silence_len=500, silence_thresh=-16
):
    audio_provided = AudioSegment.from_wav(path)
    try:
        os.mkdir(folder)
    except FileExistsError:
        pass
    os.chdir(folder)
    i = 0  # for iteration
    k = 0  # indexing the chunks
    while i < len(audio_provided):
        start = i
        end = min(start + interval, len(audio_provided))
        # detecting silence intervals
        silence_intervals = silence.detect_silence(
            audio_provided[start:end],
            min_silence_len=min_silence_len,
            silence_thresh=silence_thresh,
        )
        if silence_intervals:
            end_silence = silence_intervals[0][1]
            end = start + end_silence
        segment = audio_provided[start:end]
        segment.export(f"chunk_{k}.wav", format="wav")
        print(f"finished generating chunk_{k}.wav")
        k += 1
        i = end
    os.chdir("..")
    final_text = transcribe_audio_chunks(folder)
    return final_text


def transcribe_audio_chunks(folder):
    recognizer = sr.Recognizer()

    filenames = os.listdir(folder)
    filenames.sort(key=lambda x: int(x.split("_")[1].split(".")[0]))

    text_transcribed_as_whole = ""
    for filename in filenames:
        if filename.endswith(".wav"):
            chunk_file_path = os.path.join(folder, filename)

            # Load the audio file
            with sr.AudioFile(chunk_file_path) as source:
                audio_data = recognizer.record(source)

                try:
                    text = recognizer.recognize_google(audio_data)
                    text_transcribed_as_whole += text
                    text_transcribed_as_whole += " "
                except sr.UnknownValueError:
                    text_transcribed_as_whole += " [incoherent] "
                except sr.RequestError as e:
                    print(
                        f"Could not request results from Google Web Speech API for {chunk_file_path}; {e}"
                    )
    return text_transcribed_as_whole
