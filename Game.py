import pygame

pygame.init()

def load_playground():
    global win , win_length , win_width
    win_length = 1200
    win_width = 800
    win = pygame.display.set_mode((win_length , win_width))
    pygame.display.set_caption("Game")

    pygame.draw.rect(win , (0 , 255 , 255) , ((50 , 50) , (win_length - 100 , win_width - 100)) , 3)
    pygame.draw.rect(win , (0 , 255 , 255) , ((50 , (win_width / 2) - 75) , (50 , 150)) , 3)
    pygame.draw.rect(win , (0 , 255 , 255) , ((win_length - 100 , (win_width / 2) - 75) , (50 , 150)) , 3)
    

def load_ball():
    pygame.draw.circle(win , (255 , 255 , 255) , (win_length / 2 , win_width / 2) , 20)

def load_left_side():
    pygame.draw.circle(win , (255 , 0 , 255) , (250 , 100 + 20) , 30 , 5)
    pygame.draw.circle(win , (255 , 0 , 255) , (200 , win_width / 2) , 30 , 5)
    pygame.draw.circle(win , (255 , 0 , 255) , (250 , (win_width - 100) - 20) , 30 , 5)

def load_right_side():
    pygame.draw.circle(win , (0 , 255 , 0) , (win_length - 250 , 100 + 20) , 30 , 5)
    pygame.draw.circle(win , (0 , 255 , 0) , (win_length - 200 , win_width / 2) , 30 , 5)
    pygame.draw.circle(win , (0 , 255 , 0) , (win_length - 250 , (win_width - 100) - 20) , 30 , 5)

def running():
    while True:
        load_playground()
        load_ball()
        load_left_side()
        load_right_side()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()


if __name__ == "__main__":
    running()
