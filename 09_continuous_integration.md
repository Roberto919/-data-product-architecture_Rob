![](./docs/images/itam_logo.png)

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

Nosotros nos concentraremos en este tipo de pruebas porque son las que **nos competen** como científicos de datos.

El objetivo de estas pruebas es verificar que un función hace lo que esperamos que haga. Se require que sea atómica -que solo haga 1 cosa-, a veces pudiera llegar a ser ambiguo la definición de hacer una sola cosa o funcionalidad, pero conforme vayas empezando a generar pruebas unitarias de tu código te irás dando cuenta cuando un función hace más de una cosa, porque será difícil hacer su prueba.

Es pos eso, que hacer pruebas unitarias te hace generar mejor código.

Hay dos vertientes en el mundo de ingeniería de *software* con respecto a cuándo hay que generar la prueba de unidad.

1. Un grupo opina que es mejor diseñar la prueba de unidad **antes** de hacer la función. De esta manera evitas estar sesgado a la implementación que ya hiciste. $\leftarrow$ recuerda que tú eres quien desarrolla la prueba unitaria de la función que desarrollaste!
2. Otro grupo opina que es mejor diseñar la prueba de unidad **después** de hacer la función, pues para este momento ya sabes qué hiciste y cómo lo hiciste.

Ambos tienen puntos a favor y puntos en contra, sin embargo para poder aplicar la primer opción requieres tener mucha experiencia tanto desarrollando software como en desarrollar pruebas unitarias. En nuestro caso haremos la segunda opción, primero haremos la funcionalidad y luego haremos la prueba de unidad.

+ Métrica: cobertura , successful vs failed

#### PyTest

El paquete de pruebas de Python, hay otros muchos *frameworks* de pruebas de código, sin embargo, dado que lo que harás normalmente estará en python, es mejor ocupar este. De hecho, entre diferentes *frameworks* no cambia "mucho" el cómo utilizarlos, todos se basan en los mismos conceptos.

Para instalar PyTest necesitarás correr en tu ambiente de pyenv o anaconda o conda o virtualenv correspondiente a la clase `pip install pytest`.

Algunas reglas de `pytest`

+ Las pruebas se corren sobre scripts de python **no notebooks**. Existen extensiones para que puedas probar *notebooks*, pero es mejor crear los *scripts* asociados a tus *notebooks* pues formarán parte de un *pipeline*.
+ Tus funciones de pruebas unitarias deben vivir en un archivo que tenga como prefijo `test_` o sufijo `test_`, de otra manera `pytest` no los identifica como parte de pruebas.
+ Tus métodos de pruebas unitarias deben tener el prefijo `test_` para ser considerados por `pytest` como una prueba unitaria. De esta manera se ejecutarán automáticamente cuando corramos las pruebas.
+ En donde corras el comando `pytest` se buscarán scripts de prueba tanto en ese directorio como en subdirectorios.
+ Puedes crear una clase de pruebas y poner ahí muchas funciones de prueba. La clase tendrá que tener un prefijo `Test` y los métodos tendrán que tener el prefijo `test_`.
+ Puedes poner un directorio de pruebs.

##### Asserts

Es la forma en la que `pytest` nos permite revisar la salida obtenida de un método, existen diferentes formas en las que  asserts que puedes ocupar:

+ `assert`: Puedes hacer tu propia condición lógica a probar. Por ejemplo:

```
import math

def function_to_test(x):
  return math.pow(x, 2)

def test_example():
  assert function_to_test(5) == 25

```

+ Puedes verificar que se haya levantado una excepción utilizando `pyenv.raises`

```

```

+ Puedes verificar que se haya generado un *warning*   

##### Fixtures

Son objetos que nos permiten hacer un *setup* inicial y que sirven para no tener que estar repitiendo el mismo código en todos los lugares donde ocupas esa configuración en tus pruebas.

Un *fixture* muy utilizado es la definición de un *DataFrame*, o una sesión de Spark.

Requieren tener un decorador para indicar que son un *fixture* y puedan ser utilizados en las pruebas.

Por ejemplo:

```
@pytest.fixture()
def df():
    return pd.DataFrame({
        'col_a': ['a', 'a', 'a'],
        'col_b': ['b', 'b', 'b'],
        'col_c': ['c', 'c', 'c'],
    })

```


##### Mocks

+ Objetos que te permiten "simular" otros elementos en tu código que requieres en tu prueba, pero que no quieres realmente ocuparlos. Por ejemplo:
  + Conexiones a bases de datos: No quisieras tener que hacer todo el proceso de conexión a una base de datos **real** para poder obtener datos reales y luego probar lo que estabas interesado en probar.
  + Acceso a API
  + Acceso a red
  + ...

#### Marbles

Esta es una librería concentrada en hacer *unit testing* a **datos**. Esta basada en que como científicos de datos tenemos ciertas suposiciones sobre los datos con los que trabajamos y modelamos.

Esta librería te permite hacer pruebas unitarias para comprobar que las suposiciones que tenemos sobre los datos se siguen sosteniendo con nuevos datos (o con los mismos después de hacer transformaciones o *pipelines* de preprocesamiento).

Los objetivos son:

+ Que quede explícito hacia otros en el equipo cuáles son las suposiciones que tenemos de los datos
+ Validar nuestras suposiciones como parte del día a día como científicos de datos (en unit testing)
+ Generar confianza de que los datos con los que estamos trabajando cumplen con las suposiciones bajo las cuales construimos todo nuestro *pipeline* de ETL y modelado.


Esta librería está construida sobre `pytest` por lo que no tenemos que hacer mucho más que agregar la parte de *assumptions* a las pruebas que queremos hacer sobre nuestros datos.


### Referencias

+ [PyData conference: Unit testing for data scientists](https://www.youtube.com/watch?v=Da-FL_1i6ps)
+ [PyTest](https://docs.pytest.org/en/latest/)
+ [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf)
+ [Marbles API](https://marbles.readthedocs.io/en/stable/quickstart.html)
+ [Python mocking 101: Faking it before you make it](https://www.fugue.co/blog/2016-02-11-python-mocking-101)
+ [API Pytest](https://docs.pytest.org/en/latest/reference.html#)
+ [Marbles: PyData Amsterdam 2018](https://www.youtube.com/watch?v=enlNiRSt9nk)
