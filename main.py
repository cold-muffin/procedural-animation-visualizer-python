
import pygame
from sys import exit
import vars

def main():

    pygame.init()

    ## Default positioning ##
    start_pos = (vars.win_w*0.5, vars.win_h*0.5)
    end_pos = None
    win_size = (vars.win_w, vars.win_h)
    window = pygame.display.set_mode(win_size)
    pygame.display.set_caption('IK Visualizer')

    clock = pygame.time.Clock()

    game_running = True
    while game_running:
        for event in pygame.event.get():
            # Handle quit #
            if event.type == pygame.QUIT:
                game_running = False
                print("Quitting...")
                pygame.quit()
                exit()
        
        mouse_pos = pygame.mouse.get_pos()

        window.fill((0, 0, 0))
        
        # Update display #
        pygame.display.update()
        clock.tick(vars.FPS)

class Main:
    def __init__(self, win_w, win_h, fps):
        # Initialize window and clock
        pygame.init()
        self.window = pygame.display.set_mode((win_w, win_h))
        pygame.display.set_caption('Procedural Animation Visualizer')
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.GAME_RUNNING = True

        self.setup()

    def setup(self):
        self.events = []

        self.updateVariables()
        pass

    def updateVariables(self):
        self.mouse_pos = pygame.mouse.get_pos()

        self.updateDisplay()
        pass

    def updateDisplay(self):
        pygame.display.update()

        self.run()
        pass

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handleQuit()

        self.clock.tick(self.fps)
        print(self.mouse_pos)

        self.updateVariables()
        pass

    def handleQuit(self):
        print('Quitting')
        self.GAME_RUNNING = False
        pygame.quit()
        exit()

if __name__ == '__main__':
    main = Main(vars.WINDOW_WIDTH, vars.WINDOW_HEIGHT, vars.FPS)