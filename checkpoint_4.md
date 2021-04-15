![](./images/itam_logo.png)

M. Sc. Liliana Millán Núñez liliana.millan@itam.mx

Abril 2021

### Checkpoint 4

**Objetivo:** Guardar metadata en RDS

![](./images/checkpoint4.png)

¿Qué se entrega?

+ `README.md` actualizado -> incluye instrucciones de cómo correr tu luigi
+ `requirements.txt` actualizado
+ Imagen de DAG en verde con las 8 tareas
+ Código

-> En tu carpeta `sql` debe existir un script `create_metadata_tables.sql` en donde está el código en sql correspondiente a la creación de las tablas que ocuparás para almacenar la metadata.

**Demo en clase**

(5-7 minutos máximo)

1. Correr preprocesamiento y limpieza "nuevo" -> luigi corre
* Se muestra que se generan los metadatos de preprocesamiento y limpieza en la base de datos
* Se muestra la salida del preprocesamiento y limpieza (S3 o RDS)
* Mostrar DAG en verde
2. Correr preprocesamiento y limpieza "repetido" -> luigi no corre nada nuevo
* Se muestra que no se generaron los metadatos de preprocesamiento y limpieza en la base de datos
* Se muestra que no se genera nueva salida del preprocesamiento y limpieza (S3 o RDS)
3. Correr task de feature engineering (FE) "nuevo" -> luigi corre
* Se muestra que se generan los metadatos de FE en la base de datos
* Se muestra la salida del feature engineering (s3 o RDS)
* Se muestra DAG en verde
4. Correr task de feature engineering (FE) "repetido" -> luigi no corre nada nuevo
* Se muestra que no se generan los metadatos de FE en la base de datos
* Se muestra que no se genera nueva salida del FE (S3 o RDS)

**Fecha de entrega: 20 abril 2021**

#### ¡Ánimo!
