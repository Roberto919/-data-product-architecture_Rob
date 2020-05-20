### Checkpoint 6: Final mile(s)

+ Pipeline de predicción: Su requieres tendría que buscar el pkl en S3 (training) y haber pasado la validación de FE
  + Las predicciones se guardan en S3 (cold) y RDS (hot)
  + Metadata de predicción en RDS -> gobernanza de modelos (guardar el uuid del archivo con las predicciones)
  + Al menos 2 validaciones sobre las predicciones
+ Cálculo de bias y fairness con el mejor modelo seleccionado durante el training (a través de python no Web!)
  + Persistencia de bias/fairnes, métricas.
  + Metadata de bias
+ API para exponer tus predicciones, al menos 1 endpoint
+ Dashboard de monitoreo de modelo
+ README completo, cualquiera que se meta a su github puede reproducir su producto de datos siguiendo sus
instrucciones
  + Agrega el requirements.txt de tu pyenv
  + Agrega una foto de tu pipeline completo todo en verde!
´
Proceso:
+ Corremos bias y fairness del mejor modelo
  + Visualización de Pipeline
  + Persistencia de datos
  + Verificación de persistencia de metadatos
+ Corremos predicciones
  + Visualización de tu pipeline
+ Verificamos metadata de predicciones
+ Validaciones de predicciones marbles
  + Primera vez no pasa (si guardas metadatos, se guardan cuando falla)
  + Segunda vez pasa, guarda metadatos
+ Verificamos el endpoint de tu API
  + Regresamos predicciones
+ Verificamos dashboard de monitoreo
