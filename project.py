#!/usr/bin/env python3

from random import randrange
import random
import pygame, sys
from pygame.locals import *
import string

pygame.font.init()


MENU_WIDTH = 1000
MENU_HEIGHT = 1000

HANGMAN_WIDTH = 1300
HANGMAN_HEIGHT = 720

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
COPPER = (72, 45, 20)

frame_rate = pygame.time.Clock()
back_ground = pygame.image.load("image_kids.jpg")





class GameObject:
    def __init__(self, position):
        self.position = position

    def input(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass


class Menu(GameObject):
    def __init__(self):
        self.window = pygame.display.set_mode((MENU_WIDTH,MENU_HEIGHT))
        pygame.display.set_caption('Meniu Joc')


        # pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])
        #butoanele de accesare ale paginilor jocurilor

        self.color_hang = (203, 195, 227)
        self.color_hang_hover = (140,106,189)
        self.left_hang = MENU_WIDTH / 4 + 100
        self.top_hang = MENU_HEIGHT / 3
        self.width_hang = 250
        self.heigth_hang = 120

        self.color_guess = (51, 255, 153)
        self.color_guess_hover = (37, 186, 132)
        self.left_guess = MENU_WIDTH / 4 + 20
        self.top_guess = MENU_HEIGHT / 2 + 50
        self.width_guess = 470
        self.heigth_guess = 120



        #[left, top, width, height]
        self.hang_rect = pygame.Rect(self.left_hang, self.top_hang, self.width_hang, self.heigth_hang)
        self.guess_rect = pygame.Rect(self.left_guess, self.top_guess, self.width_guess, self.heigth_guess)

        self.hangman_rect = pygame.Rect(500, 400, 100, 80)
        self.piatra_hartie_foarfeca_rect = pygame.Rect(400, 300, 100, 80)

        self.color = pygame.Color('lightblue3')


    def input(self):
        for event in pygame.event.get():
            

            #la deschiderea unei noi ferestre cea curenta se inchide
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if self.left_hang <= mouse[0] <= self.left_hang + self.width_hang and self.top_hang <= mouse[1] <= self.top_hang + self.heigth_hang:
                    print("hello hangman")
                    hangman = Hangman()
                    hangman.run()
                    pygame.quit()
                    sys.exit()
                elif self.left_guess <= mouse[0] <= self.left_guess + self.width_guess and self.top_guess <= mouse[1] <= self.top_guess + self.heigth_guess:
                    print("hello guess")
                    guess = Guess()
                    guess.run()
                    pygeme.quit()
                    sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
    def update(self):
        pass

    def draw(self):
        #self.window.fill(back_ground)
       
        image_rect = back_ground.get_rect()
        self.window.fill(BLACK)
        self.window.blit(back_ground, image_rect)


        #fonturi
        self.font = pygame.font.SysFont('Comic Sans MS',50)

        #titlul
        title_x_pos = MENU_WIDTH / 6 + 50
        title_y_pos = MENU_HEIGHT / 6
        self.img = self.font.render('Childhood\'s Gamechest', True, BLACK)
        self.window.blit(self.img, (title_x_pos , title_y_pos ))
        

        mouse = pygame.mouse.get_pos()
        if self.left_hang <= mouse[0] <= self.left_hang + self.width_hang and self.top_hang <= mouse[1] <= self.top_hang + self.heigth_hang:
            pygame.draw.rect(self.window, self.color_hang_hover, self.hang_rect)
        else:
            pygame.draw.rect(self.window, self.color_hang, self.hang_rect)

        #pun text pe buton
        self.hang_button = self.font.render('Hangman', True, BLACK)
        self.window.blit(self.hang_button, (self.left_hang + 15, self.top_hang + 20))

        if self.left_guess <= mouse[0] <= self.left_guess + self.width_guess and self.top_guess <= mouse[1] <= self.top_guess + self.heigth_guess:
            pygame.draw.rect(self.window, self.color_guess_hover, self.guess_rect)
        else:
            pygame.draw.rect(self.window, self.color_guess, self.guess_rect)

        #pun text pe buton
        self.guess_button = self.font.render('Guess the Number', True, BLACK)
        self.window.blit(self.guess_button, (self.left_guess + 15, self.top_guess + 20))


        pygame.display.update()

        pygame.time.Clock().tick(60)

        

    def run(self):
        while True:
            self.input()
            self.update()
            self.draw()




if __name__ == "__main__":
    menu = Menu()
    menu.run()