import tkinter as tk
from tkinter import scrolledtext
import threading
import source

def sesi_al_ve_yanitla():
    """Mikrofondan sesi al, AI yanıtını göster ve seslendir."""
    metin = source.sesi_metne_cevir()
    if metin:
        txt_giris.insert(tk.END, f"\nSiz: {metin}\n")
        yanit = source.yapay_zeka_yaniti_olustur(metin)
        txt_giris.insert(tk.END, f"Asistan: {yanit}\n")
        source.metni_sese_cevir(yanit)

def dinlemeyi_baslat():
    """Arka planda ses kaydı başlatan thread oluştur."""
    thread = threading.Thread(target=sesi_al_ve_yanitla)
    thread.start()

# Tkinter Arayüz
root = tk.Tk()
root.title("Sesli Asistan")

btn_baslat = tk.Button(root, text="Konuş", command=dinlemeyi_baslat, font=("Arial", 14))
btn_baslat.pack(pady=10)

txt_giris = scrolledtext.ScrolledText(root, width=50, height=15, font=("Arial", 12))
txt_giris.pack(padx=10, pady=10)

root.mainloop()