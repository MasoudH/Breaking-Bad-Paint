from pygame import *
from math import *
from random import *
from Fonts import *

def pencil(tool, screen, canvas, mpos, mb, mx, my, ox, oy, color, thickness): #pencil tool
    if tool == "Pencil":
        screen.set_clip(canvas)
        draw.line(screen, color, (ox, oy), (mx, my), thickness)

def marker(tool, screen, canvas, mpos, mb, mx, my, ox, oy, color, thickness): # marker tool
    if tool == "Marker":
        screen.set_clip(canvas)
        if mx == ox and my == oy: #Checks if mouse was stable
            draw.circle(screen, color, (ox,oy), thickness) #draws a circle at the mouses position
        else:
            dx = mx-ox #distance between mx and ox
            dy = my-oy #distance between my andoy
            dist = hypot(dx, dy) # distance between old mouse pos and new mouse pos
            x = dx/dist
            y = dy/dist
            for i in range(int(dist)):
                draw.circle(screen, color, (int(ox+i*x), int(oy+i*y)), thickness) # drawing the circle at every pixel

def eraser(tool, screen, canvas, mpos, mb, mx, my, ox, oy, thickness): # Eraser tool
    if tool == "Eraser":
        screen.set_clip(canvas)
        if mx == ox and my == oy: #Checks if mouse was stable
            draw.circle(screen, (255, 255, 255), (ox,oy),thickness) #draws a circle at the mouses position
        else:
            dx = mx-ox #distance of mx and ox
            dy = my-oy #distance of my, oy
            dist = hypot(dx, dy) # distance between old mouse pos and new mouse pos
            x = dx/dist
            y = dy/dist
            for i in range(int(dist)):
                draw.circle(screen, (255, 255, 255), (int(ox+i*x), int(oy+i*y)), thickness) # drawing the circle at every pixel


def brush(tool, screen, canvas, mpos, mb, mx, my, ox, oy, color, thickness): # Brush tool
    if tool == "Brush":
        screen.set_clip(canvas)
        tip = Surface((thickness*2, thickness*2),SRCALPHA)
        if mx!=ox or my!=oy:
            draw.circle(tip, (color[0], color[1], color[2], 2), (thickness, thickness), thickness) # thickness, thickness is the center of tip
                                                                                                   # since thickness*2 is the diameter
            dx, dy = mx-ox, my-oy
            dist = hypot(dx, dy) #distance between old mouse pos and new mouse pos
            x = dx/dist
            y = dy/dist
            for i in range(int(dist)):
                cx, cy = int((ox+i*x)-thickness), int((oy+i*y)-thickness) # allows us to know the location at the center and since the radius 
                                                                          # is double the thickness by subtracting thickness we find the upper
                                                                          # left corner
                screen.blit(tip, (cx, cy))

def spray(tool, screen, canvas, mpos, mb, mx, my, color, thickness): #spray tool
    if tool == "Spray":
        screen.set_clip(canvas)
        for i in range(thickness*3): #increases speed
            x=randint(-thickness,thickness) # Finds a random x coordinates
            y=randint(-thickness,thickness) # Finds a random y coordinates
            if hypot(x,y) < thickness-1:
                screen.set_at((x+mx,y+my),(color))

def magic_eraser(tool, screen, canvas, color, mb, mpos, mx, my): # magic eraser tool
    if tool == "Magic Eraser" and canvas.collidepoint(mpos):
        spot = [mpos]
        screen.set_clip(canvas)
        selected_color = tuple(screen.get_at((mx, my)))
        if selected_color != (255, 255, 255, 255):
            while len(spot) > 0:
                cx, cy = spot.pop()
                if screen.get_at((cx, cy)) == selected_color and canvas.collidepoint((cx,cy)):
                    screen.set_at((cx, cy), (255, 255, 255, 255))
                    spot.append((cx+1, cy))
                    spot.append((cx-1, cy))
                    spot.append((cx, cy+1))
                    spot.append((cx, cy-1))

def flood(tool, screen, canvas, color, mb, mpos, mx, my): # Flood tool
    if tool == "Flood Fill" and canvas.collidepoint(mpos):
        spot = [mpos]
        screen.set_clip(canvas)
        selected_color = tuple(screen.get_at((mx, my)))
        if selected_color != color:
            while len(spot) > 0:
                cx, cy = spot.pop()
                if screen.get_at((cx, cy)) == selected_color and canvas.collidepoint((cx,cy)):
                    screen.set_at((cx, cy), color)
                    spot.append((cx+1, cy))
                    spot.append((cx-1, cy))
                    spot.append((cx, cy+1))
                    spot.append((cx, cy-1))

