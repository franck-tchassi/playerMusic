
from tkinter import*
from tkinter import PhotoImage
import pygame
from pygame import mixer
from playsound import playsound
import threading
import os , sys
from PIL import Image, ImageTk




root = Tk()
root.geometry("400x400")
root.title("player music")
root.config(bg="#616161")


#mettre icon
image_icon =PhotoImage(file="téléchargement.png")
root.iconphoto(False,image_icon)


mixer.init()

def play_sound():
    #pygame.mixer.music.load("mhd.wav")
    #pygame.mixer.music.play(loops=0)
    playsound('mhd.mp3')

def up_volume():
    volume =50
    if volume < 100:
        volume += 10
        mixer.music.set_volume(volume / 100)

def down_volume():
    volume = 50
    if volume > 0:
        volume -= 10
        mixer.music.set_volume(volume / 100)
    
    








frame2 = Frame(root, bg="#3c3c3c", width=300, height=250, bd=4,highlightbackground='#b4b4b4',relief=SUNKEN, highlightcolor="red", highlightthickness=2)
frame2.place(x=52, y=30)


frame = Frame(frame2, width=200, height=180)
frame.place(x=52, y=30)
image = PhotoImage(file='images.png', master=frame)
#canvas = Canvas(root, width=100, height=18)
#canvas.pack()
#canvas.create_image((30//2, 30//2), image=image)




frame1 = Frame(root, bg="#3c3c3c", width=300, height=90)
frame1.place(x=52, y=290)

canvas = Canvas(root, bg='yellow', width=350, height=-10)
canvas.place(x=24, y=280)
ligne = canvas.create_line(0, 0, 0, 0, fill='yellow', width=1 )

label = Label(frame2, text="press play..", fg="white", bg="#3c3c3c")
label.place(x=120, y=215)

#button play and vol
playMusic=Button(frame1,text="play_song",bd=0, command=play_sound).place(x=130, y=30)
volume1 = Button(frame1,text="vol(-)",bd=0, command=down_volume).place(x=60, y=30)
voluma2 = Button(frame1,text="vol(+)",bd=0, command=up_volume).place(x=220, y=30)
#tittle song
label = Label(frame2, text="MHD_AFRO_TRAP_Part.9_(Faut_les_wet).mp3", fg="white", bg="#3c3c3c")
label.place(x=30, y=5)







root.mainloop()

