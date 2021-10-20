import googletrans
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound, os

def translate(audio):
	t = Translator()
	trans = t.translate(audio)
	print(trans.text)
	return trans.text

def speak(text, langChoice):
	tts = gTTS(text=text, lang=langChoice)
	filename = 'voice.mp3'
	tts.save(filename)
	playsound.playsound(filename)
	os.remove(filename)

def takeVoice(language):
	while True:
		r = sr.Recognizer()
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source)
			print("[+] Listening for input")
			audio = r.listen((source))
			try:
				voiceInput = r.recognize_google(audio, language=language)
				print("[+] Response: " + voiceInput.lower())
				return voiceInput.lower()
			except Exception:
				print("[!] Error: Failed to recognize audio. Try typing your response")
				print("[*] Please spell out the response in your desired language. ")
				audio2 = input("[+] Start Typing: ")
				return audio2.lower() 


langChoice = "en"
print("[*] Choose a language: <In English>")
speak("Choose a language", langChoice)
lang = takeVoice("en")
language = googletrans.LANGCODES[lang]

while True:
	text = takeVoice(language)
	speak(translate(text), langChoice)
