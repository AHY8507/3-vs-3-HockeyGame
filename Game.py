import pygame
from pygame.locals import *
from random import *
from time import sleep

pygame.init()
 
win_length = 1500
win_width = 700

key_index = 0
key_event_number = 0

key_list = [[K_w , K_a , K_s , K_d , K_q , K_e , K_f],
[K_u , K_h , K_j , K_k , K_y , K_i , K_l],
[K_g , K_v , K_b , K_n , K_f , K_h , K_m],
[K_s , K_a , K_w , K_d , K_q , K_e , K_f],
[K_s , K_d , K_w , K_a , K_q , K_e , K_f],
[K_j , K_h , K_u , K_k , K_y , K_l , K_i]]

win = pygame.display.set_mode((win_length , win_width))

pygame.display.set_caption("Game")

recent_player = 1

player_score = 0
ai_score = 0

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

def start_game_again():
    global key_index , key_event_number , y , x , recent_player , player_1_x , player_1_y , player_2_x , player_2_y , player_3_x , player_3_y , ai_1_x , ai_1_y , ai_2_x , ai_2_y , ai_3_x , ai_3_y , ball_x , ball_y , player , shooter
    player_place_changer = 0
    player_place_dic = None
    player = 0
    recent_player = 1
    shooter = 0

    win_length = 1500
    win_width = 700

    x = 0
    y = 0

    distance = 20

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

    update_playground()
    update_ball()
    update_left_side()
    update_right_side()
    pygame.display.update()

    print("1")
    sleep(1)
    print("2")
    sleep(1)
    print("3")
    sleep(1)

player = 0

shooter = 0 

x = 0
y = 0

distance = 20



def catching_ball_player1():
    global player , ball_x , ball_y , shooter , recent_player
    if player == 0:
        if shooter != 1:
            if abs(ball_x - player_1_x) <= distance and abs(ball_y - player_1_y) <= distance:
                player = 1
                ball_x , ball_y = player_1_x , player_1_y
                shooter = 0
                recent_player = 1

def catching_ball_player2():
    global player , ball_x , ball_y , shooter , recent_player , player_score , ai_score
    if ball_x == 50 and ball_y == win_width / 2:
        random_number = randint(0, 100)
        if random_number <= 70:
            player = 2
            ball_x , ball_y = player_2_x , player_2_y
            shooter = 0
            recent_player = 2
            update_playground()
            update_ball()
            update_left_side()
            update_right_side()
            pygame.display.update()

            sleep(1)

            player = 1
            ball_x , ball_y = player_1_x , player_1_y
            shooter = 0
            recent_player = 1
    
        else:
            ai_score += 1
            print("AI : " + str(ai_score) + "  ,  " + "Player : " + str(player_score))
            print("AI goal!!!")
            start_game_again()


def catching_ball_player3():
    global player , ball_x , ball_y , shooter , recent_player
    if player == 0:
        if shooter != 3:
            if abs(ball_x - player_3_x) <= distance and abs(ball_y - player_3_y) <= distance:
                player = 3
                ball_x , ball_y = player_3_x , player_3_y
                shooter = 0
                recent_player = 3

def catching_ball_ai1():
    global player , ball_x , ball_y , shooter , recent_player
    if player == 0:
        if shooter != 1:
            if abs(ball_x - ai_1_x) <= distance and abs(ball_y - ai_1_y) <= distance:
                player = 4
                ball_x , ball_y = ai_1_x , ai_1_y
                shooter = 0


def catching_ball_ai2():
    global player , ball_x , ball_y , shooter , recent_player , player_score , ai_score
    if ball_x == win_length - 50 and ball_y == win_width / 2:
        random_number = randint(0, 100)
        if random_number <= 70:
            player = 5
            ball_x , ball_y = ai_2_x , ai_2_y
            shooter = 0
            update_playground()
            update_ball()
            update_left_side()
            update_right_side()
            pygame.display.update()

            sleep(1)

            player = 4
            ball_x , ball_y = ai_1_x , ai_1_y
            shooter = 0
        
        else:
            player_score += 1
            print("AI : " + str(ai_score) + "  ,  " + "Player : " + str(player_score))
            print("Player goal!!!")
            start_game_again()


def catching_ball_ai3():
    global player , ball_x , ball_y , shooter , recent_player
    if player == 0:
        if shooter != 6:
            if abs(ball_x - ai_3_x) <= distance and abs(ball_y - ai_3_y) <= distance:
                player = 6
                ball_x , ball_y = ai_3_x , ai_3_y
                shooter = 0

