# Masoud Harati 2015
# Room 149 Period 3
# Breaking Bad paint

from pygame import *
from math import *
from random import randint
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from Drawing_Tools import *
from Fonts import *
from Sub_Tools import *

init() # Initializing Font and mixer.music

root = Tk()
root.withdraw()

screen = display.set_mode((1366, 768))
background = image.load("Pictures/Background.jpg")
screen.blit(background, (0, 0))

clock = time.Clock() # Keeps Track of time

display.set_caption("Breaking Bad")

#----------The Icon for Paint---------
icon = image.load("Pictures/Icon.png")
display.set_icon(icon) # sets program icon
#-------------------------------------

#------------------------Screen Layout-----------------------------
canvas = draw.rect(screen, (255, 255, 255), (25, 50, 800, 600))
bottom_toolbar = draw.rect(screen, (50, 50, 50), (0, 748, 1366, 20)) # Bottom Toolbar
draw.rect(screen, (50, 50, 50), (845, 50, 200, 600)) # Rectangle around all the information
draw.rect(screen, (50, 50, 50), (1066, 50, 280, 600)) # Rectangle around the stickers
smoolthan(screen, 25, "Stamps", (255, 255, 255), (1160, 55))
smoolthan(screen, 20, "© Masoud Harati 2015", (255, 255, 255), (5, 748))
filled = Rect(855, 605, 90, 30) # Filled option rectangle
outline = Rect(945, 605, 90, 30) # Outlined option rectangle
snapOn = Rect(945, 605, 90, 30) # Snap On option rectangle
snapOff = Rect(855, 605, 90, 30) # Snap off option rectangle
#------------------------------------------------------------------

#--------------------------Top Toolbar-----------------------------
top_toolbar = draw.rect(screen, (230, 230, 230), (0, 0, 1366, 25)) # Top ToolBar
icon = transform.scale(icon, (20, 20))
screen.blit(icon, (2, 2))

save_rect = Rect(25, 0, 54, 25) # Save button
draw.line(screen, (125, 125, 125), (25, 2), (25, 23))
regular(screen, 20, "Save", (75, 75, 75), (28, -3))
draw.line(screen, (125, 125, 125), (79, 2), (79, 23))

open_rect = Rect(79, 0, 54, 25) # Load button
regular(screen, 20, "Load", (75, 75, 75), (84, -3))
draw.line(screen, (125, 125, 125), (134, 2), (134, 23))

undo_rect = Rect(134, 0, 54, 25) # Undo Button
regular(screen, 20, "Undo", (75, 75, 75), (138, -3))
draw.line(screen, (125, 125, 125), (188, 2), (188, 23))

redo_rect = Rect(188, 0, 54, 25) # Redo button
regular(screen, 20, "Redo", (75, 75, 75), (193, -3))
draw.line(screen, (125, 125, 125), (242, 2), (242, 23))
#------------------------------------------------------------------

#-----Different Different Start Variables------
radius = 1 # Starting line thickness
tool = "Pencil" # Starting tool
mx, my = 0, 0 # Starting mouse position
snap = False # Snap is off
fill = True # Fill is on
start = 0, 0 # first point user clicks will be kept track of
copy = screen.subsurface(canvas).copy() # copy o canvas used fro rebliting
radius_min = 1 # Minimal radius 
radius_max = 5 # Maximum radius
x, y = 0, 0 #x & y pos
ex, ey = 0, 0 # used to increase and decease the size of images
clear_screen = False # Deactivated clear screen
song = "None" # No song
current_volume = 0.5 #the volume of the program
undo = [screen.subsurface(canvas).copy()] # list for undo
redo = [] # list for redo
clicked = False # variable to see if something is drawn
blitText = "" # variable that stores the text theat will be blitted later on
#----------------------------------------------

#------------------Rectangle and Picture for each tool-------------------------
pencil_rect = draw.rect(screen, (200, 200, 200), (855, 300, 50, 50)) # Pencil
pencil_image = image.load("Pictures/Icons/Pencil.png")
pencilSelected_image = image.load("Pictures/Icons/Pencil Selected.png")

marker_rect = draw.rect(screen, (200, 200, 200), (920, 300, 50, 50)) # Marker
marker_image = image.load("Pictures/Icons/Marker.png")
markerSelected_image = image.load("Pictures/Icons/Marker Selected.png")

eraser_rect = draw.rect(screen, (200, 200, 200), (985, 300, 50, 50)) # Eraser
eraser_image = image.load("Pictures/Icons/Eraser.png")
eraserSelected_image = image.load("Pictures/Icons/Eraser Selected.png")

