![](./images/itam_logo.png)

M. Sc. Liliana Millán Núñez liliana.millan@itam.mx

## Continuous integration CI

### Agenda

+ Pruebas de código
+ Tipos de pruebas
+ Pruebas unitarias
+ PyTest
  + Asserts
  + Fixtures


### Pruebas de código

Es una prática *core* de ingeniería de *software*.

![](./docs/images/pointer.png) Piensa en una app móvil bancaria ¿por qué crees que necesitamos hacer pruebas de código?

![](./docs/images/pointer.png) Ahora piensa en tu contexto de ciencia de datos ¿por qué crees que necesitamos hacer pruebas de código?

#### Objetivos

1. Identificar *bugs* lo más temprano posible.
2. Verificar que el código hace lo que se supone debe hacer.

Otros menos directos pero igual de importantes:

3. Verificar si lo que tu entiendes que debe hacer ese código realmente es ... o el código está mal, o tu entendimiento del mismo está equivocado.
4. Permite a un nuevo usuario entender qué hace el código. Al hacer pruebas se genera una especie de colección de ejemplos ʘ‿ʘ
5. Permite verificar si la forma en la que estas generando el código es correcta ◕ ◡ ◕
6. Aunque no lo creas, debido a la 5, te obliga a escribir mejor código !!!

#### Tipos de pruebas

+ *Unit test:* Probar una unidad/funcionalidad de código aislada
+ *Integration test:* Probar cómo difrentes componentes (unidades) que forman parte de un sistema trabajan en conjunto. Verificar si la interacción entre estos componentes funciona y es la requerida.
+ *Functional test:* Tratamos al componente como una caja negra verificando que la funcionalidad cumple con los requerimientos, SLA, outputs, etc.
+ *End to end test:* Probar todos los componentes del sistema de inicio a fin. El objetivo es simular el escenario real en el que vivirá el sistema, identificando integración entre todos los componentes e integridad en los datos.
+ *Acceptance test:* Verificar que los requerimientos hechos por el usuario
+ *Performance test:* Probar todo el sistema bajo condiciones de estrés: exceso de peticiones, exceso de lectura a BD, etc.  
+ *Regression test:* Probar un programa/aplicación que ya funcionaba una vez que se le ha hecho un cambio para verificar que todo lo que antes funcionaba siga funcionando igual.
+ *Smoke test:* Un conjunto de pruebas a componentes específicos que forman el *core* de un sitema/aplicación.
+ *Alpha test:* Prueba *in-house* final de la funcionalidad de un sistema.
+ *Beta test:* Prueba con usuarios reales de una liberación inicial y oficial de un sistema/aplicación. 


#### Unit test

+ Métrica: cobertura , successful vs failed

#### PyTest

El paquete de pruebas de Python, hay otros muchos *frameworks* de pruebas de código, sin embargo, dado que lo que harás normalmente estará en python, es mejor ocupar este. De hecho, entre diferentes *frameworks* no cambia "mucho" el cómo utilizarlos, todos se basan en los mismos conceptos.

Para instalar PyTest necesitarás correr en tu ambiente de pyenv o anaconda o conda o virtualenv correspondiente a la clase `pip install pytest`.

+ Happy path
Por lo menos probar que hace lo que tiene que hacer
helps catch bugs
helps users to understand the program
ayuda a hacer código atómico y facil de hacer refactoring (deuda técnica)

asserts

marbles

### Referencias

+ [PyTest](https://docs.pytest.org/en/latest/)
+ [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf)
+ [Marbles API](https://marbles.readthedocs.io/en/stable/quickstart.html)
+ [PyTest tutorial]
