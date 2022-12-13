import pygame
import os
import settings as settings
win_height = 800
win_width = 800

world_w = 100
world_h = 60

list_world = [
    "000000000",
    "111000000",
    "000011111",
    "000000100",
    "000110100",
    "000000100",
    "010000100",
    "000100100",
    "000000100",
    "000001100",
    "000100000",
    "000000000",
    "111111111"
]
list_create_world = []
list_rect = []
class Area(settings.Settings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


def create_world(level):
    x = 0
    y = 0
    for string in list_world:
        for el in string:
            if el == "1":
                area = Area(
                    x= x,
                    y= y,
                    width= world_w,
                    height= world_h,
                    color= (255, 165, 0),
                    name_image= ("game2/images/test_image.png")
                )
                list_create_world.append(area)
                list_rect.append(area)

            x += world_w
        x = 0
        y += world_h

create_world(list_world)
