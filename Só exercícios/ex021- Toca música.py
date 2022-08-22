# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame

print('=============\n🎼TOCA MÚSICA🎼\n=============')

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021m.mp3')
pygame.mixer.music.play()
pygame.event.wait()