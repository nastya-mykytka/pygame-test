from pygame import key, K_LEFT, K_RIGHT, K_UP, K_DOWN

from constants import WINDOW_WIDTH, WINDOW_HEIGHT
from sprite import Sprite


class Player(Sprite):
    def __init__(self, x, y, image_path, width, height, window, speed, walls):
        super().__init__(x, y, image_path, width, height, window, speed)
        self.walls = walls

    def moving(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0 and not self.check_collision(-self.speed, 0):
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < WINDOW_WIDTH - self.width and not self.check_collision(self.speed, 0):
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 100 and not self.check_collision(0, -self.speed):
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < WINDOW_HEIGHT - self.height and not self.check_collision(0, self.speed):
            self.rect.y += self.speed

    def check_collision(self, dx, dy):
        for wall in self.walls:
            if self.rect.move(dx, dy).colliderect(wall.rect):
                return True

        return False


