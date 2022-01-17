"""
Uses the pygame module to show steps for a Rush Hour game
"""

import pygame

class App():
    """ The class for the app """

    def __init__(self, n):
        """ Used to set-up the pygame app """
        self.n = n
        self.states = {}
        self.WIDTH, self.HEIGHT = 50 * self.n, 50* self.n
        self.step_num = 0
        self.last_step_num = -1

        # start the window
        pygame.init()
        self.WINDOW = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Rush Hour")

        self.FPS = 5

        # load all the assets
        self.TILE = pygame.image.load("files/rush_hour_assets/tile.png").convert()
        self.TILE = pygame.transform.scale(self.TILE, (50, 50))
        self.CAR_RED = pygame.image.load("files/rush_hour_assets/red_car.png").convert()
        self.CAR_RED = pygame.transform.scale(self.CAR_RED, (100, 50))

        # load the different cars
        self.car_assets_2x1 = {}
        for i in range(4):
            new = pygame.image.load(f"files/rush_hour_assets/car_2x1_{i}.png").convert()
            self.car_assets_2x1[i] = pygame.transform.scale(new, (100, 50))

        self.car_assets_3x1 = {}
        for i in range(3):
            new = pygame.image.load(f"files/rush_hour_assets/car_3x1_{i}.png").convert()
            self.car_assets_3x1[i] = pygame.transform.scale(new, (150, 50))

        # make the background
        self.BG = pygame.Surface((self.WIDTH, self.HEIGHT))
        for row in range(self.n):
            for col in range(self.n):
                location = row * 50, col * 50
                self.BG.blit(self.TILE, location)
        
        # load a font to display text
        self.font = pygame.font.Font(pygame.font.get_default_font(), 48)

        self.is_running = True
        self.clock = pygame.time.Clock()

    def add_state(self, cars):
        """ Call this to add the next step """
        self.states[self.last_step_num + 1] = cars
        self.last_step_num += 1

    def draw_window(self):
        """ Draws the window """
        # first draw the background
        self.WINDOW.blit(self.BG, (0, 0))

        # then draw the cars
        for car in self.states[self.step_num].values():
            
            if car.length == 2 and car.name != "X":
                # get a number for the car to select an image
                num = ord(car.get_name()[-1]) % len(self.car_assets_2x1)
                location = (car.col * 50 - 50, car.row * 50 - 50)

                # rotate the image if not horizontal
                if not car.is_horizontal:
                    self.WINDOW.blit(pygame.transform.rotate(self.car_assets_2x1[num], 90), location)
                else:
                    self.WINDOW.blit(self.car_assets_2x1[num], location)
            
            if car.length == 3:
                # get a number for the car to select an image
                num = ord(car.get_name()[-1]) % len(self.car_assets_3x1)
                location = (car.col * 50 - 50, car.row * 50 - 50)
                
                # rotate the image if not horizontal
                if not car.is_horizontal:
                    self.WINDOW.blit(pygame.transform.rotate(self.car_assets_3x1[num], 90), location)
                else:
                    self.WINDOW.blit(self.car_assets_3x1[num], location)
        
        # then place the red car
        x = self.states[self.step_num]["X"].col * 50 - 50
        y = self.states[self.step_num]["X"].row * 50 - 50
        self.WINDOW.blit(self.CAR_RED, (x, y))

        # show which step is displayed
        self.WINDOW.blit(self.font.render(f"Step: {self.step_num}", True, pygame.Color("red")), (0, 0))

        pygame.display.update()


    def run(self):
        """ The main loop to run the app """
        while self.is_running:
            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

                # use the arrow keys to go to the next/previous step
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.step_num > 0:
                        self.step_num -= 1
                    elif event.key == pygame.K_RIGHT and self.step_num < self.last_step_num:
                        self.step_num += 1
                    elif event.key == pygame.K_UP:
                        self.step_num = self.last_step_num
                    elif event.key == pygame.K_DOWN:
                        self.step_num = 0
            
            # show the screen
            self.draw_window()
        
        # stop the app
        pygame.quit()

