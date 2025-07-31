# consts.py

# screen_width = 800
# screen_height = 600
# screen_params = (screen_width, screen_height)
# game_FPS = 30

# sprites.py - загружает и подготавливает изображения:

# import pygame
# background_image = pygame.image.load('sprites/back.png')
# background_image = pygame.transform.scale(background_image, (800,600))
# player_image = pygame.image.load('sprites/player.png')
# asteroid_image = pygame.image.load('sprites/asteroid.png')
# asteroid_good_image = pygame.image.load('sprites/asteroid_good.png')

# RenderableObject.py - интерфейс для отрисовываемых объектов:

# class RendarableObject:
#     def draw(self,surface):
#         pass

# CollidableObject.py - базовый класс для объектов с коллизией:

# import pygame

# class CollidableObject:
#     x = 0
#     y = 0
#     height = 0
#     width = 0
#     rect = pygame.Rect(x, y, width, height)

# RenderEngine.py - отвечает за отрисовку:

# import pygame
# import sprites
# import consts

# class RenderEngine:
#     def __init__(self):
#         self.screen = pygame.display.set_mode(consts.screen_params)
#         pygame.display.set_caption(consts.game_title)
#         self.background_rect = sprites.background_image.get_rect()
#         self.render_queue_list = []
#         pygame.font.init()
#         self.font = pygame.font.Font(None, 36)

#     def render_frame(self, lives, score):
#         pass

#     def __render_queue(self):
#         pass

#     def add_render_object(self, *renders_object):
#         pass

# PhysicEngine.py - обработка физики и коллизий:

# import pygame.mask

# class PhysicEngine:
#     @staticmethod
#     def collide_with_left_border(collidable_object):
#         pass
#
#     @staticmethod
#     def collide(collidable_object, collidable_object1):
#         pass

# Player.py - игровой персонаж:

# import pygame
# import sprites
# from CollidableObject import CollidableObject
# from RendarableObject import RendarableObject

# class Player(CollidableObject, RendarableObject):
#     def __init__(self, x, y):
#         pass

#     def move(self, directoin):
#         pass

#     def draw(self, surface):
#         pass

#     def damaged(self):
#         pass

# Asteroid.py - астероиды:

# import pygame
# import consts
# import sprites
# from CollidableObject import CollidableObject
# from RendarableObject import RendarableObject

# class Asteroid(RendarableObject, CollidableObject):
#     def __init__(self, speed):
#         pass

#     def move(self):
#         pass

#     def draw(self, surface):
#         pass

# ScoreController.py - управление счетом:

# class ScoreController:
#     def __init__(self):
#         self.score = 0

#     def update_score(self):
#         self.score += 1

# Game.py - основной класс игры:

# import pygame
# import consts
# from Asteroid import Asteroid
# from Player import Player
# from RenderEngine import RenderEngine
# from PhysicEngine import PhysicEngine
# from ScoreController import ScoreController
# import time

# class Game():

#     def event_handler(self):
#         pass

#     def game_logic(self):
#         pass

#     def main_loop(self):
#         pass

# main.py - запуск игры:

# from Game import Game
# Game = Game()
# Game.main_loop()

# Принцип работы игры

# Игрок управляет космическим кораблем с помощью стрелок

# По экрану летят астероиды двух типов:

# Опасные (70% случаев) - при столкновении отнимают жизнь

# Полезные (30% случаев) - при столкновении дают очки

# Игра продолжается, пока у игрока есть жизни

# Сложность постепенно увеличивается:

# Астероиды появляются чаще
  
# Их скорость растет