def player_alogorithm():
    global recent_player , player_1_x , player_1_y , player_2_x , player_2_y , player_3_x , player_3_y , ai_1_x , ai_1_y , ai_2_x , ai_2_y , ai_3_x , ai_3_y , ball_x , ball_y , player , shooter
    if recent_player == 1:
        if abs(player_3_x - ball_x) > 40:
            if player_3_x > ball_x:
                player_3_x -= 6
            else:
                player_3_x += 6

        if abs(player_3_y - ball_y) > 40:
            if player_3_y > ball_y:
                player_3_y -= 6
            else:
                player_3_y += 6
    else:
        if abs(player_1_x - ball_x) > 40:
            if player_1_x > ball_x:
                player_1_x -= 6
            else:
                player_1_x += 6

        if abs(player_1_y - ball_y) > 40:
            if player_1_y > ball_y:
                player_1_y -= 6
            else:
                player_1_y += 6

def player_algorithm_ai():
    global recent_player , player_1_x , player_1_y , player_2_x , player_2_y , player_3_x , player_3_y , ai_1_x , ai_1_y , ai_2_x , ai_2_y , ai_3_x , ai_3_y , ball_x , ball_y , player , shooter
    if player == 6:
        if recent_player == 1:
            if abs(player_3_x - ai_1_x) > 40:
                if player_3_x > ai_1_x:
                    player_3_x -= 6
                else:
                    player_3_x += 6

            if abs(player_3_y - ai_1_y) > 40:
                if player_3_y > ai_1_y:
                    player_3_y -= 6
                else:
                    player_3_y += 6
        
        else:
            if abs(player_1_x - ai_1_x) > 40:
                if player_1_x > ai_1_x:
                    player_1_x -= 6
                else:
                    player_1_x += 6

            if abs(player_1_y - ai_1_y) > 40:
                if player_1_y > ai_1_y:
                    player_1_y -= 6
                else:
                    player_1_y += 6
    
    elif player == 4:
        if recent_player == 1:
            if abs(player_3_x - ai_3_x) > 40:
                if player_3_x > ai_3_x:
                    player_3_x -= 6
                else:
                    player_3_x += 6

            if abs(player_3_y - ai_3_y) > 40:
                if player_3_y > ai_3_y:
                    player_3_y -= 6
                else:
                    player_3_y += 6
        
        else:
            if abs(player_1_x - ai_3_x) > 40:
                if player_1_x > ai_3_x:
                    player_1_x -= 6
                else:
                    player_1_x += 6

            if abs(player_1_y - ai_3_y) > 40:
                if player_1_y > ai_3_y:
                    player_1_y -= 6
                else:
                    player_1_y += 6


