import pygame as pg
import sys
from time import time
from drawer import *
from timer import Timer
from player import Player
from input_screen import *
from player import *
from game_logic import *


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
    
    '''         
    pg.mixer.init()
    laser_beam_sound = pg.mixer.Sound("Tick.wav")
    '''

    oskari = Player('Oskari', 'male', 82000, 0.05, (0,255,0))
    niko = Player('Niko', 'male', 64500, 0.02, (200,0,100))
    nikoliina = Player('Nikoliina', 'female', 64500, 0.02, (200,0,100))
    petsku = Player('Petsku', 'male', 90000, 0.1, (240,100,20))

    players.extend([niko, oskari, petsku, nikoliina])

    game_mode = ClassicMinuteBeerMode(players)

    drawer = Drawer(main_surface, players, game_mode)

    Timer.reset_clock()
    Timer.round_time = 5
    #Count down loop
    while Timer.get_elapsed_time() < Timer.round_time:
        game_mode.update_game()
        drawer.draw_count_down()
        pg.display.flip()

    Timer.reset_clock()
    Timer.round_time = 60
    #Main loop
    while True:
        game_mode.update_game()
        drawer.draw()
        pg.display.flip()



main()