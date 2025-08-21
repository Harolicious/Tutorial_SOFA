# Instalacion Git
Lo primero que debemos hacer es la instacion de `git` para ello pueden ir a https://git-scm.com/downloads y descargar la ultima version.


`git clone https://github.com/Harolicious/Tutorial_SOFA`

# Descargar SOFA v23.06.00

Para poder descargar la version de SOFA que utilizaremos deben ir a https://github.com/sofa-framework/sofa/releases/tag/v23.06.00 y descargar `SOFA_v23.06.00_Win64.exe` o tambien pueden hacer clic [aqui](https://github.com/sofa-framework/sofa/releases/download/v23.06.00/SOFA_v23.06.00_Win64.exe)

Deben tener en consideracion lo siguiente:

1. Instalar Microsoft Visual C++ 2019 Redistributable.
2. Instalar Python 3.8 + Numpy + Scipy debido a que se requiere utilizar un plugin SofaPython3.
   - Descargar e instalar Python 3.8 (amd64).
   - Asegúrate de habilitar la instalación de PIP y añadirla a PATH.
   - Luego, abre una consola y ejecuta python -V && python -m pip install numpy scipy.
   - Tambien es necesario que instales gmsh python -m pip install gmsh

<img width="500" height="390" alt="image" align="center" src="https://github.com/user-attachments/assets/69163191-bacb-45e2-90b9-3a5946abcfde" />

# Inicializacion de SOFA

Ejecutar el programa llamado `runSofa`. Se abrirá la consola y luego el programa 

<img width="510" alt="image" align="center" src="https://github.com/user-attachments/assets/61aad2cb-9c98-4fea-af13-418c771e70de" />

- Al presionar `barra de espacio` se debiera ejecutar la DEMO y la serpiente debiera empezar a rebotar. 
- Si presiona nuevamente `barra de espacio` la simulación se debiera pausar.
- Si presiona `Ctrl + R`, la DEMO se reinicia.
- Si se mantiene presionado `Shift` y luego sobre la serpiente se presiona y se mantiene el `clic izquierdo` se puede interactuar con la serpiente.

<img width="500" alt="image" align="center" src="https://github.com/user-attachments/assets/e139587b-5283-409d-ba38-7940f0a3d476" />

# Plugins SofaPython3

Deben ir a `Edit` > `Plugin Manager`

<img width="500" alt="image" align="center" src="https://github.com/user-attachments/assets/2ac26547-50f5-4122-95f7-a4b68c94a7b7" />

Se debiera abrir la siguiente ventana:

<img width="500" alt="image" align="center" src="https://github.com/user-attachments/assets/57166cad-7e30-4d2b-88fc-57b363fa2b97" />

Aqui deberán hacer clic en `add` y se les abrirá otra ventana emergente

<img width="500"  alt="image" align="center" src="https://github.com/user-attachments/assets/767e41b5-7e04-4349-b87d-954ab72303bc" />

Se regresan a la carpeta `SOFA_v23.06.00_Win64` y van a la carpeta `Plugins` > `SofaPython3` > `bin` y seleccionan el archivo `SofaPython3.dll`

<img width="500"  alt="image" align="center" src="https://github.com/user-attachments/assets/98faa5aa-7eb5-476a-b8eb-3545feaa28f8" />

Al seleccionar el dll, debiera actualizarse el listado de los plugins y al final de esta lista debiera estar `SofaPython3.dll`

<img width="600"  alt="image" src="https://github.com/user-attachments/assets/4d576d7b-2a6f-4d51-b1d5-d8d56c9482a3" />

# GenerateMesh

En la carpeta `Modelo_SPC` se encuentra el archivo `generateMeshes` el cual toma los archivos .step y los transforma en formato .vtk y .stl.
Para este ejemplo, se utilizó uno de los proyectos de jammin gripper. El archivo A.STEP corresponde a la estructura de silicona y el archivo B.STEP corresponde a la cavidad interna del gripper. 

## A.STEP
<img width="500" alt="image" align="center" src="https://github.com/user-attachments/assets/0dee13e3-5f30-47fa-8cde-33d70faf2fc5" />

## B.STEP
<img width="500" alt="image" align="center" src="https://github.com/user-attachments/assets/57df0fc6-b0ad-44c8-afc1-bbd061d9cda2" />

Al cerrar las ventanas emergentes de gmsh, podemos observar que en la carpeta, se han generado 3 archivos nuevos. 
- A.vtk que es el modelo 3D de la silicona 
- B.stl que es el modelo 2D de la cavidad de aire 
- A.stl que es el modelo 2D de la silicona, que se usa solo por fines esteticos.

# Modelo SPC

Desde acá pueden abrir el archivo `SPC_model` en el programa `runSofa`. Si todo salio como debiera, ya pueden ejecutar la simulación del gripper y pueden observar su comportamiento.
Si quisieran realizar modificaciones e ir probando cambios en la simulacion, pueden abrir el archivo `SPC_model` en su editor de codigo favorito. Aqui esta toda la programación del gripper en SOFA.


<img align="center" width="700" height="597" alt="image" src="https://github.com/user-attachments/assets/a49055fc-43cc-4f28-9fb4-50b5da89c848" />
<img width="250" height="599" alt="image" src="https://github.com/user-attachments/assets/b5d4adb2-f88d-4b18-910a-db8a2fd47a7b" />
<img width="250" height="599" alt="image" src="https://github.com/user-attachments/assets/82f71598-1ec5-408a-8022-6597524b487f" />
<img width="250" height="598" alt="image" src="https://github.com/user-attachments/assets/c09c5ca0-4c7b-46e7-955c-b79f8d47d5aa" />