def ai_algorithm_ai():
    global recent_player , player_1_x , player_1_y , player_2_x , player_2_y , player_3_x , player_3_y , ai_1_x , ai_1_y , ai_2_x , ai_2_y , ai_3_x , ai_3_y , ball_x , ball_y , player , shooter
    if player == 4:
        if recent_player == 1:
            if abs(player_1_x - ai_3_x) > 40:
                if player_1_x > ai_3_x:
                    ai_3_x += 8
                else:
                    ai_3_x -= 8

            elif abs(player_1_y - ai_3_y) > 40:
                if player_1_y > ai_3_y:
                    ai_3_y += 8
                else:
                    ai_3_y -= 8
        else:
            if abs(player_3_x - ai_3_x) > 40:
                if player_3_x > ai_3_x:
                    ai_3_x += 8
                else:
                    ai_3_x -= 8

            elif abs(player_3_y - ai_3_y) > 40:
                if player_3_y > ai_3_y:
                    ai_3_y += 8
                else:
                    ai_3_y -= 8
        
        
        if ai_1_x <= 200:
            ball_x = 50
            ball_y = win_width / 2

        else:
            if abs(player_1_x - ai_1_x) <= 20 and abs(player_1_y - ai_1_y) <= 20:
                random_number = randint(0 , 100)
                if random_number <= 40:
                    player = 6
                else:
                    ai_1_x -= 10
                    ball_x = ai_1_x
                    random_y = randint(1 , 2)
                    if random_y == 1:
                        if ai_1_y - 10 - 30 > 50:
                            ai_1_y -= 10
                            ball_y = ai_1_y

                    else:
                        if ai_1_y + 10 + 20 < win_width - 100:
                            ai_1_y += 10
                            ball_y = ai_1_y
            
            elif abs(player_3_x - ai_1_x) <= 20 and abs(player_3_y - ai_1_y) <= 20:
                random_number = randint(0 , 100)
                if random_number <= 40:
                    player = 4
                else:
                    ai_1_x -= 10
                    ball_x = ai_1_x
                    random_y = randint(1 , 2)
                    if random_y == 1:
                        if ai_1_y - 10 - 30 > 50:
                            ai_1_y -= 10
                            ball_y = ai_1_y

                    else:
                        if ai_1_y + 10 + 20 < win_width - 100:
                            ai_1_y += 10
                            ball_y = ai_1_y
            
            else:
                ai_1_x -= 10
                ball_x = ai_1_x
                random_y = randint(1 , 2)
                if random_y == 1:
                    if ai_1_y - 10 - 30 > 50:
                        ai_1_y -= 10
                        ball_y = ai_1_y

                else:
                    if ai_1_y + 10 + 20 < win_width - 100:
                        ai_1_y += 10
                        ball_y = ai_1_y
                    
    
    if player == 6:
        if recent_player == 1:
            if abs(player_1_x - ai_1_x) > 40:
                if player_1_x > ai_1_x:
                    ai_1_x += 8
                else:
                    ai_1_x -= 8

            elif abs(player_1_y - ai_1_y) > 40:
                if player_1_y > ai_1_y:
                    ai_1_y += 8
                else:
                    ai_1_y -= 8
        else:
            if abs(player_3_x - ai_1_x) > 40:
                if player_3_x > ai_1_x:
                    ai_1_x += 8
                else:
                    ai_1_x -= 8

            elif abs(player_3_y - ai_1_y) > 40:
                if player_3_y > ai_1_y:
                    ai_1_y += 8
                else:
                    ai_1_y -= 8

        
        if ai_3_x <= 200:
            ball_x = 50
            ball_y = win_width / 2
        
        else:
            if abs(player_3_x - ai_3_x) <= 20 and abs(player_3_y - ai_3_y) <= 20:
                random_number = randint(0 , 100)
                if random_number <= 40:
                    player = 4
                else:
                    ai_3_x -= 10
                    ball_x = ai_3_x
                    random_y = randint(1 , 2)
                    if random_y == 1:
                        if ai_3_y - 10 - 30 > 50:
                            ai_3_y -= 10
                            ball_y = ai_3_y

                    else:
                        if ai_3_y + 10 + 20 < win_width - 100:
                            ai_3_y += 10
                            ball_y = ai_3_y
            
            elif abs(player_1_x - ai_3_x) <= 20 and abs(player_1_y - ai_3_y) <= 20:
                random_number = randint(0 , 100)
                if random_number <= 40:
                    player = 6
                else:
                    ai_3_x -= 10
                    ball_x = ai_3_x
                    random_y = randint(1 , 2)
                    if random_y == 1:
                        if ai_3_y - 10 - 30 > 50:
                            ai_3_y -= 10
                            ball_y = ai_3_y 

            else:
                ai_3_x -= 10
                ball_x = ai_3_x
                random_y = randint(1 , 2)
                if random_y == 1:
                    if ai_3_y - 10 - 30 > 50:
                        ai_3_y -= 10
                        ball_y = ai_3_y

                else:
                    if ai_3_y + 10 + 20 < win_width - 100:
                        ai_3_y += 10
                        ball_y = ai_3_y


def ai_algorithm_player_off():
    global recent_player , player_1_x , player_1_y , player_2_x , player_2_y , player_3_x , player_3_y , ai_1_x , ai_1_y , ai_2_x , ai_2_y , ai_3_x , ai_3_y , ball_x , ball_y , player , shooter
    
    if abs(player_1_x - ai_1_x) > 10:
        if player_1_x > ai_1_x:
            ai_1_x += 8
        else:
            ai_1_x -= 8

    if abs(player_1_y - ai_1_y) > 10:
        if player_1_y > ai_1_y:
            ai_1_y += 8
        else:
            ai_1_y -= 8

    if abs(ball_x - ai_3_x) > 10:
        if ball_x > ai_3_x:
            ai_3_x += 8
        else:
            ai_3_x -= 8

    if abs(ball_y - ai_3_y) > 10:
        if ball_y > ai_3_y:
            ai_3_y += 8
        else:
            ai_3_y -= 8


