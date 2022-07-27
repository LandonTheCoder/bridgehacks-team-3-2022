# bridgehacks-team-3-2022
This is a program that will take an input audio file, and process with 3 steps:
 - It runs speech recognition on it (currently sending it to Google for analysis)
 - It filters out keywords from the text
 - It bulletizes each "phrase" as detected by speech recognition, and writes it to a file

This depends on the SpeechRecognition library from PyPI.

To test it, run scribe/main.py with a file to write the recognition to, and possibly an input file (or it will default to "speech-recognition-test.wav" in the current directory).

For example:
```sh
$ scribe/main.py example-1.txt scribe/speech-recognition-test.wav
Google Speech Recognition thinks you said "well hello how are you"
Google Speech Recognition thinks you said "I'm fine how are you"
Google Speech Recognition thinks you said "I'm great thanks for asking"
Google Speech Recognition thinks you said "Turtles are very cool"
Google Speech Recognition thinks you said "they come in all shapes and sizes"
Google Speech Recognition thinks you said "they are friend cells that protect them from danger"
Google Speech Recognition could not understand audio
phraselist: ['well hello how are you', "I'm fine how are you", "I'm great thanks for asking", 'Turtles are very cool', 'they come in all shapes and sizes', 'they are friend cells that protect them from danger']
 - well hello how are you
 - Am fine how are you
 - Am great thanks for asking
 - Turtles are very cool
 - come in all shapes sizes
 - are friend cells protect from danger
notestr:
 - well hello how are you
 - Am fine how are you
 - Am great thanks for asking
 - Turtles are very cool
 - come in all shapes sizes
 - are friend cells protect from danger

$ scribe/main.py example-2.txt scribe/speech-recognition-test-old.wav
Google Speech Recognition thinks you said "well hello how are you"
Google Speech Recognition thinks you said "I'm fine how are you"
Google Speech Recognition thinks you said "I'm great thanks for asking"
Google Speech Recognition could not understand audio
phraselist: ['well hello how are you', "I'm fine how are you", "I'm great thanks for asking"]
 - well hello how are you
 - Am fine how are you
 - Am great thanks for asking
notestr:
 - well hello how are you
 - Am fine how are you
 - Am great thanks for asking

$ cat example-1.txt
 - well hello how are you
 - Am fine how are you
 - Am great thanks for asking
 - Turtles are very cool
 - come in all shapes sizes
 - are friend cells protect from danger
$ cat example-2.txt
 - well hello how are you
 - Am fine how are you
 - Am great thanks for asking
```