brush_rect = draw.rect(screen, (200, 200, 200), (855, 365, 50, 50)) # Brush
brush_image = image.load("Pictures/Icons/Brush.png")
brushSelected_image = image.load("Pictures/Icons/Brush Selected.png")

spray_rect = draw.rect(screen, (200, 200, 200), (920, 365, 50, 50)) # Spray
spray_image = image.load("Pictures/Icons/Spray.png")
spraySelected_image = image.load("Pictures/Icons/Spray Selected.png")

magicEraser_rect = draw.rect(screen, (200, 200, 200), (985, 365, 50, 50)) # Magic Eraser
magicEraser_image = image.load("Pictures/Icons/Magic Eraser.png")
magicEraserSelected_image = image.load("Pictures/Icons/Magic Eraser Selected.png")

line_rect = draw.rect(screen, (200, 200, 200), (855, 430, 50, 50)) # Line
line_image = image.load("Pictures/Icons/Line.png")
lineSelected_image = image.load("Pictures/Icons/Line Selected.png")

flood_rect = draw.rect(screen, (200, 200, 200), (920, 430, 50, 50)) # Flood Fill
flood_image = image.load("Pictures/Icons/Bucket.png")
floodSelected_image = image.load("Pictures/Icons/Bucket Selected.png")

text_rect = draw.rect(screen, (200, 200, 200), (985, 430, 50, 50)) # Text
text_image = image.load("Pictures/Icons/Text.png")
textSelected_image = image.load("Pictures/Icons/Text Selected.png")

rectangle_rect = draw.rect(screen, (200, 200, 200), (890, 495, 50, 50)) # Rectangle
outlinedRectangle_image = image.load("Pictures/Icons/Rectangle_Outline.png")
outlinedRectangleSelected_image = image.load("Pictures/Icons/Rectangle_Outline Selected.png")
filledRectangle_image = image.load("Pictures/Icons/Rectangle_Filled.png")
filledRectangleSelected_image = image.load("Pictures/Icons/Rectangle_Filled Selected.png")

ellipse_rect = draw.rect(screen, (200, 200, 200), (955, 495, 50, 50)) # Circle/Ellipse
outlinedEllipse_image = image.load("Pictures/Icons/Ellipse_Outline.png")
outlinedEllipseSelected_image = image.load("Pictures/Icons/Ellipse_Outline Selected.png")
filledEllipse_image = image.load("Pictures/Icons/Ellipse_Filled.png")
filledEllipseSelected_image = image.load("Pictures/Icons/Ellipse_Filled Selected.png")

clear_rect = draw.rect(screen, (200, 200, 200), (855, 560, 180, 30))
smoolthan(screen, 25, "Clear Canvas", (0, 0, 0), (870, 560))
#---------------------------------------------------------------------------------

#----------------------Music Icons/Rects----------------------------
draw.rect(screen, (50, 50, 50), (25, 665, 215, 70))

lowVolume_rect = Rect(30, 670, 40, 40)
lowVolume = image.load("Pictures/Music/Low Volume.png")
screen.blit(lowVolume, (35, 675))

stop_rect = Rect(110, 670, 40, 40)
stop = image.load("Pictures/Music/Stop.png")
screen.blit(stop, (115, 675))

highVolume_rect = Rect(195, 670, 40, 40)
highVolume = image.load("Pictures/Music/High Volume.png")
screen.blit(highVolume, (200, 675))
#--------------------------------------------------------------------

#---------------------------Song Rects------------------------------
draw.rect(screen, (50, 50, 50), (255, 665, 570, 70))
music = image.load("Pictures/Music/Music.png")
musicSelected = image.load("Pictures/Music/Music Selected.png")

happy_rect = Rect(255, 665, 95, 70)

darkHorse_rect = Rect(350, 665, 95, 70)

neonLights_rect = Rect(445, 665, 95, 70)

blankSpace_rect = Rect(540, 665, 95, 70)

burn_rect = Rect(635, 665, 95, 70)

demons_rect = Rect(730, 665, 95, 70)
#--------------------------------------------------------------------

#------------------------------Stamps--------------------------------
meth_rect = Rect(1095, 95, 220, 130)
meth = image.load("Pictures/Stamps/heisenberg_meth.png")
meth_icon = transform.scale(meth, (220, 100))

lego_rect = Rect(1095, 235, 100, 90)
lego = image.load("Pictures/Stamps/Lego.png")
lego_icon = transform.scale(lego, (75, 75))

