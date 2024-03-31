import pygame

images = [r"tree.png",
          r"stump.png",
          r"plank.png",
          r"box.png",
          r"chest.png",
          r"cabinet.png",
          r"house.png"
          ]


def load_image(image):
    return pygame.image.load(image)
