# Overview

This project is designed to parse text from various media types: audio (`.wav`), video (`.mp4`), and text documents (`.pdf`). The implementation utilizes Python and its libraries, relying exclusively on free APIs and libraries for unlimited usage.

## Features

1. **_Parse Text from Video_**
   - Implementation:
     Extracts audio from the video in .wav format using the Moviepy library.
     Processes the audio through text extraction, reusing the logic implemented for audio parsing.
   - Issues Faced:
     Alternative libraries, such as SpeechRecognition, proved less efficient than Moviepy.
2. **_Parse Text from Audio_**
   - Implementation:
     Utilized the SpeechRecognition library with the Google Web Speech-to-Text service for audio transcription.
     Dealt with limitations of 120-second processing by splitting audio into 115-second chunks using pydub.silence.
     Errors such as UnknownValueError and RequestError were managed with appropriate fallbacks.
   - Challenges:
     Processing long audio files is time-intensive (e.g., 15-minute audio may take 30-40 minutes).
     Paid APIs with better performance were avoided due to limited free usage.
3. **_Parse Text from PDF_**
   - Implementation:
     Used the PyMuPDF library to extract clean and structured text.
   - Challenges:
     Preservation of tabular data was not supported natively. However, the row structure of tabular data was maintained by outputting each column in a new line.
     Alternatives like PyPDF2, Textract, and Tika were tested but found less efficient.

## Libraries and Tools

- Text Extraction: `SpeechRecognition`, `PyMuPDF`
- Audio Processing: `Moviepy`, `pydub`
- Error Handling: Custom error management for transcription inconsistencies

## Known Limitations

Limited accuracy and speed of the Google Web Speech-to-Text service. Inefficiency in preserving tabular data in PDF files. For further improvements, exploring better transcription APIs and tabular-specific libraries like Tabulapy is recommended.
