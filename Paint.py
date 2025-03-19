import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Простой Пейнт")
clock = pygame.time.Clock()

drawing = False
color = (255, 0, 0)
radius = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                screen.fill((255, 255, 255))
            elif event.key == pygame.K_UP:
                radius += 1
            elif event.key == pygame.K_DOWN and radius > 1:
                radius -= 1
            elif event.key == pygame.K_1:
                color = (255, 0, 0)
            elif event.key == pygame.K_2:
                color = (0, 255, 0)
            elif event.key == pygame.K_3:
                color = (0, 0, 255)

    if drawing:
        pygame.draw.circle(screen, color, pygame.mouse.get_pos(), radius)

    pygame.display.flip()
    clock.tick(60)