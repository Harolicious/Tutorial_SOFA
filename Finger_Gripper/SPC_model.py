import Sofa
import Sofa.Core
import math
import os
import numpy as np

path = os.path.dirname(os.path.abspath(__file__))+'/mesh/'

Pa_max = 300   # 30 kPa (máximo)

def createScene(rootNode):

    rootNode.addObject(
        "RequiredPlugin",
        pluginName="""SofaPython3
        SoftRobots
        SoftRobots.Inverse
        Sofa.Component.AnimationLoop
        Sofa.Component.Constraint.Lagrangian.Correction
        Sofa.Component.Constraint.Lagrangian.Solver
        Sofa.Component.Engine.Select
        Sofa.Component.IO.Mesh
        Sofa.Component.LinearSolver.Direct
        Sofa.Component.LinearSolver.Iterative
        Sofa.Component.Mapping.Linear
        Sofa.Component.Mapping.MappedMatrix
        Sofa.Component.Mapping.NonLinear
        Sofa.Component.Mass
        Sofa.Component.ODESolver.Backward
        Sofa.Component.Setting
        Sofa.Component.SolidMechanics.FEM.Elastic
        Sofa.Component.SolidMechanics.Spring
        Sofa.Component.StateContainer
        Sofa.Component.Topology.Container.Constant
        Sofa.Component.Topology.Container.Dynamic
        Sofa.Component.Topology.Mapping
        Sofa.Component.Visual
        Sofa.GL.Component.Rendering3D
        Sofa.GL.Component.Shader"""
    )

    rootNode.addObject("VisualStyle", displayFlags="showBehaviorModels showForceFields")
    rootNode.addObject('FreeMotionAnimationLoop')
    rootNode.addObject('GenericConstraintSolver', maxIterations=100, tolerance=1e-7)

    rootNode.dt = 0.1

    gripper = rootNode.addChild('gripper')

    gripper.addObject('EulerImplicitSolver', name='odesolver')
    gripper.addObject('SparseLDLSolver', name='preconditioner')

    gripper.addObject('ShewchukPCGLinearSolver',
                      name='linearsolver',
                      iterations=100,
                      tolerance=1e-5,
                      preconditioners='preconditioner',
                      use_precond=True,
                      update_step=1)

    gripper.addObject('MeshVTKLoader', name='loader', filename='dedo_v2.vtk')
    gripper.addObject('TetrahedronSetTopologyContainer', src='@loader', name='container')
    gripper.addObject('TetrahedronSetTopologyModifier')

    gripper.addObject('MechanicalObject', name='tetras', template='Vec3')
    gripper.addObject('UniformMass', totalMass=0.5)

    gripper.addObject('TetrahedronFEMForceField',
                      name='FEM',
                      method='large',
                      poissonRatio=0.4,
                      youngModulus=10000)

    gripper.addObject('BoxROI',
                      name='boxROI',
                      box=[70, 80, 0, 150, 260, 200],
                      drawBoxes=True,
                      position="@tetras.rest_position",
                      tetrahedra="@container.tetrahedra")

    gripper.addObject('RestShapeSpringsForceField',
                      points='@boxROI.indices',
                      stiffness=1e12)

    gripper.addObject('GenericConstraintCorrection',
                      linearSolver='@preconditioner')

    cavity = gripper.addChild('cavity')

    cavity.addObject('MeshSTLLoader', name='loader', filename='alma_h.stl')
    cavity.addObject('MeshTopology', src='@loader', name='topo')
    cavity.addObject('MechanicalObject', name='cavity')

    cavity.addObject('SurfacePressureConstraint',
                     name='pressure',
                     triangles='@topo.triangles',
                     value=Pa_max,
                     valueType=0)

    cavity.addObject('BarycentricMapping',
                     name='mapping',
                     mapForces=True,
                     mapMasses=True)

    gripperVisu = gripper.addChild('visu')
    gripperVisu.addObject("MeshSTLLoader", filename="dedo_h_visu.stl", name="loader")
    gripperVisu.addObject("OglModel", src="@loader")
    gripperVisu.addObject("BarycentricMapping")



    return rootNode