# Informe del Proyecto de Recuperación de Información

## Autores:
- Naomi Lahera Champagne
- Leonardo Javier Ramírez Calatayud
- Loitzel Ernesto Morales Santiesteban

## Definición del Modelo de SRI Implementado:
El modelo de Sistema de Recuperación de Información (SRI) implementado es una combinación de técnicas clásicas de recuperación de información basadas en extensiones del modelo booleano que mejoran la capacidad de recuperación mediante la expansión de consultas y la consideración de la relevancia de los términos en los documentos. Se establece omo objetivo establecer una comparativa objetiva con el modelo booleano basico. Como funcionalides se implementa una expansion de consulta utilizando wordnet, de esta manera se pueden recuperar documentos de interés aun si no se encuentra exactamente lo buscado en la consulta. Por ultimo se implementaron metodos de feedback, mediante los cuales se pueden de manera manual modificar los resultados provistos por una consulta

## Consideraciones Tomadas a la Hora de Desarrollar la Solución:
Al desarrollar la solución, se consideraron varios aspectos importantes:
- **Eficiencia:** Se buscó optimizar el tiempo de procesamiento de consultas y la recuperación de documentos.
- **Escalabilidad:** La solución se diseñó para manejar grandes volúmenes de documentos y consultas.
- **Calidad de Resultados:** Se priorizó la precisión y exhaustividad de los resultados de la recuperación.

## Explicación de Cómo Ejecutar el Proyecto:
1. Clonar el repositorio del proyecto desde [URL del Repositorio].
2. Instalar las dependencias necesarias, incluyendo bibliotecas de Python y modelos de lenguaje natural.
3. Mediante la interfaz visual se proporcionan interfaces para interactuar con el proyecto de forma intuitiva y sencilla, facilitando la realización de consultas, la visualización de resultados y la configuración de opciones.

## Definición de la Consulta:
Una consulta en el contexto de este proyecto es una cadena de texto que representa la información que un usuario desea recuperar de un conjunto de documentos. Las consultas pueden contener términos de búsqueda simples o complejos, así como operadores lógicos como "and", "or" y "not".

## Explicación de la Solución Desarrollada:
La solución desarrollada consta de varios componentes:
- **Preprocesamiento de Consultas:** Las consultas se procesan para tokenizarlas, eliminar ruido, eliminar palabras vacías y reducir la morfología.
- **Modelo de Recuperación de Documentos:** Se implementa un modelo de recuperación de documentos basado en el modelo booleano clásico y una versión extendida que considera la relevancia de los términos.
- **Evaluación de Métricas:** Se evalúan métricas de rendimiento como precisión, exhaustividad, F-measure y R-Precision para medir la efectividad de la recuperación.

## Comparativa entre el Modelo Booleano Base y el Extendido:
Se llevó a cabo una comparativa entre el modelo booleano base y el modelo extendido para evaluar su rendimiento mediante las métricas:

- Precisión
- Recobrado
- Medida F y F1
- Accuracy

Esta comparativa permitió entender cómo la extensión del modelo booleano afecta la calidad de los resultados de la recuperación de información, especialmente en consultas más complejas y en conjuntos de datos variados.

## Insuficiencias de la Solución y Mejoras Propuestas:
A pesar de su efectividad, la solución presenta algunas limitaciones:
- **Manejo de Consultas Ambiguas:** El modelo puede tener dificultades para manejar consultas muy largas, ya que la forma DNF escala en complejidad

