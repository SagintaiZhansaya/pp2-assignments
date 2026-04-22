import pygame

pygame.init()

screen = pygame.display.set_mode((400, 200))

playlist = ["track1.mp3", "track2.mp3", "track3.mp3"]

current = 0
pygame.mixer.music.load(playlist[current])

pygame.mixer.music.play(0)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
            if event.key == pygame.K_r:
                pygame.mixer.music.play(0)
            if event.key == pygame.K_n:
                current = (current + 1) % len(playlist)
                pygame.mixer.music.load(playlist[current])
                pygame.mixer.music.play(0)
            if event.key == pygame.K_b:
                current = (current - 1) % len(playlist)
                pygame.mixer.music.load(playlist[current])
                pygame.mixer.music.play(0)
            if event.key == pygame.K_q:
                running = False

    screen.fill("black")

    font = pygame.font.SysFont("Verdana", 20)

    text1 = f"Now playing: {playlist[current]}"
    text2 = "P=Pause  S=Stop  R=Restart"
    text3 = "N=Next  B=Back  Q=Quit"

    screen.blit(font.render(text1, True, "white"), (10, 50))
    screen.blit(font.render(text2, True, "white"), (10, 90))
    screen.blit(font.render(text3, True, "white"), (10, 120))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()