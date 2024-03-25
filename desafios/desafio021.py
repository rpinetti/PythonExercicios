import tkinter
from tkinter.filedialog import askopenfilename
import pygame
#from pydub import AudioSegment
#from pydub.playback import play

pygame.init()

# Desafio 021 - Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3

print('{:=^30}'.format(' DESAFIO 021 '))


def callback():
    tipos_arquivos = (("Música", "*.mp3"), ("Todos", "*.*"))
    nome_mp3 = askopenfilename(filetypes=tipos_arquivos)
    pygame.mixer.music.load(nome_mp3)
    pygame.mixer.music.play()
    pygame.event.wait()
    #song = AudioSegment.from_mp3(nome_mp3)
    #play(song)


root = tkinter.Tk()
root.title('DESAFIO 021')
tkinter.Button(root, text='Abrir MP3', command=callback).pack(fill=tkinter.X)
root.mainloop()

print('=' * 30)
