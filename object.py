import pygame
from images import images

pygame.init()


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
        for obj in self.objects:
            if obj is not self:
                obj.dragging = False

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

    @classmethod
    def merge_objects(cls, screen, obj1, obj2, objekte):
        # Check if value is the same
        if obj1.value == obj2.value and obj1.value <= 6:

            merged_image = pygame.Surface((obj1.rect.width, obj1.rect.height))
            merged_image.blit(obj1.image, (0, 0))
            merged_image.blit(obj2.image, (obj1.rect.width, 0))

            # Get new merged value
            merged_value = obj1.value + 1

            # Get new image
            new_image = images[merged_value - 1]

            # Create merged_object
            merged_object = cls(obj2.x, obj2.y, new_image, screen, merged_value)

            if obj1 in objekte:
                objekte.remove(obj1)
            if obj2 in objekte:
                objekte.remove(obj2)
            objekte.append(merged_object)

    def colliderect(self, obj1, obj2):
        obj1_rect = obj1.image.get_rect()
        obj2_rect = obj2.image.get_rect()
        obj1_rect.topleft = (obj1.x, obj1.y)
        obj2_rect.topleft = (obj2.x, obj2.y)
        return obj1_rect.colliderect(obj2_rect)

class MainMenu:
    def __init__(self, screen, main_menu_image, play_button):
        self.screen = screen
        self.main_menu_image = main_menu_image
        self.play_button = play_button
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.center = (self.screen.get_width() // 2, self.screen.get_height() // 2)

    def draw_main_menu(self):
        self.screen.blit(self.main_menu_image, (0, 0))
        self.screen.blit(self.play_button, self.play_button_rect)
        pygame.display.update()

    def check_collision(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pos_vector = pygame.math.Vector2(mouse_pos)
        return self.play_button_rect.collidepoint(mouse_pos_vector.x, mouse_pos_vector.y)
