Checkpoint 4: 28 abril 2020

+ Correr el pipeline desde central-scheduler en el EC2
+ Mostrar la visualización de su DAG
+ El pipeline debe:
  + Correr (mínimo) hasta modelado (training)
  + Generar metadata de EL
  + Generar metadata de *feature engineering*
  + Generar metadata de *modelling*
  + Almacenar en (S3) pkl de modelos generados
+ Correremos el pipeline 2 veces, la primera cambiaremos los hiperparámetros de uno de sus modelos para que se genere nueva metadata
  + Verificaremos que se crea la metadata
  + Que se guardó el pickle asociado
+ La segunda corrida será con los mismos hiperparámetros para verificar que no se genera nada nuevamente (idempotencia de Luigi)
+ Aparte: revisión de su README.md
