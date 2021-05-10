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


class Hangman(GameObject):
    def __init__(self):
        self.window = pygame.display.set_mode((HANGMAN_WIDTH, HANGMAN_HEIGHT))
        pygame.display.set_caption('Hangman')

        self.text = ''
        self.guess_text = ''

        self.current_letter = ''
        
        
        self.ultra_big_font = pygame.font.Font(None, 100)
        
        self.input_font = pygame.font.SysFont('Comic Sans MS',100)
        self.letters_font = pygame.font.SysFont('Comic Sans MS',35)
        self.title_font = pygame.font.SysFont('Algerian',100)
     

        self.hang_background = pygame.image.load("papyrus.jpg")
        self.zero_img = pygame.image.load("0.jpg")
        self.zero_img = pygame.transform.scale(self.zero_img, (self.zero_img.get_size()[0] + 100, self.zero_img.get_size()[1] + 100))

        self.three_img = pygame.image.load("3.jpg")
        self.three_img = pygame.transform.scale(self.three_img, (self.three_img.get_size()[0] + 100, self.three_img.get_size()[1] + 100))

        self.five_img = pygame.image.load("5.jpg")
        self.five_img = pygame.transform.scale(self.five_img, (self.five_img.get_size()[0] + 100, self.five_img.get_size()[1] + 100))

        self.six_img = pygame.image.load("6.jpg")
        self.six_img = pygame.transform.scale(self.six_img, (self.six_img.get_size()[0] + 100, self.six_img.get_size()[1] + 100))

        self.seven_img = pygame.image.load("7.jpg")
        self.seven_img = pygame.transform.scale(self.seven_img, (self.seven_img.get_size()[0] + 100, self.seven_img.get_size()[1] + 100))

        self.eight_img = pygame.image.load("8.jpg")
        self.eight_img = pygame.transform.scale(self.eight_img, (self.eight_img.get_size()[0] + 100, self.eight_img.get_size()[1] + 100))

        self.nine_img = pygame.image.load("9.jpg")
        self.nine_img = pygame.transform.scale(self.nine_img, (self.nine_img.get_size()[0] + 100, self.nine_img.get_size()[1] + 100))

        self.ten_img = pygame.image.load("10.jpg")
        self.ten_img = pygame.transform.scale(self.ten_img, (self.ten_img.get_size()[0] + 100, self.ten_img.get_size()[1] + 100))



        self.input_box = pygame.Rect(100, 400, 200, 200)
        self.active_box = False

        self.color_inactive = (64, 64, 64)
        self.color_active = (224, 224, 224)

        self.nr_lives = 6

        self.won = False
        self.lost = False
        self.timer_index = 0

        # cuvantul este citit dintr-un fisier unde se afla cuvinte pe prima linie separate prin spatii albe
        with open("hangman_input.txt") as file:
            lines = file.readlines()

        words = lines[randrange(len(lines))].strip("\n")
        words = words.split()
        
        self.guess_text = words[randrange(len(words))]
        print("de ghicit: " + self.guess_text)

        #lista de tupluri (litera, casuta litera, ne/ghicit)
        self.letters= []

        for i in range(len(self.guess_text)):
            self.letters.append( (self.guess_text[i], pygame.Rect(10 + 100 * i, 200, 50 , 50), False) )

    
       
        #putem sa ghicim atata timp cat nu am completat spanzuratoarea
        self.active = True
        self.count = 0

        #Menu Button
        self.color_menu = (203, 195, 227)
        self.color_menu_hover = (140, 106, 189)
        self.left_menu = HANGMAN_WIDTH / 2 - 200
        self.top_menu = HANGMAN_HEIGHT / 2 + 100
        self.width_menu = 300
        self.heigth_menu = 120
        self.menu_rect = pygame.Rect(self.left_menu, self.top_menu, self.width_menu, self.heigth_menu)


                

    def input(self):
        #pentru inchiderea meniului
        for event in pygame.event.get():
            #activarea buttonului de inchidere
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #prin escape revenim la pagina anterioara (de menu)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menu = Menu()
                    menu.run()
                    pygame.quit()
                    sys.exit()
                if self.active_box:
                    if event.key == pygame.K_RETURN:
                        if len(self.text) > 0:
                            if self.text in self.guess_text:
                                pos = self.guess_text.find(self.text)
                                while pos != -1:
                                    self.letters[pos] = (self.letters[pos][0], self.letters[pos][1], True)
                                    pos = self.guess_text.find(self.text, pos + 1, len(self.guess_text))
                                just_won = True
                                for k in self.letters:
                                    if not k[2]:
                                        just_won = False
                                if just_won:
                                    self.won = True
                            else:
                                self.nr_lives -= 1
                                if self.nr_lives == 0:
                                    self.lost = True
                            print(self.text)
                        self.text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.current_letter = event.unicode.upper()
                        if len(self.text) >= 1:
                            self.text = self.text[:-1]
                        self.text += self.current_letter
                        
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    self.active_box = not self.active_box
                else:
                    self.active_box = False
                if self.menu_rect.collidepoint(event.pos):
                    if self.won or self.lost:
                        menu = Menu()
                        menu.run()
                        pygame.quit()
                        sys.exit()
                    


                


    def update(self):
        pass

    def draw(self):

        
        

        image_rect = self.hang_background.get_rect()
        self.window.fill(BLACK)
        self.window.blit(self.hang_background, image_rect)
        
        if self.nr_lives == 6:
            image_rect = self.zero_img.get_rect()
            hang_img = self.zero_img
        elif self.nr_lives == 5:
            image_rect = self.five_img.get_rect()
            hang_img = self.five_img
        elif self.nr_lives == 4:
            image_rect = self.six_img.get_rect()
            hang_img = self.six_img
        elif self.nr_lives == 3:
            image_rect = self.seven_img.get_rect()
            hang_img = self.seven_img
        elif self.nr_lives == 2:
            image_rect = self.eight_img.get_rect()
            hang_img = self.eight_img
        elif self.nr_lives == 1:
            image_rect = self.nine_img.get_rect()
            hang_img = self.nine_img
        else:
            image_rect = self.ten_img.get_rect()
            hang_img = self.ten_img


        image_rect.x = 880
        image_rect.y = 300
        self.window.blit(hang_img, image_rect)

        #titlul
        title_x_pos = HANGMAN_WIDTH / 3 - 30
        title_y_pos = 30
        self.title = self.title_font.render('HANGMAN', True, BLACK)
        self.window.blit(self.title, (title_x_pos , title_y_pos ))

        if not self.won and not self.lost:
            for i in range(len(self.letters)):
                pygame.draw.rect(self.window, self.color_inactive, self.letters[i][1])
                text_surface = self.letters_font.render(self.letters[i][0],True, self.color_active)
                if self.letters[i][2] == True:
                    self.window.blit(text_surface, (self.letters[i][1].x + 15, self.letters[i][1].y + 5))
            
            if not self.active_box:
                pygame.draw.rect(self.window, self.color_inactive, self.input_box)
            else:
                pygame.draw.rect(self.window, self.color_active, self.input_box)

            if len(self.text) > 0:
                    text_surface = self.input_font.render(self.text,True, BLACK)
                    self.window.blit(text_surface, (self.input_box.x + 65, self.input_box.y + 20))


        if self.won:
            if self.timer_index < 1:
                self.timer_index += 0.01
                text_surface = self.title_font.render("You win", True, GREEN)
                self.window.blit(text_surface, (400, 400))
            else:
                mouse = pygame.mouse.get_pos()
                if self.left_menu <= mouse[0] <= self.left_menu + self.width_menu and self.top_menu <= mouse[1] <= self.top_menu + self.heigth_menu:
                    pygame.draw.rect(self.window, self.color_menu_hover, self.menu_rect)
                else:
                    pygame.draw.rect(self.window, self.color_menu, self.menu_rect)
                #pun text pe buton
                self.menu_button = self.letters_font.render('Back to Menu', True, self.color_inactive)
                self.window.blit(self.menu_button, (self.left_menu + 30, self.top_menu + 30))

        if self.lost:
            if self.timer_index < 1:
                self.timer_index += 0.01
                text_surface = self.title_font.render("You lost", True, RED)
                self.window.blit(text_surface, (400, 400))
            else:
                mouse = pygame.mouse.get_pos()
                if self.left_menu <= mouse[0] <= self.left_menu + self.width_menu and self.top_menu <= mouse[1] <= self.top_menu + self.heigth_menu:
                    pygame.draw.rect(self.window, self.color_menu_hover, self.menu_rect)
                else:
                    pygame.draw.rect(self.window, self.color_menu, self.menu_rect)
                #pun text pe buton
                self.menu_button = self.letters_font.render('Back to Menu', True, self.color_inactive)
                self.window.blit(self.menu_button, (self.left_menu + 30, self.top_menu + 30))

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