from sense_hat import SenseHat
from time import sleep

def drawline(theta):
    # Clear the display.
    w = 8
    h = 8
    pixels = [[0,0,0]]*w*h
    # Simple line drawing algorithm
    return pixels
    

def plotline(pixels,w,h,clr,x0,y0,x1,y1):
    # Bresenham's line drawing algorithm
    dx = x1 - x0
    dy = y1 - y0
    D = 2*dy-dx
    y = y0

    for x in range(x0,x1):
        pixels[y*w+x] = clr
        if D >= 0:
            y += 1
            D -= dx
        D += dy

    return pixels


def showcompass():
    # Connect to the sense hat.
    sense = SenseHat()
    
    pixels = drawline(0)
    pixels = plotline(pixels,8,8,[255,0,0],6,3,1,1)
    
    sense.set_pixels(pixels)
    
    # Loop forever.
    while True:
        # Read the compass orientation.
        north = sense.get_compass()

        print("North: {0}".format(north))

        # Sleep
        sleep(0.1)


# Main entry point.
if __name__ == "__main__":
    showcompass()
