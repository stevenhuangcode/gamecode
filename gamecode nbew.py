# game
import pygame
import random

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
NUM_ENEMIES = 5
TITLE = "lapras life-cycle"


# create player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        # call super constructor
        super().__init__()

        # get image and flip orientation
        self.lapras_left = pygame.image.load("./images/lapras.png")
        self.lapras_right = pygame.transform.flip(self.lapras_left, True, False)
        self.image = self.lapras_left

        # scale to 64
        self.lapras_left = pygame.transform.scale(self.lapras_left, (64, 64))
        self.lapras_right = pygame.transform.scale(self.lapras_right, (64, 64))

        # make the hitbox
        self.rect = self.lapras_right.get_rect()

        # set speed
        self.vel_x = 0
        self.vel_y = 0
        self.level = None

    def update(self):
        # gravity
        self.calc_grav()

        # update player to move left right
        self.rect.x += self.vel_x

        # if hitting a block, end up on the right side
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.vel_x > 0:
                self.rect.right = block.rect.left
            elif self.vel_x < 0:
                self.rect.left = block.rect.right

        # move up down
        self.rect.y += self.vel_y
        # if landing on a block, stop falling and stay on top
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.vel_y > 0:
                self.rect.bottom = block.rect.top
            elif self.vel_y < 0:
                self.rect.top = block.rect.bottom
            self.vel_y = 0

    def calc_grav(self):
        if self.vel_y == 0:
            self.vel_y = 1
        else:
            self.vel_y += .35

        # checks if at ground-level
        if self.rect.y >= HEIGHT - self.rect.height and self.vel_y >= 0:
            self.vel_y = 0
            self.rect.y = HEIGHT - self.rect.height

    def jump(self):
        # no air jumps
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # if it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= HEIGHT:
            self.vel_y = -10

    # player movement keys
    def go_left(self):
        self.vel_x = -6

    def go_right(self):
        self.vel_x = 6

    def fast_fall(self):
        self.vel_y = 8

    def stop(self):
        self.vel_x = 0

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        # call super constructor
        super().__init__()

        self.image = pygame.image.load("./images/mario.png")
        self.rect = self.image.get_rect()

        self.rect = self.image.get_rect()

    def update(self):
        # Move the enemy side-to-side
        self.x_vel = 2
        self.rect.bottom = 600

class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.image.load("./images/platform.png")

        # scale down
        self.image = pygame.transform.scale(self.image, (122, 32))
        self.rect = self.image.get_rect()


class Level():
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

        # background image
        self.background = None

        # How far this world has been scrolled left/right
        self.world_shift = 0

    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """
        # Draw the background
        screen.fill(WHITE)

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll
        everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x


# Create platforms for the level
class Level_01(Level):
    def __init__(self, player):
        # Call the parent constructor
        Level.__init__(self, player)
        self.level_limit = -1000

        # Array with width, height, x, and y of platform
        level = [[210, 70, 500, 550],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280],
                 ]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

    def draw(self, screen):
        # background for lvl 1
        background_image = pygame.image.load("./images/ocean.png")
        background_position = [0, 0]
        screen.blit(background_image, background_position)

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)


class Level_02(Level):
    def __init__(self, player):
        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1000

        # Array with type of platform, and x, y location of the platform.
        level = [[210, 30, 400, 550],
                 [210, 30, 600, 420],
                 [210, 30, 750, 290],
                 [210, 30, 920, 150],
                 ]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

    def draw(self, screen):
        # background for lvl 2
        background_image = pygame.image.load("./images/beach.jpg")

        # this image has to be scaled
        background_image = pygame.transform.scale(background_image, (800, 600))
        background_position = [0, 0]
        screen.blit(background_image, background_position)

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)


class Level_03(Level):
    def __init__(self, player):
        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1000

        # background for lvl 3
        background_image = pygame.image.load("./images/background.png")

        # Array with width, height, x, and y of platform
        level = [[210, 70, 500, 5600],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280],
                 ]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

    def draw(self, screen):
        # background for lvl 3
        background_image = pygame.image.load("./images/background.png")
        background_position = [0, 0]
        screen.blit(background_image, background_position)

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)


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
    enemy = Enemy()
    for i in range(NUM_ENEMIES):
        enemy = Enemy()
        enemy.rect.x = enemy.rect.x - random.choice([-400, -200])
        all_sprites.add(enemy)

    # ---- player variable
    player = Player()
    all_sprites.add(player)

    # Create all the levels
    level_list = []
    level_list.append(Level_01(player))
    level_list.append(Level_02(player))
    level_list.append(Level_03(player))

    # spawn-point?
    player.rect.x = 64

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
    player.level = current_level

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
                    player.image = player.lapras_left
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                    player.image = player.lapras_right
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_DOWN:
                    player.fast_fall()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.vel_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.vel_x > 0:
                    player.stop()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list) - 1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        # ----- LOGIC

        # ----- DRAW
        screen.fill(BLACK)
        current_level.draw(screen)
        all_sprites.draw(screen)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)
        all_sprites.update()
        current_level.update()

    pygame.quit()


if __name__ == "__main__":
    main()