def ai_algorithm_player_on():
    global recent_player , player_1_x , player_1_y , player_2_x , player_2_y , player_3_x , player_3_y , ai_1_x , ai_1_y , ai_2_x , ai_2_y , ai_3_x , ai_3_y , ball_x , ball_y , player , shooter

    if abs(player_3_x - ai_3_x) > 10:
        if player_3_x > ai_3_x:
            ai_3_x += 8
        else:
            ai_3_x -= 8

    if abs(player_3_y - ai_3_y) > 10:
        if player_3_y > ai_3_y:
            ai_3_y += 8
        else:
            ai_3_y -= 8

    if abs(player_1_x - ai_1_x) > 10:
        if player_1_x > ai_1_x:
            ai_1_x += 8
        else:
            ai_1_x -= 8

    if abs(player_1_y - ai_1_y) > 10:
        if player_1_y > ai_1_y:
            ai_1_y += 8
        else:
            ai_1_y -= 8


    if player == 1:
        if abs(player_1_y - ai_1_y) <= 10 and abs(player_1_x - ai_1_x) <= 10:
            random_number = randint(0 , 100)
            if random_number <= 20:
                player = 4
                ball_x , ball_y = ai_1_x , ai_1_y
                shooter = 0

    elif player == 2:
        pass

    elif player == 3:
        if abs(player_3_y - ai_3_y) <= 10 and abs(player_3_x - ai_3_x) <= 10:
            random_number = randint(0 , 100)
            if random_number <= 20:
                player = 6
                ball_x , ball_y = ai_3_x , ai_3_y
                shooter = 0



player_place_changer = 0
player_place_dic = None

start_game_again()

while True:
    for event in pygame.event.get():
        if key_event_number % 500 == 0:
            key_index = randint(0 , 5)
            if key_index == 0:
                print("up : w , left : a , down : s , right : d , shoot : q , get ball : e , pass : f") 
            elif key_index == 1:
                print("up : u , left : h , down : j , right : k , shoot : y , get ball : i , pass : l")
            elif key_index == 2:
                print("up : g , left : v , down : b , right : n , shoot : f , get ball : h , pass : m")
            elif key_index == 3:
                print("up : s , left : a , down : w , right : d , shoot : q , get ball : e , pass : f")
            elif key_index == 4:
                print("up : s , left : d , down : w , right : a , shoot : q , get ball : e , pass : f")
            elif key_index == 5:
                print("up : j , left : h , down : u , right : k , shoot : y , get ball : l , pass : i")

        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == key_list[key_index][4]:
                shooter = player
                x = ball_x
                y = ball_y
                player = 0
                

            if event.key == key_list[key_index][5]:
                if player == 4 or player == 6:
                    if recent_player == 1 and abs(ball_x - player_1_x) <= distance and abs(ball_y - player_1_y) <= distance:
                        ball_x , ball_y = player_1_x , player_1_y
                        player = 1
                        recent_player = 1
                    elif recent_player == 3 and abs(ball_x - player_3_x) <= distance and abs(ball_y - player_3_y) <= distance:
                        ball_x , ball_y = player_3_x , player_3_y
                        player = 3
                        recent_player = 3

            if event.key == key_list[key_index][6]:
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
                    
            
            if event.key == key_list[key_index][0]:
                player_place_changer = -10
                player_place_dic = 1
            elif event.key == key_list[key_index][2]:
                player_place_changer = 10
                player_place_dic = 1
            elif event.key == key_list[key_index][3]:
                player_place_changer = 10
                player_place_dic = 0
            elif event.key == key_list[key_index][1]:
                player_place_changer = -10
                player_place_dic = 0
            
        elif event.type == KEYUP:
            if event.key == key_list[key_index][0] or event.key == key_list[key_index][2] or event.key == key_list[key_index][3] or event.key == key_list[key_index][1]:
                player_place_changer = 0

        catching_ball_player1()
        catching_ball_player2()
        catching_ball_player3()
        catching_ball_ai1()
        catching_ball_ai2()
        catching_ball_ai3()
        
        if player == 1 or player == 3:
            ai_algorithm_player_on()
            player_alogorithm()

        if player == 0:
            ai_algorithm_player_off()
            player_alogorithm()

        if player == 4 or player == 6:
            ai_algorithm_ai()
            player_algorithm_ai()

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

        key_event_number += 1
        update_playground()
        update_ball()
        update_left_side()
        update_right_side()
        pygame.display.update()
