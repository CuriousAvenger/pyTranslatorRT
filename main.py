from googletrans import Translator
import speech_recognition as sr
import pyttsx3
from googletrans import LANGCODES

class PyTranslator:
    def __init__(self):
        self.trans, self.voice = Translator(), pyttsx3.init()
        self.rec, self.mic = sr.Recognizer(), sr.Microphone()

    def speak(self, text):
        self.voice.say(text)
        self.voice.runAndWait()

    def translate(self, text):
        translated = self.trans.translate(text)
        print(f"[+] Translation: {translated.text}")
        return translated.text
    
    def take_voice(self, lang="en"):
        while True:
            with self.mic as source:
                self.rec.adjust_for_ambient_noise(source)
                print("      [+] Listening for input")
                voice_input = self.rec.listen(source)
                try:
                    voice_input = self.rec.recognize_google(voice_input, language=lang)
                    print(f"      [+] Response: {voice_input.lower()}")
                    return voice_input.lower()
                except:
                    self.speak("Failed to recognize audio. Try again")
                    print("      [!] Error: Failed to recognize audio")

    def choose_language(self):
        print("[*] Choosing Your Language")
        while True:
            self.speak("Choose a language")
            try:
                lang_code = LANGCODES[self.take_voice()]
                return lang_code
            except Exception:
                self.speak("Failed to recognize language. Try Again")
                print("[!] Error: Invalid Language")
            
if __name__ == "__main__":
    try:
        translator = PyTranslator()
        lang_code = translator.choose_language()

        print(f"[+] Selected Language: {lang_code}")
        translator.speak("Translation Started")
        while True:
            text = translator.take_voice(lang=lang_code)
            translator.speak(translator.translate(text))
    
    except KeyboardInterrupt:
        print("[!] Keyboard Interrupt: Exiting Code")
        exit(0)
