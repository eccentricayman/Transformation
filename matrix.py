import math


def print_matrix( matrix ):
    retStr = "";
    for i in range(len(matrix)):
        #print the left border
        retStr += "|"
        #print the row, except for the last number
        for j in range(len(matrix[i]) - 1):
            retStr += str(matrix[i][j]) + "\t"
        #print last number without tab
        retStr += str(matrix[i][j])
        #print right border with newline
        retStr += "|\n"
    #get rid of last newline
    print retStr[:-1]
    
def ident( matrix ):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if row == column:
                matrix[row][column] = 1
            else:
                matrix[row][column] = 0

def scalar_mult( matrix, s ):
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            matrix[row][column] *= s

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    for column in range(len(m2[0])):
        for row in range(len(m2)):
            total = 0
            for i in range(len(m1[row])):
                total += m1[row][i] * m2[i][column]
            m2[row][column] = total

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

