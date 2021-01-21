# game
import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "game"

# create player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        # call super constructor
        super().__init__()

        # get image
        self.image = pygame.image.load("./images/mario.png")

        # make the hitbox
        self.rect = self.image.get_rect()

# made the guy show up but not do anything yet. explore how to flip the img and walk

def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    # Sprite Variables
    all_sprites = pygame.sprite.Group()

    # ---- enemy variable

    # ---- player variable
    player = Player()
    all_sprites.add(player)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC

        # ----- DRAW
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()