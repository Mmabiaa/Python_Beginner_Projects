import pygame
import sys
import random
import math
from pygame.locals import *

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Will You Marry Me?")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255, 182, 193)
LIGHT_PINK = (255, 209, 220)
BACKGROUND = (10, 10, 40)  # Dark blue background

# Font
font_large = pygame.font.SysFont('comicsansms', 60, bold=True)
font_medium = pygame.font.SysFont('comicsansms', 36)
font_small = pygame.font.SysFont('comicsansms', 24)

# Heart class
class Heart:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.size = random.randint(10, 30)
        self.speed = random.uniform(1, 3)
        self.color = (random.randint(200, 255), random.randint(0, 100), random.randint(100, 200))
        self.angle = 0
        
    def draw(self):
        # Draw a heart shape
        points = []
        for t in range(0, 360, 10):
            t_rad = math.radians(t)
            x = 16 * (math.sin(t_rad) ** 3)
            y = 13 * math.cos(t_rad) - 5 * math.cos(2*t_rad) - 2 * math.cos(3*t_rad) - math.cos(4*t_rad)
            points.append((self.x + x * self.size/16, self.y - y * self.size/16))
        
        if len(points) > 2:
            pygame.draw.polygon(screen, self.color, points)
    
    def update(self):
        self.y -= self.speed
        self.angle += 0.05
        self.x += math.sin(self.angle) * 0.5
        
        # Reset heart if it goes off screen
        if self.y < -50:
            self.y = HEIGHT + 10
            self.x = random.randint(0, WIDTH)

# Balloon class
class Balloon:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = HEIGHT + 50
        self.speed = random.uniform(1, 3)
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.size = random.randint(30, 60)
        self.sway = random.uniform(-1, 1)
        
    def draw(self):
        # Draw balloon
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)
        pygame.draw.line(screen, WHITE, (self.x, self.y + self.size), 
                         (self.x + self.sway * 10, self.y + self.size + 30), 2)
    
    def update(self):
        self.y -= self.speed
        self.x += self.sway
        
        # Reset balloon if it goes off screen
        if self.y < -100:
            self.y = HEIGHT + 50
            self.x = random.randint(0, WIDTH)

# Particle effect for splashes
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-3, 3)
        self.vy = random.uniform(-3, 3)
        self.color = (random.randint(200, 255), random.randint(100, 200), random.randint(100, 200))
        self.size = random.randint(2, 5)
        self.life = 30
        
    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.life -= 1
        return self.life > 0

# Create objects
hearts = [Heart() for _ in range(30)]
balloons = [Balloon() for _ in range(15)]
particles = []
knockout_timer = 0
knockout_duration = 60
show_message = False
message_timer = 0

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_SPACE:
                # Create a particle splash at random position
                for _ in range(50):
                    particles.append(Particle(random.randint(0, WIDTH), random.randint(0, HEIGHT)))
                knockout_timer = knockout_duration
                show_message = True
                message_timer = 300  # Show message for 5 seconds
    
    # Fill background
    screen.fill(BACKGROUND)
    
    # Update and draw hearts
    for heart in hearts:
        heart.update()
        heart.draw()
    
    # Update and draw balloons
    for balloon in balloons:
        balloon.update()
        balloon.draw()
    
    # Update and draw particles
    particles = [p for p in particles if p.update()]
    for particle in particles:
        particle.draw()
    
    # Handle knockout effect (screen flash)
    if knockout_timer > 0:
        knockout_timer -= 1
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        alpha = int(200 * (knockout_timer / knockout_duration))
        overlay.fill((255, 255, 255, alpha))
        screen.blit(overlay, (0, 0))
    
    # Display messages
    if show_message:
        # "I LOVE YOU" text
        love_text = font_large.render("I LOVE YOU", True, LIGHT_PINK)
        text_rect = love_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 50))
        screen.blit(love_text, text_rect)
        
        # Proposal text
        proposal_text = font_medium.render("Will you marry me?", True, WHITE)
        proposal_rect = proposal_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 30))
        screen.blit(proposal_text, proposal_rect)
        
        # Instructions
        if message_timer < 150:  # Blink the instruction
            if (message_timer // 10) % 2 == 0:
                instruction = font_small.render("Press SPACE for another surprise!", True, WHITE)
                instruction_rect = instruction.get_rect(center=(WIDTH//2, HEIGHT - 50))
                screen.blit(instruction, instruction_rect)
        
        message_timer -= 1
        if message_timer <= 0:
            show_message = False
    
    # Always show the initial instruction
    if not show_message:
        instruction = font_small.render("Press SPACE to see the surprise!", True, WHITE)
        instruction_rect = instruction.get_rect(center=(WIDTH//2, HEIGHT - 50))
        screen.blit(instruction, instruction_rect)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
