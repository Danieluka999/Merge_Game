import pygame, random, sys
from object import DraggableObject, MainMenu
from images import load_image, images

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Merge Game")
clock = pygame.time.Clock()
running = True
running2 = True


pygame.mixer.music.load(r"music.mp3")
pygame.mixer.music.set_volume(0)
pygame.mixer.music.play(-1, 0.0)

main_menu = MainMenu(screen, load_image(r"background.png"), load_image(r"start.png"))

while running2:
    main_menu.draw_main_menu()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if main_menu.check_collision():
                running2 = False

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)


def spawn_new_object(screen, objekte):
    x = random.randint(0, screen.get_width() - 100)
    y = random.randint(0, screen.get_height() - 100)
    new_object = DraggableObject(x, y, images[0], screen, 1)
    objekte.append(new_object)


SPAWN_INTERVAL = 10000
pygame.time.set_timer(pygame.USEREVENT, SPAWN_INTERVAL)

objekte = [DraggableObject(100, 100, images[0], screen, 1)]

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

                    for other in objekte:
                        if obj is not other and obj.colliderect(obj, other) and obj.value == other.value:
                            DraggableObject.merge_objects(screen, obj, other, objekte)

                    obj.stop_drag()

        if event.type == pygame.MOUSEMOTION:
            for obj in objekte:
                if obj.dragging:
                    obj.drag(event.pos)

        if event.type == pygame.USEREVENT:
            spawn_new_object(screen, objekte)

    # Draw Objects
    bg = pygame.image.load(r"grassbg.png")
    screen.blit(bg, (0, 0))
    for obj in objekte:
        obj.draw()

    pygame.display.update()

    clock.tick(60)

pygame.quit()
