### Checkpoint 5

Revisión de pipeline de unit testing

+ Corre desde EC2
+ Visualización del DAG desde central scheduler
+ Se integera al pipeline existente
+ Se corre 1 prueba de Extract/Load que falle
  + El pipeline se "rompe", muestra el task como fallido
  + Se muestra el contexto del error (marbles)
+ Se corre 1 prueba de Extract/Load que pase
  + Se guarda metadata de la prueba, al menos: estatus, qué prueba se corrió, cuándo se ejecutó.
+ Se corre 1 prueba de Feature engineering que falle
  + El pipeline se "rompe", muestra el task como fallido
  + Se muestra el contexto del error (marbles)
+ Se corre 1 prueba de Feature engineering que pase
  + Se guarda metadata de la prueba, al menos: estatus, qué prueba se corrió, cuándo se ejecutó.
+ Se vuelve a correr el pipeline, mismos parámetros, no se ejecutan nuevos trabajos.
+ En su README.md en su branch master se encuentra definido al menos 1 atributo protegido y las métricas de fairness que ocuparán.
