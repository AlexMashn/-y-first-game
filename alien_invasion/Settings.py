class Settings():   
	"""Класс для хранения всех настроек игры Alien Invasion."""
   
	def __init__(self):
		"""Инициализирует статические настройки игры."""
		# Параметры экрана
		self.screen_width = 1280
		self.screen_height = 1024
		self.bg_color = (0, 0, 0)

		#Настройки коробля
		self.ship_speed = 4
		self.ship_limit = 2

		# Параметры снаряда
		self.bullet_speed = 8
		self.bullet_width = 4
		self.bullet_height = 8
		self.bullet_color = (240, 240, 240)
		self.bullets_allowed = 4

		# Настройки пришельцев
		self.alien_speed = 1
		self.fleet_drop_speed = 100
		# fleet_direction = 1 обозначает движение вправо; а -1 - влево.
		self.fleet_direction = 1

		#Настройки графики.
		self.fps = 144

		# Темп ускорения игры
		self.speedup_scale = 1.5
		# Темп роста стоимости пришельцев
		self.score_scale = 1.5

		self.initialize_dynamic_settings()
		

	def initialize_dynamic_settings(self):
		"""Инициализирует настройки, изменяющиеся в ходе игры."""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3.0
		self.alien_speed_factor = 1.0

		# fleet_direction = 1 обозначает движение вправо; а -1 - влево.
		self.fleet_direction = 1

		# Подсчет очков
		self.alien_points = 10

	def increase_speed(self):
		"""Увеличивает настройки скорости и стоимость пришельцев."""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)

	
