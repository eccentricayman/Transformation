from display import *
from draw import *
import math
import random

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

print "making new matrix and prnting"
#test matrices
tmatrix = new_matrix(0, 4)
imatrix = new_matrix(0, 4)
print

print "populating matrix and printing (empty)"
add_edge(tmatrix, 1, 2, 0, 3, 4, 0)
add_edge(tmatrix, 5, 6, 0, 7, 8, 0)
print_matrix(tmatrix)
print
add_edge(imatrix, 9, 10, 0, 11, 12, 0)
add_edge(imatrix, 13, 14, 0, 15, 16, 0)
print_matrix(imatrix)
print

print "tmatrix * 2"
scalar_mult(tmatrix, 2)
print_matrix(tmatrix)
print

print "imatrix * 7"
scalar_mult(imatrix, 7)
print_matrix(imatrix)
print

print "matrix * imatrix"
matrix_mult(tmatrix, imatrix)
print_matrix(imatrix)
print

print "printing imatrix, then turning into identity"
print_matrix(imatrix)
print
ident(imatrix)
print_matrix(imatrix)
print

print "drawing"
for i in range(500):
    add_edge(matrix, int(math.sin(i / (2 * math.pi))) * i, int(math.cos(i / (2 * math.pi))) * i, 0, int(math.tan(i / (2 * math.pi))) * i, int(math.atan(i / (2 * math.pi))) * i, 0)

draw_lines( matrix, screen, color )
display(screen)