gus_rect = Rect(1215, 235, 100, 90)
gus = image.load("Pictures/Stamps/Gus.png")
gus_icon = transform.scale(gus, (94, 90))

saul_rect = Rect(1095, 335, 100, 90)
saul = image.load("Pictures/Stamps/Saul.png")
saul_icon = transform.scale(saul, (64, 90))

jesse_rect = Rect(1215, 335, 100, 90)
jesse = image.load("Pictures/Stamps/Jesse.png")
jesse_icon = transform.scale(jesse, (53, 90))

mike_rect = Rect(1095, 435, 100, 90)
mike = image.load("Pictures/Stamps/Mike.png")
mike_icon = transform.scale(mike, (62, 90))

walter_rect = Rect(1215, 435, 100, 90)
walter = image.load("Pictures/Stamps/Walter.png")
walter_icon = transform.scale(walter, (56, 90))


heisenberg_rect = Rect(1095, 535, 100, 90)
heisenberg = image.load("Pictures/Stamps/Heisenberg.png")
heisenberg_icon = transform.scale(heisenberg, (94, 90))

crystalShip_rect = Rect(1215, 535, 100, 90)
crystalShip = image.load("Pictures/Stamps/Crystal Ship.png")
crystalShip_icon = transform.scale(crystalShip, (90,90))
#--------------------------------------------------------------------

#------------Color of writing/drawing images/variables---------------
color_image = image.load("Pictures/color.jpg")
color_image = transform.scale(color_image, (172, 90)) # Pallete image
color_rect = Rect(858, 63, 172, 90) # Pallete Rect
color = (0, 0, 0, 255)# default color
draw.rect(screen, color, (858, 163, 172, 20))
regular(screen, 15, "R:  "+str(color[0]), (255, 255, 255), (858, 193)) # Gives user infor about the color they are using
regular(screen, 15, "G:  "+str(color[1]), (255, 255, 255), (918, 193)) # Gives user infor about the color they are using
regular(screen, 15, "B:  "+str(color[2]), (255, 255, 255), (978, 193)) # Gives user infor about the color they are using
#---------------------------------------------------------------------
running = True
while running:
    click = False # used to find out if mouse was clicked for undo/redo
    myClock = clock.tick() # Keeps track of time
    ox, oy = mx, my # Old mx and old my
    mx, my = mouse.get_pos() # mouse position
    mb = mouse.get_pressed() # Mouse clicked or not
    mpos = mouse.get_pos() # mouse postion with one variable not 2
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == KEYDOWN:
            if tool == "Text":
                if e.key == K_BACKSPACE: # checks for backspace
                    blitText = blitText[0:-2] # erases a part if backspace is held.
                if e.key < 256:
                    blitText += e.unicode # uncodes the keyboard
                screen.set_clip(canvas)
                smoolthan(screen, radius, blitText, color, start) # Blits the color on to canvas
        if e.type == MOUSEBUTTONUP:
            if tool == "Text":
                screen.set_clip(canvas)
                smoolthan(screen, radius, blitText, color, start)
            blitText = ""
            canvasCopy = screen.subsurface(canvas).copy()
            if clicked:
                clicked = False
                redo = []
                undo.append(canvasCopy)
        if e.type == MOUSEBUTTONDOWN:
            click = True
            if e.button == 4: # Checks if scrolling up to increase size
                if radius < radius_max:
                    radius += 1
            if e.button == 5: # Checks if scrolling down to decrease size
                if radius > radius_min:
                    radius -= 1
            if e.button == 1:
                copy = screen.subsurface(canvas).copy()
                start = e.pos
