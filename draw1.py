import pygame
import sys

pygame.init()


""" // Making the Bricks and Window """
width, height = 600, 350
brickWidth = 40
brickHeight = 20
brickSpace = 9.5
numRows = 5
numCol = 12
brickColor = (255, 0, 0)



""" // making Ball.. """
ballX = width // 2
ballY = width // 2
ballRadius = 10
ballColor = (0, 250, 0)
ballSpeedX = 3
ballSpeedY = 3

""" // Making the Paddle """
pdlleWidth = 80 
pdlleHeight = 10
pdlColor = (255, 255, 255)
pdlX = (width - pdlleWidth) // 2
pdlY = height - 30
pdlSpeed = 5




scrn = pygame.display.set_mode((width, height)) # // create the window for game
pygame.display.set_caption('Breackout Atari Dk')

bricks = []
for row in range(numRows):
    for col in range(numCol):
        xPos = col * (brickWidth + brickSpace) + brickSpace
        yPos = row * (brickHeight + brickSpace) + brickSpace
        bricks.append(pygame.Rect(xPos, yPos, brickWidth, brickHeight))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    scrn.fill((0, 0, 0))

    for brik in bricks:
        pygame.draw.rect(scrn, brickColor, brik)
    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and pdlX > 0:
        pdlX -= pdlSpeed
    if keys[pygame.K_RIGHT] and pdlX < width - pdlleWidth:
        pdlX += pdlSpeed

    # // Move the ball
    ballX += ballSpeedX
    ballY += ballSpeedY
    
    # // ball Collission with the walls
    if ballX <= ballRadius or ballX >= width - ballRadius:
        ballSpeedX *= -1
    if ballY <= ballRadius:
        ballSpeedY *= -1

    # // ball collison with the paddles
    if pdlY <= ballY + ballRadius <= pdlY + pdlleHeight and pdlX <= ballX + pdlleWidth:
        ballSpeedY *= -1

    # // ball collison with the bricks
    ballRect = pygame.Rect(ballX - ballRadius, ballY - ballRadius, ballRadius * 2, ballRadius * 2)
    for brik in bricks[:]:
        if ballRect.colliderect(brik):
            bricks.remove(brik)
            ballSpeedY *= -1
            break
        
    # // ball Miss the Paddl and Game Over
    if ballY >= height - ballRadius:
        print("GAME OVER")
        pygame.quit()
        sys.exit()
        
    
    
    pygame.draw.circle(scrn, ballColor, (ballX, ballY), ballRadius)
    
    pygame.draw.rect(scrn, pdlColor, pygame.Rect(pdlX, pdlY, pdlleWidth, pdlleHeight))


    pygame.display.flip()

    pygame.time.Clock().tick(60)


