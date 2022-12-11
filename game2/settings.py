import pygame
import os

pygame.init()

def create_path():
    path_abs = os.path.abspath(__file__ + "/..")
    path_abs = path_abs.split("\\") 
    del path_abs[-1]
    path_abs = "\\".join(path_abs)
    return path_abs

class Settings:
    def __init__(self, x = None, y = None, width = None, height = None, name_image = None, color = None):
        self.X = x
        self.Y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.NAME_IMAGE = name_image
        self.IMAGE = None
        self.RECT = pygame.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT) 
        self.COLOR = color
        if self.NAME_IMAGE:
            self.load_image()

    def load_image(self):
        path_image = create_path()
        path_image = os.path.join(path_image, self.NAME_IMAGE)
        self.IMAGE = pygame.image.load(path_image)
        self.IMAGE = pygame.transform.scale(self.IMAGE, (self.WIDTH, self.HEIGHT))

    def blit_sprite(self,win):
        win.blit(self.IMAGE, (self.X,self.Y))


    def draw_rect(self, win):
            pygame.draw.rect(win, self.COLOR, self.RECT)

bg = Settings(x = 0,y = 0, width = 800, height = 800,name_image = "game2/images/bg.png")
bg_menu = Settings(x = 0,y = 0, width = 800, height = 800,name_image = "game2/images/bg_menu.png")
play = Settings(color =(255,0,0), x = 350,y = 100, width = 100, height = 50,name_image = "game2/images/play.png")
developers = Settings(color =(255,0,0),x = 350,y = 175, width = 100, height = 50,name_image = "game2/images/developers.png")
exit = Settings(color =(255,0,0),x = 350,y = 250, width = 100, height = 50,name_image = "game2/images/exit.png")
bg_developers = Settings(x = 0,y = 0, width = 800, height = 800,name_image = "game2/images/bg_developers.png")
back = Settings(x = 700,y = 0, width = 100, height = 100,name_image = "game2/images/back.png")
lever = Settings(x = 10,y = 620, width = 100, height = 100,name_image = "game2/images/lever.png")
injured = Settings(x = 730,y = 670, width = 50, height = 50,name_image = "game2/images/injured.png")
