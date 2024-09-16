
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
        self.limbs = []

        # Create objects
        for i in range(20):
            self.limb = classes.SegmentConstraint((0, 0), (0, 0), 25, 25)
            self.limbs.append(self.limb)

        self.run()
        pass

    def getInputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handleQuit()

        self.mouse_pos = pygame.mouse.get_pos()
        pass

    def updateVariables(self):
        self.limbs[0].anchor_pos = self.mouse_pos
        self.limbs[0].updateForwards()
        for i in range(1, len(self.limbs)):
            self.limbs[i].anchor_pos = self.limbs[i - 1].head_pos
            self.limbs[i].updateForwards()
        pass

    def updateDisplay(self):
        self.window.fill((0, 0, 0))

        # Draw objects
        for i in range(len(self.limbs)):
            self.limbs[i].draw(self.window)
            pygame.draw.circle(self.window, (255, 0, 0), self.limbs[i].anchor_pos, 4)
            pygame.draw.circle(self.window, (255, 255, 0), self.limbs[i].head_pos, 4)

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