#---------------------Tool Check------------------------
            if pencil_rect.collidepoint(mpos):
                tool = "Pencil"
                radius_min = 1
                radius_max = 5
                radius = 1
            elif marker_rect.collidepoint(mpos):
                tool = "Marker"
                radius_min = 5
                radius_max = 40
                radius = 5
            elif eraser_rect.collidepoint(mpos):
                tool = "Eraser"
                radius_min = 5
                radius_max = 60
                radius = 5
            elif brush_rect.collidepoint(mpos):
                tool = "Brush"
                radius_min = 15
                radius_max = 50
                radius = 15
            elif spray_rect.collidepoint(mpos):
                tool = "Spray"
                radius_min = 15
                radius_max = 40
                radius = 15
            elif magicEraser_rect.collidepoint(mpos):
                tool = "Magic Eraser"
            elif flood_rect.collidepoint(mpos):
                tool = "Flood Fill"
            elif text_rect.collidepoint(mpos):
                tool = "Text"
                radius_min = 10
                radius_max = 50
                radius = 10
                blitText = ""
            elif line_rect.collidepoint(mpos):
                tool = "Line"
                radius_min = 1
                radius_max = 20
                radius = 1
            elif rectangle_rect.collidepoint(mpos):
                tool = "Rectangle"
                radius_min = 1
                radius_max = 20
                radius = 1
            elif ellipse_rect.collidepoint(mpos):
                tool = "Ellipse"
                radius_min = 1
                radius_max = 20
                radius = 1
            elif meth_rect.collidepoint(mpos):
                tool = "Crystal Meth Logo"
                x, y = 220, 100
                radius_min = 0
                radius_max = 35
                radius = 0
                ex, ey = 11, 5
            elif lego_rect.collidepoint(mpos):
                tool = "Lego Figurine"
                x, y = 80, 80
                radius_min = 0
                radius_max = 15
                radius = 0
                ex, ey = 5, 5
            elif gus_rect.collidepoint(mpos):
                tool = "Gus Fring"
                x, y = 94, 90
                radius_min = 0
                radis_max = 25
                radius = 0
                ex, ey = 5, 5
            elif saul_rect.collidepoint(mpos):
                tool = "Saul Goodman"
                x, y = 64, 90
                radius_min = 0
                radius_max = 25
                radius = 0
                ex, ey = 4, 5
            elif jesse_rect.collidepoint(mpos):
                tool = "Jesse Pinkman"
                x, y = 53, 90
                radius_min = 0
                radius_max = 25
                radius = 0
                ex, ey = 3, 5
            elif mike_rect.collidepoint(mpos):
                tool = "Mike E."
                x, y = 62, 90
                radius_min = 0
                radius_max = 25
                radius = 0
                ex, ey = 4, 5
            elif walter_rect.collidepoint(mpos):
                tool = "Walter White"
                x, y = 56, 90
                radius_min = 0
                radius_max = 25
                radius = 0
                ex, ey = 3, 5
            elif heisenberg_rect.collidepoint(mpos):
                tool = "Heisenberg"
                x, y = 94, 90
                radius_min = 0
                radius_max = 25
                radius = 0
                ex, ey = 5, 5
            elif crystalShip_rect.collidepoint(mpos):
                tool = "Crystal Ship"
                x, y = 90, 90
                radius_min = 0
                radius_max = 25
                radius = 0
                ex, ey = 5, 5

            if clear_rect.collidepoint(mpos):
                clear_screen = True
            else:
                clear_screen = False
#-------------------------------------------------------

#------------------------Music Check--------------------
# If music is turned on it will play on an infinite loop
            if happy_rect.collidepoint(mpos):
                song = "Happy"
                mixer.music.load("Music/Happy.mp3")
                mixer.music.play(-1, 0.0)
                mixer.music.set_volume(current_volume)
                draw.rect(screen, (50, 50, 50), (30, 710, 200, 25))
                smoolthan(screen, 15, "Happy by Pharrell Williams", (255, 255, 255), (30, 710))
                play = True
            elif darkHorse_rect.collidepoint(mpos):
                song = "Dark Horse"
                mixer.music.load("Music/Dark Horse.mp3")
                mixer.music.play(-1, 0.0)
                mixer.music.set_volume(current_volume)
                draw.rect(screen, (50, 50, 50), (30, 710, 200, 25))
                smoolthan(screen, 15, "Dark Horse by Katy Perry", (255, 255, 255), (30, 710))
                play = True
            elif neonLights_rect.collidepoint(mpos):
                song = "Neon Lights"
                mixer.music.load("Music/Neon Lights.mp3")
                mixer.music.play(-1, 0.0)
                mixer.music.set_volume(current_volume)
                draw.rect(screen, (50, 50, 50), (30, 710, 200, 25))
                smoolthan(screen, 15, "Neon Lights by Demi Lovato", (255, 255, 255), (30, 710))
                play = True
            elif blankSpace_rect.collidepoint(mpos):
                song = "Blank Space"
                mixer.music.load("Music/Blank Space.mp3")
                mixer.music.play(-1, 0.0)
                mixer.music.set_volume(current_volume)
                draw.rect(screen, (50, 50, 50), (30, 710, 200, 25))
                smoolthan(screen, 15, "Blank Space by Taylor Swift", (255, 255, 255), (30, 710))
                play = True
            elif burn_rect.collidepoint(mpos):
                song = "Burn"
                mixer.music.load("Music/Burn.mp3")
                mixer.music.play(-1, 0.0)
                mixer.music.set_volume(current_volume)
                draw.rect(screen, (50, 50, 50), (30, 710, 200, 25))
                smoolthan(screen, 15, "Burn by Ellie Goulding", (255, 255, 255), (30, 710))
                play = True
            elif demons_rect.collidepoint(mpos):
                song = "Demons"
                mixer.music.load("Music/Demons.mp3")
                mixer.music.play(-1, 0.0)
                mixer.music.set_volume(current_volume)
                draw.rect(screen, (50, 50, 50), (30, 710, 200, 25))
                smoolthan(screen, 15, "Demons by Imagine Dragons", (255, 255, 255), (30, 710))
                play = True