def line(tool, screen, snap, canvas, color, copy, start, mpos, mb, mx, my, thickness): # Line tool
    if tool == "Line" and canvas.collidepoint(mpos):
        screen.set_clip(canvas)
        screen.blit(copy, (25, 50))
        if snap:
            dx, dy = abs(start[0] - mx), abs(start[1] - my)
            if dx > dy:
                draw.line(screen, color, start, (mx, start[1]))
            elif dx < dy:
                draw.line(screen, color, start, (start[0], my)) 
        else:
            draw.line(screen, color, start, (mx, my), thickness)

def rectangle(tool, screen, canvas, color, fill, start, copy, mpos, mb, mx, my, thickness): # Rectangle tool
    if tool == "Rectangle" and canvas.collidepoint(mpos):
        screen.set_clip(canvas)
        screen.blit(copy, canvas)
        if fill:
            draw.rect(screen, color, (start[0], start[1], mx-start[0], my-start[1]))
        if not fill:
            halfThick = thickness//2 # only half the thickness is needed to make it the right size without any empty spots
            if (mx - start[0]) >= 0:
                if thickness%2 == 0:
                    draw.line(screen ,color, (start[0] - (halfThick-1), start[1]),(mx + halfThick, start[1]), thickness)
                    draw.line(screen ,color, start, (start[0], my), thickness)
                    draw.line(screen ,color, mpos, (mx, start[1]), thickness)
                    draw.line(screen ,color, (start[0] - (halfThick-1), my),(mx +halfThick, my), thickness)
                        
                elif thickness%2 == 1:
                    draw.line(screen ,color, (start[0]-halfThick,start[1]),(mx+halfThick,start[1]), thickness)
                    draw.line(screen ,color, start,(start[0], my), thickness)
                    draw.line(screen ,color, mpos ,(mx,start[1]), thickness)
                    draw.line(screen ,color, (start[0]-halfThick,my),(mx+halfThick, my), thickness)

            elif (mx - start[0]) < 0: # If inverted
                if thickness%2 == 0:
                    draw.line(screen ,color, (mx-(halfThick-1), my),(start[0]+halfThick, my), thickness)
                    draw.line(screen ,color, mpos,(mx,start[1]), thickness)
                    draw.line(screen ,color, start,(start[0], my), thickness)
                    draw.line(screen ,color, (mx-(halfThick-1),start[1]),(start[0]+halfThick,start[1]), thickness)
                        
                elif thickness%2 == 1:
                    draw.line(screen ,color, (mx-halfThick, my),(start[0]+halfThick, my),thickness)
                    draw.line(screen ,color, mpos,(mx,start[1]), thickness)
                    draw.line(screen ,color, start,(start[0], my), thickness)
                    draw.line(screen ,color, (mx-halfThick,start[1]),(start[0]+halfThick,start[1]), thickness)


def ellipse(tool, screen, canvas, color, fill, copy, start, mpos, mb, mx, my, thickness): # Ellipse tool
    if tool == "Ellipse" and canvas.collidepoint(mpos):
        screen.set_clip(canvas)
        screen.blit(copy, (25, 50))
        if fill:
            elRect = Rect(start[0], start[1], mx-start[0], my-start[1])
            elRect.normalize()
            draw.ellipse(screen, color, elRect)

        elif not fill:
            if min(abs(start[0]-mx), abs(start[1]-my)) < thickness*2:
                elRect = Rect(start[0], start[1], mx-start[0], my-start[1])
                elRect.normalize()
                draw.ellipse(screen, color, elRect)
            else:
                draw.arc(screen, color, (min(start[0], mx), min(start[1], my), abs(start[0]-mx), abs(start[1]-my)), 0, 360, thickness) # draws a 360 arc to that looks like an ellipse

def clear(screen, canvas, clear_screen): # Clear tool
    if clear_screen:
        clicked = True
        draw.rect(screen, (255, 255, 255), canvas)

def sticker(screen, tool, tool_name, canvas, copy, stamp, mpos, mb, sx, sy, mx, my, ex, ey, thickness): # Stamp tool
    if tool == str(tool_name) and canvas.collidepoint(mpos):
        clicked = True
        screen.set_clip(canvas)
        screen.blit(copy, (25, 50))
        stamp = transform.scale(stamp, (sx+(thickness*ex), sy+(thickness*ey)))
        screen.blit(stamp, (mx-((sx+(thickness*ex))//2), my-((sy+(thickness*ey))//2)))