# sorry for the bad commenting...

from PIL import Image #Image manipulation library
import os
        # This script converts from .png to .txt
def main( ): #{
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

    done = 0
    x = 0
    y = 0
    img = ""
    n = 0
    # allows these to be used in the code

    filename = ("input.png")
    # filename of the image I'm using

    cfile = ( os.path.join(__location__, filename) )
    # cfile is set to the location of the png in the same
    # directory as the python script

    image = Image.open( cfile )
    # loads the image

    size = width, height = image.size
    # gets the size of the image

    while(done == 0): #{
        # adds 1 to x every loop

        coordinate = x, y
        # sets the coordinates

        pxl = image.getpixel( coordinate )
        print (coordinate)
        # sets pxl to the color of the selected pixel

        img = img + "**" + str(x) \
         + "." + str(y) \
         + "." + str(pxl[0]) \
         + "." + str(pxl[1]) \
         + "." + str(pxl[2])
        # creates the long string that gets written to the text file.
        # I'm aware that this is very RAM intensive, I might fix it in the future,
        # but keep in mind that this script wasn't designed to be efficient.

        x = x + 1
        if(x == width and y == (height - 1)): #{
            done = 1
            x = 0
            y = 0
            print ("Done!")

            text_file = open(os.path.join(__location__, "Image.txt"), "w")
            n = text_file.write(img)
            text_file.close()

            print (size)
            # if x equals the width and y equals the height of the image, set "done" 
            # to 1 to break the while loop and print the string into a text file and print the image size
        #}
        if(x == width): #{
            x = 0
            y = y + 1
            #if x equals the width of the image, set x to 0 and add 1 to y
        #}
    #}
    del image
    del n
    #deletes the stroed values 'image' and 'n'
#}

if( __name__ == "__main__"): #{
    
    main()
    
#}