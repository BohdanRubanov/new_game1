import pygame 
import dicts 
import settings
import area
import sprite
pygame.init()
smoke_width = 50
smoke_height = 50
smoke_x = 0
smoke_y = 750
smoke = sprite.Sprite(x = smoke_x, y = smoke_y, width = smoke_width, height = smoke_height, name_image = "game2/images/smoke.png")
scene1 = False
level1 = True
scene3 = False
smoke_count = 0
fps = 60
win = pygame.display.set_mode((dicts.SETTINGS_WIN["WIDTH"], dicts.SETTINGS_WIN["HEIGHT"]))
pygame.display.set_caption("game")
def run_game():
    global smoke
    global scene1
    global level1
    global scene3
    
    clock = pygame.time.Clock()
    game = True
    while game:
        global smoke_x
        global smoke_y
        global smoke_height
        global smoke_width
        global smoke_count
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False  
        if scene1:
            settings.bg_menu.blit_sprite(win)
            settings.play.blit_sprite(win)
            settings.developers.blit_sprite(win)
            settings.exit.blit_sprite(win)
            # settings.play.draw_rect(win)
            # settings.developers.draw_rect(win)
            # settings.exit.draw_rect(win)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click = event.pos 
                    if settings.play.RECT.collidepoint(click):
                        print(1)
                        level1 = True
                        scene1 = False
                    if settings.exit.RECT.collidepoint(click):
                        print(2)
                        game = False 
                    if settings.developers.RECT.collidepoint(click):
                        print(3)
                        scene3 = True
                        scene1 = False
                if event.type == pygame.MOUSEMOTION:
                    if settings.play.RECT.collidepoint(event.pos):
                        settings.play = settings.Settings(x = 365,y = 115, width = 75, height = 35,name_image = "game2/images/play.png")
                    if not settings.play.RECT.collidepoint(event.pos):
                        settings.play = settings.Settings(x = 350,y = 100, width = 100, height = 50,name_image = "game2/images/play.png")

                    if settings.developers.RECT.collidepoint(event.pos):
                       
                        settings.developers = settings.Settings(x = 365,y = 200, width = 75, height = 35,name_image = "game2/images/developers.png")
                    if not settings.developers.RECT.collidepoint(event.pos):
                        settings.developers = settings.Settings(x = 350,y = 175, width = 100, height = 50,name_image = "game2/images/developers.png")

                    if settings.exit.RECT.collidepoint(event.pos):
                        settings.exit = settings.Settings(x = 365,y = 275, width = 75, height = 35,name_image = "game2/images/exit.png")
                    if not settings.exit.RECT.collidepoint(event.pos):
                        settings.exit = settings.Settings(x = 350,y = 250, width = 100, height = 50,name_image = "game2/images/exit.png")

            pygame.display.flip()
            # pass
        if level1:
            smoke_count += 1
            settings.bg.blit_sprite(win)
            sprite.sprite.can_move_right(area.list_rect)
            sprite.sprite.can_move_left(area.list_rect)
            # sprite.sprite.can_move_down(area.list_rect)
            sprite.sprite.move_sprite()
            sprite.sprite.jump(area.list_rect)
            sprite.sprite.blit_sprite(win)
            sprite.sprite.gravity(list_rect= area.list_rect)
            # sprite.smoke.blit_sprite(win)
            sprite.mask.blit_sprite(win)
            sprite.mask.gravity(list_rect= area.list_rect)
            settings.lever.blit_sprite(win)
            settings.injured.blit_sprite(win)
      
            for el in area.list_create_world:
                el.blit_sprite(win)
            # if smoke_count == 50:
            #     # sprite.smoke.WIDTH += 50
            #     # sprite.smoke.HEIGHT += 50
            #     print(1)
            #     smoke_width += 50
            #     smoke_height += 50
            #     # smoke_x += 20
            #     smoke_y -= 20
            #     smoke = sprite.Sprite(x = smoke_x, y = smoke_y, width = smoke_width, height = smoke_height, name_image = "game2/images/smoke.png")
            #     # smoke.blit_sprite(win)
            #     smoke_count = 0
            smoke.blit_sprite(win)
            pygame.display.flip()
        if scene3:
            settings.bg_developers.blit_sprite(win)
            settings.back.blit_sprite(win)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click = event.pos
                    if settings.back.RECT.collidepoint(click):
                        scene1 = True
                        scene3 = False
                if event.type == pygame.MOUSEMOTION:
                    if settings.back.RECT.collidepoint(event.pos):
                        settings.back = settings.Settings(x = 715,y = 0, width = 75, height = 45,name_image = "game2/images/back.png")
                    if not settings.back.RECT.collidepoint(event.pos):
                        settings.back = settings.Settings(x = 700,y = 0, width = 100, height = 50,name_image = "game2/images/back.png")

            pygame.display.flip()

        clock.tick(fps) 
        

run_game()