import pygame
from pygame.locals import *
pygame.mixer.init()
sound_clip = pygame.mixer.Sound("F:\python_livewire\soundfile.wav")
channel = pygame.mixer.find_channel()
channel = pygame.mixer.find_channel(True)
channel.set_volume(0.5)
channel.play(sound_clip)
