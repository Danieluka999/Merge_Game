import pygame
import itertools
from object import DraggableObject

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Merge Game")
clock = pygame.time.Clock()
running = True

# Spawn Objects
objekte = [DraggableObject(100, 100, r"C:\Users\Nutzer\PycharmProjects\Merge_Game\ROT.png", screen, 1),
           DraggableObject(300, 100, r"C:\Users\Nutzer\PycharmProjects\Merge_Game\GRÜN.png", screen, 2),
           DraggableObject(500, 100, r"C:\Users\Nutzer\PycharmProjects\Merge_Game\BLAU.png", screen, 3),
            DraggableObject(100, 300, r"C:\Users\Nutzer\PycharmProjects\Merge_Game\ROT.png", screen, 1),
            DraggableObject(300, 300, r"C:\Users\Nutzer\PycharmProjects\Merge_Game\GRÜN.png", screen, 2),
            DraggableObject(500, 300, r"C:\Users\Nutzer\PycharmProjects\Merge_Game\BLAU.png", screen, 3),
           ]

# Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for obj in objekte:
                if obj.is_over(event.pos):
                    obj.start_drag()

        if event.type == pygame.MOUSEBUTTONUP:
            for obj in objekte:
                if obj.dragging:
                    obj.stop_drag()

        if event.type == pygame.MOUSEMOTION:
            for obj in objekte:
                if obj.dragging:
                    obj.drag(event.pos)
                    collisions = [(obj1, obj2) for obj1, obj2 in itertools.combinations(objekte, 2)
                                  if DraggableObject.colliderect(obj1, obj2) and obj1.dragging and obj2.dragging]
                    for obj1, obj2 in collisions:
                        DraggableObject.merge_objects(screen, obj1, obj2, objekte)

    # Draw Objects
    screen.fill("White")
    for obj in objekte:
        obj.draw()


    pygame.display.update()

    clock.tick(60)

pygame.quit()
