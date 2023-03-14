import pygame

background_colour = (12, 139, 61)


tela = pygame.display.set_mode((1300, 600))

pygame.display.set_caption('olá manoel')

tela.fill(background_colour)

pygame.display.flip()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False