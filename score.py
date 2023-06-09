import pygame.font
from gun import Gun
from pygame.sprite import Group
class Score():
    #вывод игровой информации
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (139,195,74)
        self.font = pygame.font.SysFont(None, 35)
        self.image_score()
        self.image_high_score()
        self.image_guns()

    def image_score(self):
        #преобразывавает текст счета в графическое изображение
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right-20
        self.score_rect.top = 10

    def image_high_score(self):
        #преобразует рекорд в графическое изображение
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.high_score_rect  = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def image_guns(self):
        #количество жизней
        self.guns = Group()
        for gun_number in range(self.stats.guns_left):
            gun = Gun(self.screen)
            gun.rect.x = 15 + gun_number * gun.rect.width
            gun.rect.y = 20
            self.guns.add(gun)

    def show_score(self):
        #вывод счета на экран
        f1 = pygame.font.Font(None, 36)
        text1 = f1.render('Current score:', True, (139,195,74))
        f2 = pygame.font.Font(None, 36)
        text2 = f2.render('High score:', True, (139, 195, 74))
        self.screen.blit(text1, (475,10))
        self.screen.blit(text2, (195, 20))
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.guns.draw(self.screen)