import pygame
from pygame.locals import *
from random import *
from time import sleep

pygame.init()
 
win_length = 1500
win_width = 800


win = pygame.display.set_mode((win_length , win_width))
# win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.display.set_caption("Game")

recent_player = 1

player_1_x = 250
player_1_y = 100 + 20

player_2_x = 100
player_2_y = win_width / 2

player_3_x = 250
player_3_y = (win_width - 100) - 20

ai_1_x = win_length - 250 
ai_1_y = 100 + 20

ai_2_x = win_length - 100
ai_2_y = win_width / 2

ai_3_x = win_length - 250
ai_3_y = (win_width - 100) - 20

ball_x = win_length / 2
ball_y = win_width / 2

color_red = 0
color_green = 0
color_blue = 255

color_blue_changer = -1

def update_ball():
    pygame.draw.circle(win , (255 , 0 , 0) , (ball_x , ball_y) , 20)
    pygame.draw.circle(win , (255 , 255 , 255) , (ball_x , ball_y) , 15)
    pygame.draw.circle(win , (255 , 0 , 0) , (ball_x , ball_y) , 10)

def update_playground():
    win.fill((0 , 0 , 0))
    pygame.draw.rect(win , (color_red , color_green , color_blue) , ((50 , 50) , (win_length - 100 , win_width - 100)) , 3)
    pygame.draw.rect(win , (color_red , color_green , color_blue) , ((5 , (win_width / 2) - 90) , (48 , 180)) , 3)
    pygame.draw.rect(win , (color_red , color_green , color_blue) , ((win_length - 53 , (win_width / 2) - 90) , (50 , 180)) , 3)
    pygame.draw.line(win , (color_red , color_green , color_blue) , (win_length / 2 , 50) , (win_length / 2 , win_width - 50 - 3) , 3)
    pygame.draw.circle(win , (color_red , color_green , color_blue) , (win_length / 2 , win_width / 2) , 150 , 3)
    

def update_left_side():
    pygame.draw.circle(win , (255 , 0 , 255) , (player_1_x , player_1_y) , 30 , 5)
    pygame.draw.circle(win , (255 , 0 , 255) , (player_2_x , player_2_y) , 30 , 5)
    pygame.draw.circle(win , (255 , 0 , 255) , (player_3_x , player_3_y) , 30 , 5)

def update_right_side():
    pygame.draw.circle(win , (0 , 255 , 0) , (ai_1_x , ai_1_y) , 30 , 5)
    pygame.draw.circle(win , (0 , 255 , 0) , (ai_2_x , ai_2_y) , 30 , 5)
    pygame.draw.circle(win , (0 , 255 , 0) , (ai_3_x , ai_3_y) , 30 , 5)

def find_keeper_place(ball_y , size_y , ground_y):
    return (ball_y * size_y) // ground_y

player = 0

shooter = 0 #shooter of the ball

x = 0
y = 0

distance = 20

def catching_ball_player1():
    global player , ball_x , ball_y
    if abs(ball_x - player_1_x) <= distance and abs(ball_y - player_1_y) <= distance:
        player = 1
        ball_x , ball_y = player_1_x , player_1_y
        shooter = 0

def catching_ball_player2():
    global player , ball_x , ball_y
    if abs(ball_x - player_2_x) <= distance and abs(ball_y - player_2_y) <= distance:
        player = 2
        ball_x , ball_y = player_2_x , player_2_y
        shooter = 0

def catching_ball_player3():
    global player , ball_x , ball_y
    if abs(ball_x - player_3_x) <= distance and abs(ball_y - player_3_y) <= distance:
        player = 3
        ball_x , ball_y = player_3_x , player_3_y
        shooter = 0

