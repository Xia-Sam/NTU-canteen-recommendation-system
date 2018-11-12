import pygame
pygame.init()

introscreenimage = pygame.image.load("newmap.jpg")
screen = pygame.display.set_mode((1221, 862))
pygame.display.set_caption("NTU map")
screen.blit(introscreenimage, (0, 0))
pygame.display.flip()
crashed = False
while not crashed:
    for event in pygame.event.get():  # get events
        if event.type == pygame.QUIT:
            crashed = True            # quit
pygame.quit()