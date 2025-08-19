# Descargar SOFA v23.06.00

Para poder descargar la version de SOFA que utilizaremos deben ir a https://github.com/sofa-framework/sofa/releases/tag/v23.06.00 y descargar `SOFA_v23.06.00_Win64.exe` o tambien pueden hacer clic [aqui](https://github.com/sofa-framework/sofa/releases/download/v23.06.00/SOFA_v23.06.00_Win64.exe)

Deben tener en consideracion lo siguiente:

1. Instalar Microsoft Visual C++ 2019 Redistributable.
2. Instalar Python 3.8 + Numpy + Scipy debido a que se requiere utilizar un plugin SofaPython3.
   - Descargar e instalar Python 3.8 (amd64).
   - Asegúrate de habilitar la instalación de PIP y añadirla a PATH.
   - Luego, abre una consola y ejecuta python -V && python -m pip install numpy scipy.

<img width="500" height="390" alt="image" src="https://github.com/user-attachments/assets/69163191-bacb-45e2-90b9-3a5946abcfde" />

# Inicializacion de SOFA

Ejecutar el programa llamado `runSofa`. Se abrirá la consola y luego el programa 

<img width="1350" height="728" alt="image" src="https://github.com/user-attachments/assets/61aad2cb-9c98-4fea-af13-418c771e70de" />

- Al presionar `barra de espacio` se debiera ejecutar la DEMO y la serpiente debiera empezar a rebotar. 
- Si presiona nuevamente `barra de espacio` la simulacion se debiera pausar.
- Si presiona `Ctrl + R`, la DEMO se reinicia.
- Si se mantiene presionado `Shift` y luego sobre la serpiente se presiona y se mantiene el `clic izquierdo` se puede interactuar con la serpiente

<img width="1098" height="671" alt="image" src="https://github.com/user-attachments/assets/e139587b-5283-409d-ba38-7940f0a3d476" />

# Plugins SofaPython3

Deben ir a `Edit` > `Plugin Manager`

<img width="1098" height="671" alt="image" src="https://github.com/user-attachments/assets/2ac26547-50f5-4122-95f7-a4b68c94a7b7" />

Se debiera abrir la siguiente ventana

<img width="803" height="434" alt="image" src="https://github.com/user-attachments/assets/57166cad-7e30-4d2b-88fc-57b363fa2b97" />

Aqui deberán hacer clic 
