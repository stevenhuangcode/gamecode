# my platform game
import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "platform"

# create player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        # call super constructor
        super().__init__()

        # Set height, width
        self.image.load(R_mario)

        self.rect = self.image.get_rect()

        # set velocity
        self.vel_x = 0
        self.vel_y = 0

        R_mario = pygame.image.load("mario.png")
        L_mario = pygame.transform.flip(R_mario, True, False)

        self.image = pygame.image.load("./images/mariopng")






def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    player = Player()
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC

        # ----- DRAW
        screen.fill(BLACK)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()