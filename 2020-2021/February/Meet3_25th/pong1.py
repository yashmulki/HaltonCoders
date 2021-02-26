import sys
import pygame

# Text to RGB
# A dictionary where the color word is the key and the rbg equivalent is the value
Colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "darkRed": (55, 0, 0),
    "lightRed": (255, 108, 23),
    "green": (0, 255, 0),
    "darkGreen": (0, 55, 0),
    "blue": (0, 0, 255),
    "darkBlue": (0, 0, 55),
    "navyBlue": (0, 30, 100),
    "lightPurple": (113, 0, 155),
    "darkPurple": (55, 0, 55),
    "lightGrey": (200, 200, 200),
    "paleTurquoise": (175, 238, 238),
    "lightYellow": (255, 240, 23)
}

pygame.init()  # init stands for initialize
clock = pygame.time.Clock()  # Makes a clock in pygame that you can access with the variable 'clock'

# win: window
winWidth, winHeight = 800, 600  # Sets the dimensions of the window
win = pygame.display.set_mode((winWidth, winHeight))  # makes the display(window) with the dimensions you gave
pygame.display.set_caption("Pong")  # sets the name of the window
winColor = pygame.Color('grey12')  # Sets a color for the window that I will use in the future

paddleWidth, paddleHeight = 10, 90  # sets the dimensions of the paddles
paddleColor = Colors['lightGrey']  # the colour of the paddle
paddleSpeed = 5  # the number of pixels the paddle will move by each time

ballDiameter = 16
ballSpeedX = 4
ballSpeedY = 4
ballStartX = winWidth/2 - ballDiameter/2
ballStartY = winHeight/2 - ballDiameter/2
ball = pygame.rect.Rect(ballStartX, ballStartY, ballDiameter, ballDiameter)
# As the height and width are the same, it will be a square

ballMove = False  # Variable for the whether the ball is moving
while True:
    keysPressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if keysPressed[pygame.K_SPACE]:
            ballMove = not ballMove

    if ballMove:
        if ball.x < 0:
            ballSpeedX = abs(ballSpeedX)
        if ball.y < 0:
            ballSpeedY = abs(ballSpeedY)
        if ball.x + ballDiameter > winWidth:
            ballSpeedX = - abs(ballSpeedX)
        if ball.y + ballDiameter > winHeight:
            ballSpeedY = - abs(ballSpeedY)
        ball.x += ballSpeedX
        ball.y += ballSpeedY

    win.fill(winColor)
    pygame.draw.ellipse(win, Colors["lightGrey"], ball)

    pygame.display.flip()  # update the pygame window/redraw it
    clock.tick(60)  # in milliseconds
