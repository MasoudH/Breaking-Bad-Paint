from pygame import *

font.init()

def smoolthan(screen, size, text, color, location):
    screen.blit(font.Font("Fonts/Smoolthan.otf", size).render(str(text), True, color), location)

def regular(screen, size, text, color, location):
	screen.blit(font.SysFont("Comic Sans MS", size).render(str(text), True, color), location)
