"""
EXERCÍCIO 021: Tocando um MP3

Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
"""
from pygame import event, mixer
#from time import sleep
mixer.init()
mixer.music.load('musica.mp3')
mixer.music.play()
event.wait()
#sleep(120)
