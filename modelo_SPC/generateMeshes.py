
import gmsh

gmsh.initialize()

gmsh.merge("Parte_A.STEP")

gmsh.model.mesh.generate(3)
gmsh.model.mesh.refine()
gmsh.write("PARTE_A.vtk")
gmsh.fltk.run()

gmsh.clear()

gmsh.merge("Parte_B.step")

gmsh.model.mesh.generate(2)
gmsh.model.mesh.refine()

# gmsh.model.mesh.refine()
gmsh.write("PARTE_B.stl")
gmsh.fltk.run()
