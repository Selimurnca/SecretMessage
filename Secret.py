from tkinter import *
from PIL import Image, ImageTk


#Screen
window = Tk()
window.title = "Secret Massage"
window.configure(background="black")
window.minsize(width=500, height=500)

#Image
img  = Image.open("matrix.png")
photo=ImageTk.PhotoImage(img)
lab=Label(image=photo,bg="black").place(x=0,y=10)

img2  = Image.open("matrix2.png")
photo2=ImageTk.PhotoImage(img2)
lab2=Label(image=photo,bg="black").place(x=340,y=0)

#Func
def text_write():
    message = text_text.get(1.0, END)
    key = key_entry.get()

    if not key:  # Key boşsa
        warning_label.config(text="Please enter your key !")
        return

    encrypted_message = ""
    key_length = len(key)
    key_index = 0

    for char in message:
        if char != "\n":
            shift = ord(key[key_index % key_length])
            encrypted_char = chr((ord(char) + shift) % 256)
            encrypted_message += encrypted_char
            key_index += 1
        else:
            encrypted_message += "\n"

    with open("SecretMessage.txt", "w", encoding="utf-8") as file:
        file.write(encrypted_message)

    text_text.delete(1.0, END)
    print("Mesaj şifreli şekilde kaydedildi!")


    def text_decryp():
        # Şifreli mesajı dosyadan al
        with open("SecretMessage.txt", "r", encoding="utf-8") as file:
            encrypted_message = file.read()

        # Key'i al
        key = key_entry.get()

        if not key:  # Eğer key boşsa
            warning_label.config(text="Please enter your key words!")
            return

        decrypted_message = ""
        key_length = len(key)
        key_index = 0

        for char in encrypted_message:
            if char != "\n":  # Enter karakterine dokunma
                shift = ord(key[key_index % key_length])  # Key'den bir karakter al, ASCII koduna bak
                decrypted_char = chr((ord(char) - shift) % 256)  # Key'in ASCII değerini çıkar, 0-255 aralığında tut
                decrypted_message += decrypted_char  # Çözülmüş karakteri mesajımıza ekle
                key_index += 1  # Key'deki bir sonraki harfe geç
            else:
                decrypted_message += "\n"  # Enter karakterini olduğu gibi bırak

        # Decrypted mesajı Text kutusuna yerleştir
        text_text.delete(1.0, END)  # Eski metni sil
        text_text.insert(1.0, decrypted_message)  # Yeni (çözülen) mesajı ekle

        print("Şifre çözülmüş mesaj:", decrypted_message)

def text_decrypt():
        # Şifreli mesajı dosyadan al
        with open("SecretMessage.txt", "r", encoding="utf-8") as file:
            encrypted_message = file.read()

        # Key'i al
        key = key_entry.get()

        if not key:  # Eğer key boşsa
            warning_label.config(text="Please enter your key words!")
            return

        decrypted_message = ""
        key_length = len(key)
        key_index = 0

        for char in encrypted_message:
            if char != "\n":  # Enter karakterine dokunma
                shift = ord(key[key_index % key_length])  # Key'den bir karakter al, ASCII koduna bak
                decrypted_char = chr((ord(char) - shift) % 256)  # Key'in ASCII değerini çıkar, 0-255 aralığında tut
                decrypted_message += decrypted_char  # Çözülmüş karakteri mesajımıza ekle
                key_index += 1  # Key'deki bir sonraki harfe geç
            else:
                decrypted_message += "\n"  # Enter karakterini olduğu gibi bırak

        # Decrypted mesajı Text kutusuna yerleştir
        text_text.delete(1.0, END)  # Eski metni sil
        text_text.insert(1.0, decrypted_message)  # Yeni (çözülen) mesajı ekle

        print("Şifre çözülmüş mesaj:", decrypted_message)


#Label
title_label = Label(text="Message Title", font=("Arial", 15, "bold"), fg="#22f111", bg="black")
title_label.pack(padx=5, pady=5)

title_entry = Entry(width=20)
title_entry.pack(padx=5, pady=5)

text_label = Label(text="Secret Message", font=("Arial", 15, "bold"), fg="#22f111", bg="black")
text_label.pack(padx=5, pady=5)

text_text = Text(width=20, height=10, bg="white")
text_text.pack(padx=5, pady=5)


key_label = Label(text="Key Words",font=("Arial" ,15 ,"bold"),bg="black",fg="#22f111" )
key_label.pack(padx=5,pady=5)

key_entry = Entry(width=20)
key_entry.pack()

text_button = Button(text="Save & Encrypt",font=("Arial",10,"bold") ,bg="black",fg="#22f111",command=text_write)
text_button.pack(padx=5,pady=5)

descrypt_button = Button(text="Descrypt",font=("Arial",10,"bold"),bg="black",fg="#22f111",command=text_decrypt)
descrypt_button.pack(padx=5,pady=5)

warning_label = Label(text="",font=("Arial",12,"bold"),bg="black",fg="#22f111")
warning_label.pack(padx=5,pady=5)



window.mainloop()
