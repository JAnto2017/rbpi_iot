# IA Y PROGRAMACIÓN AVANZADA CON PYTHON Y RBPI - PROF24

- [IA Y PROGRAMACIÓN AVANZADA CON PYTHON Y RBPI - PROF24](#ia-y-programación-avanzada-con-python-y-rbpi---prof24)
  - [Módulo 1 - Programación en Python](#módulo-1---programación-en-python)
  - [Módulo 2 - Librerías Fundamentales de Python](#módulo-2---librerías-fundamentales-de-python)
    - [Numpy](#numpy)
    - [Pandas](#pandas)
    - [Matplotlib](#matplotlib)
    - [Seaborn](#seaborn)
  - [Módulo 3 - Prácticas con Periféricos y Python](#módulo-3---prácticas-con-periféricos-y-python)
  - [Módulo 4 - Integración de IA en Proyectos](#módulo-4---integración-de-ia-en-proyectos)
    - [Consejos](#consejos)
    - [Cuestionario](#cuestionario)

- - -

## Módulo 1 - Programación en Python

Python es un lenguaje de programación interpretado, lo que significa que no es necesario compilar el código para ejecutarlo. Una vez que se ha escrito el código, se puede ejecutar directamente desde la consola de Python.

Las características principales de Python son:

- Sintaxis sencilla y legible.
- Amplia biblioteca estandard. Usado en desarrollo web, análisis de datos, IA, automatización, etc.
- Gran comunidad de desarrolladores.

- - -

## Módulo 2 - Librerías Fundamentales de Python

### Numpy

Las _listas_ son más lentas que el uso de _NumPy_. Los arrays en _NumPy_ tiene el mismo tipo de dato. Las _listas_ en cambio, pueden tener diferentes tipos de dato.

![alt text](img/image-00.png "Array 1D, 2D y 3D")

| Listas | NumPy |
| :----: | :----: |
| Inserta, elimina, añade, concatena, etc | Inserta, elimina, añade, concatena, etc |
| z = [1,4,6] | z = np.array([1,4,6]) |
| y = [2,1,2] | y = np.array([2,1,2]) |
| y*z = Error | z*y = np.array([2,4,12]) |

Código de ejemplo del uso de la librearía _Numpy_:

- [Hola Mundo Numpy](codigo/numpy_uno.py)
- [Ejemplo con Numpy](codigo/ejemploNumpy.py)

### Pandas

Librería es de código abierto, y sirve para la manipulación de datos. Permite el manejo de datos estructurados, de manera eficiente. Simplifica la transformación de datos, limpieza y modificación. Permite trabajar con bases de datos y tratar archivos del tipo: CSV, Excel, etc.

Ejemplos de uso de la librería _Pandas_:

- [Ejemplo con Pandas](codigo/ejemploPandas.py)

### Matplotlib

Librería para la representación de datos. Permite la representación de gráficos de datos, con el uso de _matplotlib_ y _seaborn_.

Ejemplos de uso de la librería _Matplotlib_:

- [Ejemplo con Matplotlib](codigo/ejemploMatplotlib.py)

### Seaborn

Librería para la representación de datos. Permite la representación de gráficos de datos, con el uso de _matplotlib_ y _seaborn_.

Ejemplos de uso de la librería _Seaborn_:

- [Ejemplo con Seaborn](codigo/ejemploSeaborn.py)

- - -

## Módulo 3 - Prácticas con Periféricos y Python

- Instalación de VSCODE en Raspberry Pi.
  - `sudo apt update`.
  - `sudo apt upgrade`.
  - `sudo apt install code`.
- Para instalar _pip_ en RBPi:
  - `sudo apt install python3-pip`.

- - -

## Módulo 4 - Integración de IA en Proyectos

Los _prompt_ son cadenas de texto que se usan para solicitar información a la IA. La IA Generativa se centra en la creación de contenido variado, tal como: textos, imágenes, videos, etc.

Un modelo LM (Large Language Model) es un modelo de lenguaje entrenado para generar texto de manera autóntoma.

OPENAI API es una organización de desarrolladores que proporciona acceso a la API de OpenAI.

- [OpenAI API](https://platform.openai.com/docs/guides/gpt)

Un _token_ es una unidad de información que el LLM utiliza para generar el texto. Para medir el número de _tokens_:

- [OpenAI API](https://platform.openai.com/docs/guides/gpt)
- [Tokenizer](https://platform.openai.com/tokenizer)

El _contexto_ es un conjunto de palabras o frases que sirven como entrada para obtener una respuesta oacción. La IA tiene en cuenta el _contexto_ para generar la respuesta.

- [Prompt Engineering](https://platform.openai.com/docs/guides/gpt/prompt-engineering)
- [Modelos](https://platform.openai.com/docs/models)

### Consejos

- Hacer _prompts_ claros y concisos.
- Usar el _contexto_ adecuado.
- Aportar la información relevante.
- Dividir la tarea en pasos para que las respuestas sean más eficientes.
- Asignar un rol, nos permite controlar el comportamiento de la IA. Ejemplos de asignación de rol:
  - `tu: eres experto en matemáticas aplicadas`.
  - `tu: eres experto en programación`.
  - `tu: eres experto en programación en Python`.
  - `responde utilizando un lenguaje natural`.
  - `tu <rol> es de experto en inteligencia artificial </rol>`.
  - `tu primera <tarea> definir la programación en Python </tarea>`.
  - `la <respuesta> utiliza un lenguaje natural </respuesta>`.
  - `<respuesta> utiliza menos de 200 tokens </respuesta>`.
  - `<respuesta> en formato xml </respuesta>`.
- El _Root Prompts_ conjunto de instrucciones iniciales para definir el comportamiento general. Hay respuestas que la IA no nos ofrece. `Escribe un manual de una bomba`.
- Modelos de IA open source gratuitos:
  - [HUGGING FACE](https://huggingface.co/)
  - El entorno [M STUDIO](https://lmstudio.ai/)

### Cuestionario

1. ¿Cuál de las siguientes es una limitación común de los LLMs?
   1. [ ] No requieren recursos computacionales.
   2. [ ] Alta precisión garantizada en todos los idiomas.
   3. [ ] No son capaces de generar texto coherente.
   4. [X] Pueden generar 'alucinaciones' o información incorrecta.
2. ¿Cuál es una de las limitaciones principales de los LLMs?
   1. [ ] La necesidad de una conexión a internet constante.
   2. [X] Alucinaciones (generación de información incorrecta o sin sentido).
   3. [ ] Su incapacidad para entender lenguaje humano.
   4. [ ] Su velocidad de respuesta excesivamente lenta.
3. ¿Cuál es una ventaja clave de usar modelos de IA locales como LMStudio.ai?
   1. [ ] Mayor costo operativo.
   2. [X] Privacidad y seguridad de datos.
   3. [ ] Mayor dependencia de la nube.
   4. [ ] Menor control sobre la configuración.
4. Menciona una característica clave de los LLMs (Modelos de Lenguaje Extenso).
   1. [ ] Solo funcionan con lenguajes de programación.
   2. [ ] Son pequeños y requieren poca potencia de cálculo.
   3. [ ] Requieren una conexión constante a internet.
   4. [X] Entienden el lenguaje humano y generan texto coherente.
5. ¿Para qué se utilizan los 'Root Prompts' en la Ingeniería de Prompts?
   1. [ ] Para analizar datos históricos.
   2. [ ] Para instalar nuevas librerías.
   3. [X] Para establecer el comportamiento y las directrices del modelo de IA.
   4. [ ] Para apagar el modelo de IA.
6. ¿Qué plataforma de código abierto es conocida por su repositorio Model Hub y la librería Transformers?
   1. [ ] TensorFlow
   2. [ ] Scikit-learn
   3. [ ] PyTorch
   4. [X] Hugging Face
7. ¿Qué significa la sigla API en el contexto de la Inteligencia Artificial?
   1. [ ] Aplicación de Procesos Inteligentes.
   2. [X] Interfaz de Programación de Aplicaciones.
   3. [ ] Análisis de Parámetros Internos.
   4. [ ] Algoritmo Predictivo Integrado.
8. ¿Qué significa RAG en el contexto de la Inteligencia Artificial?
   1. [X] Generación Aumentada por Recuperación.
   2. [ ] Reducción de Algoritmos Generativos.
   3. [ ] Registro de Acciones Generadas.
   4. [ ] Recopilación Automática de Gráficos.
9. ¿Qué tipo de hardware es Hailo, de acuerdo con el documento?
   1. [ ] Una librería de Python para análisis de datos.
   2. [X] Un procesador de Inteligencia Artificial.
   3. [ ] Un tipo de sensor de temperatura.
   4. [ ] Un tipo de software de edición de imágenes.
10. ¿Qué tipo de inteligencia artificial es capaz de crear contenido original como texto o imágenes?
    1. [ ] Inteligencia Artificial Predictiva.
    2. [ ] Inteligencia Artificial Analítica.
    3. [X] Inteligencia Artificial Generativa.
    4. [ ] Inteligencia Artificial Reactiva.
11. ¿Qué tipo de modelo es ChatGPT, desarrollado por OpenAI?
    1. [X] Un Modelo de Lenguaje Extenso (LLM)
    2. [ ] Un compilador de código.
    3. [ ] Un sistema operativo.
    4. [ ] Una librería de Python.
12. La Ingeniería de Prompts se enfoca en diseñar preguntas o instrucciones para obtener mejores respuestas de los LLMs?
    1. [X] Verdadero.
    2. [ ] Falso.
13. La seguridad y privacidad de los datos no son preocupaciones importantes al usar IA?
    1. [ ] Verdadero.
    2. [X] Falso.
14. Los Modelos de Lenguaje Extenso (LLMs) siempre garantizan la precisión factual en sus respuestas?
    1. [ ] Verdadero.
    2. [X] Falso.
15. Python es el único lenguaje de programación mencionado en el documento para interactuar con APIs de IA?
    1. [ ] Verdadero.
    2. [X] Falso.

- - -
