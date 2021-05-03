![](./images/itam_logo.png)

M. Sc. Liliana Millán Núñez liliana.millan@itam.mx

Mayo 2021

### Checkpoint final: Last mile

#### **Objetivos:**

+ Generar predicciones
+ Exponer tus predicciones a través de una API en Flask Swagger
+ Dashboard de monitoreo de modelo con Dash


#### Pipeline

![](./images/checkpoint_7.png)

#### Demo

Tienes 10 minutos para mostrar desde tu EC2 tu producto de datos:

+ Correr "predicciones metadata" nuevo
  + Se generan predicciones en BD
  + Se guarda salida de prueba unitaria correcta en BD
  + Se genera metadata en BD
  + DAG Verde
+ Correr "predicciones metadata" mismos parámetros, no corre luigi
  + No corren procesos, luigi OK
+ Correr "predicciones metadata" con prueba unitaria "mala"
  + Trueba prueba unitaria, se muestra contexto de Marbles
  + No se genera metadata
  + DAG rojo
+ Correr "almacenamiento API"
  + Mostrar registro en BD
  + DAG verde
+ Correr "Monitoreo modelo"
  + Mostrar registro en BD
  + DAG verde
+ Mostrar la API y utilizar el primer *endpoint* solicitando los datos necesarios para ver el *score* de predicción y la etiqueta predicha (*port forwarding* EC2)
+ Mostrar el monitoreo del modelo (*port forwarding* EC2) con histograma de scores de predicción del modelo

#### ¿Qué se entrega?

+ Al menos 2 *endpoints* de API:
  + *Endpoint* 1:
    + *Input*: `id establecimiento`, y lo que necesites.
    + *Output*: JSON con *score* de predicción, etiqueta predicha
  + *Endpoint* 2:
    + *Input*: `fecha prediccion`
    + *Output*: JSON con una lista que contienen para cada establecimiento que tiene una predicción para ese día: id establecimiento, *score* de predicción, etiqueta predicha
+ *Dashboard* en `dash` de **al menos** la distribución de scores del modelo seleccionado en el último punto en el tiempo con el que fue validado y la distribución obtenida para las últimas predicciones (último consecutivo).
+ `README.md` Actualizado con tu DAG final en verde
+ `requirements.txt` actualizado
+ Código actualizado
