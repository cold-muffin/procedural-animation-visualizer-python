
import pygame
from sys import exit
import vars
import classes

class Main:
    def __init__(self, win_w, win_h, fps):
        pygame.init()
        self.window = pygame.display.set_mode((win_w, win_h))
        pygame.display.set_caption('Procedural Animation Visualizer')
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.GAME_RUNNING = True

        self.setup()

    def setup(self):
        self.events = []
        #self.limbs = []

        # Create objects
        self.chain = classes.FABRIKChain(20, (200, 300), (0, 0), 10, 10)
        self.schain = classes.DCChain(6, (0, 0), (0, 0), 20, 20)
        self.fabrikchain2 = classes.FABRIKChain(5, (400, 200), (0, 0), 20, 20)

        self.run()
        pass

    def getInputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handleQuit()

        self.mouse_pos = pygame.mouse.get_pos()
        pass

    def updateVariables(self):
        self.chain.updateHead(self.mouse_pos)
        self.chain.update()

        self.schain.updateHead(self.mouse_pos)
        self.schain.update()

        self.fabrikchain2.updateHead(self.mouse_pos)
        self.fabrikchain2.update()

        pass

    def updateDisplay(self):
        self.window.fill((0, 0, 0))

        # Draw objects
        self.chain.draw(self.window)
        #self.schain.draw(self.window)
        #self.fabrikchain2.draw(self.window)
        
        pygame.display.update()
        pass

    def run(self):
        while self.GAME_RUNNING:
            self.getInputs()
            self.updateVariables()
            self.updateDisplay()

            self.clock.tick(self.fps)

        self.handleQuit()

    def handleQuit(self):
        print('Quitting...')
        self.GAME_RUNNING = False
        pygame.quit()
        exit()

if __name__ == '__main__':
    main = Main(vars.WINDOW_WIDTH, vars.WINDOW_HEIGHT, vars.FPS)