from sprite import Sprite


class Enemy(Sprite):
    def __init__(self, x, y, image_path, width, height, window, speed, x_right, x_left):
        super().__init__(x, y, image_path, width, height, window, speed)
        self.x_right = x_right
        self.x_left = x_left

    direction = "self"

    def moving(self):
        if self.rect.x <= self.x_left:
            self.direction = "right"
        if self.rect.x >= self.x_right:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        if self.direction == "right":
            self.rect.x += self.speed
