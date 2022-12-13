import settings
import pygame
import area 
import dicts 
win = pygame.display.set_mode((dicts.SETTINGS_WIN["WIDTH"], dicts.SETTINGS_WIN["HEIGHT"]))
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
        self.OPEN_DOOR = False
        self.MASK_ON = False
        self.INJURED = False
    def move_sprite(self):
            event = pygame.key.get_pressed()
            if event[pygame.K_RIGHT] and self.X + self.WIDTH <= dicts.SETTINGS_WIN["WIDTH"]:
                if self.CAN_MOVE_RIGHT == True:
                    self.X += self.STEP
                    # self.RECT.x = self.RECT.x + self.STEP
            elif event[pygame.K_LEFT] and self.X + 1 >= 0:   
                   if self.CAN_MOVE_LEFT == True:      
                        self.X -= self.STEP
                        # self.RECT.x = self.RECT.x - self.STEP 

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
            # self.RECT.y -= 11
            self.Y -= 11
            self.can_move_up(list_rect)
        if self.COUNT_JUMP > 30:
            self.JUMP = False 
            # self.KEY_PRESSED = False
            # self.COUNT_JUMP = 0
            
             

    def gravity(self, list_rect):
       
        self.can_move_down(list_rect)
        if self.ACTIVE_GRAVITY:
            self.Y += self.GRAVITY
            
        
    def can_move_right(self, list_rect):
        for block in list_rect:
            if self.Y + self.HEIGHT - 10 <= block.Y + block.HEIGHT and self.Y + 10 >= block.Y and self.Y + 10 <= block.Y + block.HEIGHT and self.Y + self.HEIGHT - 10 >= block.Y:
                print(block.HEIGHT, "23e43ed3sede")
                if self.X + self.WIDTH >= block.X and self.X < block.X:
                    self.CAN_MOVE_RIGHT = False
                    self.X -= 3
                    # self.RECT.x -= 3
                    break
                else:
                    self.CAN_MOVE_RIGHT = True
    def can_move_left(self, list_rect):
        for block in list_rect:
            if self.Y + self.HEIGHT + 10 < block.Y + block.HEIGHT and self.Y + self.HEIGHT - 10 > block.Y:
                    if self.X < block.X + block.WIDTH and self.X + self.WIDTH > block.X + block.WIDTH:
                        self.CAN_MOVE_LEFT = False
                        self.X += 3
                        # self.RECT.x += 3
                        break
                    else:
                        self.CAN_MOVE_LEFT = True
            else:
                self.CAN_MOVE_LEFT = True
    def can_move_down(self, list_rect):
        for block in list_rect:
            if self.Y + self.HEIGHT >= block.Y and self.Y <= block.Y:
                # print(self.RECT.Y + self.RECT.height, block.Y)
                if self.X + 50 >= block.X and self.X + self.WIDTH - 50 <= block.X + block.WIDTH:
                    print(self.Y + self.HEIGHT, block.Y)
                    # self.RECT.Y = block.Y - self.RECT.height - 1
                # if block.Y + block.height > self.RECT.Y:
                    self.ACTIVE_GRAVITY = False
                    self.COUNT_JUMP = 0
                    self.FIX_COLLISION = True
                    self.KEY_PRESSED = False
                    if self.FIX_COLLISION:
                        self.Y = block.Y - self.HEIGHT
                        self.FIX_COLLISION = False
                    break
                else:
                    self.ACTIVE_GRAVITY = True
                

    def can_move_up(self, list_rect):
        for block in list_rect:
            if self.Y <= block.Y + block.HEIGHT and self.Y + self.HEIGHT >= block.Y + block.HEIGHT:
                if self.X + 50>= block.X and self.X + self.WIDTH - 50 <= block.X + block.WIDTH:
                    self.COUNT_JUMP = 41
                    self.ACTIVE_GRAVITY = True
            # if block.x <= self.X + self.WIDTH and block.x + block.width >= self.X + self.WIDTH:
            #     if block.Y + block.height > self.Y:
            #         self.COUNT_JUMP = 41
            #         self.ACTIVE_GRAVITY = True
    def draw_text(self, win):
        font = pygame.font.SysFont("kokila", 20)
        follow = font.render("нажмите E что бы взаимодействовать с предметами!", 1, (0,0,0))
        win.blit(follow, (100, 200))

    def lever_collide(self, win):
        event = pygame.key.get_pressed()
        if self.X + self.WIDTH <= settings.lever.X + settings.lever.WIDTH + 20 and self.X + 20 >= settings.lever.X:
            if self.Y >= settings.lever.HEIGHT + 20 and self.Y + self.HEIGHT <= settings.lever.Y + settings.lever.HEIGHT + 20:
                self.draw_text(win)
                if event[pygame.K_e]:
                #    print(22222)
                   self.OPEN_DOOR = True
    def mask_collide(self, win):
        event = pygame.key.get_pressed()
        if self.X + self.WIDTH <= mask.X + mask.WIDTH + 20 and self.X + 20 >= mask.X:
            # print(5555)
            # print(self.RECT.y  + 21 >= mask.RECT.y, self.RECT.y + 21, mask.RECT.y)
            if self.Y + 21 >= mask.Y and self.Y + self.HEIGHT <= mask.Y + mask.HEIGHT + 20:
                self.draw_text(win)
                # print(2222223333)
                if event[pygame.K_r]:
                    # print(222222)'
                    self.MASK_ON = True
                    self.NAME_IMAGE = "game2/images/sprite_with_injured.png"
                    self.load_image()

    def injured_collide(self):
        event = pygame.key.get_pressed()
        if self.X + self.WIDTH <= settings.injured.X + settings.injured.WIDTH + 20 and self.X + 20 >= settings.injured.X:
            if self.Y + 21 >= settings.injured.Y and self.Y + self.HEIGHT <= settings.injured.Y + settings.injured.HEIGHT + 20:
                self.draw_text(win)
                if event[pygame.K_f]:
                    self.NAME_IMAGE = "game2/images/sprite_with_injured.png"
                    self.load_image()
                    self.INJURED = True
    def position(self):
        event = pygame.key.get_pressed()
        if event[pygame.K_t]:
            print(self.X)
    def door_collide(self):
        if not self.OPEN_DOOR:
            if self.Y >= door.Y and self.Y + self.HEIGHT - 10 <= door.Y + door.HEIGHT:
                # print(11111)
                if self.X + self.WIDTH >= door.X:
                    # print(5555)
                    self.CAN_MOVE_RIGHT = False
                    self.X -= 3
                    self.X -= 3
        if self.OPEN_DOOR:
            # print(1111)
            door.NAME_IMAGE = None
    # def open_door(self):
    #     if self.OPEN_DOOR:
    #         print(1111)
    #         self.NAME_IMAGE = None
    def door_exit_collide(self):
        if self.INJURED:
            if self.Y >= door_exit.Y and self.Y + self.HEIGHT - 10 <= door_exit.Y + door_exit.HEIGHT:
                # print(11111)
                if self.X + self.WIDTH >= door_exit.X:
                    print("игшмгпийширмМГМгпцвм???")
                
                


sprite = Sprite(color = (0,0,0), x = 330, y = 600, width = 50, height = 60, name_image = "game2/images/sprite.png")
smoke = Sprite(x = 0, y = 750, width = 50, height = 50, name_image = "game2/images/smoke.png")
mask = Sprite(x = 5, y = 5, width = 50, height = 50, name_image = "game2/images/mask.png")
door = Sprite(x = 520, y = 600, width = 120, height = 120, name_image = "game2/images/door.png")
door_exit = Sprite(x = 600, y = 0, width = 120, height = 120, name_image = "game2/images/door.png")
