import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Retro Pong Game")

WHITE = (255,255,255)
BLACK = (0,0,0)

paddle_w, paddle_h = 10, 60
left_paddle = pygame.Rect(10, HEIGHT //2 - paddle_h // 2, paddle_w, paddle_h)
right_paddle = pygame.Rect(WIDTH - 20, HEIGHT // 2 - paddle_h // 2, paddle_w, paddle_h)

ball = pygame.Rect(WIDTH // 2-7, HEIGHT //2-7, 14, 14)
ball_speed_x, ball_speed_y = 4,4

paddle_speed = 5

left_score = 0
right_score = 0

font = pygame.font.Font(None, 36)

run = True
clock = pygame.time.Clock()

while run:
    clock.tick(60)
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
         left_paddle.y -= paddle_speed
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
         left_paddle.y += paddle_speed    
    if keys[pygame.K_UP] and right_paddle.top > 0:
         right_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
         right_paddle.y += paddle_speed
         
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if ball.top <=0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y
        
    if ball.colliderect(left_paddle) and ball_speed_x < 0:
        ball_speed_x = -ball_speed_x
    if ball.colliderect(right_paddle) and ball_speed_x > 0:
        ball_speed_x = -ball_speed_x
        
    if ball.left <= 0:
        right_score += 1
        ball.center = (WIDTH // 2, HEIGHT //2)
    if ball.left >= WIDTH:
        left_score += 1
        ball.center = (WIDTH // 2, HEIGHT //2)
    
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH// 2,0), (WIDTH // 2, HEIGHT))
    
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (WIDTH // 4, 10))
    screen.blit(right_text, (WIDTH * 3 // 4, 10)) 
    
    pygame.display.flip()
    
pygame.quit()