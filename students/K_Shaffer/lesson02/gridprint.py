'''
Grid Print
Dev: K. Shaffer
Date: 10/20/18
'''


def print_grid(n):
    space_count = int((n-1)/2)
    row_count = n + 2
    for i in range(row_count):
        if i == 0 or i == space_count+1 or i == row_count-1 :
            print ('+' + space_count*'-' +'+' + space_count*'-' + "+")
        else:
            print ('|' + space_count*' ' + '|' + space_count*' '+ '|')

def print_grid2(r, c):
    cell_count = c
    row_count = r*(c+1) + 1
    for i in range(row_count):
        if i == 0 or i % (cell_count + 1) == 0 or i == row_count-1:
            print('+' + (cell_count*'-' + '+')*r)
        else:
            print('|' + (cell_count*' ' + '|')*r)


#print_grid(21)
print_grid2(5, 3)
