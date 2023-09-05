# K-Net95-Alzheimer
El proyecto denominado "Implementación de un modelo predictivo basado en redes neuronales convolucionales 3D en el paso de deterioro cognitivo leve a Alzheimer sobre imágenes por resonancia magnética" muestra una estructura de red neuronal convolucional 3D cuyo objetivo es servir como apoyo médico en la detección temprana del Alzheimer.

Esta fue una tesis realizada con el fin de desarrollar nuevas técnicas que sirvan para la detección de enfermedades neurodegenerativas y así, permitir que más personas puedan obtener un diagnóstico más confiable y preciso para su debido tratamiento.

## **Resumen**
La enfermedad del Alzheimer es un trastorno neurológico que causa la pérdida de autonomía y memoria en las personas que la padecen. Debido al aumento de casos de este padecimiento y la falta de precisión de las herramientas de diagnóstico se da paso al desarrollo de nuevas herramientas capaces de disminuir esta problemática. El objetivo principal de este trabajo investigativo es implementar un modelo de red neuronal convolucional tridimensional con estructura base tipo AlexNet3D para obtener la predicción de un posible diagnóstico de la enfermedad Alzheimer (AD) a partir del análisis de imágenes por resonancia magnética, utilizando como etapa temprana el síndrome de deterioro cognitivo leve (MCI). Este proyecto
brindará la explicación de cada fase planteada, las cuales fueron dividas en selección de las bases de datos, elección de características, procesamiento de los datos, desarrollo del modelo para su entrenamiento y validación, y por último, resultados obtenidos a partir de las pruebas de predicción. Con las cuales pudo obtenerse un porcentaje del 72,222 %, permitiendo catalogar al modelo K-Net95 como una red estable y eficiente, a pesar de las limitaciones computacionales a las que se vio limitado el proyecto.

### **Bases de datos**
Se utilizó el conocido repositorio ADNI para las fases de entrenamiento y validación. Para la fase de prueba se contó con la base de datos brindada por la clínica _Comfamiliar_ de Pereira.

### **Selección de características**
Fue fundamental la selección de un grupo de mediana-avanzada edad (50 a 80 años) para así disponer de una mejor comparación entre los paquetes de imágenes de resonancia magnética. La ponderación utilizada fue T1.

### **Procesamiento de imágenes**
Siguiendo con la división en la sección de Bases de datos, los métodos utilizados para las fases de entrenamiento y validación fueron diferentes a los de la fase de prueba.

Para las primeras fases, se utilizó el software _FreeSurfer_ para la generación del modelo tridimensional del cerebro limpio. Para la fase de prueba, se utilizó un método más liviano que permitiera obtener los paquetes de imágenes de forma más rápida denominada _FastSurfer_, la cual está basada en la técnica presentada por el software de las primeras fases.

### **Estructura y configuración**
Se basó la estructura de la red neuronal final con la arquitectura _AlexNet_, destacada por sus capas totalmente conectadas y de agrupación, permitiendo un aprendizaje profundo de características tridimensionales. Esta estructura fue modificada para que pudiera recibir los paquetes de imágenes de resonancia magnética en las fases de entrenamiento, validación y prueba facilitando así la detección de características y patrones relevantes para ña detección y clasificación de un paciente enfermo y un paciente sano.

Cabe resaltar que se realizó una división del 100% de los datos. El 70% se concentró en las fases de entrenamiento y validación, minetras que el 30% restante fue destinado para la fase de prueba

### **Entrenamiento y validación**
Se monitoreó el avance de la red a partir de los resultados obtenidos de exactitud (_accuracy_), pérdida (_loss_) y las curvas de aprendizaje presentadas por estos valores. A partir de estos resultados, fue necesaria la modificación de la red base que se planteó durante la fase de Estructura y configuración. Parte de los cambios fueron el aumento de neuronas por capa, cantidad de paquetes de imágenes en cada prueba, variación de las funciones de activación, entre otros.

### **Prueba**
Estas pruebas fueron divididas en 3. Primero, fue la modificación de parámetros que fue anteriormente explicada, en la cual se realizaron 10 pruebas totales para la obtención de la red final. Luego, se realizó una comparación entre la red obtenida y denominada "_K-Net95_" con otros modelos conocidos (UNet3D y ResNet3D) para determinar cual es mejor en factores de rendimiento, precisión y capacidad computacional, para este paso se utilizó una cantidad de paquetes de imágenes similar en cada modelo. Por último, se prueba la red obtenida con el grupo de prueba (30% del total de los datos) para así determinar la capacidad que tiene la red de clasificar un paciente enfermo (1) de un paciente sano (0) a partir de una predicción.


## Gracias por leer! 🪄
Muchas gracias por leer sobre mi proyecto, espero te pueda servir para tu trabajo o entretenimmiento. La inteligencia artificial es una gran herramienta que podrá abrir nuevos caminos para la ciencia. Este trabajo es realmente significativo para mí y me alegra poder publicarlo y que más personas puedan ver una de las muchas aplicaciones de esta nueva tecnología.





