from pygame import transform, image, sprite


class Wall(sprite.Sprite):
    def __init__(self, x, y, ice_count, direction, window, image_path='images/square-24.gif', width=25, height=25 ):
        super().__init__()
        self.window = window
        self.ice_count = ice_count
        self.direction = direction
        self.image = transform.scale(image.load(image_path), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height

    def draw(self):
        self.window.blit(self.image, (self.rect.x, self.rect.y))