#-------------------------------------------------------

#----------------------------Music Functions---------------------------
            if song == "Happy" or song == "Dark Horse" or song == "Neon Lights" or song == "Blank Space" or song == "Burn" or song == "Demons":
                if lowVolume_rect.collidepoint(mpos): # checks if user wants to lower volume
                    if current_volume > 0:
                        current_volume = mixer.music.get_volume()-0.1 # makes the volume 10% less
                        mixer.music.set_volume(current_volume)
                if stop_rect.collidepoint(mpos):
                    song = "None"
                    mixer.music.stop() # stops song
                if highVolume_rect.collidepoint(mpos):
                    if current_volume < 1:
                        current_volume = mixer.music.get_volume()+0.1 # makes volume higher
                        mixer.music.set_volume(current_volume)
#----------------------------------------------------------------------

#-------------------------------Undo/Redo------------------------------
    if undo_rect.collidepoint(mpos) and len(undo) > 1 and click:
        redo.append(undo.pop()) # erases from undo and appends to redo
        screen.blit(undo[-1], canvas) # blits the last one on to canvas

    if redo_rect.collidepoint(mpos) and len(redo) > 0 and click:
        reblit = redo.pop()
        screen.blit(reblit, canvas)
        undo.append(reblit)
#----------------------------------------------------------------------

#------------------------------Save/Open-------------------------------
    if save_rect.collidepoint(mpos) and mb[0] == 1:
        drawing = screen.subsurface(canvas).copy()
        name = asksaveasfilename(parent=root,title="Save the image as...") # gets file name to save image
        if name[-4:] == ".jpg":
            image.save(drawing, name + ".jpg")

    if open_rect.collidepoint(mpos) and mb[0] == 1:
        screen.set_clip(canvas)
        fileName = askopenfilename(parent=root,title="Open Image:") # gets which directory it needs to open the image froma
        screen.blit(image.load(fileName), canvas)
#----------------------------------------------------------------------

    if mb[0] == 1 and outline.collidepoint(mpos):
        fill = False
    elif mb[0] == 1 and filled.collidepoint(mpos):
        fill = True

    if mb[0] == 1 and snapOff.collidepoint(mpos):
        snap = False
    elif mb[0] == 1 and snapOn.collidepoint(mpos):
        snap = True
#-------------------------------Color Selection---------------------------------------
    if color_rect.collidepoint(mpos):
        screen.set_clip(color_rect)
        screen.blit(color_image, (858, 63))
        draw.circle(screen, (255, 255, 255), (mx ,my), 5, 3)
        draw.circle(screen, (0, 0, 0), (mx, my), 6, 2)
        if mb[0] == 1:
            screen.set_clip(None)
            color = tuple(screen.get_at((mx, my))) # Shows the user what color they have chosen
            draw.rect(screen, color, (858, 163, 172, 20))
            draw.rect(screen, (50, 50, 50), (845, 193, 200, 20))
            regular(screen, 15, "R:  "+str(color[0]), (255, 255, 255), (858, 193)) # tells the user the color they have chosen
            regular(screen, 15, "G:  "+str(color[1]), (255, 255, 255), (918, 193)) # tells the user the color they have chosen
            regular(screen, 15, "B:  "+str(color[2]), (255, 255, 255), (978, 193)) # tells the user the color they have chosen
    else:
        screen.blit(color_image, (858, 63))
#-------------------------------------------------------------------------------------

