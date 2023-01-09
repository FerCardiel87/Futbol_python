import pygame

pygame.init()

X = 1000
Y = 600
screen = pygame.display.set_mode((X, Y))
running = True

pygame.display.set_caption("Pelota que rebota")

# Ball
ballImg = pygame.image.load("soccer-ball-94.png")
ballX = 50  # position x
ballY = 50  # position y
ballX_change = 4  # velocity x
ballY_change = 4# velocity y

# Game Loop
while running:
    # set background
    screen.fill((10, 10, 10))

    # set ball
    screen.blit(ballImg, (ballX, ballY))

    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update ball
    ballX += ballX_change
    ballY += ballY_change

    # collision detection
    # top
    if ballX >= X - 90:
        ballX_change = -1.5
    # bottom
    elif ballX <= 0:
        ballX_change = 1.5

    # right
    if ballY >= Y - 90:
        ballY_change = -1.5
    # left
    elif ballY <= 0:
        ballY_change = 1.5

    credit_font = pygame.font.Font("freesansbold.ttf", 12)
    credit = credit_font.render("Luis Fernando Cardiel Avila", True, (255, 255, 0))
    screen.blit(credit, (10, 580))
    # update frame
    pygame.display.update()
