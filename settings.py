class Settings():
	"""管理设置类"""

	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = 0, 0, 0

		# 玩家移动速度
		self.player_speed_factor = 2.5

		# 球的速度
		self.ball_speed_factor = 5.5