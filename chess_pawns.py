from Requried_functions import *


class chess_piece(pygame.sprite.Sprite):


    def __init__(self, image, position, team):
        pygame.sprite.Sprite.__init__(self)
        self.team = team
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(70,70))
        self.position = position
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = position.topleft
        self.rect.center = position.center

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def drag(self, cursor):
        self.rect.center = cursor

    def update(self, position):
        self.position = position
        self.rect.center = position.center




drawboard()
# This function is called to initialise the following chess pieces with in the square boxes defined in the function

piece = chess_piece(r"C:\Users\SuresH\Pictures\chess\wking.jpeg", square_boxes[60], 'White')

