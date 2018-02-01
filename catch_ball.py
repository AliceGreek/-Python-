import pygame
import sys
from pygame.sprite import Group
from settings import Settings
from player import Player
from ball import Ball
import functions as f

def run_game():
	"""接球游戏"""

	pygame.init()
	settings = Settings()

	# 创建屏幕对象
	screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
	pygame.display.set_caption('Catch Balls')

	# 创建玩家编组，内部只存储一个玩家对象
	players = Group()

	# 创建玩家对象并加入编组
	f.create_player(players, screen, settings)

	# 创建一个球编组
	balls = Group()

	# 创建球并加入组中
	f.create_balls(balls, screen, settings)

	# 开始游戏循环
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					player.moving_left = True
				elif event.key == pygame.K_RIGHT:
					player.moving_right = True
				elif event.key == pygame.K_q:
					sys.exit()

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					player.moving_left = False
				elif event.key == pygame.K_RIGHT:
					player.moving_right = False
		players.update()
		balls.update()
		f.update_balls(balls, players, screen, settings)
		screen.fill(settings.bg_color)
		for player in players.sprites():
			player.blitme()

		#在玩家后面绘制球
		for ball in balls.sprites():
			ball.blitme()

		pygame.display.flip()

run_game()