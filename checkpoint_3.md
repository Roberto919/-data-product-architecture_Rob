![](images/itam_logo.png)

M. Sc. Liliana Millán Núñez liliana.millan@itam.mx

Marzo 2021

## Checkpoint 3

**Objetivo:** Uso de Luigi como orquestador de nuestro ETL pipeline.

* Generar el task de Luigi que se encargará de la ingesta de datos de la API de Food Inspections.
* Generar el task de Luigi que se encargará del almacenamiento ingestados de la API de Food Inspections.

**Cuándo se entrega:** Jueves 18 de marzo repositorio a las 23:59:59, demostración en clase.

### ¿Qué tienen que entregar?

En tu repositorio:

+ Actualización de tu README.md
+ Foto de tu DAG con las tasks de este checkpoint en verde
+ Actualización del código

### En clase

Tienes 5 minutos para mostrar:

1. En tu S3 bucket en la ruta adecuada, el pickle de la ingesta inicial histórica
2. Correr el task de almacenamiento desde luigi enviando un parámetro que indica que quieres que se corra la ingesta histórica -> la ingesta histórica ya ha sido corrida previamente por lo que no correrá el task.
3. Correr el task de almacenamiento desde luigi enviando un parámetro que indica que quieres que se corra la ingesta consecutiva con la fecha del día en el que lo corres.
4. Mostrar tu S3 bucket en la ruta adecuada, con el pickle de la ingesta cosecutiva que se hizo
5. Correr nuevamente el paso 3 con los mismos parámetros, Luigi no corre el task
7. Mostrar tu S3 bucket en la ruta adecuada, con el pickle de la ingesta realizada previamente
