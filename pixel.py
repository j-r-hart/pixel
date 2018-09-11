import pygame
 
# Define some colors
BLACK =  (0  , 0  , 0  )
GREY =   (128, 128, 128)
WHITE =  (255, 255, 255)
GREEN =  (0  , 255, 0  )
RED =    (255, 0  , 0  )
BLUE =   (0  , 0  , 255)

WIDTH = 20
HEIGHT = 20
MARGIN = (WIDTH+HEIGHT)//8

# Define layout GRIDSIZE x GRIDSIZE
GRIDSIZE = 35

# Determine the size of the screen
SWIDTH = int((GRIDSIZE+2)*WIDTH)+(MARGIN*(GRIDSIZE+1))
SHEIGHT = int((GRIDSIZE)*HEIGHT)+(MARGIN*(GRIDSIZE+1))


grid = []
for row in range(GRIDSIZE):
    grid.append([])
    for column in range(GRIDSIZE):
        grid[row].append(0)


pixel_drawing = False
 
pygame.init()
 
# Set the width and height of the screen [SWIDTH, SHEIGHT]
size = (SWIDTH, SHEIGHT)
screen = pygame.display.set_mode(size)

# Set initial color selection to white
sel = 0
sel_color = WHITE
 
pygame.display.set_caption("Pixel")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pixel_drawing = True
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH+MARGIN)
            row = pos[1] // (HEIGHT+MARGIN)
            if column < GRIDSIZE:
                if grid[row][column] != sel:
                    grid[row][column] = sel
            elif column == GRIDSIZE+1:
                if row == 0:
                    sel = 0
                    sel_color = WHITE
                    print("White")
                elif row == 1:
                    sel = 1
                    sel_color = GREEN
                    print("Green")
                elif row == 2:
                    sel = 2
                    sel_color = RED
                    print("Red")
                elif row == 3:
                    sel = 3
                    sel_color = BLUE
                    print("Blue")
                elif row == 4:
                    sel = 4
                    sel_color = BLACK
                    print("Black")
                elif row == GRIDSIZE-2:
                    grid = []
                    for row in range(GRIDSIZE):
                        grid.append([])
                        for column in range(GRIDSIZE):
                            grid[row].append(0)
                    

            print("Click", pos, row, column)
                
                    
        elif event.type == pygame.MOUSEBUTTONUP:
            pixel_drawing = False
            print("Release")
                
            
        elif event.type == pygame.MOUSEMOTION:
            if pixel_drawing:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH+MARGIN)
                row = pos[1] // (HEIGHT+MARGIN)
                if column < GRIDSIZE:
                    if grid[row][column] != sel:
                        grid[row][column] = sel
            
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREY)
 
    # --- Drawing code should go here
    pygame.draw.rect(screen, WHITE, [(SWIDTH - WIDTH - MARGIN),
                    (MARGIN), WIDTH, HEIGHT])
    pygame.draw.rect(screen, GREEN, [(SWIDTH - WIDTH - MARGIN),
                                    (HEIGHT+2*MARGIN), WIDTH, HEIGHT])
    pygame.draw.rect(screen, RED, [(SWIDTH - WIDTH - MARGIN),
                                    (2*HEIGHT+3*MARGIN), WIDTH, HEIGHT])
    pygame.draw.rect(screen, BLUE, [(SWIDTH - WIDTH - MARGIN),
                                    (3*HEIGHT+4*MARGIN), WIDTH, HEIGHT])
    pygame.draw.rect(screen, BLACK, [(SWIDTH - WIDTH - MARGIN),
                                    (4*HEIGHT+5*MARGIN), WIDTH, HEIGHT])


    # Show option to clear / reset
    pygame.draw.rect(screen, RED, [(SWIDTH - WIDTH - MARGIN),
                                    (SHEIGHT- 2*HEIGHT- 2*MARGIN),
                                   WIDTH, HEIGHT])
    pygame.draw.rect(screen, WHITE, [(SWIDTH - WIDTH - MARGIN),
                                    (SHEIGHT- 2*HEIGHT- 2*MARGIN),
                                   0.5*WIDTH, 0.5*HEIGHT])
    

    # Show selected color
    pygame.draw.rect(screen, sel_color, [(SWIDTH - WIDTH - MARGIN),
                                    (SHEIGHT- HEIGHT- MARGIN),
                                   WIDTH, HEIGHT])
 
    
    
    for row in range(GRIDSIZE):
        for column in range(GRIDSIZE):
            color =WHITE
            if grid[row][column] == 1:
                color = GREEN
            elif grid[row][column] == 2:
                color = RED
            elif grid[row][column] == 3:
                color = BLUE
            elif grid[row][column] == 4:
                color = BLACK
                          
            pygame.draw.rect(screen,
                            color, [(WIDTH+MARGIN)*column+MARGIN,
                                    (HEIGHT+MARGIN)*row+MARGIN,WIDTH,HEIGHT])
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
