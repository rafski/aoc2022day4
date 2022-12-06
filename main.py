import numpy
import re

with open('input.txt') as f:

    sections = f.read().splitlines()
    sections_array = numpy.array(sections)
    #print(len(sections_array))
    full_overlaps = 0
    part_overlaps = 0
    for section in sections_array:
        section_inner_array = re.split(r',|-', section)
        #print(section_inner_array)
        inner_array_int = list(map(int, section_inner_array))
        #print(inner_array_int)
        first = False
        if inner_array_int[0] in range(inner_array_int[2], inner_array_int[3] +1):
            #print("1")
            if inner_array_int[1] in range(inner_array_int[2], inner_array_int[3]+1):
               #print("2")
                full_overlaps += 1
                first = True
                print("first ", full_overlaps)
        if inner_array_int[2] in range(inner_array_int[0], inner_array_int[1]+1):
            #print("3")
            if inner_array_int[3] in range(inner_array_int[0], inner_array_int[1]+1):
                #print("4")
                if first == False:
                    full_overlaps += 1
                    print("second ", full_overlaps)
                else:
                    first = False
        second = False
        if inner_array_int[0] in range(inner_array_int[2], inner_array_int[3] +1) or inner_array_int[1] in range(inner_array_int[2], inner_array_int[3]+1):
               #print("2")
                part_overlaps += 1
                second = True
                print("first ", part_overlaps)
        if inner_array_int[2] in range(inner_array_int[0], inner_array_int[1]+1) or inner_array_int[3] in range(inner_array_int[0], inner_array_int[1]+1):
                #print("4")
                if second == False:
                    part_overlaps += 1
                    print("second ", part_overlaps)
                else:
                    second = False
    print(full_overlaps)
    print(part_overlaps)