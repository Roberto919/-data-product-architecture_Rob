![](./images/itam_logo.png)

M. Sc. Liliana Millán Núñez liliana.millan@itam.mx

Enero 2021


## Introducción

### Agenda

+ Productos de datos
+ Ejemplos
 ***

#### Productos de datos

![](./images/pointer.png) ¿Cuál es el típico *pipeline* para hacer un modelo de *machine learning*?
<br>
<br>

Un producto de datos a.k.a. *intelligent system* tiene al menos un componente de *machine learning* o modelo (bayesiano, PGM, etc.) y nos permite conectarlo con el usuario para alcanzar los objetivos para los que el modelo fue creado. Además, este  sistema **debe** evolucionar y mejorar con el tiempo sobretodo a través del *feedback* generado a través de la interacción que los usuarios tienen con él.


![](images/pointer.png) ¿Qué es un sistema?

![](images/filosoraptor.jpg)
<br>

> A system is an entity with interrelated and interdependent parts; it is defined by its boundaries and it is more than the sum of its parts (subsystem). Changing one part of the system affects other parts and the whole system. Henry Modisett.

¿Por qué es un sistema?


Existen varios componentes que requieren de una gestión adecuada para que todo funcione correctamente. Por ejemplo, necesitamos ingestar datos con cierta frecuencia, limpiarlos y acomodarlos de cierta manera para que puedan ser ocupados como nuestro modelo(s) los necesita, luego necesitamos generar una predicción y luego emitir esa recomendación hacia alguien o algo que permita realizar una acción adecuada.


Para que un sistema inteligente sea exitoso requiere de 5 elementos:

1. Un objetivo de importancia (*meaningful*): Una razón de existir, esta razón debe ser de importancia para sus usuarios. Recuerda que las propiedades de un buen objetivo son: es medible, alcanzable y comunicable para el equipo que lo va a implementar y para los que lo van a financiar!.
2. Creación de inteligencia: La inteligencia puede venir de diferentes formas, desde simples heurísticas hasta modelos complejos de *machine learning*. La inteligencia se refiere a la parte lógica del sistema.  
3. Una experiencia inteligente: La predicción generada deberá ser presentada a los usuarios de alguna forma para que el usuario haga lo requerido dada la predicción. Normalmente esta experiencia está asociada a un *dashboard* o interfaz -gráfica o no-.
4. La implementación de la inteligencia: La implementación incluye todo lo que se requiera para ejecutar la inteligencia, moverla, escalarla, administrarla, recolectar métricas de su uso y funcionamiento.
5. Orquestación: Un sistema inteligente está vivo, y por lo tanto debemos asegurarnos que todas sus partes sigan balanceados para cumplir con sus objetivos. Es responsable de monitorear los objetivos, inspeccionar y modificar la interacción en caso de ser necesario, actualizar la inteligencia, hacer *override* de la inteligencia si así se requiere. También tiene que lidiar con el manejo de los errores, controlar el riesgo y no permitir el abuso.

En general:

La **inteligencia** es la parte lógica del sistema, la que toma las decisiones sobre qué es lo correcto de hacer y cuándo, la **implementación** corresponde a todos los servicios, sistemas *back-end* y *front-end* como interfaz con el usuario para hacerle llegar la salida de la inteligencia, y la **orquestación** es la administración del sistema a través de su ciclo de vida incluyendo el manejo de errores.

Un producto de datos eficiente balancea estos 5 componentes y además toma en consideración cómo este producto puede ser ocupado de forma inadecuada por otro humano con anticipación.

El capítulo 2, 5 y 20 del libro de texto tiene mucho más información al respecto.

En un sistema inteligente o producto de datos el *pipeline* se debe ver así:

![](./images/ml_pipeline_2.png)
<br>
Fuente: [Components of an AI-Enabled System](https://ckaestne.github.io/seai/slides/02_components/components.html#/4/4)

#### Ejemplos

+ Sistema de recomendación de Netflix
  + ¿Cuál es el objetivo?
  + ¿Cuál es la experiencia inteligente?
  + ¿Cuál es la implementación de la inteligencia?
  + ¿Cuál es la orquestación?

+ Buscador de Google (*Information Retrieval*)
  + ¿Cuál es el objetivo?
  + ¿Cuál es la experiencia inteligente?
  + ¿Cuál es la implementación de la inteligencia?
  + ¿Cuál es la orquestación?

+ Prevención de fraude Banorte

![](./images/banorte.jpg)
<br>

+ ¿Cuál es el objetivo?
+ ¿Cuál es la experiencia inteligente?
+ ¿Cuál es la implementación de la inteligencia?
+ ¿Cuál es la orquestación?

+ UberEats: Predicción de tiempo de entrega
  + ¿Cuál es el objetivo?
  + ¿Cuál es la experiencia inteligente?
  + ¿Cuál es la implementación de la inteligencia?
  + ¿Cuál es la orquestación?
