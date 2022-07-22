# Ideas for the Prototype
 - Internal representation: Audio data associated with a user, in a certain order. The audio will be run through a speech-to-text algorhithm to transcribe it, and get reassociated with that user.
 - It will reconstruct into a plain text file as follows:
```
John:
  Hi, how are you?
Jane:
  I'm great! How are you?
```
 - Alternatively, use a storage format like JSON or XML, and generate that nice text from it.
 - For speech recognition: 
   - ~https://pypi.org/project/automatic-speech-recognition/~ (it looks like this project is broken beyond my ability to repair.)
   - https://pypi.org/project/SpeechRecognition/ (looks fairly large, so it's actively developed? Big pro: transcription demo.)
