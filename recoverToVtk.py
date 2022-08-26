def recoverToVtk():
    #read from txt to pos and tet
    with open("pos.txt") as f:
        for line in f.readlines():
            line = line.split()
            pos.append([line[0], line[1], line[2]])

    with open("tet.txt") as f:
        for line in f.readlines():
            line = line.split()
            tet.append(["4", line[0], line[1], line[2], line[3]])

    #write to the txt
    # first convert pos and tet to list of str
    [str(i) for i in pos]
    [str(i) for i in tet]
    with open("bunny.vtk",'w') as f:
        header = [
        "# vtk DataFile Version 2.0\n",
        "Unstructured Grid\n",
        "ASCII\n",
        "DATASET UNSTRUCTURED_GRID\n"]
        f.writelines(header)
        f.write("POINTS "+ str(len(pos)) + " double\n")
        for i, x in enumerate(pos):
            pos[i] = " ".join(x)
            f.write(pos[i])
            f.write("\n")
        
        f.write("\nCELLS "+ str(len(tet)) + " " + str(len(tet)*5)+"\n")
        for i, x in enumerate(tet):
            tet[i] = " ".join(x)
            f.write(tet[i])
            f.write("\n")

        f.write("\nCELL_TYPES "+ str(len(tet)) + "\n")
        for i, x in enumerate(tet):
            f.write("10")
            f.write("\n")
        


pos = []
tet = []
recoverToVtk()