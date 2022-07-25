#! /usr/bin/python3
# For speech recognition API reference, see https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst
# Example loosely based on https://github.com/Uberi/speech_recognition/blob/master/examples/audio_transcribe.py

import speech_recognition as sr

def recognize_file(fobj):
    """Return a list of phrases for a file object or filename. Accepts WAV or FLAC."""
    rec = sr.Recognizer() # Performs action of recognizing speech
    phraselist = []
    with sr.AudioFile(fobj) as source:
        while True: # Will break when nothing is returned from speech
            audio = rec.listen(source) # Records 1 phrase
            try:
                text = rec.recognize_google(audio) # Google Speech Recognition has the best quality.
                if text != "":
                    phraselist.append(text)
                print("Google Speech Recognition thinks you said \"%s\"" % text)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                break;
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                break;
    return phraselist

def main(passed_args=None):
    import argparse
    parser = argparse.ArgumentParser(description="Load an audio file and recognize its contents. ")
    parser.add_argument("file", help="The audio file to recognize. If unspecified, assumed to be \"./speech-recognition-test.wav\"", nargs='?')
    args = parser.parse_args(passed_args)
    FNAME = "./speech-recognition-test.wav"
    if args.file == None:
        phraselist = recognize_file(FNAME)
    else:
        phraselist = recognize_file(args.file)
    print("phraselist:", phraselist)
