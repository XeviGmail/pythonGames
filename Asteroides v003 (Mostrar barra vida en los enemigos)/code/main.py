import os.path
import random
import pygame, sys
import pymunk
from player import Player
from rock import Rock
from residuo import Residuo
from laser import Laser
from grupo_enemigos import GrupoEnemigos

H_50D2FE = (80,210,254)

class Game():
    def __init__(self):
        self.FPS = 60
        self.clock = pygame.time.Clock()

        # Edges
        self.screen_width = 1024
        self.screen_height = 800
        self.space = pymunk.Space()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Asteroides')

        # Rocks (space, pos_x, pos_y, velocity, radius)
        self.rocks = pygame.sprite.Group()
        self.residuos = pygame.sprite.Group()
        for _ in range(4):
            velocity = (random.uniform(-60, 60), random.uniform(-200, 0))
            self.rock_sprite = Rock(self.space, random.uniform(0 + 50, self.screen_width - 50), self.screen_height + 20, velocity, random.randint(1,2) * 10, self.screen_width, self.screen_height)
            self.rocks.add(self.rock_sprite)

        # Enemies
        self.enemies = pygame.sprite.Group()
        self.groupo_enemies = GrupoEnemigos(self.enemies, self.screen_width, self.screen_height, self.screen)

        # Enemies Lasers
        self.enemy_lasers = pygame.sprite.Group()

        #Player (pos, speed, constraint, images)
        speed_player = 5
        self.player_sprite = Player((self.screen_width/2, self.screen_height-10), speed_player, (0, self.screen_width, 0, self.screen_height), self.get_player_image(), self.screen_width, self.screen_height)
        self.player = pygame.sprite.GroupSingle(self.player_sprite)
        # self.player_sprite.set_images(self.get_player_image_2())

        # Fonts
        self.consolas = pygame.font.SysFont('consolas', 30)

        # Puntuacion
        self.puntuacion = 0
        self.num_residuos = 0

    def update_nave(self):
        if self.puntuacion >=  20 and self.puntuacion<40:
            self.player_sprite.set_num_laser(2)
        if self.puntuacion >= 40:
            self.player_sprite.set_num_laser(3)

    def cc(self, point):
        """
            Concert coordinades
        """
        return int(point[0]), self.screen_height - int(point[1])

    def get_player_image(self):
        animacion_nave = []
        for i in range(15):
            archivo_nave = f'nave-1-{i:02d}.png'
            image_raw = pygame.image.load(os.path.join('../graphics/ship/01', archivo_nave))
            image = pygame.transform.scale(image_raw, (64, 32))
            animacion_nave.append(image)
        return animacion_nave

    def get_player_image_2(self):
        """
            para demostrar que se puede cambiar na nave on the fly
        """
        animacion_nave = []
        for i in range(16):
            archivo_nave = f'nave-1-{i:02d}.png'
            image = pygame.image.load(os.path.join('../graphics/ship/02', archivo_nave))
            animacion_nave.append(image)
        return animacion_nave

    def collision_checks(self):
        # player laser
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                laser_rocks_colision = pygame.sprite.spritecollide(laser, self.rocks, False)
                if laser_rocks_colision:
                    for rock in laser_rocks_colision:
                        residuo_sprite = Residuo(rock.rect.x, rock.rect.y, rock.rock_radius, rock.body.velocity)
                        self.residuos.add(residuo_sprite)
                        rock.eliminar()
                        self.puntuacion += 1
                        velocity = (random.uniform(-60, 60), random.uniform(-200, 0))
                        self.rock_sprite = Rock(self.space, random.uniform(50, self.screen_width - 50), self.screen_height + 20, velocity, random.randint(1,2) * 10, self.screen_width, self.screen_height)
                        self.rocks.add(self.rock_sprite)
                        laser.kill()
                laser_enemy_colision = pygame.sprite.spritecollide(laser, self.enemies, False)
                if laser_enemy_colision:
                    for enemy in laser_enemy_colision:
                        enemy.substract_life(self.player_sprite.get_power())
                        if enemy.is_dead():
                            enemy.kill()
                            self.puntuacion += 10
                        laser.kill()
        # Laser de los enemigos
        if self.enemy_lasers:
            for laser in self.enemy_lasers:
                if pygame.sprite.spritecollide(laser, self.player, False):
                    self.player_sprite.substract_life(laser.get_power())
                    print('te han dado')
                    if self.player_sprite.is_dead():
                        print('estas muerto')
                    laser.kill()

        # colision de rocas con player
        player_rocks_collision = pygame.sprite.spritecollide(self.player_sprite, self.rocks, False)
        if player_rocks_collision:
            for rock in player_rocks_collision:
                rock.eliminar()
                velocity = (random.uniform(-60, 60), random.uniform(-200, 0))
                self.rock_sprite = Rock(self.space, random.uniform(50, self.screen_width - 50), self.screen_height + 20, velocity, random.randint(1,2) * 10, self.screen_width, self.screen_height)
                self.rocks.add(self.rock_sprite)

        # Captura de residuos
        player_residuos_collision = pygame.sprite.spritecollide(self.player_sprite, self.residuos, False)
        if player_residuos_collision:
            for residuo in player_residuos_collision:
                residuo.kill()
                self.num_residuos += 1

    def bounds(self):
        for rock in self.rocks:
            if rock.rect.x <= -50 or rock.rect.x >= self.screen_width + 50 or rock.rect.y <= -50 or rock.rect.y >= self.screen_width + 50 :
                rock.eliminar()
                velocity = (random.uniform(-60, 60), random.uniform(-200, 0))
                self.rock_sprite = Rock(self.space, random.uniform(50, self.screen_width - 50), self.screen_height + 20, velocity, 20, self.screen_width, self.screen_height)
                self.rocks.add(self.rock_sprite)
        for residuo in self.residuos:
            if residuo.rect.x <= -50 or residuo.rect.x >= self.screen_width + 50 or residuo.rect.y <= -50 or residuo.rect.y >= self.screen_width + 50 :
                residuo.kill()

        for enemy in self.enemies:
            if enemy.rect.x <= -50 or enemy.rect.x >= self.screen_width + 50 or enemy.rect.y <= -50 or enemy.rect.y >= self.screen_width + 50 :
                enemy.kill()

    def background(self):
        self.screen.fill('grey')

    # def muestra_texto(self, fuente, texto, color, dimensiones, x, y):
    #     tipo_letra = pygame.font.Font(fuente, dimensiones)
    #     superficie = tipo_letra.render(texto, False, color)
    #     rect = superficie.get_rect()
    #     rect.center = (x, y)
    #     self.screen.blit(superficie, rect)

    def enemy_shoot(self):
        if self.enemies.sprites():
            # con la linia siguiente conseguimos que los lasers sean coherentes con la cantidad de enemigos
            pygame.time.set_timer(ENEMY_LASER, random.randint(int(2*500/len(self.enemies)), int(2*1000/len(self.enemies))))
            random_enemy = random.choice(self.enemies.sprites())
            laser_sprite = Laser(random_enemy.rect.center, -6, 'blue', random_enemy.get_power(), self.screen_width, self.screen_height)
            self.enemy_lasers.add(laser_sprite)

    def life_bar(self, screen, x, y, life):
        largo = 200
        ancho = 25
        calculo_barra = int((life/100) * largo)
        borde = pygame.Rect(x, y, largo, ancho)
        rectangulo = pygame.Rect(x, y, calculo_barra, ancho)
        pygame.draw.rect(screen, 'blue', borde, 3)
        pygame.draw.rect(screen, H_50D2FE, rectangulo)
        screen.blit(pygame.transform.scale(self.player_sprite.image, (25, 25)), (545, 15))

    def run(self):
        self.background()
        self.player.update()
        self.update_nave()
        self.player.sprite.lasers.draw(self.screen)
        self.player.draw(self.screen)

        # Rocas
        self.rocks.update()
        self.rocks.draw(self.screen)

        # Residuos
        self.residuos.update()
        self.residuos.draw(self.screen)

        # Enemigos
        self.enemies.update()
        self.enemies.draw(self.screen)
        self.groupo_enemies.update()

        self.enemy_lasers.update()
        self.enemy_lasers.draw(self.screen)

        self.bounds()
        self.collision_checks()
        self.space.step(1/self.FPS)

        # Text
        # self.muestra_texto(self.consolas, str(self.puntuacion).zfill(4), 'red', 40, 550, 50)
        # self.muestra_texto(self.consolas, f'Residuos: {str(self.num_residuos).zfill(4)}', 'red', 40, 250, 50)
        self.life_bar(self.screen, 380, 15, self.player_sprite.get_life())
        pygame.display.flip()
        self.clock.tick(self.FPS)

    def intro(self):
        tecla = pygame.key.get_pressed()
        return False if tecla[pygame.K_RETURN] else True

    def ventana_intro(self):
        self.screen.fill((0,0,0))
        instrucciones = self.consolas.render('Asteroides y mas...', False, 'red')
        self.screen.blit(instrucciones, (self.screen_width//2 - instrucciones.get_width()//2, 300))
        pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    game = Game()
    """ 
        creamos un evento que se ejecutara cada entre el random(1000, 2000)
        Al ejecutarse el evento se ejecutara game.enemy_shoot()
    """

    while game.intro():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        game.ventana_intro()

    ENEMY_LASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ENEMY_LASER, random.randint(500, 1000))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()
            if event.type == ENEMY_LASER:
                game.enemy_shoot()
        game.run()

