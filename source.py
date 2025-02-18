import speech_recognition as sr
from gtts import gTTS
from transformers import pipeline
import os
import torch


def metni_sese_cevir(metin):
    tts = gTTS(text=metin, lang="en")  #İngilizce için
    tts.save("yanit.mp3")
    os.system("start yanit.mp3")  #Windows'ta ses oynatma


chatbot = pipeline("text-generation")
def yapay_zeka_yaniti_olustur(soru):
    response = chatbot(soru)
    return response[0]['generated_text']


def sesi_metne_cevir():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinliyorum...")
        audio = recognizer.listen(source)
        
        try:
            metin = recognizer.recognize_google(audio, language="tr-TR")  #Türkçe komut verebilmek için
            print(f"Söylediğiniz: {metin}")
            return metin
        except sr.UnknownValueError:
            print("Anlayamadım, lütfen tekrar söyleyin.")
            return None



#sürücü kod
def main():
    while True:
        print("Lütfen bir soru sorun veya komut verin...")
        
        #komut al
        soru = sesi_metne_cevir()
    
        if soru:
            yanit = yapay_zeka_yaniti_olustur(soru)
            print(f"Yapay Zeka Yanıtı: {yanit}")

            metni_sese_cevir(yanit)

            #devam kontrolü
            print("\nYeni bir soru sormak ister misiniz? (Evet/Hayır)")
            cevap = input().strip().lower()
            if cevap not in ["evet", "e", "yes", "y"]:
                print("Görüşmek üzere!")
                break

if __name__ == "__main__":
    main()