import speech_recognition as S
speech_recognizer = S.Recognizer()
print('Listening...')
with S.Microphone() as microphone:
    speech_recognizer.adjust_for_ambient_noise(microphone)
    audio = speech_recognizer.listen(microphone)
    query = speech_recognizer.recognize_google(audio, language='eng-in')
    print(query)