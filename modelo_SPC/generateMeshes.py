
import gmsh

gmsh.initialize()

gmsh.merge("A.STEP")

gmsh.model.mesh.generate(3)
gmsh.write("A.vtk")
gmsh.fltk.run()
gmsh.clear()

gmsh.merge("B.step")

gmsh.model.mesh.generate(2)
gmsh.write("B.stl")
gmsh.fltk.run()
gmsh.clear()

gmsh.merge("A.STEP")

gmsh.model.mesh.generate(2)
gmsh.model.mesh.refine()
gmsh.model.mesh.refine()
gmsh.write("A_visu.stl")
gmsh.fltk.run()
gmsh.clear()
