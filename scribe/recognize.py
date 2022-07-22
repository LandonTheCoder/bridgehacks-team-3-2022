#! /usr/bin/python3
# For speech recognition API reference, see https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst
# Example loosely based on https://github.com/Uberi/speech_recognition/blob/master/examples/audio_transcribe.py

import speech_recognition as sr
rec = sr.Recognizer() # Performs action of recognizing speech
FNAME = "./speech-recognition-test.wav"
phraselist = []
with sr.AudioFile(FNAME) as source:
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
print("phraselist:", phraselist)
