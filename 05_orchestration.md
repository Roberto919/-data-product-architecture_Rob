### Orchestration

![](./docs/images/itam_logo.png)

M. Sc. Liliana Millán Núñez liliana.millan@itam.mx

Febrero 2020

### Agenda

+ Data Pipeline
+ DAG
+ Luigi

#### Data Pipeline

Asi como el ETL es un *pipeline*, agregar todo el procesamiento que requieres durante todas las fases de un proyecto de ciencia de datos forman parte de un *pipeline*, a este *pipeline* en particular le llamamos *data pipeline*.

Un *pipeline* puede estar conformado por diferentes *pipelines*, y estos pueden o no correr en una secuencia o en paralelo. Para ordenar esa secuencia existen los orquestadores, herramientas que nos permiten definir cómo, cuándo y con qué debemos correr cada parte de nuestro *data pipeline*.

Existen varios orquestadores, los científicos de datos generalmente ocupamos Luigi ya que es muy sencillo de ocupar -aunque no cumple con algunos patrones de diseño muy importantes de ingeniería de software :(-, pero cumple con características que nos facilitan la vida para poder realizar un *data pipeline* sin necesidad de ser tan expertos en ingeniería de software.

#### DAG

Acrónimo de *Directed Acyclic Graph*, un grafo acíclico dirigido. Esta estructura de datos conformada por vértices -nodos- y aristas -arcos. Cada arco nodo representa una tarea a ejecutar - *task*- y cada arco la dirección de flujo. No está permitido tener ciclos, más adelante quedará claro el por qué (espero).

 nos permite organizar cómo los diferentes *tasks* de nuestro *data pipeline* correrán. Cada nodo es un *task* y cada arista la dirección que debe seguir el flujo de procesamiento.

Dado que en un DAG *no* hay ciclos, es posible determinar sin ambigüedad qué forma la entrada a un *task* y qué la salida.  

Principios de DAG:

+ **Idempotencia:** Cuando corremos un proceso muchas veces con los mismos parámetros debemos obtener la misma salida, sin excepción. También implica que no queremos generar salidas repetidas.

¿Por qué un DAG en el orquestador?

+ Evita tener ciclos
+ Permite tener más de 1 entrada y solo 1 salida
+ Permite ejecutar tareas en paralelo
+ Permite ejecutar **solo la parte necesaria** gracias a su propiedad de idempotencia.
