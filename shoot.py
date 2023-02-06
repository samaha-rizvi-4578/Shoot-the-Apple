import pygame
from random import randint

message = " "
score = 0
# Initialize the Pygame display
pygame.display.init()
pygame.mixer.init()

# Load the music file
pygame.mixer.music.load("music.ogg")

# Play the music file in an infinite loop
pygame.mixer.music.play(-1)

# Set a video mode
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Load the image file
apple_image = pygame.image.load("apple.png")
orange_image = pygame.image.load("orange.png")

# Create a surface from the image
apple_surface = pygame.Surface.convert_alpha(apple_image)
orange_surface = pygame.Surface.convert_alpha(orange_image)

# Create a rect from the surface
apple_rect = apple_surface.get_rect()
orange_rect = orange_surface.get_rect()

# Add font object
font = pygame.font.Font(None, 36)

def draw(message):
    screen.fill((153, 0, 255))
    screen.blit(apple_surface, apple_rect)
    screen.blit(orange_surface, orange_rect)
    score_label = font.render("Score:", 1, (255, 255, 255))
    score_text = font.render(str(score), 1, (255, 255, 255))
    screen.blit(score_label, (10, 10))
    screen.blit(score_text, (100, 10))
    message_text=font.render(message, 1, (255, 255, 255))
    screen.blit(message_text, (200, 10))
    pygame.display.update()

def place_apple():
    apple_rect.x = randint(10, 600)
    apple_rect.y = randint(10, 400)
    orange_rect.x = randint(10, 600)
    orange_rect.y = randint(10, 400)
def welcome_screen():
    screen.fill((153, 0, 255))
    welcome_text = font.render("Welcome to the Apple Shooter Game!", 1, (102, 0, 51))
    instruct = font.render("Only Shoot Apples!",1,(255,255,255))
    screen.blit(welcome_text, (200, 300))
    screen.blit(instruct, (200,500))
    pygame.display.update()
    pygame.time.wait(3000)

def end_screen():
    screen.fill((107, 0, 179))
    end_text = font.render("Game Over!", 1,(102, 0, 51))
    screen.blit(end_text, (500,300))
    score_label = font.render("Score:", 1, (255, 255, 255))
    score_text = font.render(str(score), 1, (255, 255, 255))
    screen.blit(score_label, (500, 400))
    screen.blit(score_text, (700, 400))
    pygame.display.update()
    pygame.time.wait(2000)
    
welcome_screen()
place_apple()

def on_mouse_down(pos):
    global message
    if apple_rect.collidepoint(pos):
        print("Good Shot!")
        message = "Good Shot!"
        global score
        score += 1
        place_apple()
    else:
        print("You Missed!")
        message = "You Missed!"
        draw(message)
        end_screen()
        quit()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            on_mouse_down(pygame.mouse.get_pos())

    draw(message)
    
end_screen()
pygame.display.quit()
