# Instalacion Git
Lo primero que debemos hacer es la instacion de `git` para ello pueden ir a https://git-scm.com/downloads y descargar la ultima version o tambien pueden hacer clic [Aqui](https://github.com/git-for-windows/git/releases/download/v2.51.0.windows.1/Git-2.51.0-64-bit.exe).

Para seguir los pasos de instalación se recomienda utilizar el siguiente archivo
[Instalacion_Git.pdf](https://github.com/user-attachments/files/21926400/Instalacion_Git.pdf)

# Instalacion python 3.8.10

Instalen python 3.8.10 https://www.python.org/downloads/release/python-3810/ o hagan clic [aquí](https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe) Windowsx64 

1. Instalar Microsoft Visual C++ 2019 Redistributable. (es posible que no lo tengan)
2. Instalar Python 3.8.10 
   - Descargar e instalar Python 3.8.10  (amd64).
   - Check en `Add Python 3.8.10 to PATH`. !
   
<img width=600 alt="image" src="https://github.com/user-attachments/assets/705e78f4-cb5c-4e71-b8cc-84a232620764" />


# Gitclone

Ejecuta el programa GitBash, se debiera abrir una ventana como lo siguiente.

<img width=600 alt="image" src="https://github.com/user-attachments/assets/fe1666aa-4247-4ea9-8ff9-b8777dfe13b9" />

Aqui se deberá ingresar los siguientes codigos:
1. `cd \Desktop` Crea la carpeta en el escritorio, pueden elegir cualquier otra
2. `git clone https://github.com/Harolicious/Tutorial_SOFA.git` Clona la carpeta del git al escritorio 
3. `cd Tutorial_SOFA/` 

<img width=600 alt="image" src="https://github.com/user-attachments/assets/eb09e6a7-6345-4475-966d-b200a7f132bc" />

4. ` pip install -r requirements.txt` Con esto se instalaran las versiones necesarias para Numpy, Scipy y Gmsh. 
Numpy y Scipy son necesarios para utilizar el plugin SofaPython3. Gmsh es un generador de mallas de elementos finitos 3D.

<img width=600 alt="image" src="https://github.com/user-attachments/assets/3ca035b4-53a7-4514-8420-8399c84f66d3" />

# Spyder-IDE

Pueden utilizar cualquier editor de código o entorno de desarrollo de su preferencia. En mi caso trabajaré con [Spyder-IDE](https://www.spyder-ide.org/).
Al abrir Spyder, pueden observar en la terminal 1/A que tiene una version de python diferente a la instalada previamente. Para ello debemos cambiar el interprete de python.
Vayan a `Herramientas` > `Preferencias` > `Interprete de Python` Aqui la seleccionada es la interna de Spyder

<img width=600 alt="image" src="https://github.com/user-attachments/assets/45482472-d1ce-4b5d-9d58-fa8c50bc23f0" />

En GitBash ejecuten el codigo `which python` y les debiera dar la direccion donde esta el python instalado. 

<img width=600 alt="image" src="https://github.com/user-attachments/assets/073d4284-cf51-4d8f-9b7e-68ffcfa6cc94" />

En spyder deben elegir `Usar el siguiente interprete`, despues clic en la carpeta, busquen con la dirección entregada en GitBash y seleccione python.exe

<img width=600 alt="image" src="https://github.com/user-attachments/assets/8cbf7ea1-2d31-45ba-90b6-4ea52e88cd91" />

<img width=600 alt="image" src="https://github.com/user-attachments/assets/06a4967d-8e8d-4346-bdc3-c747fcbb8b57" />

En Terminal 1/A le das clic derecho y le das reiniciar el nucleo. 

<img width=600 alt="image" src="https://github.com/user-attachments/assets/2b15e30e-bc1f-4343-9b53-d5ba6cc21572" />

Si te da un error, tranqui! lo más seguro es que te falte instalar algo más. Si no te dio problemas Parabienes!

<img width=600 alt="image" src="https://github.com/user-attachments/assets/77bbbd1d-0783-422a-9a31-1a2049e6e3d8" />

En GitBash ejecuta el codigo `pip install spyder-kernels==3.0.*` (esto instalará la última versión disponible 3.0.x) 

<img width=600 alt="image" src="https://github.com/user-attachments/assets/ba6b3121-a3a6-457a-99ff-f346abf871c0" />

Regresamos a Spyder y en la Terminal 1/A le das clic derecho y le das reiniciar el nucleo 

<img width=600 alt="image" src="https://github.com/user-attachments/assets/5affd7cf-90aa-41e2-8308-cc91fc5eb9f5" />

Con esto ya estaría todo listo!

Pueden en la terminal escribir `import gmsh` y si no pasa nada es porque esta todo bien! Si escriben `print(gmsh.__version__)` les debiera salir la version `4.12.2`

# Descarga e Inicio de SOFA v23.06.00

Para poder descargar la version de SOFA que utilizaremos deben ir a https://github.com/sofa-framework/sofa/releases/tag/v23.06.00 y descargar `SOFA_v23.06.00_Win64.exe` o tambien pueden hacer clic [aqui](https://github.com/sofa-framework/sofa/releases/download/v23.06.00/SOFA_v23.06.00_Win64.exe)

<img width=600 alt="image" align="center" src="https://github.com/user-attachments/assets/69163191-bacb-45e2-90b9-3a5946abcfde" />

Ejecutar el programa llamado `runSofa`. Se abrirá la consola y luego el programa 

<img width=600 alt="image" align="center" src="https://github.com/user-attachments/assets/61aad2cb-9c98-4fea-af13-418c771e70de" />

- Al presionar `barra de espacio` se debiera ejecutar la DEMO y la serpiente debiera empezar a rebotar. 
- Si presiona nuevamente `barra de espacio` la simulación se debiera pausar.
- Si presiona `Ctrl + R`, la DEMO se reinicia.
- Si se mantiene presionado `Shift` y luego sobre la serpiente se presiona y se mantiene el `clic izquierdo` se puede interactuar con la serpiente.

<img width=600 alt="image" align="center" src="https://github.com/user-attachments/assets/e139587b-5283-409d-ba38-7940f0a3d476" />

# Plugins SofaPython3

Deben ir a `Edit` > `Plugin Manager`

<img width=600 alt="image" align="center" src="https://github.com/user-attachments/assets/2ac26547-50f5-4122-95f7-a4b68c94a7b7" />

Se debiera abrir la siguiente ventana:

<img width=600 alt="image" align="center" src="https://github.com/user-attachments/assets/57166cad-7e30-4d2b-88fc-57b363fa2b97" />

Aqui deberán hacer clic en `add` y se les abrirá otra ventana emergente

<img width=600  alt="image" align="center" src="https://github.com/user-attachments/assets/767e41b5-7e04-4349-b87d-954ab72303bc" />

Se regresan a la carpeta `SOFA_v23.06.00_Win64` y van a la carpeta `Plugins` > `SofaPython3` > `bin` y seleccionan el archivo `SofaPython3.dll`

<img width=600  alt="image" align="center" src="https://github.com/user-attachments/assets/98faa5aa-7eb5-476a-b8eb-3545feaa28f8" />

Al seleccionar el dll, debiera actualizarse el listado de los plugins y al final de esta lista debiera estar `SofaPython3.dll`

<img width=600  alt="image" src="https://github.com/user-attachments/assets/4d576d7b-2a6f-4d51-b1d5-d8d56c9482a3" />

# GenerateMesh

En la carpeta `Finger_gripper` se encuentra el archivo `generateMeshes` el cual toma los archivos .step y los transforma en formato .vtk y .stl.
Para este ejemplo, se utilizó uno de los proyectos de jammin gripper. El archivo A.STEP corresponde a la estructura de silicona y el archivo B.STEP corresponde a la cavidad interna del gripper. 

## Dedo_h.STEP
<img width=600 alt="image" src="https://github.com/user-attachments/assets/f7353046-0a9c-4f19-8033-1e4dcd87a3a5" />

## Alma_h.STEP
<img width=600 alt="image" src="https://github.com/user-attachments/assets/7902d0af-7068-43db-aabd-768929f751b2" />

## Carcasa
<img width=600 alt="image" src="https://github.com/user-attachments/assets/739b2155-c701-4eb1-a440-deb96964642f" />

Al cerrar las ventanas emergentes de gmsh, podemos observar que en la carpeta, se han generado 3 archivos nuevos. 
- A.vtk que es el modelo 3D de la silicona 
- B.stl que es el modelo 3D de la cavidad de aire 
- A.stl que es el modelo 2D de la silicona, que se usa solo por fines esteticos.

# Modelo SPC

Desde acá pueden abrir el archivo `SPC_model` en el programa `runSofa`. Si todo salio como debiera, ya pueden ejecutar la simulación del gripper y pueden observar su comportamiento.
Si quisieran realizar modificaciones e ir probando cambios en la simulacion, pueden abrir el archivo `SPC_model` en su editor de codigo favorito. Aqui esta toda la programación del gripper en SOFA.

<img width=600 alt="ezgif-12b1a981d5af3101" src="https://github.com/user-attachments/assets/4b51c3a9-9643-4047-b022-acdd46c9d071" />
