# Mesh Node Index Helper

The goal of this small python script is to help you find the index of nodes in a given vtk file consisting only of a tetrahedrical mesh, the nodes being in specified areas defined through command line args.
Use-case is limited to beam-like meshes and to gather node indexes within three areas, defined by the gap and square_width parameters.

<u>Example<u>:

```
python find_nodes_index.py data/test.vtk gap square_width
```
First argument, ```data/test.vtk``` is the .vtk file name.
Second argument, ```gap``` is the gap between longitudinal edge of the object and center of first researched nodes area.
Third argument, ```square_width``` is the square area side length.
