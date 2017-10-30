BOX_ROW = 2
BOX_COL = 3
N = BOX_ROW*BOX_COL

with open('py_out.smv', 'w') as f:
# start define
    f.write("DEFINE")
    moves_prefix = '\t\tmoves :=\t[\n'
    moves_suffix = '\t\t\t\t];';
    move_rows = []
    i = 0
    s = "\t\t\t\t\t\t{},\t\t\t--R{}C{}#{}\n"
    s1 = "\t\t\t\t\t\t{},\t\t\t\t--R{}C{}#{}\n"
    for row in range(N):
        for col in range(N):
            for num in range(N):
                if i<10:
                    move_rows.append(s1.format(str(i),row,col,str(num)))
                else:
                    move_rows.append(s.format(str(i),row,col,str(num))) 
                i += 1

    f.write(moves_prefix)                
    for row in move_rows:
        f.write(row)
    f.write(moves_suffix)                
    # start constraint definitions

    constraint_prefix = '\t\tconstraints :=\t[\n'
    constraints_suffix = '\t\t\t\t];';
    row_num = []
    s = "\t\t\t\t\t\t{}\t\t\t--{}{}#{}\n"
    t = 'R'
    for row in range(N):
        # represents the constraint that row i have exactly one num j
        for num in range(N):
            row_num.append((''.join([' grid[{}] = {} |'.format(N*row+col, num) for col in range(N)]))[0:-1]+',')

    for n in row_num:
        print(n)
            
'''    t = 'C'
    for col in range(N):
        for num in range(N):
    t = 'B'
    for box in range(N):
        for num in range(N):
'''
# end define                
                




