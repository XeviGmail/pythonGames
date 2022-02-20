import pygame 

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,constraint,speed):
		super().__init__()
		self.image = pygame.image.load('../graphics/player.png').convert_alpha()
		self.rect = self.image.get_rect(midbottom = pos)
