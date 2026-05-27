# Prototipo Predictivo y Análisis de Sensibilidad de Calidad del Aire (Estación Belisario, Quito)
# Prototipo Predictivo de Calidad del Aire - Estación Belisario

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1TTA0_p_inRbDSWFoCl5dwGL14qn54lUa?usp=sharing)

# Prototipo Predictivo de Calidad del Aire - Estación Belisario

<a href="AQUÍ_PEGA_EL_ENLACE_QUE_COPIASTE_DE_COLAB" target="_blank">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab">
</a>

Este repositorio contiene el desarrollo del proyecto aplicado de 340 horas para el Curso Preparatorio de la **Maestría en Ciencia de Datos y Máquinas de Aprendizaje con mención en Inteligencia Artificial** de la **UIDE (Powered by Arizona State University)**.

## Descripción del Proyecto
El objetivo central de este proyecto es predecir las concentraciones de partículas finas ($PM_{2.5}$) utilizando datos históricos masivos (2010-2026) provistos por la REMMAQ. El sistema integra un pipeline completo de Ciencia de Datos: desde la ingesta y limpieza, pasando por la persistencia relacional en SQL, hasta el modelado predictivo mediante arquitecturas de Deep Learning.

## Tecnologías e Infraestructura
* **Lenguaje Principal:** Python 3.x
* **Manipulación y Análisis Estadístico:** Pandas, NumPy, Visualizaciones con Seaborn y Matplotlib.
* **Motor de Base de Datos:** SQLite3 (Estructuración de la tabla `monitoreo_belisario`).
* **Modelamiento Core e IA:** Scikit-Learn y TensorFlow / Keras para la Red Neuronal Prototipo.

## Componentes del Repositorio
1. **Pipeline ETL:** Consolidación y limpieza de más de 77,000 registros de contaminantes ($NO_2$) y meteorología (Lluvia, Viento, Humedad, Temperatura).
2. **Modelo de Red Neuronal Profunda:** Arquitectura secuencial optimizada con regularización Dropout y Early Stopping.
3. **Interpretación Ética:** Implementación de la *Técnica de Permutación* para auditar el modelo e identificar las variables con mayor peso predictivo.

## Resultados Principales
* El modelo de **Red Neuronal Profunda** obtuvo el rendimiento más robusto con el menor error medio absoluto (**MAE: 5.71**).
* Tras el análisis de sensibilidad, se determinó que el **$NO_2$ es el factor más influyente con el 32.79%**, evidenciando la alta incidencia de las emisiones por tráfico vehicular en el sector Belisario.

## Marco Ético y Transparencia
En concordancia con las directrices de la UIDE, el proyecto aborda el dilema de la "caja negra" en algoritmos complejos mediante métodos de interpretabilidad y explicabilidad, garantizando que los resultados de la IA sean auditables, transparentes y útiles para el diseño de políticas de salud pública en la ciudad.
