import tga, math

def flip_vertically(image: tga.Image):
    image.data.reverse()
    
def line(image: tga.Image, x1:int, y1:int, x2:int, y2:int, color: tga.Color):
    dx = x1 - x2
    dy = y1 - y2
    
    if dx > dy:
        steps = abs(dx)
    else:
        steps = abs(dy)
        
    x = x1
    y = y1
    
    x_inc = -(dx / steps)
    y_inc = -(dy / steps)
    for i in range(0, steps):
        image.set_pixel(math.floor(round(x)), math.floor(round(y)), red)
        x = x + x_inc
        y = y + y_inc

black = tga.Color(0, 0, 0)
white = tga.Color(255, 255, 255)
red = tga.Color(255, 0, 0) 

im = tga.Image(20, 20, black)

# im.set_pixel(1, 1, red)
line(im, 3, 3, 7, 10, red)
flip_vertically(im)

with open('image.tga', 'wb') as file:
    file.write(im.to_bytes())