import pygame
import csv
import copy

def visualize_csv(output, original_board):
    """ perfroms moves in output on a board """

    # load in the board
    autos = []
    board = copy.deepcopy(original_board)

    # add the initial state to the list 
    state = {}
    for car in board.cars.values():
        state[car.name] = {"row" : car.row, "col" : car.col, "length" : car.length, "is_horizontal" : car.is_horizontal}

    with open(f"data/output/{output}") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for step in csv_reader:
            state = {}
            board.move(board.cars[step["car"]], int(step["move"]))

            for car in board.cars.values():
                state[car.name] = {"row" : car.row, "col" : car.col, "length" : car.length, "is_horizontal" : car.is_horizontal}
            
            autos.append(state)
            
    # start the app
    app = App(board.dimension, autos)
    app.run()


class App():
    """ The class for the app """

    def __init__(self, n, autos):
        """ Used to set-up the pygame app """
        self.n = n
        self.WIDTH, self.HEIGHT = 780, 780
        self.tile_size = 780 // self.n
        self.step_num = 0
        self.last_step_num = len(autos) - 1
        self.autos = autos

        # start the window
        pygame.init()
        self.WINDOW = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Rush Hour")

        self.FPS = 5

        # load all the assets
        self.TILE = pygame.image.load("code/visualisation/rush_hour_assets/tile.png").convert()
        self.TILE = pygame.transform.scale(self.TILE, (self.tile_size, self.tile_size))
        self.CAR_RED = pygame.image.load("code/visualisation/rush_hour_assets/red_car.png").convert()
        self.CAR_RED = pygame.transform.scale(self.CAR_RED, (2 * self.tile_size, self.tile_size))

        # load the different cars
        self.car_assets_2x1 = {}
        for i in range(4):
            new = pygame.image.load(f"code/visualisation/rush_hour_assets/car_2x1_{i}.png").convert()
            self.car_assets_2x1[i] = pygame.transform.scale(new, (2 * self.tile_size, self.tile_size))

        self.car_assets_3x1 = {}
        for i in range(3):
            new = pygame.image.load(f"code/visualisation/rush_hour_assets/car_3x1_{i}.png").convert()
            self.car_assets_3x1[i] = pygame.transform.scale(new, (3 * self.tile_size, self.tile_size))

        # make the background
        self.BG = pygame.Surface((self.WIDTH, self.HEIGHT))
        for row in range(self.n):
            for col in range(self.n):
                location = row * self.tile_size, col * self.tile_size
                self.BG.blit(self.TILE, location)
        
        # load a font to display text
        self.font = pygame.font.Font(pygame.font.get_default_font(), 96)

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
                location = (state[car_name]["col"] * self.tile_size, state[car_name]["row"] * self.tile_size)

                # rotate the image if not horizontal
                if not state[car_name]["is_horizontal"]:
                    self.WINDOW.blit(pygame.transform.rotate(self.car_assets_2x1[num], 90), location)
                else:
                    self.WINDOW.blit(self.car_assets_2x1[num], location)
            
            if state[car_name]["length"] == 3:
                # get a number for the car to select an image
                num = ord(car_name[-1]) % len(self.car_assets_3x1)
                location = (state[car_name]["col"] * self.tile_size, state[car_name]["row"] * self.tile_size)
                
                # rotate the image if not horizontal
                if not state[car_name]["is_horizontal"]:
                    self.WINDOW.blit(pygame.transform.rotate(self.car_assets_3x1[num], 90), location)
                else:
                    self.WINDOW.blit(self.car_assets_3x1[num], location)
        
        # then place the red car
        x = state["X"]["col"] * self.tile_size
        y = state["X"]["row"] * self.tile_size
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
