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
        self.image = pygame.image.load("./images/lapras.png")
        # scale to 64
        self.image = pygame.transform.scale(self.image, (64,64))

        # make the hitbox
        self.rect = self.image.get_rect()

        # set speed
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        # gravity
        self.calc_grav()

        # update player to move left right
        self.rect.x += self.vel_x
        # move up down
        self.rect.y += self.vel_y

    def calc_grav(self):
        if self.vel_y == 0:
            self.vel_y = 1
        else:
            self.vel_y += .35

        # checks if at ground-level
        if self.rect.y >= HEIGHT - self.rect.height and self.vel_y >= 0:
            self.vel_y = 0
            self.rect.y = HEIGHT - self.rect.height


    # player movement keys
    def go_left(self):
        self.vel_x = -6

    def go_right(self):
        self.vel_x = 6

    def stop(self):
        self.vel_x = 0

class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()

        self.image = pygame.image.load("./images/platform.png")
        # scale down
        self.image = pygame.transform.scale(self.image, (192, 32))

        self.rect = self.image.get_rect()

class Level():
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

        # How far this world has been scrolled left/right
        self.world_shift = 0

        def update(self):
            """ Update everything in this level."""
            self.platform_list.update()
            self.enemy_list.update()

        def draw(self, screen):
            """ Draw everything on this level. """

            # Draw the background
            self.image = pygame.image.load("./images/platform")

            # Draw all the sprite lists that we have
            #self.platform_list.draw(screen)
            #self.enemy_list.draw(screen)


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

    # Object
    platform = Platform(340,340)
    all_sprites.add(platform)

    # spawn-point?
    player.rect.x = 64

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            # movement details
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()

                #if event.key == pygame.K_UP:

                #if event.key == pygame.K_DOWN:

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.vel_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.vel_x > 0:
                    player.stop()

        # ----- LOGIC

        # ----- DRAW
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)
        all_sprites.update()


    pygame.quit()


if __name__ == "__main__":
    main()