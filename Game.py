import pygame

pygame.init()

def load_playground():
    global win , win_length , win_width
    win_length = 1500
    win_width = 800
    win = pygame.display.set_mode((win_length , win_width))
    pygame.display.set_caption("Game")

    global player_1_x , player_2_x , player_3_x , player_1_y , player_2_y , player_3_y
    global ai_1_x , ai_2_x , ai_3_x , ai_1_y , ai_2_y , ai_3_y

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

    pygame.draw.rect(win , (0 , 255 , 255) , ((50 , 50) , (win_length - 100 , win_width - 100)) , 3)
    pygame.draw.rect(win , (0 , 255 , 255) , ((50 , (win_width / 2) - 75) , (50 , 150)) , 3)
    pygame.draw.rect(win , (0 , 255 , 255) , ((win_length - 100 , (win_width / 2) - 75) , (50 , 150)) , 3)
    

def load_ball():
    pygame.draw.circle(win , (255 , 255 , 255) , (win_length / 2 , win_width / 2) , 20)

def load_left_side():
    pygame.draw.circle(win , (255 , 0 , 255) , (player_1_x , player_1_y) , 30 , 5)
    pygame.draw.circle(win , (255 , 0 , 255) , (player_2_x , player_2_y) , 30 , 5)
    pygame.draw.circle(win , (255 , 0 , 255) , (player_3_x , player_3_y) , 30 , 5)

def load_right_side():
    pygame.draw.circle(win , (0 , 255 , 0) , (ai_1_x , ai_1_y) , 30 , 5)
    pygame.draw.circle(win , (0 , 255 , 0) , (ai_2_x , ai_2_y) , 30 , 5)
    pygame.draw.circle(win , (0 , 255 , 0) , (ai_3_x , ai_3_y) , 30 , 5)

def running():
    load_playground()
    load_ball()
    load_left_side()
    load_right_side()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()


if __name__ == "__main__":
    running()
