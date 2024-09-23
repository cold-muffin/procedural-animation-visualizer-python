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
        pass

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

        if e is not None:
            raise Exception(e)

    def update(self) -> None:
        self.m = 1
        self.old_line_len = self.line_len
        self.line_len = self.calculateDistance(self.anchor_pos, self.head_pos)

        try:
            self.lineLenGuardClause()
        except Exception as e:
            raise Exception(e)
        
        if self.line_len > self.max_len:
            self.m = self.max_len / self.line_len

        elif self.line_len < self.min_len:
            self.m = self.min_len / self.line_len
        
        self.old_anchor_pos, self.old_head_pos = self.anchor_pos, self.head_pos

    def updateForwards(self):
        try:
            self.update()
        except Exception as e:
            warnings.warn(str(e))
            return

        self.head_pos = self.lerpPoint(self.anchor_pos, self.head_pos, self.m)

    def updateBackwards(self) -> None:
        try:
            self.update()
        except Exception as e:
            warnings.warn(str(e))
            return
        
        self.anchor_pos = self.lerpPoint(self.head_pos, self.anchor_pos, self.m)
    
    def draw(self, window):
        pygame.draw.line(window, (255, 255, 255), self.anchor_pos, self.head_pos, 6)


class FABRIKChain:
    def __init__(self, quantity, c_anchor_pos, c_head_pos, min_len, max_len) -> None:
        self.quantity = quantity
        self.c_anchor_pos = c_anchor_pos
        self.c_head_pos = c_head_pos
        self.min_len = min_len
        self.max_len = max_len

        self.createObjects()

    def createObjects(self):
        self.objs = []
        for i in range(self.quantity):
            self.obj = SegmentConstraint((0, 0), (0, 0), self.min_len, self.max_len)
            self.objs.append(self.obj)

        pass

    def updateHead(self, new_h_pos):
        self.c_head_pos = new_h_pos

    def update(self):
        if len(self.objs) == 1:
            self.objs[0].head_pos = self.c_head_pos
            self.objs[0].anchor_pos = self.c_anchor_pos
            self.objs[0].updateForwards()

        else:
            self.objs[0].head_pos = self.c_head_pos
            self.objs[0].anchor_pos = self.objs[1].head_pos
            self.objs[0].updateBackwards()

            for i in range(1, len(self.objs) - 1):
                self.objs[i].head_pos = self.objs[i - 1].anchor_pos
                self.objs[i].anchor_pos = self.objs[i + 1].head_pos
                self.objs[i].updateBackwards()
            
            self.objs[len(self.objs) - 1].head_pos = self.objs[len(self.objs) - 2].anchor_pos
            self.objs[len(self.objs) - 1].anchor_pos = self.c_anchor_pos
            self.objs[len(self.objs) - 1].updateForwards()

            for i in range(len(self.objs) - 1):
                self.objs[len(self.objs) - 2 - i].anchor_pos = self.objs[len(self.objs) - 1 - i].head_pos
                self.objs[len(self.objs) - 2 - i].updateForwards()
    
        pass
    
    def draw(self, window):
        for obj in self.objs:
            obj.draw(window)

        pass

class DCChain:
    def __init__(self, quantity, c_anchor_pos, c_head_pos, min_len, max_len) -> None:
        self.quantity = quantity
        self.c_anchor_pos = c_anchor_pos
        self.c_head_pos = c_head_pos
        self.min_len = min_len
        self.max_len = max_len

        self.createObjects()
    
    def createObjects(self):
        self.objs = []
        for obj in range(self.quantity):
            cons = SegmentConstraint(self.c_anchor_pos, self.c_head_pos, self.min_len, self.max_len)
            self.objs.append(cons)
        
        pass

    def updateHead(self, new_h_pos):
        self.c_head_pos = new_h_pos

        pass
    
    def update(self):
        self.objs[0].head_pos = self.c_head_pos
        self.objs[0].updateBackwards()
        for i in range(1, len(self.objs)):
            self.objs[i].head_pos = self.objs[i - 1].anchor_pos
            self.objs[i].updateBackwards()

        pass
    
    def draw(self, window):
        for obj in self.objs:
            obj.draw(window)

        pass