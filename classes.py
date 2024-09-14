import pygame

class SegmentConstraint:
    def __init__(self, anchor_pos, head_pos, min_len, max_len) -> None:
        self.anchor_pos = anchor_pos
        self.head_pos = head_pos
        self.min_len = min_len
        self.max_len = max_len

    def update(self) -> None:
        self.line_len = float((self.anchor_pos[0] - self.head_pos[0])**2 + 
                              (self.anchor_pos[1] - self.head_pos[1])**2)**0.5
        
        if self.line_len == 0:
            pass
        else:
            self.m = round(self.max_len / self.line_len, 2)

            self.x1, self.x2 = self.anchor_pos[0], self.head_pos[0]
            self.y1, self.y2 = self.anchor_pos[1], self.head_pos[1]

        if self.line_len > self.max_len:
            self.x3 = round(self.m*(self.x2 - self.x1) + self.x1)
            self.y3 = round(self.m*(self.y2 - self.y1) + self.y1)
        else:
            self.x3 = self.head_pos[0]
            self.y3 = self.head_pos[1]
        
        self.updatePos()

    def updatePos(self):
        self.head_pos = (self.x3, self.y3)
    
    def draw(self, window):
        pygame.draw.line(window, (255, 255, 255), self.anchor_pos, self.head_pos, 6)