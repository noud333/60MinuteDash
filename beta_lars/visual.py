"""
Uses the pygame module to show steps for a Rush Hour game
"""

import pygame

class App():
    """ The class for the app """

    def __init__(self, n, cars):
        self.n = n
        self.cars = cars
        self.WIDTH, self.HEIGHT = 50 * self.n, 50* self.n

        pygame.init()
        self.WINDOW = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Rush Hour")

        self.FPS = 5

        # load all the assets
        self.TILE = pygame.image.load("files/rush_hour_assets/tile.png").convert()
        self.TILE = pygame.transform.scale(self.TILE, (50, 50))
        self.CAR_RED = pygame.image.load("files/rush_hour_assets/red_car.png").convert()
        self.CAR_RED = pygame.transform.scale(self.CAR_RED, (100, 50))

        self.car_assets_2x1 = {}
        self.CAR_2x1_0 = pygame.image.load("files/rush_hour_assets/car_2x1_0.png").convert()
        self.car_assets_2x1[0] = pygame.transform.scale(self.CAR_2x1_0, (100, 50))
        self.CAR_2x1_1 = pygame.image.load("files/rush_hour_assets/car_2x1_1.png").convert()
        self.car_assets_2x1[1] = pygame.transform.scale(self.CAR_2x1_1, (100, 50))
        self.CAR_2x1_2 = pygame.image.load("files/rush_hour_assets/car_2x1_2.png").convert()
        self.car_assets_2x1[2] = pygame.transform.scale(self.CAR_2x1_2, (100, 50))
        self.CAR_2x1_3 = pygame.image.load("files/rush_hour_assets/car_2x1_3.png").convert()
        self.car_assets_2x1[3] = pygame.transform.scale(self.CAR_2x1_3, (100, 50))

        self.car_assets_3x1 = {}
        self.CAR_3x1_0 = pygame.image.load("files/rush_hour_assets/car_3x1_0.png").convert()
        self.car_assets_3x1[0] = pygame.transform.scale(self.CAR_3x1_0, (150, 50))
        self.CAR_3x1_1 = pygame.image.load("files/rush_hour_assets/car_3x1_1.png").convert()
        self.car_assets_3x1[1] = pygame.transform.scale(self.CAR_3x1_1, (150, 50))
        self.CAR_3x1_2 = pygame.image.load("files/rush_hour_assets/car_3x1_2.png").convert()
        self.car_assets_3x1[2] = pygame.transform.scale(self.CAR_3x1_2, (150, 50)) 

        self.is_running = True
        self.clock = pygame.time.Clock()

    def new_grid(self, grid):
        self.grid = grid

    def draw_window(self):
        """ Draws the window """
        # first draw the background
        self.WINDOW.fill((255, 255, 255))
        for row in range(self.n):
            for col in range(self.n):
                location = row * 50, col * 50
                self.WINDOW.blit(self.TILE, location)

        # then draw the cars
        for car in self.cars.values():
            
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
        x = self.cars["X"].col * 50 - 50
        y = self.cars["X"].row * 50 - 50
        self.WINDOW.blit(self.CAR_RED, (x, y))

        pygame.display.update()


    def run(self):
        """ The main loop to run the app """
        while self.is_running:
            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
            self.draw_window()
        
        # stop the app
        pygame.quit()