#-------------------Highlighting Selected tool-------------------------
    if tool == "Pencil":
        screen.blit(pencilSelected_image, (857, 302))
    else:
        screen.blit(pencil_image, (857, 302))
    if tool == "Marker":
        screen.blit(markerSelected_image, (922, 302))
    else:
        screen.blit(marker_image, (922, 302))
    if tool == "Eraser":
        screen.blit(eraserSelected_image, (987, 302))
    else:
        screen.blit(eraser_image, (987, 302))
    if tool == "Brush":
        screen.blit(brushSelected_image, (857, 367))
    else:
        screen.blit(brush_image, (857, 367))
    if tool == "Spray":
        screen.blit(spraySelected_image, (922, 367))
    else:
        screen.blit(spray_image, (922, 367))
    if tool == "Magic Eraser":
        screen.blit(magicEraserSelected_image, (987, 367))
    else:
        screen.blit(magicEraser_image, (987, 367))
    if tool == "Flood Fill":
        screen.blit(floodSelected_image, (922, 432))
    else:
        screen.blit(flood_image, (922, 432))
    if tool == "Text":
        screen.blit(textSelected_image, (987, 432))
    else:
        screen.blit(text_image, (987, 432))
    if tool == "Line":
        screen.blit(lineSelected_image, (857, 432))
    else:
        screen.blit(line_image, (857, 432))
    if tool == "Rectangle":
        screen.blit(outlinedRectangleSelected_image, (895, 498))
        screen.blit(filledRectangleSelected_image, (905, 512))
    else:
        screen.blit(outlinedRectangle_image, (895, 498))
        screen.blit(filledRectangle_image, (905, 512))
    if tool == "Ellipse":
        screen.blit(outlinedEllipseSelected_image, (960, 498))
        screen.blit(filledEllipseSelected_image, (970, 512))
    else:
        screen.blit(outlinedEllipse_image, (960, 498))
        screen.blit(filledEllipse_image, (970, 512))
#----------------------------------------------------------------------

#---------------------Highlighting Selected Stamp----------------------
    if tool == "Crystal Meth Logo":
        draw.rect(screen, (25, 88, 29), meth_rect)
        screen.blit(meth_icon, (1095, 100))
    else:
        draw.rect(screen, (200, 200, 200), meth_rect)
        screen.blit(meth_icon, (1095, 100))

    if tool == "Lego Figurine":
        draw.rect(screen, (25, 88, 29), lego_rect)
        screen.blit(lego_icon, (1105, 240))
    else:
        draw.rect(screen, (200, 200, 200), lego_rect)
        screen.blit(lego_icon, (1105, 240))

    if tool == "Gus Fring":
        draw.rect(screen, (25, 88, 29), gus_rect)
        screen.blit(gus_icon, (1215, 235))
    else:
        draw.rect(screen, (200, 200, 200), gus_rect)
        screen.blit(gus_icon, (1215, 235))

    if tool == "Saul Goodman":
        draw.rect(screen, (25, 88, 29), saul_rect)
        screen.blit(saul_icon, (1113, 335))
    else:
        draw.rect(screen, (200, 200, 200), saul_rect)
        screen.blit(saul_icon, (1113, 335))

    if tool == "Jesse Pinkman":
        draw.rect(screen, (25, 88, 29), jesse_rect)
        screen.blit(jesse_icon, (1237, 335))
    else:
        draw.rect(screen, (200, 200, 200), jesse_rect)
        screen.blit(jesse_icon, (1237, 335))

    if tool == "Mike E.":
        draw.rect(screen, (25, 88, 29), mike_rect)
        screen.blit(mike_icon, (1112, 435))
    else:
        draw.rect(screen, (200, 200, 200), mike_rect)
        screen.blit(mike_icon, (1112, 435))

    if tool == "Walter White":
        draw.rect(screen, (25, 88, 29), walter_rect)
        screen.blit(walter_icon, (1235, 435))
    else:
        draw.rect(screen, (200, 200, 200), walter_rect)
        screen.blit(walter_icon, (1235, 435))

    if tool == "Heisenberg":
        draw.rect(screen, (25, 88, 29), heisenberg_rect)
        screen.blit(heisenberg_icon, (1098, 533))
    else:
        draw.rect(screen, (200, 200, 200), heisenberg_rect)
        screen.blit(heisenberg_icon, (1098, 533))

    if tool == "Crystal Ship":
        draw.rect(screen, (25, 88, 29), crystalShip_rect)
        screen.blit(crystalShip_icon, (1218, 540))
    else:    
        draw.rect(screen, (200, 200, 200), crystalShip_rect)
        screen.blit(crystalShip_icon, (1218, 540))    
#----------------------------------------------------------------------

