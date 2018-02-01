import pygame
from random import randint
from pygame.sprite import Sprite

class Ball(Sprite):
	"""初始化球并设置球的位置"""

	def __init__(self, screen, settings):
		super(Ball, self).__init__()
		self.screen = screen
		self.settings = settings

		# 加载球的图片并获得图片边距
		self.image = pygame.image.load('../images/ball.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		# 将球放在顶部随机位置
		self.rect.x = randint(0, int(self.settings.screen_width))
		self.rect.top = self.screen_rect.top

		# 存储球位置的精确位置
		self.x = self.rect.y

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""更新球的位置"""
		self.x += self.settings.ball_speed_factor
		self.rect.y = self.x
