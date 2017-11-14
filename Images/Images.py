from PIL import Image
from math import gcd
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
def det_mod(m, mod):
    return (m[0][0] * m[1][1] - m[0][1] * m[1][0]) % mod

def inv_mod(a, m):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    return None

def scalar_mult_mod(m, s, mod):
    m2 = copy.deepcopy(m)
   
    for x in range(len(m)):
        for y in range(2):
            m2[x][y] = (m2[x][y] * s) % mod
    return m2

def matrix_mult_mod(m1, m2, mod):
    ans = []
    for row in range(len(m1)):
        ans.append([])
        for col in range(len(m2[0])):
            a = (m1[row][0] * m2[0][col] + m1[row][1] * m2[1][col]) % mod
            ans[row].append(a)
    return ans

def matrix_inverse_mod(m1, mod):
    d = det_mod(m1, mod)
    inv = inv_mod(d, mod)
    if inv == None:
        return None
    m2 = [[m1[1][1], -1 * m1[0][1]], [-1 * m1[1][0], m1[0][0]]]
    return scalar_mult_mod(m2, inv, mod)

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
            
def hill_cipher_decode(im, matrix):
    for i in range(0, im.size[1]):
        for j in range(0, im.size[0],2):
            #print(i,j)
            pixel1 = im.getpixel((j,i))
            pixel2 = im.getpixel((j+1,i))
            mpixels = [[pixel1, pixel2]]
            inv = matrix_inverse_mod(matrix, 256)
            decrypted = matrix_mult_mod(mpixels, inv, 256)
            im.putpixel((j,i), decrypted[0][0])
            im.putpixel((j+1,i), decrypted[0][1])

def hill_cipher_augment_encode(im, matrix, vector):
    row_to_mult = 0
    for i in range(0,im.size[1]):
        for j in range(0, im.size[0],2):
            #print(i,j)
            #print(matrix)
            pixel1 = im.getpixel((j,i))
            pixel2 = im.getpixel((j+1,i))
            mpixels = [[pixel1, pixel2]]
            encrypted = matrix_mult_mod(mpixels, matrix, 256)
            #multiply by vector
            matrix[row_to_mult][0] *= vector[0]
            matrix[row_to_mult][1] *= vector[1]
            matrix[row_to_mult][0] %= 256
            matrix[row_to_mult][1] %= 256
            if row_to_mult == 0:
                row_to_mult = 1
            else:
                row_to_mult = 0
            #put pixels
            im.putpixel((j,i), encrypted[0][0])
            im.putpixel((j+1,i), encrypted[0][1])
            
def hill_cipher_augment_decode(im, matrix, vector):
    row_to_mult = 0
    for i in range(0,im.size[1]):
        for j in range(0, im.size[0],2):
            #print(i,j)
            #print(matrix)
            pixel1 = im.getpixel((j,i))
            pixel2 = im.getpixel((j+1,i))
            mpixels = [[pixel1, pixel2]]
            inv = matrix_inverse_mod(matrix, 256)
            decrypted = matrix_mult_mod(mpixels, inv, 256)
            #multiply by vector
            matrix[row_to_mult][0] *= vector[0]
            matrix[row_to_mult][1] *= vector[1]
            matrix[row_to_mult][0] %= 256
            matrix[row_to_mult][1] %= 256
            if row_to_mult == 0:
                row_to_mult = 1
            else:
                row_to_mult = 0
            #put pixels
            im.putpixel((j,i), decrypted[0][0])
            im.putpixel((j+1,i), decrypted[0][1])

def affine_encode(num, a, b, mod):
    #test coprime
    if gcd(a, mod) != 1:
        return num
    return (a*num+ b) % mod

def inv_mod(a, m):
    for i in range(m):
        if(a*i) % m == 1:
            return i
    return None

def affine_decode(num, a, b, mod):
    return (num + mod - b) * inv_mod(a, mod) % mod

