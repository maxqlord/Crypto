from PIL import Image
import copy

'''im = Image.open("Disco.bmp")    #open an image
print(im.size)                  #retrieve the length & width as a tuple
print(im.getpixel((499,341)))   #get the value of a pixel (for this project, a single number from 0 to 255)
im.putpixel((499,341),0)        #change the value of a pixel (note: does not change the FILE, just the OBJECT, until saved)
im.show()                       #display the image (probably...this sometimes doesn't work)
                                #look carefully for one black pixel in the bottom left of the R in "STAR"
im.save("DiscoModified.bmp")    #save the image object as a new file
'''
'''PLEASE NOTE: for this project, all files have been modified to be grayscale images only, with one value for each
pixel, from 0 to 255, defining its brightness.  The vast majority of images you find will be in RGB format, as you have
learned before.  To convert an RGB image to a true grayscale image, use this code:

im = Image.open("filename").convert("L")  #"L" is the shorthand for the format we are using
im.save("new filename")
'''
def matrix_mult_mod(m1, m2, mod):

    ans = []
  
    for row in range(len(m1)):
        ans.append([])
        for col in range(len(m2[0])):
            a = (m1[row][0] * m2[0][col] + m1[row][1] * m2[1][col]) % mod
            ans[row].append(a)
    return ans

def caesar(im, shift):
    for i in range(0, im.size[0]):
        for j in range(0, im.size[1]):
            pixel= im.getpixel((i,j))
            im.putpixel((i,j), ((pixel + shift) % 256))
            
def hill_cipher_encode(im, matrix):
    for i in range(0, im.size[1]):
        for j in range(0, im.size[0],2):
            #print(i,j)
            pixel1 = im.getpixel((j,i))
            pixel2 = im.getpixel((j+1,i))
            mpixels = [[pixel1, pixel2]]
            encrypted = matrix_mult_mod(mpixels, matrix, 256)
            im.putpixel((j,i), encrypted[0][0])
            im.putpixel((j+1,i), encrypted[0][1])
            
            
            
def main():
    '''
    im = Image.open("Disco.bmp").convert("L")
    caesar(im, 53)
    im.show()
    im.save("DiscoCaesarShifted.bmp")
    '''
    im = Image.open("SC.bmp").convert("L")
    matrix = [[2,3],[5,20]]
    hill_cipher_encode(im, matrix)
    im.show()
    im.save("SCHillCipher.bmp")
main()