#-----------------Highlighting Selected Music----------------------
    if song == "Happy":
        draw.rect(screen, (50, 50, 50), happy_rect)
        screen.blit(musicSelected, (282, 670))
        smoolthan(screen, 15, "Happy", (25, 88, 29), (277, 713))
    else:
        draw.rect(screen, (50, 50, 50), happy_rect)
        screen.blit(music, (282, 670))
        smoolthan(screen, 15, "Happy", (255, 255, 255), (277, 713))

    if song == "Dark Horse":
        draw.rect(screen, (50, 50, 50), darkHorse_rect)
        screen.blit(musicSelected, (377, 670))
        smoolthan(screen, 15, "Dark Horse", (25, 88, 29), (358, 713))
    else:
        draw.rect(screen, (50, 50, 50), darkHorse_rect)
        screen.blit(music, (377, 670))
        smoolthan(screen, 15, "Dark Horse", (255, 255, 255), (358, 713))

    if song == "Neon Lights":
        draw.rect(screen, (50, 50, 50), neonLights_rect)
        screen.blit(musicSelected, (472, 670))
        smoolthan(screen, 15, "Neon Lights", (25, 88, 29), (450, 713))
    else:
        draw.rect(screen, (50, 50, 50), neonLights_rect)
        screen.blit(music, (472, 670))
        smoolthan(screen, 15, "Neon Lights", (255, 255, 255), (450, 713))

    if song == "Blank Space":
        draw.rect(screen, (50, 50, 50), blankSpace_rect)
        screen.blit(musicSelected, (567, 670))
        smoolthan(screen, 15, "Blank Space", (25, 88, 29), (545, 713))
    else:
        draw.rect(screen, (50, 50, 50), blankSpace_rect)
        screen.blit(music, (567, 670))
        smoolthan(screen, 15, "Blank Space", (255, 255, 255), (545, 713))

    if song == "Burn":
        draw.rect(screen, (50, 50, 50), burn_rect)
        screen.blit(musicSelected, (662, 670))
        smoolthan(screen, 15, "Burn", (25, 88, 29), (662, 713))
    else:
        draw.rect(screen, (50, 50, 50), burn_rect)
        screen.blit(music, (662, 670))
        smoolthan(screen, 15, "Burn", (255, 255, 255), (662, 713))

    if song == "Demons":
        draw.rect(screen, (50, 50, 50), demons_rect)
        screen.blit(musicSelected, (757, 670))
        smoolthan(screen, 15, "Demons", (25, 88, 29), (748, 713))
    else:
        draw.rect(screen, (50, 50, 50), demons_rect)
        screen.blit(music, (757, 670))
        smoolthan(screen, 15, "Demons", (255, 255, 255), (748, 713))
#----------------------------------------------------------------------

#---------------------------Tool Feedback--------------------------------
    draw.rect(screen, (50, 50, 50), (845, 665, 501, 70))
    if tool == "Pencil" or tool == "Marker" or tool == "Brush":
        smoolthan(screen, 15, "Click to draw, and scroll to adjust the thickness.", (255, 255, 255), (850, 675))
    if tool == "Eraser":
        smoolthan(screen, 15, "Click to erase, and scroll to adjust the thickness of the eraser.", (255, 255, 255), (850, 675))
    if tool == "Spray":
        smoolthan(screen, 15, "Click to spray, and scroll to Adjust the thickness.", (255, 255, 255), (850, 675))
    if tool == "Select":
        smoolthan(screen, 15, "Draw a rectangle around the area you want to select. Let go of the left", (255, 255, 255), (850, 675))
        smoolthan(screen, 15, "mouse button. Click on the selected area and move it to the desired", (255, 255, 255), (850, 690))
        smoolthan(screen, 15, "location.", (255, 255, 255), (850, 705))
    if tool == "Magic Eraser":
        smoolthan(screen, 15, "Click on the selected color, you would like to erase and every pixel", (255, 255, 255), (850, 675))
        smoolthan(screen, 15, "with the same color that is interconnected with it will be erased.", (255, 255, 255), (850, 690))
    if tool == "Flood Fill":
        smoolthan(screen, 15, "Click on the selected color, you would like to erase and every pixel", (255, 255, 255), (850, 675))
        smoolthan(screen, 15, "with the same color that is interconnected with it will be replaced", (255, 255, 255), (850, 690))
        smoolthan(screen, 15, "with the selected color.", (255, 255, 255), (850, 705))
    if tool == "Text":
        smoolthan(screen, 15, "Hold left-mouse button down and type the prefered phrase. Scroll to", (255, 255, 255), (850, 675))
        smoolthan(screen, 15, "adjust font size", (255, 255, 255), (850, 690))
    if tool == "Line":
        smoolthan(screen, 15, "Click on the area you would like to start drawing the line from. You", (255, 255, 255), (850, 675))
        smoolthan(screen, 15, "can chose snap to only draw at a 90, 180, 270 and 360 degree angle.", (255, 255, 255), (850, 690))
        smoolthan(screen, 15, "release the mouse button to place the line on the canvas.", (255, 255, 255), (850, 705))
    if tool == "Rectangle":
        smoolthan(screen, 15, "Click on the area you would like to start drawing the rectangle from.", (255, 255, 255), (850, 675))
        smoolthan(screen, 15, "You can chose the fill option to have the outline of the rectangle. If", (255, 255, 255), (850, 690))
        smoolthan(screen, 15, "you chose the outline function, scroll to change the width.", (255, 255, 255), (850, 705))
    if tool == "Ellipse":
        smoolthan(screen, 15, "Click on the area you would like to start drawing the ellipse from. You", (255, 255, 255), (850, 675))
        smoolthan(screen, 15, "can chose the outline option to have the outline of the ellipse. If you", (255, 255, 255), (850, 690))
        smoolthan(screen, 15, "chose the outline function, scroll to change the width.", (255, 255, 255), (850, 705))
    elif tool == "Crystal Meth Logo" or tool == "Lego Figurine" or tool == "Gus Fring" or tool == "Saul Goodman" or tool == "Jesse Pinkman" or tool == "Mike E." or tool == "Walter White" or tool == "Heisenberg" or tool == "Crystal Ship":
        smoolthan(screen, 15, "Scroll to change the size of the image.", (255, 255, 255), (850, 675))
