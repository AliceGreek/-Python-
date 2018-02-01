import pygame
from pygame.sprite import Sprite

from settings import Settings

class Player(Sprite):
	"""初始化玩家并设置玩家的初始位置"""
	def __init__(self, screen, settings):
		super(Player, self).__init__()
		self.screen = screen
		self.settings = settings

		# 加载玩家图片并获得图片边距
		self.image = pygame.image.load('../images/tray.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		# 设置玩家的初始位置
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#移动标志
		self.moving_left = False
		self.moving_right = False

		#将小数值存储在x中
		self.x = self.rect.centerx

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def update(self):
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.x -= self.settings.player_speed_factor
			self.rect.x = self.x
		elif self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.player_speed_factor
			self.rect.x = self.x
