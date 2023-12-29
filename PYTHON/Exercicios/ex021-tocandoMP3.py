
# Exercício 21 – Tocando um MP3

print('====== Exercício 21 – Tocando um MP3')
import pygame
pygame.init()
pygame.mixer.music.load('../music/ex021.mp3')
pygame.mixer.music.play()
input(pygame.event.wait())
