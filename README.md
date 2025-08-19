# Descargar SOFA v23.06.00

Para poder descargar la version de SOFA que utilizaremos deben ir a https://github.com/sofa-framework/sofa/releases/tag/v23.06.00 y descargar `SOFA_v23.06.00_Win64.exe` o tambien pueden hacer clic [aqui](https://github.com/sofa-framework/sofa/releases/download/v23.06.00/SOFA_v23.06.00_Win64.exe)

Deben tener en consideracion lo siguiente:

1. Instalar Microsoft Visual C++ 2019 Redistributable.
2. Instalar Python 3.8 + Numpy + Scipy debido a que se requiere utilizar un plugin SofaPython3.
   - Descargar e instalar Python 3.8 (amd64).
   - Asegúrate de habilitar la instalación de PIP y añadirla a PATH.
   - Luego, abre una consola y ejecuta python -V && python -m pip install numpy scipy.
   - Tambien es necesario que instales gmsh python -m pip install gmsh

<img width="500" height="390" alt="image" src="https://github.com/user-attachments/assets/69163191-bacb-45e2-90b9-3a5946abcfde" />

# Inicializacion de SOFA

Ejecutar el programa llamado `runSofa`. Se abrirá la consola y luego el programa 

<img width="1350" height="728" alt="image" src="https://github.com/user-attachments/assets/61aad2cb-9c98-4fea-af13-418c771e70de" />

- Al presionar `barra de espacio` se debiera ejecutar la DEMO y la serpiente debiera empezar a rebotar. 
- Si presiona nuevamente `barra de espacio` la simulación se debiera pausar.
- Si presiona `Ctrl + R`, la DEMO se reinicia.
- Si se mantiene presionado `Shift` y luego sobre la serpiente se presiona y se mantiene el `clic izquierdo` se puede interactuar con la serpiente.

<img width="1098" height="671" alt="image" src="https://github.com/user-attachments/assets/e139587b-5283-409d-ba38-7940f0a3d476" />

# Plugins SofaPython3

Deben ir a `Edit` > `Plugin Manager`

<img width="1098" height="671" alt="image" src="https://github.com/user-attachments/assets/2ac26547-50f5-4122-95f7-a4b68c94a7b7" />

Se debiera abrir la siguiente ventana:

<img width="803" height="434" alt="image" src="https://github.com/user-attachments/assets/57166cad-7e30-4d2b-88fc-57b363fa2b97" />

Aqui deberán hacer clic en `add` y se les abrirá otra ventana emergente

<img width="534" height="112" alt="image" src="https://github.com/user-attachments/assets/767e41b5-7e04-4349-b87d-954ab72303bc" />

Se regresan a la carpeta `SOFA_v23.06.00_Win64` y van a la carpeta `Plugins` > `SofaPython3` > `bin` y seleccionan el archivo `SofaPython3.dll`

<img width="533" height="247" alt="image" src="https://github.com/user-attachments/assets/98faa5aa-7eb5-476a-b8eb-3545feaa28f8" />

Al seleccionar el dll, debiera actualizarse el listado de los plugins y al final de esta lista debiera estar `SofaPython3.dll`

<img width="800" height="74" alt="image" src="https://github.com/user-attachments/assets/4d576d7b-2a6f-4d51-b1d5-d8d56c9482a3" />

# GenerateMesh

En la carpeta `Modelo_SPC` se encuentra el archivo `generateMeshes` el cual toma los archivos .step y los transforma en formato .vtk y .stl.


# Modelo SPC

Abrimos el archivo `SPC_model`



