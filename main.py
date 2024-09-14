
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

        # Create objects
        self.limb1 = classes.SegmentConstraint((0, 0), (0, 0), 50, 50)
        self.limb2 = classes.SegmentConstraint((0, 0), (0, 0), 50, 30)
        self.limb3 = classes.SegmentConstraint((0, 0), (0, 0), 50, 50)

        self.run()
        pass

    def getInputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handleQuit()

        self.mouse_pos = pygame.mouse.get_pos()
        pass

    def updateVariables(self):
        self.limb1.anchor_pos = self.mouse_pos
        self.limb2.anchor_pos = self.limb1.head_pos
        self.limb3.anchor_pos = self.limb2.head_pos

        #self.limb1.head_pos = self.mouse_pos

        self.limb1.update()
        self.limb2.update()
        self.limb3.update()
        pass

    def updateDisplay(self):
        self.window.fill((0, 0, 0))

        # Draw objects
        self.limb1.draw(self.window)
        self.limb2.draw(self.window)
        self.limb3.draw(self.window)

        pygame.display.update()
        pass

    def run(self):
        while self.GAME_RUNNING:
            self.getInputs()
            self.updateVariables()
            self.updateDisplay()

            self.clock.tick(self.fps)
            print(self.mouse_pos)

        self.handleQuit()

    def handleQuit(self):
        print('Quitting...')
        self.GAME_RUNNING = False
        pygame.quit()
        exit()

if __name__ == '__main__':
    main = Main(vars.WINDOW_WIDTH, vars.WINDOW_HEIGHT, vars.FPS)