from time import *
from pygame import *
from math import *
from random import *
from Drawing_Tools import *
from Fonts import *

def FPS(screen, clock): # finds the frames per second of the program and displays it
    screen.set_clip(None)
    draw.rect(screen, (50, 50, 50), (1250, 750, 166, 21))
    frames = clock.get_fps()
    fps = smoolthan(screen, 18, "FPS: %.2f" % frames, (255, 255, 255), (1250, 747))
    clock.tick()

def selected_tool(screen, tool): # Tells the user what tool they have selected and wether its a shape, drawing tool or stammp.
    draw.rect(screen, (50, 50, 50), (845, 237, 200, 23))
    if tool == "Crystal Meth Logo" or tool == "Lego Figurine" or tool == "Gus Fring" or tool == "Saul Goodman" or tool == "Jesse Pinkman" or tool == "Mike E." or tool == "Walter White" or tool == "Heisenberg" or tool == "Crystal Ship":
        regular(screen, 15, "Stamp:  %s" % tool, (255, 255, 255), (858, 237))
    elif tool == "Line" or tool == "Rectangle" or tool == "Ellipse":
        regular(screen, 15, "Shape:  %s" % tool, (255, 255, 255), (858, 237))
    else:
        regular(screen, 15, "Tool:  %s" % tool,  (255, 255, 255), (858, 237))

def x_y(screen, mx, my): # Tells the user what there x and y coordinate on the canvas
    x = mx-25
    y = my-50
    if x > 800 or y > 600 or y < 0 or x < 0:
        draw.rect(screen, (50, 50, 50), (845, 259, 200, 20))
        regular(screen, 15, "Mouse is off Canvas", (255, 255, 255), (858, 259))
    else:
        draw.rect(screen, (50, 50, 50), (845, 259, 200, 20))
        regular(screen, 15, "X: "+str(x), (255, 255, 255), (858, 259))
        regular(screen, 15, "Y: "+str(y), (255, 255, 255), (944, 259))

def thickness(screen, tool, thickness, start, x, y, ex, ey, mx, my, fill): # Tells user the size of there image or or width of drawing tool
    draw.rect(screen, (50, 50, 50), (845, 215, 200, 22))
    if tool == "Crystal Meth Logo" or tool == "Lego Figurine" or tool == "Gus Fring" or tool == "Saul Goodman" or tool == "Jesse Pinkman" or tool == "Mike E." or tool == "Walter White" or tool == "Heisenberg" or tool == "Crystal Ship":
        regular(screen, 15, "Size:  %d X %d" % (x+(thickness*ex), y+(thickness*ey)),  (255, 255, 255), (858, 215))
    elif tool == "Line" or tool == "Rectangle" or tool == "Ellipse":
        regular(screen, 15, "Width:  %d" % (thickness), (255, 255, 255), (858, 215))
    elif tool == "text":
        regular(screen, 15, "Font-size:  %d" % (thickness), (255, 255, 255), (858, 215))
    else:
        if thickness == 1:
            regular(screen, 15, "Radius:  %d pixel" % thickness, (255, 255, 255), (858, 215))
        else:
            regular(screen, 15, "Radius:  %d pixels" % thickness, (255, 255, 255), (858, 215))


def date_time(screen): # Gives the user the date and time
    month = {1:"Jan.", 2:"Feb.", 3:"Mar.", 4:"Apr.", 5:"May", 6:"Jun.", 7:"Jul.", 8:"Aug.", 9:"Sep.", 10:"Oct.",
             11:"Nov.", 12:"Dec."}

    if strftime("%H:%M:%S") < "12:00:00":
        end = "AM"
    else:
        end = "PM"

    draw.rect(screen, (230, 230, 230), (1120, 0, 246, 25))
    smoolthan(screen, 20, strftime(" %I : %M ")+end+"   "+month[int(strftime("%m"))]+strftime(" %d, %Y"), (0, 0, 0), (1120, 2))

    if strftime("%I") < "10":
        draw.rect(screen, (230, 230, 230), (1125, 0, 14, 25))

    if strftime("%d") < "10":
        draw.rect(screen, (230, 230, 230), (1277, 0, 14, 25))
        # %a for day of the week

def fill_outline(screen, tool, fill, mpos, mb, filled, outline): # Fill and outline bar drawn from here allowing user to know which one they are using
    screen.set_clip(None)
    draw.rect(screen, (200, 200, 200),(855, 605, 180, 30))
    if fill:
        draw.rect(screen, (0, 255, 0), filled)
        smoolthan(screen, 15, "Fill", (0, 0, 0), (890, 610))
        smoolthan(screen, 15, "Outline", (0, 0, 0), (965, 610))
    elif not fill:
        draw.rect(screen, (0, 255, 0), outline)
        smoolthan(screen, 15, "Fill", (0, 0, 0), (890, 610))
        smoolthan(screen, 15, "Outline", (0, 0, 0), (965, 610))

def snap_OnOff(screen, tool, snap, mpos, mb, snapOn, snapOff): # snap on and snap off bar drawn from here allowing user to know which one they are using
    if tool == "Line":
        screen.set_clip(None)
        draw.rect(screen, (200, 200, 200), (855, 605, 180, 30))
        if snap:
            draw.rect(screen, (0, 255, 0), snapOn)
            smoolthan(screen, 15, "Snap Off", (0, 0, 0), (870, 610))
            smoolthan(screen, 15, "Snap On", (0, 0, 0), (960, 610))
        else:
            draw.rect(screen, (0, 255, 0), snapOff)
            smoolthan(screen, 15, "Snap Off", (0, 0, 0), (870, 610))
            smoolthan(screen, 15, "Snap On", (0, 0, 0), (960, 610))

def mouse_visibility(canvas, color_rect, mpos, mb): # Checks if mouse should be visible or not
    if canvas.collidepoint(mpos) and mb[0] == 1 or color_rect.collidepoint(mpos):
        mouse.set_visible(False)
    else:
        mouse.set_visible(True)