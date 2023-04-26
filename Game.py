import pygame
from pygame.locals import *
from random import *

pygame.init()
 
win_length = 1500
win_width = 800
win = pygame.display.set_mode((win_length , win_width))
pygame.display.set_caption("Game")

recent_player = 1

player_1_x = 250
player_1_y = 100 + 20

player_2_x = 200
player_2_y = win_width / 2

player_3_x = 250
player_3_y = (win_width - 100) - 20

ai_1_x = win_length - 250 
ai_1_y = 100 + 20

ai_2_x = win_length - 200
ai_2_y = win_width / 2

ai_3_x = win_length - 250
ai_3_y = (win_width - 100) - 20

ball_x = win_length / 2
ball_y = win_width / 2

pygame.draw.circle(win , (255 , 255 , 255) , (ball_x , ball_y) , 20)
pygame.draw.rect(win , (0 , 255 , 255) , ((50 , 50) , (win_length - 100 , win_width - 100)) , 3)
pygame.draw.rect(win , (0 , 255 , 255) , ((50 , (win_width / 2) - 75) , (50 , 150)) , 3)
pygame.draw.rect(win , (0 , 255 , 255) , ((win_length - 100 , (win_width / 2) - 75) , (50 , 150)) , 3)


def update_ball():
    pygame.draw.circle(win , (255 , 255 , 255) , (ball_x , ball_y) , 20)

def update_playground():
    win.fill((0 , 0 , 0))
    pygame.draw.rect(win , (0 , 255 , 255) , ((50 , 50) , (win_length - 100 , win_width - 100)) , 3)
    pygame.draw.rect(win , (0 , 255 , 255) , ((50 , (win_width / 2) - 75) , (50 , 150)) , 3)
    pygame.draw.rect(win , (0 , 255 , 255) , ((win_length - 100 , (win_width / 2) - 75) , (50 , 150)) , 3)
    

def update_left_side():
    pygame.draw.circle(win , (255 , 0 , 255) , (player_1_x , player_1_y) , 30 , 5)
    pygame.draw.circle(win , (255 , 0 , 255) , (player_2_x , player_2_y) , 30 , 5)
    pygame.draw.circle(win , (255 , 0 , 255) , (player_3_x , player_3_y) , 30 , 5)

def update_right_side():
    pygame.draw.circle(win , (0 , 255 , 0) , (ai_1_x , ai_1_y) , 30 , 5)
    pygame.draw.circle(win , (0 , 255 , 0) , (ai_2_x , ai_2_y) , 30 , 5)
    pygame.draw.circle(win , (0 , 255 , 0) , (ai_3_x , ai_3_y) , 30 , 5)

player = 0 # 0 : No Player , 1: Player 1 , 2: Player 2 , 3: Player 3

def catching_ball_player1():
    if abs(ball_x - player_1_x) <= 20 and abs(ball_y - player_1_y) <= 20:
        global player
        player = 1

def catching_ball_player2():
    if abs(ball_x - player_2_x) <= 20 and abs(ball_y - player_2_y) <= 20:
        global player
        player = 2

def catching_ball_player3():
    if abs(ball_x - player_3_x) <= 20 and abs(ball_y - player_3_y) <= 20:
        global player
        player = 3

player_place_changer = 0
player_place_dic = None

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_f:
                if recent_player <= 2:
                    recent_player += 1
                else:
                    recent_player = 1
            
            if event.key == K_w:
                player_place_changer = -10
                player_place_dic = 1
            elif event.key == K_s:
                player_place_changer = 10
                player_place_dic = 1
            elif event.key == K_d:
                player_place_changer = 10
                player_place_dic = 0
            elif event.key == K_a:
                player_place_changer = -10
                player_place_dic = 0
            
        elif event.type == KEYUP:
            if event.key == K_w or event.key == K_s or event.key == K_d or event.key == K_a:
                player_place_changer = 0
        
        catching_ball_player1()
        catching_ball_player2()
        catching_ball_player3()

        if recent_player == 1:
            if player_place_dic == 1 and player_1_y + player_place_changer - 20 < win_width - 100 and player_1_y + player_place_changer - 30 > 50:
                player_1_y += player_place_changer
                if player == 1:
                    ball_y += player_place_changer
            elif player_place_dic == 0 and player_1_x + player_place_changer - 20 < win_length - 100 and player_1_x + player_place_changer - 30 > 50:
                player_1_x += player_place_changer
                if player == 1:
                    ball_x += player_place_changer
        elif recent_player == 2:
            if player_place_dic == 1 and player_2_y + player_place_changer - 20 < win_width - 100 and player_2_y + player_place_changer - 30 > 50:
                player_2_y += player_place_changer
                if player == 2:
                    ball_y += player_place_changer
            elif player_place_dic == 0 and player_2_x + player_place_changer - 20 < win_length - 100 and player_2_x + player_place_changer - 30 > 50:
                player_2_x += player_place_changer
                if player == 2:
                    ball_x += player_place_changer
        else:
            if player_place_dic == 1 and player_3_y + player_place_changer - 20 < win_width - 100 and player_3_y + player_place_changer - 30 > 50:
                player_3_y += player_place_changer
                if player == 3:
                    ball_y += player_place_changer
            elif player_place_dic == 0 and player_3_x + player_place_changer - 20 < win_length - 100 and player_3_x + player_place_changer - 30 > 50:
                player_3_x += player_place_changer
                if player == 3:
                    ball_x += player_place_changer
        
        update_playground()
        update_ball()
        update_left_side()
        update_right_side()
        pygame.display.update()
        pygame.time.Clock()
