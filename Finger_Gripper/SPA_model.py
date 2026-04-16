import Sofa
import Sofa.Core
import math
import os
import numpy as np

path = os.path.dirname(os.path.abspath(__file__))+'/mesh/'

Pa_max = 30000

class PressureController(Sofa.Core.Controller):

    def __init__(self, node, **kwargs):
        super().__init__(**kwargs)
        
        self.RootNode = kwargs['RootNode']
        self.SPA = kwargs['SPA']
        self.Maxpressure = Pa_max
        self.Increment = 1000
        self.Pressure = 0        
        self.Decreasing = False
        self.animation_finished = False 

    def update_pressure_increase(self, pressure, SPA):
        pressure += self.Increment
        if pressure > self.Maxpressure and self.animation_finished==False:
            pressure = self.Maxpressure
        SPA.value.value = [pressure]
        return pressure

    def update_pressure_decrease(self, pressure, SPA):
        pressure -= self.Increment
        if pressure < 0 and not self.animation_finished:
            pressure = 0
        SPA.value.value = [pressure]
        return pressure

        
    def onAnimateBeginEvent(self, eventType):
        
            
        # Imprimir mensaje si la animación ha terminado
        if self.animation_finished:
            self.RootNode.dt = 0 
            self.Pressure = 0
            return

        if not self.Decreasing:
            # Incrementar presiones
            self.Pressure = self.update_pressure_increase(self.Pressure, self.SPA)
            
            if self.Pressure >= self.Maxpressure:
                self.Decreasing = True  
        else:
            # Decrementar presiones
            self.Pressure = self.update_pressure_decrease(self.Pressure, self.SPA)
            
            if self.Pressure <= 0:
                self.Decreasing = False  
                self.animation_finished = True

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
            rootNode.addObject("QPInverseProblemSolver", printLog=1, epsilon=0.1, maxIterations=1000,tolerance=1e-5)
        
            rootNode.dt = 0.1
        
            gripper = rootNode.addChild('gripper')
        
            gripper.addObject('EulerImplicitSolver', name='odesolver')
            gripper.addObject('SparseLDLSolver', name='preconditioner',template='CompressedRowSparseMatrixMat3x3d')
        
            gripper.addObject('ShewchukPCGLinearSolver',
                              name='linearsolver',
                              iterations=15,
                              tolerance=1e-5,
                              preconditioners='@preconditioner',
                              use_precond=True)
        
            Loader = gripper.addObject('MeshVTKLoader', name='loader', filename='dedo_v2.vtk')
            Container = gripper.addObject('TetrahedronSetTopologyContainer', src='@loader', name='container',
                                          createTriangleArray=True)
            gripper.addObject('TetrahedronSetTopologyModifier')
        
            MO = gripper.addObject('MechanicalObject', name='tetras', template='Vec3')
            gripper.addObject('UniformMass', totalMass=0.5)
        
            boxROIStiffness = gripper.addObject('BoxROI', 
                                               name='boxROIStiffness', 
                                               box=[150, 210, 0, 730, 260, 200], 
                                               drawBoxes=True, 
                                               position="@tetras.rest_position", 
                                               tetrahedra="@container.tetrahedra")
            Container.init()
            MO.init()
            boxROIStiffness.init()

            YM1 = 10000  #cuerpo blando 
            YM2 = 1000000  #lamina rigida
            YMArray = np.ones(len(Loader.tetras))*YM1
            IdxElementsInROI = np.array(boxROIStiffness.tetrahedronIndices.value)
            YMArray[IdxElementsInROI] = YM2        
        
        
            gripper.addObject('TetrahedronFEMForceField', 
                              template='Vec3', 
                              name='FEM_stiffness', 
                              method='large', 
                              poissonRatio=0.3,  
                              youngModulus=YM2)
        
                
            gripper.addObject('TetrahedronFEMForceField',
                              name='FEM',
                              method='large',
                              poissonRatio=0.4,
                              youngModulus=YM1)
        
        
            gripper.addObject('BoxROI',
                              name='boxROI',
                              box=[70, 80, 0, 150, 260, 200],
                              drawBoxes=True,
                              position="@tetras.rest_position",
                              tetrahedra="@container.tetrahedra")
        
            gripper.addObject('RestShapeSpringsForceField',
                              points='@boxROI.indices',
                              stiffness=1e12)
            gripper.addObject('GenericConstraintCorrection', linearSolver='@preconditioner')
        
        
        
            cavity = gripper.addChild('cavity')
        
            cavity.addObject('MeshSTLLoader', name='loader', filename='alma_h.stl')
            cavity.addObject('MeshTopology', src='@loader', name='topo')
            cavity.addObject('MechanicalObject', name='cavity')
        
            SPA=cavity.addObject('SurfacePressureActuator',
                             name='pressure',
                             triangles='@topo.triangles')
        
            cavity.addObject('BarycentricMapping',
                             mapForces=True,
                             mapMasses=True)
        
        
            gripperVisu = gripper.addChild('visu')
            gripperVisu.addObject("MeshSTLLoader", filename="dedo_h_visu.stl", name="loader")
            gripperVisu.addObject("OglModel", src="@loader")
            gripperVisu.addObject("BarycentricMapping")
            
            rootNode.addObject(PressureController(name="ActuationController",RootNode=rootNode,SPA=SPA))        
            
            return rootNode