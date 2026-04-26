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

def calculate_rhombus(x1, y1, x2, y2):
    width  = abs(x1 - x2)
    height = abs(y1 - y2)
    # find top left corner of bounding box
    left_x = min(x1, x2)
    top_y  = min(y1, y2)
    
    # top vertex: middle of top side
    top_point    = (left_x + width // 2, top_y)
    # right vertex: middle of right side
    right_point  = (left_x + width, top_y + height // 2)
    # bottom vertex: middle of bottom side
    bottom_point = (left_x + width // 2, top_y + height)
    # left vertex: middle of left side
    left_point   = (left_x, top_y + height // 2)

    return (top_point, right_point, bottom_point, left_point)

def calculate_square(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), max(abs(x2 - x1), abs(y2 - y1)), max(abs(x2 - x1), abs(y2 - y1)))

def calculate_right_triangle(x1, y1, x2, y2):
    return ((x1, y1), (x2, y2), (x1, y2))

def calculate_eq_triangle(x1, y1, x2, y2):
    # calculate base length and direction: left or right
    base = x2 - x1
    direction_x = 1 if base >= 0 else -1

    base = abs(base)
    height = int((3 ** 0.5) / 2 * base)
    # determine vertical direction: up or down
    direction_y = -1 if y2 < y1 else 1

    # define three vertices of the triangle
    p1 = (x1, y1)
    p2 = (x1 + direction_x * base, y1)
    p3 = (x1 + direction_x * base // 2, y1 + direction_y * height)

    return (p1, p2, p3)

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

                # draw the preview figure
                if tool == "rect":
                    pygame.draw.rect(screen, current_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)

                if tool == "rhombus":
                    pygame.draw.polygon(screen, current_color, calculate_rhombus(prevX, prevY, currX, currY), THICKNESS)

                if tool == "circle":
                    radius = int(((currX - prevX) ** 2 + (currY - prevY) ** 2) ** 0.5)
                    pygame.draw.circle(screen, current_color, (prevX, prevY), radius, THICKNESS)

                if tool == "square":
                    pygame.draw.rect(screen, current_color, calculate_square(prevX, prevY, currX, currY), THICKNESS)

                if tool == "right triangle":
                    pygame.draw.polygon(screen, current_color, calculate_right_triangle(prevX, prevY, currX, currY), THICKNESS)

                if tool == "eq triangle":
                    pygame.draw.polygon(screen, current_color, calculate_eq_triangle(prevX, prevY, currX, currY), THICKNESS)

                if tool == "eraser":
                    pygame.draw.circle(screen, colorWHITE, (currX, currY), 20)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released!")
            LMBpressed = False

            currX = event.pos[0]
            currY = event.pos[1]

            # draw the final figure
            if tool == "rect":
                pygame.draw.rect(base_layer, current_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)

            if tool == "rhombus":
                pygame.draw.polygon(base_layer, current_color, calculate_rhombus(prevX, prevY, currX, currY), THICKNESS)

            if tool == "circle":
                radius = int(((currX - prevX) ** 2 + (currY - prevY) ** 2) ** 0.5)
                pygame.draw.circle(base_layer, current_color, (prevX, prevY), radius, THICKNESS)

            if tool == "square":
                pygame.draw.rect(base_layer, current_color, calculate_square(prevX, prevY, currX, currY), THICKNESS)

            if tool == "right triangle":
                pygame.draw.polygon(base_layer, current_color, calculate_right_triangle(prevX, prevY, currX, currY), THICKNESS)

            if tool == "eq triangle":
                pygame.draw.polygon(base_layer, current_color, calculate_eq_triangle(prevX, prevY, currX, currY), THICKNESS)

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
            if event.key == pygame.K_r and (event.mod & pygame.KMOD_LSHIFT):
                tool = "rect"
                print("tool: rect")

            if event.key == pygame.K_r and (event.mod & pygame.KMOD_LCTRL):
                tool = "rhombus"
                print("tool: rhombus")

            if event.key == pygame.K_c:
                tool = "circle"
                print("tool: circle")

            if event.key == pygame.K_s:
                tool = "square"
                print("tool: square")
 
            if event.key == pygame.K_t and (event.mod & pygame.KMOD_LSHIFT):
                tool = "right triangle"
                print("tool: right triangle")

            if event.key == pygame.K_t and (event.mod & pygame.KMOD_LCTRL):
                tool = "eq triangle"
                print("tool: eq triangle")

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