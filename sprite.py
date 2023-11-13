from pygame import sprite, image, transform


class Sprite(sprite.Sprite):
    def __init__(self, x, y, image_path, width, height, window, speed=5):
        super().__init__()
        self.image = transform.scale(image.load(image_path), (width, height))
        self.width = width
        self.height = height
        self.speed = speed
        self.window = window
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        self.window.blit(self.image, (self.rect.x, self.rect.y))

    def move_to(self, x, y):
        self.rect.x = x
        self.rect.y = y