player_place_changer = 0
player_place_dic = None

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_r:
                shooter = player
                x = ball_x
                y = ball_y
                player = 0
                

            if event.key == K_f:
                if recent_player == 1:
                    recent_player = 3
                    if player == 1:
                        player = 3
                        ball_x = player_3_x
                        ball_y = player_3_y
                elif recent_player == 3:
                    recent_player = 1
                    if player == 3:
                        player = 1
                        ball_x = player_1_x
                        ball_y = player_1_y
                    
            
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

        if player == 0:
            if shooter != 1:
                catching_ball_player1()
            if shooter != 2:
                catching_ball_player2()
            if shooter != 3:
                catching_ball_player3()
        
        if shooter != 0:
            if abs(win_length - 50 - ball_x) >= 20 or abs(win_width / 2 - ball_y) >= 20:
                if abs(win_length - 50 - x) > abs(win_width / 2 - y):
                    ball_x += 20
                    if win_width / 2 - y < 0:
                        ball_y -= abs(win_width / 2 - y) / abs(win_length - 50 - x) * 20
                    else:
                        ball_y += abs(win_width / 2 - y) / abs(win_length - 50 - x) * 20
                else:
                    ball_x += abs(win_length - 50 - x) / abs(win_width / 2 - y) * 20
                    if win_width / 2 - y < 0:
                        ball_y -= 20
                    else:
                        ball_y += 20
            else:
                ball_x = win_length - 50
                ball_y = win_width / 2
                shooter = 0


        if recent_player == 1:
            if player_place_dic == 1 and player_1_y + player_place_changer - 20 < win_width - 100 and player_1_y + player_place_changer - 30 > 50:
                player_1_y += player_place_changer
                if player == 1:
                    ball_y = player_1_y
            elif player_place_dic == 0 and player_1_x + player_place_changer - 20 < win_length - 100 and player_1_x + player_place_changer - 30 > 50:
                player_1_x += player_place_changer
                if player == 1:
                    ball_x = player_1_x
        elif recent_player == 3:
            if player_place_dic == 1 and player_3_y + player_place_changer - 20 < win_width - 100 and player_3_y + player_place_changer - 30 > 50:
                player_3_y += player_place_changer
                if player == 3:
                    ball_y = player_3_y
            elif player_place_dic == 0 and player_3_x + player_place_changer - 20 < win_length - 100 and player_3_x + player_place_changer - 30 > 50:
                player_3_x += player_place_changer
                if player == 3:
                    ball_x = player_3_x

        if color_green < 255 and color_red == 0:
            color_green += 1

        elif color_green == 255 and color_red < 255:
            color_red += 1
        
        elif color_green > 0 and color_red == 255:
            color_green -= 1

        elif color_green == 0 and color_red > 0:
            color_red -= 1

        if color_blue == 255:
            color_blue_changer = -1
        elif color_blue == 0:
            color_blue_changer = 1

        color_blue += color_blue_changer


        if ball_x <= win_length / 2:
            if ai_2_y - (win_width / 2) >= 1:
                ai_2_y -= 1
            elif ai_2_y - (win_width / 2) <= -1:
                ai_2_y += 1

            if abs(player_2_y - (find_keeper_place(ball_y , 160 , win_width - 100) + win_width / 2 - 90)) <= 20 and player != 1 and player != 3:
                player_2_y = (find_keeper_place(ball_y , 160 , win_width - 100) + win_width / 2 - 90)
            elif abs(player_2_y - (find_keeper_place(ball_y , 160 , win_width - 100) + win_width / 2 - 90)) > 20 and player != 1 and player != 3:
                if player_2_y - (find_keeper_place(ball_y , 160 , win_width - 100) + win_width / 2 - 90) < 0:
                    player_2_y += 5
                else:
                    player_2_y -= 5
        
        elif ball_x > win_length / 2:
            if player_2_y - (win_width / 2) >= 1:
                player_2_y -= 1
            elif player_2_y - (win_width / 2) <= -1:
                player_2_y += 1

            if abs(ai_2_y - (find_keeper_place(ball_y , 160 , win_width - 100) + win_width / 2 - 90)) <= 20 and player != 4 and player != 6:
                ai_2_y = (find_keeper_place(ball_y , 160 , win_width - 100) + win_width / 2 - 90)
            elif abs(ai_2_y - (find_keeper_place(ball_y , 160 , win_width - 100) + win_width / 2 - 90)) > 20 and player != 4 and player != 6:
                if ai_2_y - (find_keeper_place(ball_y , 160 , win_width - 100) + win_width / 2 - 90) < 0:
                    ai_2_y += 5
                else:
                    ai_2_y -= 5

        update_playground()
        update_ball()
        update_left_side()
        update_right_side()
        pygame.display.update()
        sleep(0.01)
