![](/docs/images/itam_logo.png)

## Data Product Architercture

+ MSc Liliana Millán Núñez liliana.millan@itammx
+ Enero 2020

+ **Horario:** Martes 19-22
+ **Salón:** RH 203


### Temario

||Fecha|Tema|
|:---|:----|:---------------|
|1|21 enero 2020|Introducción, productos de datos|
|2|28 enero 2020|Cómputo distribuido|
|3|4 febrero 2020|Infraestructura|
|4|11 febrero 2020|ETL|
|5|18 febrero 2020|Orquestadores|
|6|25 febrero 2020|Gobernanza de datos|
|7|3 marzo 2020|CI/CD|
|8|10 marzo 2020|Feature engineering|
|9|17 marzo 2020|Gobernanza de modelos|
|10|24 marzo 2020|Modelling|
|11|31 marzo 2020|Modelling|
|12|7 abril 2020|ASUETO|
|13|14 abril 2020|Predicciones|
|14|21 abril 2020|Delivery|
|15|28 abril 2020|Delivery|
|16|5 mayo 2020|Post-modelling|
|17|12 mayo 2020|Proyecto|
|18|19 mayo 2020|Proyecto|


#### Detalle

**Semana 1: Introducción, productos de datos, arquitectura empresarial**
+ Forma de trabajo, calificación, datasets disponibles
+ Productos de datos
+ Arquitectura empresarial

Tarea: Definir equipo de trabajo y dataset a ocupar

**Semana 2: Cómputo distribuido:**
+ Conceptos de cómputo distribuido
  + cómputo distribuido
  + master, workers
  + procesamiento en paralelo
  + escalamiento vertical, escalamiento horizontal
+ Ambiente local, nube

Deliverable: Equipo de trabajo, dataset a ocupar

**Semana 3: Infraestructura**
+ Seguridad: Bastión, tunneline
+ AWS: S3, EC2, EMR, RDS
+ Configuración como DSSG
+ Conceptos de CI/CD (Terraform)

Tarea:
+ Bastión funcionando para el equipo Dirección ip, usuarios que están, mi llave
+ Definición de proyecto a realizar
+ Diseño del producto de datos (mockup), incluir el entregable: BD, API, Dashboard
+ Crear cuenta de AWS (education)

**Semana 4: ETL**
+ Pipeline: qué es
+ ETL: Qué es eso
+ Diseño de ETL: Ejemplo
+ Storage: Parquet, AVRO

Checkpoint:
+ Bastión funcionando
Deliverables:
+ Definición de proyecto a realizar
+ Diseño del producto de datos (mockup)
Tarea:
+ Definir el mockup de ETL de su proyecto (sección ingestión de datos)
+ Creación de tu archivo `READMEmd` con la sección de ETL

**Semana 5: Orquestadores**
+ Orquestadores: DAG, Luigi  (Airflow, DataFactory, AWS Data Pipeline)

Tarea:
+ Definir DAG primera iteración de su proyecto con tasks de ETL empezando a desarrollarse
+ Actualización de tu archivo `READMEmd`

**Semana 6: Gobernanza de datos**
+ Gobernanza de datos: DB (esquema, índices), DWH, Data Lake
+ Linaje de datos

Deliverable:
+ Diseño de DAG, tareas DAG para ETL en desarrollo
Tarea:
+ Diseño de tu linaje de datos
+ Actualización de tu archivo `READMEmd`

**Semana 7: CI/CD**
+ Unit testing ETLs (python, pandas, marbles)
+ Unit testing: ejemplos

Checkpoint:
+ Al menos 2 tareas del ETL de ingestión de datos implementadas en Luigi Correr el DAG
Deliverable:
+ Linaje de datos
Tarea:
+ Definición de funciones del ETL a probar
+ Actualización de tu archivo `READMEmd`

**Semana 8: Feature engineering**
+ Pipelines de transformación de datos
+ Spark, Modin, Koalas, SQL window functions, WITH (CTE)

Deliverable:
+ Unit Testing de algunas funciones del ETL
Tarea:
+ Diseño de las funciones para transformación de datos
+ Actualización de tu archivo `READMEmd`

**Semana 9: Gobernanza de modelos**
+ Unit testing (Python/Pandas)
+ Gobernanza de modelos

Deliverable:
+ Implementación de algunas funciones de transformación de datos
Tarea:
+ Diseño de las funciones unit test para las funciones de transformación de datos
+ Diseño de tablas para gobernanza de modelos
+ Actualización de tu archivo `READMEmd`

**Semana 10: Modelling**
+ Pyspark, sklearn, H2O, Rapids
+ Storage
+ Cómo abordar el modelo: ventajas y desventajas

Checkpoint:
+ Corrida de tu DAG
Deliverables:
+ Diseño de tablas para gobernanza de modelos  
+ Implementación de algunas funciones unit test para transformación de datos
Tarea:
+ Implementación de al menos 1 de los modelos haciendo storage
+ Actualización de tu archivo `READMEmd`

**Semana 11: Modelling**
+ Deuda técnica
+ Cálculos éticos: Bias and Fairness

Delivery:
+ Storage de datos de modelo (al menos 1)
Tarea
+ Selección de métrica de *bias* y *fairness* a ocupar de acuerdo a tu proyecto
+ Actualización de tu archivo `READMEmd`

**Semana 12: ASUETO**

**Semana 13: Predicciones**
+ Pipeline de ejecución

Checkpoint:
+ Corrida del DAG hasta la corrida y storage de al menos 1 algoritmo (al menos 3 modelos), incluyendo el cálculo de *bias* y *faireness* seleccionado
Tarea:
+ Actualización del diseño del pipeline de training
+ Pipeline de ejecución en producción (diseño)
+ Actualización de tu archivo `READMEmd`

**Semana 14: Delivery**
+ BD
+ API: Flask, Bottle, DJango
+ API: Ejemplo

Deliverable:
+ Pipelines de ejecución para trainin y producción
Tarea:
+ Actualización del diseño de tu entregable
+ Inicio de implementación de tu entregable *front*
+ Actualización de tu archivo `READMEmd`

**Semana 15: Delivery**
+ Dashboards: Bokeh, Dash
+ Monitoreo de desempeño (1/2)

Deliverable:
+ Pipeline de ejecución productiva funcional integrado al DAG
Tarea:
+ Continuar implementación de tu entregable *front*
+ Actualización de tu archivo `READMEmd`

**Semana 16: Post-modelling**
+ Monitoreo de desempeño (2/2)
+ SLAs

Checkpoint:
+ Corrida de pipeline productivo desde DAG
+ Mostrar shallow *front* con alguna funcionalidad
Tarea:
+ Implementación de tu entregable *front*
+ Actualización al documento de entrega `README.md` y `requirements.txt`

**Semana 17: Proyecto**
+ Últimos detalles a tu implementación a tu producto de datos

Checkpoint:
+ Revisión de tu `READMEmd` y `requirements.txt`
Deliverable:
+ Entrega de documentación de tu producto de datos en tu repositorio
Tarea:
+ Crear el video de la corrida funcional completa del pipeline productivo

**Semana 18: Proyecto**

Presentación de tu proyecto de datos

+ Producto de datos funcional: Video de corrida final del producto de datos
+ Presentación de "*front*"
+ Entrega de documento final en repositorio
+ Último `commit` del proyecto
