from pygame.locals import *
import pygame
#pygame.mixer.pre_init(44100, -16, 2, 2048)

pygame.mixer.init()
pygame.mixer.music.load("McPoze.mp3")
pygame.mixer.music.play()
pygame.time.wait(121000)

