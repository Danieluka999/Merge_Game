import pygame

class DraggableObject:
    objects = []

    def __init__(self, x, y, image_file, screen, value):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.screen = screen
        self.value = value
        self.dragging = False
        DraggableObject.objects.append(self)

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def is_over(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos[0] - self.x, mouse_pos[1] - self.y)

    def start_drag(self):
        self.dragging = True

    def stop_drag(self):
        self.dragging = False

    def drag(self, mouse_pos):
        if self.dragging:
            new_x = mouse_pos[0] - self.rect.width // 2
            new_y = mouse_pos[1] - self.rect.height // 2

            if new_x < 0:
                new_x = 0
            elif new_x + self.rect.width > self.screen.get_width():
                new_x = self.screen.get_width() - self.rect.width

            if new_y < 0:
                new_y = 0
            elif new_y + self.rect.height > self.screen.get_height():
                new_y = self.screen.get_height() - self.rect.height

            self.x = new_x
            self.y = new_y

    # @classmethod
    # def spawn_objects(cls, screen):
        # red_image = pygame.image.load(r"C:\Users\Nutzer\Pictures\ROT.png")
        # red_image = pygame.transform.scale(red_image, (100, 100))
        # red_object = cls(100, 100, red_image, screen, 1)

        # blue_image = pygame.image.load(r"C:\Users\Nutzer\Pictures\BLAU.png")
        # blue_image = pygame.transform.scale(blue_image, (100, 100))
        # blue_object = cls(100, 300, blue_image, screen, 2)

        # green_image = pygame.image.load(r"C:\Users\Nutzer\Pictures\GRÜN.png")
        # green_image = pygame.transform.scale(green_image, (100, 100))
        # green_object = cls(100, 500, green_image, screen, 3)

    @classmethod
    def merge_objects(cls, screen, obj1, obj2, objekte):
        # Check if value is the same
        if obj1.value == obj2.value:
            # New position of merged object
            merged_x = min(obj1.rect.x, obj2.rect.x)
            merged_y = min(obj1.rect.y, obj2.rect.y)

            # Load new merged image + new DraggableObject instance
            merged_image = pygame.Surface((obj1.rect.width, obj1.rect.height))
            merged_image.blit(obj1.image, (0, 0))
            merged_image.blit(obj2.image, (obj1.rect.width, 0))

            # Save merged image to temporary file
            new_image = r"C:\Users\Nutzer\PycharmProjects\Merge_Game\GELB.png"

            # Get new merged value
            merged_value = obj1.value + obj2.value

            # Create merged_object
            merged_object = cls(merged_x, merged_y, new_image, screen, merged_value)

            if obj1 in objekte:
                objekte.remove(obj1)
            if obj2 in objekte:
                objekte.remove(obj2)
            objekte.append(merged_object)

    @classmethod
    def colliderect(cls, obj1, obj2):
        return obj1.rect.colliderect(obj2.rect)

