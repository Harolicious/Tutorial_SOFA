import Sofa

import os
import numpy as np
path = os.path.dirname(os.path.abspath(__file__))+'/mesh/'

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
                    Sofa.Component.Visual
                    Sofa.GL.Component.Rendering3D
                    Sofa.GL.Component.Shader"""
                )
                
                rootNode.addObject(
                    "VisualStyle",
                    displayFlags="""
                        hideWireframe
                        showBehaviorModels
                        hideCollisionModels
                        hideBoundingCollisionModels
                        showForceFields
                        showInteractionForceFields""",
                )
                # rootNode.addObject('VisualStyle', displayFlags='showVisualModels hideBehaviorModels showCollisionModels hideBoundingCollisionModels showForceFields showInteractionForceFields hideWireframe')

                rootNode.addObject('RequiredPlugin', name='Sofa.Component.Topology.Mapping') # Needed to use components [Tetra2TriangleTopologicalMapping]
                rootNode.addObject('FreeMotionAnimationLoop')
                rootNode.addObject('GenericConstraintSolver', maxIterations=100, tolerance = 0.0000001)
                rootNode.dt = 0.1

		#gripper
                gripper = rootNode.addChild('gripper')
                gripper.addObject('EulerImplicitSolver', name='odesolver')
                
                gripper.addObject('SparseLDLSolver', name='preconditioner')

                gripper.addObject('ShewchukPCGLinearSolver', iterations=15, name='linearsolver', tolerance=1e-5, preconditioners='preconditioner', use_precond=True, update_step=1)

                gripper.addObject('MeshVTKLoader', name='loader', filename='A.vtk')
                gripper.addObject('TetrahedronSetTopologyContainer', src='@loader', name='container')
                gripper.addObject('TetrahedronSetTopologyModifier')

                gripper.addObject('MechanicalObject', name='tetras', template='Vec3', showIndices=False)
                gripper.addObject('UniformMass', totalMass=0.5)
                
    
                gripper.addObject('TetrahedronFEMForceField', template='Vec3', name='FEM', method='large', poissonRatio=0.4,  youngModulus=1000000)

                gripper.addObject('BoxROI', name='boxROI', box=[20, 20, 50,  -20, -20, 35], drawBoxes=True, position="@tetras.rest_position", tetrahedra="@container.tetrahedra")
                gripper.addObject('RestShapeSpringsForceField', points='@boxROI.indices', stiffness=1e12)
                gripper.addObject('GenericConstraintCorrection', linearSolver='@preconditioner')

                              
                
		#gripper/cavity
                
        
                cavity = gripper.addChild('cavity')
                cavity.addObject('MeshSTLLoader', name='loader', filename='B.stl')
                cavity.addObject('MeshTopology', src='@loader', name='topo')
                cavity.addObject('MechanicalObject', name='cavity')
                cavity.addObject('SurfacePressureConstraint', triangles='@topo.triangles', value=-1600, valueType=0)
                cavity.addObject('BarycentricMapping', name='mapping',  mapForces=True, mapMasses=True)


		#gripper/gripperVisu
                gripperVisu = gripper.addChild('visu')
                gripperVisu.addObject("MeshSTLLoader", filename="A_visu.stl", name="loader")
                gripperVisu.addObject("OglModel", src="@loader")
                gripperVisu.addObject("BarycentricMapping")


                return rootNode
