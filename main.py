from utils import *

pygame.init()

# screen
WIDTH, HEIGHT = 500, 500
pygame.display.set_icon(pygame.image.load('assets/cross.png'))
pygame.display.set_caption("Tic Tac Toe 2")
screen = pygame.display.set_mode((WIDTH, HEIGHT+20))
tacgame = Game(screen, WIDTH, HEIGHT)

# Main loop
while 1:
    screen.fill((8, 238, 249))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            tacgame.trackpos(pos)
            
    tacgame.draw_screen()
    pygame.display.update()