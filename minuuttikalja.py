import pygame as pg
import sys
from time import time
from drawer import *
from timer import Timer
from player import Player

from input_screen import *
from player import *


def main():

    pg.init()      
    surface_height = 500   
    surface_width = 1000
    main_surface = pg.display.set_mode((surface_width, surface_height))
    

    players = []
    more_players = True
    while more_players:
        ask = "Press Enter for new player, or anything else to start"
        fontobject = pg.font.Font(None,46)
        main_surface.blit(fontobject.render(ask, 1, (255,255,255)), (main_surface.get_width()/2-fontobject.size(ask)[0]/2, main_surface.get_height()/2-75))
        pygame.display.flip()

        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.key == K_RETURN:
                    main_surface.fill((0, 0, 0))
                    players.append(addPlayer(main_surface))
                else:
                    more_players = False
                




    pg.mixer.init()
    laser_beam_sound = pg.mixer.Sound("Tick.wav")

    Timer.start_clock()
    Timer.circle_time = 10

    drawer = Drawer(main_surface, players)

    while True:
        
        drawer.draw()
        pg.display.flip()



main()