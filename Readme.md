# Proyecto: Funciones de Activación en Python

Este proyecto implementa y grafica varias funciones de activación utilizadas en redes neuronales, junto con sus respectivas derivadas. Está estructurado para facilitar su uso y expansión en proyectos de aprendizaje automático.

## Estructura del Proyecto
```
- src/
  - linear.py        # Función de activación lineal
  - relu.py          # Función ReLU (Rectified Linear Unit)
  - sigmoid.py       # Función Sigmoide
  - sign.py          # Función Signo
  - step.py          # Función Escalón (Step)
  - tanh.py          # Función Tangente Hiperbólica
- main.py            # Script principal que ejecuta las funciones y genera gráficos
- Readme.md          # Documentación del proyecto
- .gitignore         # Archivos a ignorar por Git
- Requirements.txt   # Dependencias necesarias para ejecutar el proyecto
```

## Instalación y Uso
### 1. Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

### 2. Instalar Dependencias
Se recomienda el uso de un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r Requirements.txt
```

### 3. Ejecutar el Proyecto
```bash
python main.py
```
Esto generará y mostrará gráficos de las funciones de activación y sus derivadas.

## Descripción de los Archivos
### - `main.py`
   - Llama a las funciones de activación y grafica sus resultados.
   - Utiliza `matplotlib` para visualizar las funciones.

### - `src/`
   - Contiene implementaciones individuales de cada función de activación.
   - Cada archivo define la función junto con su derivada.

## Funciones de Activación Implementadas
1. **Sigmoide**: Suaviza la salida entre 0 y 1, útil en clasificación binaria.
2. **ReLU**: Activa valores positivos y bloquea los negativos, popular en redes profundas.
3. **Tangente Hiperbólica**: Mapea valores entre -1 y 1, similar a Sigmoide.
4. **Signo**: Devuelve -1, 0 o 1 según el signo de la entrada.
5. **Escalón**: Función discontinua que devuelve 1 para valores positivos y 0 para negativos.
6. **Lineal**: Retorna el mismo valor de entrada, útil en regresión.

## Requisitos
El archivo `Requirements.txt` lista las dependencias necesarias:
```
numpy
matplotlib
```