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

- Deben de haber pasos para llegar al modelo y después la predicción.
- Ya que seleccionamos al modelo, cómo lo usamos?

Un producto de datos a.k.a. *intelligent system* tiene al menos un componente de *machine learning* o modelo (bayesiano, PGM, etc.) y nos permite conectarlo con el usuario para alcanzar los objetivos para los que el modelo fue creado. Además, este  sistema **debe** evolucionar y mejorar con el tiempo sobretodo a través del *feedback* generado a través de la interacción que los usuarios tienen con él.

- Este sistema debe estar vivo.
- La conexión y la interacción con el cliente es clave.


![](images/pointer.png) ¿Qué es un sistema?

![](images/filosoraptor.jpg)
<br>

> A system is an entity with interrelated and interdependent parts; it is defined by its boundaries and it is more than the sum of its parts (subsystem). Changing one part of the system affects other parts and the whole system. Henry Modisett.

- Un producto de datos es un sistema.

¿Por qué es un sistema?

Existen varios componentes que requieren de una gestión adecuada para que todo funcione correctamente. Por ejemplo, necesitamos ingestar datos con cierta frecuencia, limpiarlos y acomodarlos de cierta manera para que puedan ser ocupados como nuestro modelo(s) los necesita, luego necesitamos generar una predicción y luego emitir esa recomendación hacia alguien o algo que permita realizar una acción adecuada.

- Nuestros artefactos son software pero no necesariamente desarrollamos sistemas de software.


Para que un sistema inteligente sea exitoso requiere de 5 elementos:

1. Un objetivo de importancia (*meaningful*): Una razón de existir, esta razón debe ser de importancia para sus usuarios. Recuerda que las propiedades de un buen objetivo son: es medible, alcanzable y comunicable para el equipo que lo va a implementar y para los que lo van a financiar!
2. Creación de inteligencia: La inteligencia puede venir de diferentes formas, desde simples heurísticas hasta modelos complejos de *machine learning*. La inteligencia se refiere a la parte lógica del sistema.  
3. Una experiencia inteligente: La predicción generada deberá ser presentada a los usuarios de alguna forma para que el usuario haga lo requerido dada la predicción. Normalmente esta experiencia está asociada a un *dashboard* o interfaz -gráfica o no-.
   - No nos referimos tanto al UEX, más bien nos referimos a que las predicciones las presentamos de manera adecuada. Con esto se deben exponer de forma clara.
   - Una API es una forma fácil de exponer los modelos.
   - Es común que las predicciones también salgan por dashboards. Muchos dashboards solo son para presentar la información bonita, pero se requiere más que eso.
4. La implementación de la inteligencia: La implementación incluye todo lo que se requiera para ejecutar la inteligencia, moverla, escalarla, administrarla, recolectar métricas de su uso y funcionamiento.
   - Es más como las herramientas que usas como MLlib
5. Orquestación: Un sistema inteligente está vivo, y por lo tanto debemos asegurarnos que todas sus partes sigan balanceados para cumplir con sus objetivos. Es responsable de monitorear los objetivos, inspeccionar y modificar la interacción en caso de ser necesario, actualizar la inteligencia, hacer *override* de la inteligencia si así se requiere. También tiene que lidiar con el manejo de los errores, controlar el riesgo y no permitir el abuso.
   - El abuso se refiere a impedir que las personas hagan mal uso del producto de datos.

En general:

La **inteligencia** es la parte lógica del sistema, la que toma las decisiones sobre qué es lo correcto de hacer y cuándo, la **implementación** corresponde a todos los servicios, sistemas *back-end* y *front-end* como interfaz con el usuario para hacerle llegar la salida de la inteligencia, y la **orquestación** es la administración del sistema a través de su ciclo de vida incluyendo el manejo de errores.

Un producto de datos eficiente balancea estos 5 componentes y además toma en consideración cómo este producto puede ser ocupado de forma inadecuada por otro humano con anticipación.

El capítulo 2, 5 y 20 del libro de texto tiene mucho más información al respecto.

En un sistema inteligente o producto de datos el *pipeline* se debe ver así:

![](./images/ml_pipeline_2.png)
<br>
Fuente: [Components of an AI-Enabled System](https://ckaestne.github.io/seai/slides/02_components/components.html#/4/4)

- Nosotros veremos una actualización que es en Batch.
- Los datos que vamos a ocupar esta clase se actualizan diario. Nosotros lo vamos a hacer actualizando cada semana.

#### Ejemplos

+ Sistema de recomendación de Netflix
  + ¿Cuál es el objetivo?
    + Ofrecer recomendación película/serie.
  + ¿Cuál es la experiencia inteligente?
    + Se presenta la información de forma evidente en la plataforma.
+ ¿Cuál es la implementación de la inteligencia?
    + Recabando información de hábitos.
    + Por el ranking que das.
  + ¿Cuál es la orquestación?
    + La ingesta de Netflix son las nuevas películas que vas viendo y lo que dices que me gusta.
    + 
  
+ Buscador de Google (*Information Retrieval*)
  + ¿Cuál es el objetivo?
  + ¿Cuál es la experiencia inteligente?
  + ¿Cuál es la implementación de la inteligencia?
  + ¿Cuál es la orquestación?

+ Prevención de fraude Banorte
  + ¿Cuál es el objetivo?
  + ¿Cuál es la experiencia inteligente?
  + ¿Cuál es la implementación de la inteligencia?
  + ¿Cuál es la orquestación?

![](./images/banorte.jpg)
<br>


+ UberEats: Predicción de tiempo de entrega
  + ¿Cuál es el objetivo?
  + ¿Cuál es la experiencia inteligente?
  + ¿Cuál es la implementación de la inteligencia?
  + ¿Cuál es la orquestación?
