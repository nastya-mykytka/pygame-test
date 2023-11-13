from pygame import sprite, image, transform


class Gift(sprite.Sprite):
    def __init__(self, x, y, window, width=50, height=50, image_path='images/gift.png'):
        super().__init__()
        self.image = transform.scale(image.load(image_path), (width, height))
        self.width = width
        self.height = height
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.window = window

    def draw(self):
        self.window.blit(self.image, (self.rect.x, self.rect.y))
