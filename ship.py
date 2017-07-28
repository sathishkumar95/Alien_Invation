import pygame
class Ship():
    def __init__(self,screen):
        """intialize ship and set its starting position"""
        self.screen=screen
        """load the ship image and get its rect"""
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        """Start every ship at the bottom of the screen"""
        self.rect.centrex = self.screen_rect.centrex
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)
