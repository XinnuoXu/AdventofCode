#coding=utf8

import copy 
import numpy

# Read data
#fd = open("a_example.in", 'rU')
fd = open("b_small.in", 'rU')
data = [[c for c in line][:-1] for line in fd]
row = int(data[0][0])
columns = int(data[0][2])
min_ing = int(data[0][4])
max_ing = int(data[0][6])
pizza = data[1:]


# Get shapes by required cell numbers
shapes_by_num = {}
for cell_num in range(min_ing * 2, max_ing + 1):
    shapes = []
    for i in range(1, cell_num+1):
        if cell_num % i == 0:
            shapes.append([i, cell_num / i])
    shapes_by_num[cell_num] = shapes

def collision(i, j, shape, cells):
    # collision with edge
    if i + shape[0] > row or j + shape[1] > columns:
        return True
    for r in range(i, i + shape[0]):
        for c in range(j, j + shape[1]):
            if cells[r][c] == 1:
                return True
    return False

def full_ingredient(i, j, shape, cells):
    igd = {'T':0, 'M':0}
    for r in range(i, i + shape[0]):
        for c in range(j, j + shape[1]):
            igd[pizza[r][c]] += 1
    if igd['T'] < min_ing or igd['M'] < min_ing:
        return False
    return True
    
def cutting(i, j, shape, records, cells):
    # update records
    next_records = copy.deepcopy(records)
    next_records.append([i, j, i + shape[0]-1, j + shape[1]-1])
    # update cell
    next_cells = copy.deepcopy(cells)
    for r in range(i, i + shape[0]):
        for c in range(j, j + shape[1]):
            next_cells[r][c] = 1
    # move to the next
    next_j = j + shape[1]
    next_i = i
    if next_j == columns:
        next_j = 0; next_i += 1
    while next_i < row and cells[next_i][next_j] == 1:
        next_j += 1
        if next_j == columns:
            next_j = 0; next_i += 1
    '''
    print "[OLD]", i, j, shape, cells
    print "[NEW]", next_i, next_j, next_records, next_cells
    print ""
    '''
    return next_i, next_j, next_records, next_cells

import time
c_time = time.time()

def processing(i, j, records, cells, max_coverage, max_records):
    global c_time
    # Finished on exploration
    if i == row:
        print int(numpy.sum(cells)), records
        print time.time() - c_time
        c_time = time.time()
        if int(numpy.sum(cells)) > max_coverage:
            max_coverage = int(numpy.sum(cells))
            max_records = copy.deepcopy(records)
        return max_coverage, max_records
    # Skip current cell and move to the next cell
    next_j = j + 1; next_i = i
    if next_j == columns:
        next_j = 0; next_i += 1
    next_cells = copy.deepcopy(cells)
    next_records = copy.deepcopy(records)
    max_coverage, max_records = processing(next_i, next_j, next_records, next_cells, max_coverage, max_records)
    # Explore all combination (cell_numbers, shapes)
    #for exp_num in range(min_ing*2, max_ing+1):
    for exp_num in range(max_ing, min_ing*2 - 1, -1):
        shapes = copy.deepcopy(shapes_by_num[exp_num])
        while len(shapes) != 0:
            shape = shapes.pop()
            #print i, j, exp_num, shape
            if (not collision(i, j, shape, cells)) and full_ingredient(i, j, shape, cells):
                next_i, next_j, next_records, next_cells = cutting(i, j, shape, records, cells)
                max_coverage, max_records = processing(next_i, next_j, next_records, next_cells, max_coverage, max_records)
    return max_coverage, max_records

if __name__ == '__main__':
    cells = numpy.zeros((row, columns))
    max_coverage = 0
    max_records = []
    max_coverage, max_records = processing(0, 0, [], cells, max_coverage, max_records)
    print max_coverage, max_records
