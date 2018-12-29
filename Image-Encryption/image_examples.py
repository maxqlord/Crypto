from PIL import Image

im = Image.open("Disco.bmp")    #open an image
print(im.size)                  #retrieve the length & width as a tuple
print(im.getpixel((499,341)))   #get the value of a pixel (for this project, a single number from 0 to 255)
im.putpixel((499,341),0)        #change the value of a pixel (note: does not change the FILE, just the OBJECT, until saved)
im.show()                       #display the image (probably...this sometimes doesn't work)
                                #look carefully for one black pixel in the bottom left of the R in "STAR"
im.save("DiscoModified.bmp")    #save the image object as a new file

'''PLEASE NOTE: for this project, all files have been modified to be grayscale images only, with one value for each
pixel, from 0 to 255, defining its brightness.  The vast majority of images you find will be in RGB format, as you have
learned before.  To convert an RGB image to a true grayscale image, use this code:

im = Image.open("filename").convert("L")  #"L" is the shorthand for the format we are using
im.save("new filename")
'''