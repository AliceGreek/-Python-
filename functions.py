import pygame

from ball import Ball
from player import Player

def create_balls(balls, screen, settings):
	new_ball = Ball(screen, settings)
	balls.add(new_ball)

def update_balls(balls, players, screen, settings):
	"""删除被玩家接住的球和到达屏幕底部的球"""
	for ball in balls.copy():
		if ball.rect.top >= settings.screen_height:
			balls.remove(ball)

	collisions = pygame.sprite.groupcollide(balls, players, True, False)
	"""如果编组没有球了重新创建一个球，并加入编组"""
	if len(balls) == 0:
		create_balls(balls, screen, settings)


def create_player(players, screen, settings):
	new_player = Player(screen, settings)
	players.add(new_player)