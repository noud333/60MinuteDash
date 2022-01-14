from matplotlib import pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import pygame
import os

def graph(board):
    plt.plot()
    plt.xticks(list(range(0, board.dimension + 1)))
    plt.yticks(list(range(0, board.dimension + 1)))
    for car in board.cars.values():
        if car.is_horizontal:
            rect = Rectangle((car.col,board.dimension - car.row - 1),car.length, 1)
        else:
            rect = Rectangle((car.col,board.dimension - car.row - car.length),1, car.length)
        if car.name == "X":
            rect.set_color("red")
        else:
            rect.set_color(list(np.random.choice(range(256), size=3)/256))
        rect.set_edgecolor("black")
        rect.set_linewidth(2)
        plt.gca().add_patch(rect)
    plt.savefig("test.png")



class App():
    """ The class for the app """

    def __init__(self, n, autos):
        """ Used to set-up the pygame app """
        self.n = n
        self.WIDTH, self.HEIGHT = 50 * self.n, 50* self.n
        self.step_num = 0
        self.last_step_num = len(autos)
        self.autos = autos

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

    def draw_window(self):
        """ Draws the window """
        # first draw the background
        self.WINDOW.blit(self.BG, (0, 0))

        state = self.autos[self.step_num]

        # then draw the cars
        for car_name in state.keys():
            
            if state[car_name]["length"] == 2 and car_name != "X":
                # get a number for the car to select an image
                num = ord(car_name[-1]) % len(self.car_assets_2x1)
                location = (state[car_name]["col"] * 50, state[car_name]["row"] * 50)

                # rotate the image if not horizontal
                if not state[car_name]["is_horizontal"]:
                    self.WINDOW.blit(pygame.transform.rotate(self.car_assets_2x1[num], 90), location)
                else:
                    self.WINDOW.blit(self.car_assets_2x1[num], location)
            
            if state[car_name]["length"] == 3:
                # get a number for the car to select an image
                num = ord(car_name[-1]) % len(self.car_assets_3x1)
                location = (state[car_name]["col"] * 50, state[car_name]["row"] * 50)
                
                # rotate the image if not horizontal
                if not state[car_name]["is_horizontal"]:
                    self.WINDOW.blit(pygame.transform.rotate(self.car_assets_3x1[num], 90), location)
                else:
                    self.WINDOW.blit(self.car_assets_3x1[num], location)
        
        # then place the red car
        x = state["X"]["col"] * 50
        y = state["X"]["row"] * 50
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
