import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))

# an additional layer to save the drawing
base_layer.fill((255, 255, 255))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorGREEN = (0, 255, 0)
colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)

colors = [colorRED, colorBLUE, colorGREEN, colorBLACK]
color_index = 0
current_color = colors[color_index]

clock = pygame.time.Clock()

LMBpressed = False
THICKNESS = 5

# current mouse coordinates
currX = 0
currY = 0

# initial mouse coordinates
prevX = 0
prevY = 0

tool = "rect"   # tools for drawing: rect, circle, eraser


def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))


running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed!")
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]

        if event.type == pygame.MOUSEMOTION:

            screen.blit(base_layer, (0, 0))
            print("Position of the mouse:", event.pos)

            if LMBpressed:

                currX = event.pos[0]
                currY = event.pos[1]

                if tool == "rect":
                    # draw a rectangle
                    pygame.draw.rect(screen, current_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)

                if tool == "circle":
                    radius = int(((currX - prevX) ** 2 + (currY - prevY) ** 2) ** 0.5)
                    pygame.draw.circle(screen, current_color, (prevX, prevY), radius, THICKNESS)

                if tool == "eraser":
                    pygame.draw.circle(screen, colorWHITE, (currX, currY), 20)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released!")
            LMBpressed = False

            currX = event.pos[0]
            currY = event.pos[1]

            if tool == "rect":
                # draw the final rectangle
                pygame.draw.rect(base_layer, current_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)

            if tool == "circle":
                radius = int(((currX - prevX) ** 2 + (currY - prevY) ** 2) ** 0.5)
                pygame.draw.circle(base_layer, current_color, (prevX, prevY), radius, THICKNESS)

            if tool == "eraser":
                pygame.draw.circle(base_layer, colorWHITE, (currX, currY), 20)

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_EQUALS:
                print("increased thickness")
                THICKNESS += 1

            if event.key == pygame.K_MINUS:
                print("reduced thickness")
                THICKNESS -= 1

            # tools for drawing
            if event.key == pygame.K_r:
                tool = "rect"
                print("tool: rect")

            if event.key == pygame.K_c:
                tool = "circle"
                print("tool: circle")

            if event.key == pygame.K_e:
                tool = "eraser"
                print("tool: eraser")

            # color switch
            if event.key == pygame.K_SPACE:
                color_index = (color_index + 1) % len(colors)
                current_color = colors[color_index]
                print("color changed")

    pygame.display.flip()
    clock.tick(60)