def custom_encode(im, matrix, vector, a, b):
    row_to_mult = 0
    for i in range(0,im.size[1]):
        for j in range(0, im.size[0],2):
            #print(i,j)
            #print(matrix)
            pixel1 = im.getpixel((j,i))
            pixel2 = im.getpixel((j+1,i))
            b = i+j*j
            enc_pixel1 = affine_encode(pixel1, a, b, 256)
            enc_pixel2 = affine_encode(pixel2, a, b, 256)
            mpixels = [[enc_pixel1, enc_pixel2]]
            encrypted = matrix_mult_mod(mpixels, matrix, 256)
            #multiply by vector
            matrix[row_to_mult][0] *= vector[0]
            matrix[row_to_mult][1] *= vector[1]
            matrix[row_to_mult][0] %= 256
            matrix[row_to_mult][1] %= 256
            if row_to_mult == 0:
                row_to_mult = 1
            else:
                row_to_mult = 0
            #put pixels
            im.putpixel((j,i), encrypted[0][0])
            im.putpixel((j+1,i), encrypted[0][1])

def custom_decode(im, matrix, vector, a, b):
    row_to_mult = 0
    for i in range(0,im.size[1]):
        for j in range(0, im.size[0],2):
            #print(i,j)
            #print(matrix)
            pixel1 = im.getpixel((j,i))
            pixel2 = im.getpixel((j+1,i))
            mpixels = [[pixel1, pixel2]]
            inv = matrix_inverse_mod(matrix, 256)
            decrypted = matrix_mult_mod(mpixels, inv, 256)
            #multiply by vector
            matrix[row_to_mult][0] *= vector[0]
            matrix[row_to_mult][1] *= vector[1]
            matrix[row_to_mult][0] %= 256
            matrix[row_to_mult][1] %= 256
            if row_to_mult == 0:
                row_to_mult = 1
            else:
                row_to_mult = 0
            b = i+j*j
            pixel1 = affine_decode(decrypted[0][0], a, b, 256)
            pixel2 = affine_decode(decrypted[0][1], a, b, 256)
            #put pixels
            im.putpixel((j,i), pixel1)
            im.putpixel((j+1,i), pixel2)


            '''b = i+j*j
            enc_pixel1 = affine_encode(pixel1, a, b, 256)
            enc_pixel2 = affine_encode(pixel2, a, b, 256)
            '''
            
def main():
    '''
    im = Image.open("Disco.bmp").convert("L")
    caesar(im, 53)
    im.show()
    im.save("DiscoCaesarShifted.bmp")
    '''
    '''
    im = Image.open("SC.bmp").convert("L")
    matrix = [[2,3],[5,20]]
    hill_cipher_encode(im, matrix)
    im.show()
    im.save("SCHillCipher.bmp")
    '''
    '''
    im = Image.open("SCHillCipher.bmp").convert("L")
    matrix = [[2,3],[5,20]]
    hill_cipher_decode(im, matrix)
    im.show()
    im.save("SCHillCipherDecoded.bmp")
    '''
    '''
    im = Image.open("Mystery1.bmp").convert("L")
    matrix = [[2,3],[5,20]]
    hill_cipher_decode(im, matrix)
    im.show()
    im.save("Mystery1Decoded.bmp")
    '''
    '''
    im = Image.open("SC.bmp").convert("L")
    matrix = [[2,3],[5,20]]
    vector = [19,21]
    hill_cipher_augment_encode(im, matrix,vector)
    im.show()
    #im.save("SCHillCipherAugment.bmp")
    '''
    '''
    im = Image.open("Mystery2.bmp").convert("L")
    matrix = [[2,3],[5,20]]
    vector = [101,141]
    hill_cipher_augment_decode(im, matrix,vector)
    im.show()
    im.save("SCHillCipherAugmentDecode.bmp")
    '''
    '''
    im = Image.open("CustomEncodeLogo1.bmp").convert("L")
    matrix = [[2,3],[5,20]]
    vector = [19,21]
    custom_decode(im, matrix, vector,29,7)
    im.show()
    #im.save("CustomEncodeLogo1.bmp")
    '''
    im = Image.open("Logo2.bmp").convert("L")
    matrix = [[2,3],[5,20]]
    vector = [19,21]
    custom_decode(im, matrix, vector,29,7)
    im.show()
    im.save("CustomEncodeLogo2.bmp")
    
main()
