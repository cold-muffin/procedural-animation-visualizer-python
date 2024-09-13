
import pygame
from sys import exit

def main():

    ### DISPLAY VARIABLES ###
    win_w = 800
    win_h = 600
    FPS = 30

    ## Default positioning ##
    start_pos = (win_w*0.5, win_h*0.5)
    end_pos = None
    win_size = (win_w, win_h)
    window = pygame.display.set_mode(win_size)
    pygame.display.set_caption('IK Visualizer')

    clock = pygame.time.Clock()

    def getLineLen(start_pos, end_pos):
        line_len = float((start_pos[0] - end_pos[0])**2 + (start_pos[1] - end_pos[1])**2)**0.5
        return line_len

    def drawLimb(start_pos, end_pos, max_len):
        global prev_end_pos
        line_len = getLineLen(start_pos, end_pos)

        if line_len < max_len:
            pygame.draw.line(window, (255, 255, 255), start_pos, end_pos, 6)
            prev_end_pos = end_pos
            return prev_end_pos
        
        elif 'prev_end_pos' in globals():
            if prev_end_pos is not None:
                pygame.draw.line(window, (255, 255, 255), start_pos, prev_end_pos, 6)

    def calculateEndPos(start_pos, end_pos, max_len):
        m = round(max_len/getLineLen(start_pos, end_pos), 2)
        x1, x2 = start_pos[0], end_pos[0]
        y1, y2 = start_pos[1], end_pos[1]

        x3 = round(m*(x2 - x1) + x1)
        y3 = round(m*(y2 - y1) + y1)

        return (x3, y3)

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

        ### LINE VARIABLES ###
        max_len = 100
        min_len = max_len
        start_pos = start_pos
        end_pos = calculateEndPos(start_pos, mouse_pos, max_len)

        line_len = getLineLen(start_pos, end_pos)

        ## Draw lines ##
        pygame.draw.line(window, (255, 255, 255), start_pos, end_pos, 6)
        

        # Update display #
        pygame.display.update()
        clock.tick(FPS)

main()