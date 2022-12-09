import settings
import pygame
import area 
import dicts 

class Sprite(settings.Settings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.STEP = 2
        self.GRAVITY = 6
        self.ACTIVE_GRAVITY = True
        self.CAN_MOVE_RIGHT = True
        self.CAN_MOVE_LEFT = True
        self.COUNT_JUMP = 0
        self.JUMP = False
        self.KEY_PRESSED = False
        self.FIX_COLLISION = True
    def move_sprite(self):
            event = pygame.key.get_pressed()
            if event[pygame.K_RIGHT] and self.RECT.x + self.WIDTH <= dicts.SETTINGS_WIN["WIDTH"]:
                if self.CAN_MOVE_RIGHT == True:
                    self.X += self.STEP
                    self.RECT.x = self.RECT.x + self.STEP
            elif event[pygame.K_LEFT] and self.RECT.x + 1 >= 0:   
                   if self.CAN_MOVE_LEFT == True:      
                        self.X -= self.STEP
                        self.RECT.x = self.RECT.x - self.STEP 

     #
    def jump(self, list_rect):
        event = pygame.key.get_pressed()
        #
        if event[pygame.K_UP] and self.KEY_PRESSED == False:
            self.KEY_PRESSED = True
        #
        if self.KEY_PRESSED and self.COUNT_JUMP <= 30:
            self.JUMP = True
            self.COUNT_JUMP += 1
            self.RECT.y -= 11
            self.Y -= 11
            self.can_move_up(list_rect)
        if self.COUNT_JUMP > 30:
            self.JUMP = False 
            # self.KEY_PRESSED = False
            # self.COUNT_JUMP = 0
            
             

    def gravity(self, list_rect):
        # # self.can_move_down(area.list_rect)
        # # if self.ACTIVE_GRAVITY:
        # #     self.Y += self.GRAVITY
        # #     self.RECT.y = self.RECT.y + self.GRAVITY
        # index = self.RECT.collidelist(list_rect)
        # if not self.RECT.colliderect(list_rect[index]) or self.ACTIVE_GRAVITY: 
        #     if self.RECT.y < dicts.SETTINGS_WIN["HEIGHT"] - self.HEIGHT:
        #         self.Y += self.GRAVITY
        #         self.RECT.y = self.RECT.y + self.GRAVITY
        #         self.FIX_COLLISION = True
        #         self.ACTIVE_GRAVITY = False
        # else:
        #     self.KEY_PRESSED = False
        #     self.COUNT_JUMP = 0
        #     if self.FIX_COLLISION:
        #         self.Y = list_rect[index].y - self.HEIGHT 
        #         self.FIX_COLLISION = False
        self.can_move_down(list_rect)
        if self.ACTIVE_GRAVITY:
            self.Y += self.GRAVITY
            self.RECT.y = self.RECT.y + self.GRAVITY
        
    def can_move_right(self, list_rect):
        for block in list_rect:
            if self.RECT.y + self.RECT.height - 10 < block.y + block.height and self.RECT.y + self.RECT.height - 10 > block.y:
                if self.RECT.x + self.RECT.width > block.x and self.RECT.x < block.x:
                    self.CAN_MOVE_RIGHT = False
                    self.X -= 3
                    self.RECT.x -= 3
                    break
                else:
                    self.CAN_MOVE_RIGHT = True
            else:
                self.CAN_MOVE_RIGHT = True
    def can_move_left(self, list_rect):
        for block in list_rect:
            if self.RECT.y + self.RECT.height - 10 < block.y + block.height and self.RECT.y + self.RECT.height - 10 > block.y:
                    if self.RECT.x < block.x + block.width and self.RECT.x + self.RECT.width > block.x + block.width:
                        self.CAN_MOVE_LEFT = False
                        self.X += 3
                        self.RECT.x += 3
                        break
                    else:
                        self.CAN_MOVE_LEFT = True
            else:
                self.CAN_MOVE_LEFT = True
    def can_move_down(self, list_rect):
        for block in list_rect:
            block = pygame.Rect(block.x, block.y, block.width, 1)
            if self.RECT.colliderect(block):
                # if block.y + block.height > self.RECT.y:
                self.ACTIVE_GRAVITY = False
                self.COUNT_JUMP = 0
                self.FIX_COLLISION = True
                self.KEY_PRESSED = False
                if self.FIX_COLLISION:
                    self.Y = block.y - self.HEIGHT
                    self.FIX_COLLISION = False
                break
            else:
                self.ACTIVE_GRAVITY = True
                

    def can_move_up(self, list_rect):
        for block in list_rect:
            if block.x <= self.RECT.x and block.x + block.width >= self.RECT.x:
                if self.RECT.colliderect(block) and block.y + block.height > self.RECT.y:
                    self.COUNT_JUMP = 41
                    self.ACTIVE_GRAVITY = True
            if block.x <= self.RECT.x + self.RECT.width and block.x + block.width >= self.RECT.x + self.RECT.width:
                if self.RECT.colliderect(block) and block.y + block.height > self.RECT.y:
                    self.COUNT_JUMP = 41
                    self.ACTIVE_GRAVITY = True

                    
    # def jump(self, list_rect):
    #     event = pygame.key.get_pressed()
            
    # def move_sprite(self, list_rect):
    #    event = pygame.key.get_pressed()
    #    if event[pygame.K_RIGHT] and self.RECT.x + self.WIDTH <= win_width:
    #        self.DIRECTION = 'R' 
    #        if self.CAN_MOVE_RIGHT:
    #            self.X += self.STEP
    #            self.RECT.x = self.RECT.x + self.STEP
    #        self.animation(folder= "player",count_while=5,last_img= 11, first_img=5) 
    #    elif event[pygame.K_LEFT] and self.RECT.x + 10 >= 0:            
    #        self.DIRECTION = 'L'
    #        if self.CAN_MOVE_LEFT:
    #            self.X -= self.STEP
    #            self.RECT.x = self.RECT.x - self.STEP
    #        self.animation(folder= "player",count_while=5,last_img= 11, first_img=5)
    #    else:
    #        self.NAME_IMAGE = "game2/sprite"
    #        self.direction()

sprite = Sprite(x = 330, y = 600, width = 50, height = 50, name_image = "game2/images/sprite.png")
smoke = Sprite(x = 0, y = 750, width = 50, height = 50, name_image = "game2/images/smoke.png")
mask = Sprite(x = 5, y = 5, width = 50, height = 50, name_image = "game2/images/mask.png")