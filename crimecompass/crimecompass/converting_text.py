with open("dangerous_nodes.txt") as file:
    lines = file.readlines()[2:]
    coords_array = [[float(value) for value in line.split()[1:]] for line in lines]

print(coords_array)