import pygame


def main():
    initializePygame()
    running = True

    while running:
        pygame.display.update()
        pygame.time.delay(50)
        pygame.event.pump()
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False


def initializePygame():
    pygame.init()
    pygame.display.set_caption("Connect Four: COMP4106 Style")
    screen = pygame.display.set_mode((1500, 1500))
    screen.fill((253, 253, 253))
    pygame.font.init()
    f = pygame.font.SysFont('Arial', 20)
    textsurface = f.render("Connect Four: COMP4106 Style", True, (0, 0, 0))
    screen.blit(textsurface, (625, 40))
    pygame.display.flip()


if __name__ == "__main__":
    main()


