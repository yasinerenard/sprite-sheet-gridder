import pygame,os

def spritesheet(image_file, rect, rows=1, cols=1):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, image_file)
    sprite_sheet = pygame.image.load(image_path).convert_alpha()
    sprite_width, sprite_height = rect[2] // cols, rect[3] // rows
    return [sprite_sheet.subsurface(pygame.Rect(rect[0] + col * sprite_width, rect[1] + row * sprite_height, sprite_width, sprite_height))
            for row in range(rows) for col in range(cols)]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))

# Define sprite sheet and parameters
rect = (0, 0, 64, 96)
sprites = spritesheet("walking_mini.png", rect, 4, 4)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    for i, sprite in enumerate(sprites):
        screen.blit(sprite, (i * 64, 100))  # Blit sprites in a row

    pygame.display.flip()

pygame.quit()
