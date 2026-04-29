import pygame
from datetime import datetime

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))
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


currX = 0
currY = 0
prevX = 0
prevY = 0

tool = "rect"   


def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))


def calculate_rhombus(x1, y1, x2, y2):
    width  = abs(x1 - x2)
    height = abs(y1 - y2)
    left_x = min(x1, x2)
    top_y  = min(y1, y2)
    
    top_point    = (left_x + width // 2, top_y)
    right_point  = (left_x + width, top_y + height // 2)
    bottom_point = (left_x + width // 2, top_y + height)
    left_point   = (left_x, top_y + height // 2)

    return (top_point, right_point, bottom_point, left_point)


def calculate_square(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), max(abs(x2 - x1), abs(y2 - y1)), max(abs(x2 - x1), abs(y2 - y1)))


def calculate_right_triangle(x1, y1, x2, y2):
    return ((x1, y1), (x2, y2), (x1, y2))


def calculate_eq_triangle(x1, y1, x2, y2):
    base = x2 - x1
    direction_x = 1 if base >= 0 else -1

    base = abs(base)
    height = int((3 ** 0.5) / 2 * base)
    direction_y = -1 if y2 < y1 else 1

    p1 = (x1, y1)
    p2 = (x1 + direction_x * base, y1)
    p3 = (x1 + direction_x * base // 2, y1 + direction_y * height)

    return (p1, p2, p3)


def flood_fill(surface, x, y, fill_color):
    surface_color = surface.get_at((x, y))
    if surface_color == fill_color:
        return

    pixels = [(x, y)] 

    while pixels:
        px, py = pixels.pop()

        if px < 0 or px >= WIDTH or py < 0 or py >= HEIGHT:
            continue

        if surface.get_at((px, py)) != surface_color:
            continue

        surface.set_at((px, py), fill_color)

        pixels.append((px + 1, py))
        pixels.append((px - 1, py))
        pixels.append((px, py + 1))
        pixels.append((px, py - 1))


font = pygame.font.SysFont(None, 24)
text_active = False
text_input = ""
text_pos = (0, 0)

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
        
            if tool == "fill":
                flood_fill(base_layer, prevX, prevY, current_color)

            if tool == "text":
                text_active = True
                text_input = ""
                text_pos = event.pos


        if event.type == pygame.MOUSEMOTION:
            print("Position of the mouse:", event.pos)
            screen.blit(base_layer, (0, 0))

            if LMBpressed:

                currX = event.pos[0]
                currY = event.pos[1]

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
                    pygame.draw.circle(base_layer, colorWHITE, (currX, currY), 20)
                    prevX, prevY = currX, currY

                if tool == "pencil":
                    pygame.draw.line(base_layer, current_color, (prevX, prevY), (currX, currY), THICKNESS)
                    prevX, prevY = currX, currY

                if tool == "line":
                    pygame.draw.line(screen, current_color, (prevX, prevY), (currX, currY), THICKNESS)


        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released!")
            LMBpressed = False

            currX = event.pos[0]
            currY = event.pos[1]

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

            if tool == "line":
                pygame.draw.line(base_layer, current_color, (prevX, prevY), (currX, currY), THICKNESS)


        if event.type == pygame.KEYDOWN:
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

            if event.key == pygame.K_p:
                tool = "pencil"

            if event.key == pygame.K_l:
                tool = "line"
            
            if event.key == pygame.K_f:
                tool = "fill"
            
            if event.key == pygame.K_x:
                tool = "text"

            if event.key == pygame.K_s and (event.mod & pygame.KMOD_CTRL):
                filename = datetime.now().strftime("drawing_%Y%m%d_%H%M%S.png")
                pygame.image.save(base_layer, filename)
                print("Saved:", filename)
            
            if event.key == pygame.K_e:
                tool = "eraser"
                print("tool: eraser")

            if event.key == pygame.K_SPACE:
                color_index = (color_index + 1) % len(colors)
                current_color = colors[color_index]
                print("color changed")

            if tool == "text" and text_active:
                if event.key == pygame.K_RETURN:
                    text_surface = font.render(text_input, True, current_color)
                    base_layer.blit(text_surface, text_pos)
                    text_active = False
                    text_input = ""
                elif event.key == pygame.K_ESCAPE:
                    text_active = False
                    text_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]
                else:
                    text_input += event.unicode
                
            if event.key == pygame.K_1:
                THICKNESS = 2
            if event.key == pygame.K_2:
                THICKNESS = 5
            if event.key == pygame.K_3:
                THICKNESS = 10

        if text_active:
            txt_surface = font.render(text_input, True, current_color)
            screen.blit(txt_surface, text_pos)

        pygame.display.flip()
        clock.tick(60)

pygame.quit()