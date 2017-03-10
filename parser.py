from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    script = open(fname, "r");
    line = script.readline().strip()
    while line != "" and line != "quit":
        line = line.strip()
        if line == "line":
            data = script.readline().strip().split(" ")
            if len(data) != 6:
                print "Bad line."
            else:
                print "Adding line."
                add_edge(points, int(data[0]), int(data[1]), int(data[2]), int(data[3]), int(data[4]), int(data[5]))
        elif line == "ident":
            print "Identity matrix."
            ident(transform);
        elif line == "scale":
            data = script.readline().strip().split(" ")
            if len(data) != 3:
                "Bad scale."
            else:
                print "Scaling."
                scale = make_scale(int(data[0]), int(data[1]), int(data[2]))
                matrix_mult(scale, transform)
        elif line == "move":
            data = script.readline().strip().split(" ")
            if len(data) != 3:
                print "Bad move."
            else:
                print "Moving."
                move = make_translate(int(data[0]), int(data[1]), int(data[2]))
                matrix_mult(move, transform)
        elif line == "rotate":
            data = script.readline().strip().split(" ")
            if len(data) != 2:
                print "Bad rotate."
            else:
                print "Rotating."
                if data[0] == "x":
                    rotate = make_rotX(int(data[1]))
                    matrix_mult(rotate, transform)
                elif data[0] == "y":
                    rotate = make_rotY(int(data[1]))
                    matrix_mult(rotate, transform)
                elif data[0] == "z":
                    rotate = make_rotZ(int(data[1]))
                    matrix_mult(rotate, transform)
                else:
                    print "Bad axis."
        elif line == "apply":
            print "Applying."
            matrix_mult(transform, points)
        elif line == "display":
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        elif line == "save":
            data = script.readline().strip().split(" ")
            if len(data) != 1:
                print "No filename."
            else:
                clear_screen(screen)
                draw_lines(points, screen, color)
                display(screen)
                save_extension(screen, data[0])
        else:
            print "Bad command."
            break
        line = script.readline().strip()
