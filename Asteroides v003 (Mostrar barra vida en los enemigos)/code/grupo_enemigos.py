import random

import pygame
from enemy import Enemy

class GrupoEnemigos():
    def __init__(self, enemies, screen_width, screen_height, screen):
        self.enemies = enemies
        self.screen = screen
        self.numero_enemigos = 8
        self.numero_enemigos_lanzados = 0
        self.pos_x_grupo = 100
        self.pos_y_grupo = -10
        self.grupo_iniciado = False
        self.grupo_finalizado = False
        self.distancia_entre_enemigos = 1000
        self.distancia_entre_grupos = 1000
        self.tiempo_pasado = 0
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.tipo_grupo = ['linia', 'lluvia', 'equis']
        self.tipo_grupo_seleccionado = self.tipo_grupo[random.randrange(0,len(self.tipo_grupo))]

    def equis(self):
        if self.tipo_grupo_seleccionado == 'equis':
            if not self.enemies or self.grupo_iniciado:
                self.grupo_iniciado = True
                current_time = pygame.time.get_ticks()
                if current_time - self.tiempo_pasado >= self.distancia_entre_enemigos:
                    if self.numero_enemigos_lanzados < self.numero_enemigos:
                        self.enemy_sprite = Enemy((self.pos_x_grupo + 70*self.numero_enemigos_lanzados, self.pos_y_grupo), 300, 50, self.screen)
                        self.enemies.add(self.enemy_sprite)
                        self.enemy_sprite = Enemy((self.screen_width - self.pos_x_grupo - 70 * self.numero_enemigos_lanzados, self.pos_y_grupo), 300, 50, self.screen)
                        self.enemies.add(self.enemy_sprite)
                        self.tiempo_pasado = current_time
                        self.numero_enemigos_lanzados += 2
                    else:
                        self.grupo_finalizado = True
                        self.grupo_iniciado = False
                        self.numero_enemigos_lanzados = 0
                        self.tipo_grupo_seleccionado = self.tipo_grupo[random.randrange(0,len(self.tipo_grupo))]


    def linia(self):
        if self.tipo_grupo_seleccionado=='linia':
            if not self.enemies or self.grupo_iniciado:
                self.grupo_iniciado = True
                current_time = pygame.time.get_ticks()
                if current_time - self.tiempo_pasado >= self.distancia_entre_enemigos:
                    if self.numero_enemigos_lanzados < self.numero_enemigos:
                        self.numero_enemigos_lanzados += 1
                        self.enemy_sprite = Enemy((self.pos_x_grupo, self.pos_y_grupo), 50, 50, self.screen)
                        self.enemies.add(self.enemy_sprite)
                        self.tiempo_pasado = current_time
                    else:
                        self.grupo_finalizado = True
                        self.grupo_iniciado = False
                        self.numero_enemigos_lanzados = 0
                        self.tipo_grupo_seleccionado = self.tipo_grupo[random.randrange(0,len(self.tipo_grupo))]

    def lluvia(self):
        if self.tipo_grupo_seleccionado == 'lluvia':
            if not self.enemies or self.grupo_iniciado:
                self.grupo_iniciado = True
                current_time = pygame.time.get_ticks()
                if current_time - self.tiempo_pasado >= self.distancia_entre_enemigos:
                    if self.numero_enemigos_lanzados < self.numero_enemigos:
                        self.enemy_sprite = Enemy((self.pos_x_grupo + 70*self.numero_enemigos_lanzados, self.pos_y_grupo), 100, 50, self.screen)
                        self.numero_enemigos_lanzados += 1
                        self.enemies.add(self.enemy_sprite)
                        self.tiempo_pasado = current_time
                    else:
                        self.grupo_finalizado = True
                        self.grupo_iniciado = False
                        self.numero_enemigos_lanzados = 0
                        self.tipo_grupo_seleccionado = self.tipo_grupo[random.randrange(0,len(self.tipo_grupo))]

    def update(self):
        self.equis()
        self.linia()
        self.lluvia()