#--------------------------------------------------------------------

#----------------Calling all the tools-----------------
    if mb[0] == 1 and canvas.collidepoint(mpos):
        clicked = True
        pencil(tool, screen, canvas, mpos, mb, mx, my, ox, oy, color, radius)
        marker(tool, screen, canvas, mpos, mb, mx, my, ox, oy, color, radius)
        eraser(tool, screen, canvas, mpos, mb, mx, my, ox, oy, radius)
        brush(tool, screen, canvas, mpos, mb, mx, my, ox, oy, color, radius)
        spray(tool, screen, canvas, mpos, mb, mx, my, color, radius)
        magic_eraser(tool, screen, canvas, color, mb, mpos, mx, my)
        flood(tool, screen, canvas, color, mb, mpos, mx, my)
        line(tool, screen, snap, canvas, color, copy, start, mpos, mb, mx, my, radius)
        rectangle(tool, screen, canvas, color, fill, start, copy, mpos, mb, mx, my, radius)
        ellipse(tool, screen, canvas, color, fill, copy, start, mpos, mb, mx, my, radius)
        clear(screen, canvas, clear_screen)
        sticker(screen, tool, "Crystal Meth Logo", canvas, copy, meth, mpos, mb, x, y, mx, my, ex, ey, radius)
        sticker(screen, tool, "Lego Figurine", canvas, copy, lego, mpos, mb, x, y, mx, my, ex, ey, radius)
        sticker(screen, tool, "Gus Fring", canvas, copy, gus, mpos, mb, x, y, mx, my, ex, ey, radius)
        sticker(screen, tool, "Saul Goodman", canvas, copy, saul, mpos, mb, x, y, mx, my, ex, ey, radius)
        sticker(screen, tool, "Jesse Pinkman", canvas, copy, jesse, mpos, mb, x, y, mx, my, ex, ey, radius)
        sticker(screen, tool, "Mike E.", canvas, copy, mike, mpos, mb, x, y, mx, my, ex, ey, radius)
        sticker(screen, tool, "Walter White", canvas, copy, walter, mpos, mb, x, y, mx, my, ex, ey, radius)
        sticker(screen, tool, "Heisenberg", canvas, copy, heisenberg, mpos, mb, x, y, mx, my, ex, ey, radius)
        sticker(screen, tool, "Crystal Ship", canvas, copy, crystalShip, mpos, mb, x, y, mx, my, ex, ey, radius)
    FPS(screen, clock)
    selected_tool(screen, tool)
    x_y(screen, mx, my)
    thickness(screen, tool, radius, start, x, y, ex, ey, mx, my, radius)
    date_time(screen)
    fill_outline(screen, tool, fill, mpos, mb, filled, outline)
    snap_OnOff(screen, tool, snap, mpos, mb, snapOn, snapOff)
    mouse_visibility(canvas, color_rect, mpos, mb)
#-------------------------------------------------------
    display.flip()
quit()
