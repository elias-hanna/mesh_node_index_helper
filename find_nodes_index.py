import os, sys


"""
This script gives the index of the nodes in a given in argument vtk file, the nodes being in specified areas defined through command line args.
arg1: vtk file name
arg2: gap between longitudinal edge of the object and center of first researched nodes area 
arg3: square area side length
"""


"""
Args: file handler
Ret: point_list, longest_axis
"""
def get_file_data(vtk_file):
    j=0
    nb_of_points = 0
    point_list = []
    # first element of max is axis, second one is max value
    longest_axis = [0, 0]
    max_xyz = [0, 0, 0]
    for i in vtk_file:
        splitted_string = i.split(" ")
        
        if nb_of_points != 0:
            # Store all the points for future operations
            point_list.append([float(j) for j in splitted_string])
            axis = 0
            for k in point_list[-1]:
                if k > max_xyz[axis]:
                    max_xyz[axis] = k 
                if longest_axis[1] < k:
                    longest_axis[1] = k
                    longest_axis[0] = axis
                axis = axis + 1
            nb_of_points = nb_of_points - 1
            if nb_of_points == 0:
                break
            
        if 'POINTS' in splitted_string:
            # Start to record points
            nb_of_points  = int(splitted_string[1])
    return point_list, longest_axis, max_xyz
    
def find_nodes_index(file_name, gap, square_width):
    print(sys.argv)

    vtk_file = open(file_name)
    # Get the point list and the axis of the longest part of the object, together with the object length
    point_list, longest_axis, max_xyz = get_file_data(vtk_file)
    print(point_list)
    print(longest_axis)
    print(max_xyz)
    point_in_areas = [[],[],[]]
    ## We only take points on the surface on null value on z-axis
    center_area_0 = gap
    center_area_1 = longest_axis[1]/2.0
    center_area_2 = longest_axis[1] - gap
    center_secondary_axis = max_xyz[1]/2.0
    point_index = 0
    for point in point_list:
        if point[2] == 0:
            if abs(center_area_0 - point[0]) < square_width and abs(center_secondary_axis - point[1]) < square_width:
                point_in_areas[0].append(point + [point_index])
            elif abs(center_area_1 - point[0]) < square_width and abs(center_secondary_axis - point[1]) < square_width:
                point_in_areas[1].append(point + [point_index])
            elif abs(center_area_2 - point[0]) < square_width and abs(center_secondary_axis - point[1]) < square_width:
                point_in_areas[2].append(point + [point_index])
        point_index = point_index + 1
    for i in point_in_areas:
        print()
        print(i)
    pass


if __name__=='__main__':
    if(len(sys.argv) != 4):
        raise ValueError('The script requires exactly 3 arguments. Check the script to see what they correspond too')
    file_name = sys.argv[1]
    gap = float(sys.argv[2])
    square_width = float(sys.argv[3])
    find_nodes_index(file_name, gap, square_width)
    pass
