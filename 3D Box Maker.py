import numpy as np
from stl import mesh

# Define the 8 vertices of the cube
'''vertices = np.array([\
    [-1, -1, -1],
    [+1, -1, -1],
    [+1, +1, -1],
    [-1, +1, -1],
    [-1, -1, +1],
    [+1, -1, +1],
    [+1, +1, +1],
    [-1, +1, +1]])
# Define the 12 triangles composing the cube
faces = np.array([\
    [0,3,1],
    [1,3,2],
    [0,4,7],
    [0,7,3],
    [4,5,6],
    [4,6,7],
    [5,1,2],
    [5,2,6],
    [2,3,6],
    [3,7,6],
    [0,1,5],
    [0,5,4]])

# Create the mesh
cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        cube.vectors[i][j] = vertices[f[j],:]

# Write the mesh to file "cube.stl"
cube.save('cube.stl')'''

#Width - X
#Height - Y
#Length - Z

#Start at front right and go clockwise from bottom to top
#Length (depth) = y
#Width = x
#Height = z
#Use right hand rule for what pos what neg
def make_box(Name,Length,Width,Height,Shell_Thickness,Base_Thickness,Lip_Thickness,Lip_Percentage):
    vertices_bottom = np.array([\
    #Outer Bottom
    [-(Width/2 + Shell_Thickness + Lip_Thickness), -(Length/2 + Shell_Thickness + Lip_Thickness), 0],
    [-(Width/2 + Shell_Thickness + Lip_Thickness), (Length/2 + Shell_Thickness + Lip_Thickness), 0],
    [(Width/2 + Shell_Thickness + Lip_Thickness), (Length/2 + Shell_Thickness + Lip_Thickness), 0],
    [(Width/2 + Shell_Thickness + Lip_Thickness), -(Length/2 + Shell_Thickness + Lip_Thickness), 0],
    #Lip Bottom Outer
    [-(Width/2 + Shell_Thickness + Lip_Thickness), -(Length/2 + Shell_Thickness + Lip_Thickness), Height/2 + Base_Thickness],
    [-(Width/2 + Shell_Thickness + Lip_Thickness), (Length/2 + Shell_Thickness + Lip_Thickness), Height/2 + Base_Thickness],
    [(Width/2 + Shell_Thickness + Lip_Thickness), (Length/2 + Shell_Thickness + Lip_Thickness), Height/2 + Base_Thickness],
    [(Width/2 + Shell_Thickness + Lip_Thickness), -(Length/2 + Shell_Thickness + Lip_Thickness), Height/2 + Base_Thickness],
    #Inner Bottom
    [-(Width/2), -(Length/2), Base_Thickness],
    [-(Width/2), (Length/2), Base_Thickness],
    [(Width/2), (Length/2), Base_Thickness],
    [(Width/2), -(Length/2), Base_Thickness],
    #Lip Bottom Inner
    [-(Width/2 + Lip_Thickness), -(Length/2 + Lip_Thickness), Height/2 + Base_Thickness],
    [-(Width/2 + Lip_Thickness), (Length/2 + Lip_Thickness), Height/2 + Base_Thickness],
    [(Width/2 + Lip_Thickness), (Length/2 + Lip_Thickness), Height/2 + Base_Thickness],
    [(Width/2 + Lip_Thickness), -(Length/2 + Lip_Thickness), Height/2 + Base_Thickness],
    #Lip Top Outer (Above Lip Bottom Inner)
    [-(Width/2 + Lip_Thickness), -(Length/2 + Lip_Thickness), Height * Lip_Percentage/100 + Base_Thickness],
    [-(Width/2 + Lip_Thickness), (Length/2 + Lip_Thickness), Height * Lip_Percentage/100 + Base_Thickness],
    [(Width/2 + Lip_Thickness), (Length/2 + Lip_Thickness), Height * Lip_Percentage/100 + Base_Thickness],
    [(Width/2 + Lip_Thickness), -(Length/2 + Lip_Thickness), Height * Lip_Percentage/100 + Base_Thickness],
    #Lip Top Inner
    [-(Width/2), -(Length/2), Height * Lip_Percentage/100 + Base_Thickness],
    [-(Width/2), (Length/2), Height * Lip_Percentage/100 + Base_Thickness],
    [(Width/2), (Length/2), Height * Lip_Percentage/100 + Base_Thickness],
    [(Width/2), -(Length/2), Height * Lip_Percentage/100 + Base_Thickness],
    ])

    faces_bottom = np.array([\
    #Outer Bottom
    [0,1,2],
    [0,3,2],
    #Outer Front
    [0,3,4],
    [7,3,4],
    #Outer Right
    [0,1,4],
    [5,1,4],
    #Outer Back
    [1,2,5],
    [6,2,5],
    #Outer Left
    [2,3,6],
    [7,3,6],
    #These are trapezoids
    #Lip Front
    [4,7,12],
    [15,7,12],
    #Lip Right
    [4,5,12],
    [13,5,12],
    #Lip Back
    [5,6,13],
    [14,6,13],
    #Lip Left
    [6,7,14],
    [15,7,14],
    #Mid Front
    [12,15,16],
    [19,15,16],
    #Mid Right
    [12,13,16],
    [17,13,16],
    #Mid Back
    [13,14,17],
    [18,14,17],
    #Mid Left
    [14,15,18],
    [19,15,18],
    #Inner Bottom
    [8,9,10],
    [8,11,10],
    #Lip Top Front
    [16,19,20],
    [23,19,20],
    #Lip Top Right
    [16,17,20],
    [21,17,20],
    #Lip Top Back
    [17,18,21],
    [22,18,21],
    #Lip Top Left
    [18,19,22],
    [23,19,22],
    #Inner Front
    [8,11,20],
    [23,11,20],
    #Inner Right
    [8,9,20],
    [21,9,20],
    #Inner Back
    [9,10,21],
    [22,10,21],
    #Inner Left
    [10,11,22],
    [23,11,22],
    
    ])

    bottom = mesh.Mesh(np.zeros(faces_bottom.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces_bottom):
        for j in range(3):
            bottom.vectors[i][j] = vertices_bottom[f[j],:]
    bottom.save(Name+'_Bottom.stl')


    vertices_top = np.array([\
    #Outer Bottom
    [-(Width/2 + Shell_Thickness + Lip_Thickness), -(Length/2 + Shell_Thickness + Lip_Thickness), 0],
    [-(Width/2 + Shell_Thickness + Lip_Thickness), (Length/2 + Shell_Thickness + Lip_Thickness), 0],
    [(Width/2 + Shell_Thickness + Lip_Thickness), (Length/2 + Shell_Thickness + Lip_Thickness), 0],
    [(Width/2 + Shell_Thickness + Lip_Thickness), -(Length/2 + Shell_Thickness + Lip_Thickness), 0],
    #Lip Bottom Outer
    [-(Width/2 + Shell_Thickness + Lip_Thickness), -(Length/2 + Shell_Thickness + Lip_Thickness), Height/2 + Base_Thickness],
    [-(Width/2 + Shell_Thickness + Lip_Thickness), (Length/2 + Shell_Thickness + Lip_Thickness), Height/2 + Base_Thickness],
    [(Width/2 + Shell_Thickness + Lip_Thickness), (Length/2 + Shell_Thickness + Lip_Thickness), Height/2 + Base_Thickness],
    [(Width/2 + Shell_Thickness + Lip_Thickness), -(Length/2 + Shell_Thickness + Lip_Thickness), Height/2 + Base_Thickness],
    #Inner Bottom
    [-(Width/2), -(Length/2), Base_Thickness],
    [-(Width/2), (Length/2), Base_Thickness],
    [(Width/2), (Length/2), Base_Thickness],
    [(Width/2), -(Length/2), Base_Thickness],
    #Lip Bottom Inner
    [-(Width/2 + Lip_Thickness), -(Length/2 + Lip_Thickness), Height/2 + Base_Thickness],
    [-(Width/2 + Lip_Thickness), (Length/2 + Lip_Thickness), Height/2 + Base_Thickness],
    [(Width/2 + Lip_Thickness), (Length/2 + Lip_Thickness), Height/2 + Base_Thickness],
    [(Width/2 + Lip_Thickness), -(Length/2 + Lip_Thickness), Height/2 + Base_Thickness],
    #Lip Top Outer (Above Lip Bottom Inner)
    [-(Width/2 + Lip_Thickness), -(Length/2 + Lip_Thickness), Height * (1 - Lip_Percentage/100) + Base_Thickness],
    [-(Width/2 + Lip_Thickness), (Length/2 + Lip_Thickness), Height * (1 - Lip_Percentage/100) + Base_Thickness],
    [(Width/2 + Lip_Thickness), (Length/2 + Lip_Thickness), Height * (1 - Lip_Percentage/100) + Base_Thickness],
    [(Width/2 + Lip_Thickness), -(Length/2 + Lip_Thickness), Height * (1 - Lip_Percentage/100) + Base_Thickness],
    #Lip Top Inner
    [-(Width/2), -(Length/2), Height * (1 - Lip_Percentage/100) + Base_Thickness],
    [-(Width/2), (Length/2), Height * (1 - Lip_Percentage/100) + Base_Thickness],
    [(Width/2), (Length/2), Height * (1 - Lip_Percentage/100) + Base_Thickness],
    [(Width/2), -(Length/2), Height * (1 - Lip_Percentage/100) + Base_Thickness],
    ])


    faces_top = np.array([\
  
    #Outer Bottom
    [0,1,2],
    [0,3,2],
    #Outer Front
    [0,3,4],
    [7,3,4],
    #Outer Right
    [0,1,4],
    [5,1,4],
    #Outer Back
    [1,2,5],
    [6,2,5],
    #Outer Left
    [2,3,6],
    [7,3,6],
    #These are trapezoids
    #Lip Front
    [4,7,12],
    [15,7,12],
    #Lip Right
    [4,5,12],
    [13,5,12],
    #Lip Back
    [5,6,13],
    [14,6,13],
    #Lip Left
    [6,7,14],
    [15,7,14],
    #Mid Front
    [12,15,16],
    [19,15,16],
    #Mid Right
    [12,13,16],
    [17,13,16],
    #Mid Back
    [13,14,17],
    [18,14,17],
    #Mid Left
    [14,15,18],
    [19,15,18],
    #Inner Bottom
    [8,9,10],
    [8,11,10],
    #Lip Top Front
    [16,19,20],
    [23,19,20],
    #Lip Top Right
    [16,17,20],
    [21,17,20],
    #Lip Top Back
    [17,18,21],
    [22,18,21],
    #Lip Top Left
    [18,19,22],
    [23,19,22],
    #Inner Front
    [8,11,20],
    [23,11,20],
    #Inner Right
    [8,9,20],
    [21,9,20],
    #Inner Back
    [9,10,21],
    [22,10,21],
    #Inner Left
    [10,11,22],
    [23,11,22],

    ])

    top = mesh.Mesh(np.zeros(faces_top.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces_top):
        for j in range(3):
            top.vectors[i][j] = vertices_top[f[j],:]
    top.save(Name+'_Top.stl')

def make_par_rect(x,y,z):
    vertices = np.array([\
    [0,0,0],
    [0,0,z],
    [0,y,0],
    [0,y,z],
    [x,0,0],
    [x,0,z],
    [x,y,0],
    [x,y,z],
    
    
    ])

    faces = np.array([\
    #Back
    [0,1,2],
    [3,1,2],
    #Bottom
    [0,2,4],
    [6,2,4],
    #Left
    [0,1,4],
    [5,1,4],
    #Front
    [4,5,6],
    [7,5,6],
    #Top
    [1,3,5],
    [7,3,5],
    #Right
    [2,3,6],
    [7,3,6]


    ])

    cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            cube.vectors[i][j] = vertices[f[j],:]
    cube.save('cube1.stl')

#make_par_rect(5,10,15)
make_box("hey",20,20,40,2,2,2,80)
