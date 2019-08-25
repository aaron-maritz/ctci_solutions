# Aaron Maritz
# Question 1.7
# Given an image represented by an NxN matrix, -> each pixel in the image is 4 byte
# Rotate the image by 90 degress -> Do this in place.
# So this is an N x N integer matrix
#[0] -> [0]
#[2,3] -> [5,2]
#[5,4]    [4,3]

# Algorithm -> x,y -> rows becomes columns
# You just swap index's
# Go layer by layer

def rotate90(matrix) :
    n = len(matrix) / 2
    for level in range (n)
        # Have the number of layers
        start = level
        end = n - 1 - level
        for x in range (start, end)
            offset = x - start
