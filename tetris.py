from sense_hat import SenseHat
import time

# Shape object.
class Shape():
    # Different shapes
    Straight = 1
    Square = 2
    T = 3
    J = 4
    L = 5
    S = 6
    Z = 7

    # Constructor
    def __init__(self, shapetype = Square, X = 0, Y = 0):
        # Type of shape.
        self.shapetype = shapetype
        # Location.
        self.X = X
        self.Y = Y

    # Draw the shape.
    def getshape(self):
        if self.shapetype == Straight:
            return [[1,1,1,1]]
        elif self.shapetype == Square:
            return [[1,1],[1,1]]
        elif self.shapetype == T:
            return [[1,1,1],[0,1,0]]

    def getcolor(self):
        if self.shapetype == Straight:
            return [0,255,255]
        elif self.shapetype == Square:
            return [255,255,0]
        elif self.shapetype == T:
            return [255,0,255]
        elif self.shapetype == J:
            return [0,0,255]
        elif self.shapetype == L:
            return [255,165,0]
        elif self.shapetype == S:
            return [0,255,0]
        elif self.shapetype == Z:
            return [255,0,0]


class Tetris:
    def __init__(self):
        # Connect to the sense hat.
        self.sensehat = SenseHat()
        # List of all shapes.
        self.shapes = [Shape(Shape.Square)]

    def play(self):
        # TODO - Loop the game.
        self.drawscreen()

        # Sleep for a while.
        time.sleep(4)

    def drawscreen(self):
        # Create a new background.
        B = [0,0,0] # Black
        R = [255,0,0] # Red
        pixels = []
        for ij in range(8):
            row = []
            for jk in range(8):
                if jk == ij:
                    row.append(R)
                else:
                    row.append(B)

            pixels.append(row)

        # Flatten out to one list.
        pixels = [p for l in pixels for p in l]
        # Draw.
        self.sensehat.set_pixels(pixels)
        
        

# Main entry point.
if __name__ == "__main__":
    # Create a game of tetris.
    mygame = Tetris()
    mygame.play()


