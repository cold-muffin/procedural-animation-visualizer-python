import pygame
import math
import warnings

class SegmentConstraint:
    def __init__(self, anchor_pos, head_pos, min_len, max_len) -> None:
        self.anchor_pos = anchor_pos
        self.old_anchor_pos = self.anchor_pos
        self.head_pos = head_pos
        self.old_head_pos = self.head_pos
        self.min_len = min_len
        self.max_len = max_len
        self.line_len = self.calculateDistance(self.anchor_pos, self.head_pos)

        self.setup()

    def setup(self):
        self.TOLERANCE = 0.05

    @staticmethod
    def calculateDistance(pos1, pos2):
        return (float((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)**0.5)
    
    @staticmethod
    def lerpPoint(pos1, pos2, ratio):
        return (round(ratio * (pos2[0] - pos1[0]) + pos1[0]), 
                round(ratio * (pos2[1] - pos1[1]) + pos1[1]))
    
    def lineLenGuardClause(self):
        e = None

        # Avoid division by 0
        if self.line_len == 0:
            e = "Line length equal to 0"

        if abs(self.line_len - self.old_line_len) < self.TOLERANCE:
            e = "New line length is below tolerance"

        if e is not None:
            raise Exception(e)

    def update(self) -> None:
        self.old_line_len = self.line_len
        self.line_len = self.calculateDistance(self.anchor_pos, self.head_pos)

        try:
            self.lineLenGuardClause()
        except Exception as e:
            #warnings.warn(e)
            return

        if self.line_len > self.max_len:
            self.m = self.max_len / self.line_len

        elif self.line_len < self.min_len:
            self.m = self.min_len / self.line_len

        elif self.line_len == self.max_len:
            self.m = self.max_len / self.line_len
        
        self.old_anchor_pos, self.old_head_pos = self.anchor_pos, self.head_pos

    def updateForwards(self):
        self.update()
        self.head_pos = self.lerpPoint(self.anchor_pos, self.head_pos, self.m)

    def updateBackwards(self) -> None:
        self.update()
        self.anchor_pos = self.lerpPoint(self.head_pos, self.anchor_pos, self.m)

    def updatePosBackwards(self):
        self.anchor_pos = self.updated_pos
    
    def draw(self, window):
        pygame.draw.line(window, (255, 255, 255), self.anchor_pos, self.head_pos, 6)