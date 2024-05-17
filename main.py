import pygame
import sys
import circle as c
import pygame.color as color
import time

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 800
FPS = 60

# Set up the display
screen = pygame.display.set_mode((800, 800), pygame.FULLSCREEN)

# Set up the clock
clock = pygame.time.Clock()


circle = c.circle(screen, color.Color("red"), (WIDTH // 2, HEIGHT // 2), 150, 10)
circle1 = c.circle(screen, color.Color("blue"), (200, 200), 150, 10)
circle.balls.append(circle1)
circle.balls.append(circle)



# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.size
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.quit()
                sys.exit()

    # Update
    
    # Draw / render
    screen.fill((0, 0, 0))
    for ball in circle.balls:
        ball.draw()
        ball.move()
        
    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)