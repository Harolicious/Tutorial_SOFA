
import gmsh

gmsh.initialize()

gmsh.merge("dedo_h.STEP")

gmsh.model.mesh.generate(3)
# gmsh.model.mesh.refine()
gmsh.write("dedo_v2.vtk")
gmsh.fltk.run()
gmsh.clear()

gmsh.merge("alma_h.STEP")

gmsh.model.mesh.generate(3)
# gmsh.model.mesh.refine()
gmsh.write("alma_h.stl")
gmsh.fltk.run()
gmsh.clear()

gmsh.merge("dedo_h.STEP")

gmsh.model.mesh.generate(2)
# gmsh.model.mesh.refine()
gmsh.write("dedo_h_visu.stl")
gmsh.fltk.run()
gmsh.clear()

gmsh.finalize()