import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((1152, 864))


clock_img = pygame.image.load("mickey.jpg")
left_hand = pygame.image.load("left_hand.png")  
right_hand = pygame.image.load("right_hand.png") 

center = (576, 432)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute

    sec_angle = -seconds * 6     
    min_angle = -minutes * 6

    rotated_sec = pygame.transform.rotate(left_hand, sec_angle)
    rotated_min = pygame.transform.rotate(right_hand, min_angle)
    sec_rect = rotated_sec.get_rect(center=center)
    min_rect = rotated_min.get_rect(center=center)

    screen.blit(clock_img, (0, 0))
    screen.blit(rotated_min, min_rect)
    screen.blit(rotated_sec, sec_rect)

    pygame.display.flip()
    clock.tick(1) 

pygame.quit()