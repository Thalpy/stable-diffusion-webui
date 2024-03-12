# Import the modules
import pygame
import random

# Define the screen size and the pixel size
screen_width = 3840 # 4k width
screen_height = 2160 # 4k height
pixel_size = 1 # 1 pixel

# Initialize pygame and create a screen object
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# Define a function to generate a random colour (no greys or blacks)
def random_colour():
    r = random.randint(0, 255) # red component
    g = random.randint(0, 255) # green component
    b = random.randint(0, 255) # blue component
    # Check if the colour is grey or black (all components are equal or zero)
    if r == g == b or r == g == b == 0:
        # If so, generate a new colour recursively
        return random_colour()
    else:
        # Otherwise, return the colour as a tuple
        return (r, g, b)

# Define a function to draw a pixel on the screen with a random colour
def draw_pixel(x, y):
    # Get a random colour
    colour = random_colour()
    # Create a rectangle object with the pixel size and position
    pixel = pygame.Rect(x, y, pixel_size, pixel_size)
    # Draw the rectangle on the screen with the colour
    pygame.draw.rect(screen, colour, pixel)

# Define a function to update the screen with random pixels every 10ms
def update_screen():
    # Loop through every pixel on the screen
    for x in range(0, screen_width, pixel_size):
        for y in range(0, screen_height, pixel_size):
            # Draw a pixel with a random colour
            draw_pixel(x, y)
    # Update the display
    pygame.display.flip()
    # Set a timer to call this function again after 10ms
    pygame.time.set_timer(pygame.USEREVENT, 10)

# Start the main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        # If the user presses the escape key or closes the window, exit the loop
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
            running = False
        # If the timer event occurs, update the screen
        elif event.type == pygame.USEREVENT:
            update_screen()
# Quit pygame
pygame.quit()