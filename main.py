import pygame
pygame.init()

photo = pygame.image.load("/Users/evahiso/Desktop/buildingPic.png")

RED = (255, 0, 0)
size = (500, 500)
screen = pygame.display.set_mode((size))


rectangle = pygame.Rect(50, 50, 200, 100)
pygame.draw.rect(screen, RED, rectangle)
screen.blit(photo, (10,10))

# Update the screen
pygame.display.update()

# Keep the window open until the user closes it
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()