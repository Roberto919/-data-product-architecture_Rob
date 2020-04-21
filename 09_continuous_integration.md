![](./docs/images/itam_logo.png)

M. Sc. Liliana Millán Núñez liliana.millan@itam.mx

## Continuous integration CI

### Agenda

+ Pruebas de código
+ Tipos de pruebas
+ Pruebas unitarias
+ Unittest
  + Asserts
  + Fixtures
  + Mocks
+ Unit test para DS/ML


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

1. Un grupo opina que es mejor diseñar la prueba de unidad **antes** de hacer la función *Test-driven development*. De esta manera evitas estar sesgado a la implementación que ya hiciste. $\leftarrow$ recuerda que tú eres quien desarrolla la prueba unitaria de la función que desarrollaste!
2. Otro grupo opina que es mejor diseñar la prueba de unidad **después** de hacer la función, pues para este momento ya sabes qué hiciste y cómo lo hiciste.

Ambos tienen puntos a favor y puntos en contra, sin embargo para poder aplicar la primer opción requieres tener mucha experiencia tanto desarrollando software como en desarrollar pruebas unitarias. En nuestro caso haremos la segunda opción, primero haremos la funcionalidad y luego haremos la prueba de unidad, porque además, pruebas unitarias para ciencia de datos son "un poquito" diferentes a las de software... hay cosas que no son determinísticas!

+ Métrica: cobertura , *successful vs failed*

#### Unit Testing

`unittest` es uno de los *frameworks* más utilizados de pruebas de código. Está basado en JUnit (del mundo de java), estaremos utilizando éste *framework* en python en lugar del PyTest **solo** porque `marbles` -una librería que veremos más adelante- está basado en este framework, de otra forma ocuparíamos PyTest.

En realidad todos los *frameworks* de pruebas unitarias se parecen mucho en su funcionamiento, solo cambian algunos detalles.

Esta librería es parte de Python base. Algunas reglas de `unittest`.

+ Las pruebas se corren sobre scripts de python **no notebooks**. Existen extensiones para que puedas probar *notebooks*, pero es mejor crear los *scripts* asociados a tus *notebooks* pues formarán parte de un *pipeline*.
+ Tus *scripts* de prueba deben vivir en un archivo (hasta directorio) aparte. Cada función de prueba debe tener el prefijo *test_* para que pueda ser identificado por el *test runner*.
+ La clase donde viven las funciones de prueba debe ser de tipo *unittest.TestCase* y el nombre de la clase debe tener el prefijo *Test*. Recuerda que las clases en Python inician con mayúscula y son *CamelCase* (a diferencia del *snake_case* de R o Python en código normal).
+ En el *path* donde corras el comando de `unittest` se buscarán scripts de prueba tanto en ese directorio como en subdirectorios.

#### Lingo

+ *test fixture*: Los recursos y condiciones iniciales que una prueba unitaria puede requerir para ser probada de forma aislada. Por ejemplo, Si queremos probar una sección particular de el código de transformación de variables realizado en PySpark, no queremos que la prueba también sea probar obtener la sesión de Spark y etc. También incluye la limpieza de esos recursos una vez que la prueba termina.
+ *test case*: Es la prueba de unidad que queremos realizar.
+ *test suite*: Un conjunto de pruebas unitarias que se deben ejecutar juntas. También pueden tener un *test suite* de *test suites*.
+ *test runner*: El orquestador de las pruebas de unidad, es el encargado de encontrar todas las pruebas que se tienen que ejecutar y gestionar los recursos que estas pruebas requieren, por ejemplo *fixtures*.

##### Asserts

Es la forma en la que en los *frameworks* de pruebas unitarias se revisa la salida obtenida de un método. Dependiendo del *framework* existen diferentes formas de ocupar los *asserts*. En `unittest` existen los siguientes `asserts`:

+ `assertEqual()`: Para ver si el valor de un parámetro es lo que estabas esperando.
+ `assertTrue()`: Si la condición es verdadera.
+ `assertFalse()`: Si la condición es falsa.
+ `assertRaises()`: Para verificar que ser haya efectivamente levantado una excepción cuando tenía que levantarse.
+ `assertAlmostEqual()`: Si el valor está en un rango -por aquello de precisión en números flotantes-.
+ `assertWarns()`: Puedes verificar que se haya generado un *warning*   

**Ejemplos:**

En la carpeta `testing`, los *scripts* `test_asserts.py` y `test_exceptions.py` ocupan `asserts` diferentes. Para correr estos *scripts* ocupa el comando `python -m unittest script` (dentro del directorio que contiene las pruebas). Puedes agregar la bandera `-v` para tener más información de la corrida de las pruebas.


#### Numpy unit test

La librería de Numpy tiene sus propios métodos `assert`!, adecuados a las funciones que se ocupan en Numpy. Por ejemplo, puedes verificar que un arreglo de Numpy cumpla con algunas condiciones.

**NOTA:** Los `assert` y métodos de `unittest` siguen la convención *CamelCase*, mientras que el resto de las librerías de "datos" siguen la convención *snake_case*, esto es porque `unittest` viene del mundo de JUnit (Java) y en Java la convención de nombres sigue *CamelCase*.

```
a = np.array([0.54, 0.33])
b = np.array([0.13, 0.22])

def test_sum():
  self.assertAlmostEqual(a+b, np.array([0.678, 0.554]), 2)
```

#### Pandas unit test

Pandas también tiene su propio *set* de funciones que ayudan a realizar *unit testing* muy acoplado a la manipulación y análisis de datos :). Los métodos disponibles se encuentran en la sección [*General utility functions*](https://pandas.pydata.org/pandas-docs/stable/reference/general_utility_functions.html).

Por ejemplo, podemos verificar si el contenido de un DataFrame es el que estamos esperando:

```
def test_df(self):
    df_1 = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
    df_2 = pd.DataFrame({'a': [1, 2], 'b': [3.0, 4.0]})

    pd._testing.assert_frame_equal(df_1, df_2)
```


##### Fixtures

Son objetos que nos permiten hacer un *setup* inicial y que sirven para no tener que estar repitiendo el mismo código en todos los lugares donde ocupas esa configuración en tus pruebas.

Un *fixture* muy utilizado es la definición de un *DataFrame*, o una sesión de Spark, o una conexión a una BD.

En `unittest` se ocupan dos métodos:

+ `SetUp()`: Éste método corre antes de la prueba.
+ `TearDown()`: Éste método corre después de la prueba.
+ `SetUpClass()`: Corre antes de que se ejecute cualquier prueba en la clase de prueba, las configuraciones que se realizan aquí están disponibles para todos los métodos en la clase.
+ `TearDownClass()`: Corre después de que se ejecuten los métodos de la clase.

**NOTA:** Hasta este momento no habíamos comentado que el orden en el que se ejecutan las pruebas es ordenado de acuerdo al nombre de la prueba. **No** hay secuencia entre pruebas, pues no estamos haciendo una prueba de integración, por lo que debe ser posible ejecutar las pruebas bajo cualquier orden -son pruebas unitarias!-.




##### Mocks

+ Objetos que te permiten "simular" otros elementos en tu código que requieres en tu prueba, pero que no quieres realmente ocuparlos. Por ejemplo:
  + Conexiones a bases de datos: No quisieras tener que hacer todo el proceso de conexión a una base de datos **real** para poder obtener datos reales y luego probar lo que estabas interesado en probar.
  + Acceso a API
  + Acceso a red
  + ...

La llamada a un objeto *mock* devuelve un valor predeterminado sin hacer nada. Los objetos *mock* se encuentran en el módulo `unittest.mock`. Los objetos más importantes son `patch` -que es un decorador- y `MagicMock`.

Para crear un objeto *mock* ocupas un objeto `patch` y cuando `patch` es llamado, se genera un objeto `MagicMock` que es lo que se regresa. Basta con que configuremos el `MagicMock` para que nos regrese lo que necesitemos para simular un objeto.

Por ejemplo, si en una prueba unitaria necesitas conectarte a una API, pones un `patch` en la llamada al API, eso te regresará un `MagicMock` el cuál configuramos para que te regresará una cierta estructura de datos -aquí no estamos probando la llamada al API sino algo que ocupa los datos obtenidos a través de la API-.

De esta manera aislas la prueba a lo que de verdad quieres probar, "deshaciéndote" de todo lo que te estorba para probarlo. No deberías de necesitar tener muchos `patch` en una prueba, si sí, es una buena señal de que tu función hace varias cosas, por lo que deberás simplificarlo.


El `patch` será ocupado como un decorador a la función que queremos probar y para el `MagicMock` necesitaremos configurar el `return_value` y el `side_effect`.

+ `return_value`: Corresponde a lo que regresaría el objecto real al que estamos haciendo *mock*. Por ejemplo, si estamos haciendo la llamada a un API, el `return_value` normalmente es un JSON, un csv, un zip, etc., inclusive puede ser un objeto `MagicMock`! Nosotros regresaremos un valor real a una llamada real pero no a un objeto real.
  + `spec`: Dado que un `MockObject` puede regresar un `MockObject` es muy utilir ocupar en la configuración del `MockObject` un `spec` que indica de qué tipo de objeto en específico se tiene que regresar la respuesta.

+ `side_effect`: Este se ocupa cuando lo que quieres probar es que se levanta una excepción correctamente.

### Unit test para DS/ML

#### Marbles

Esta es una librería concentrada en hacer *unit testing* a **datos** -> *Data Unit Testing* -me emociono hasta de escribirlo!-. Esta pensada en que como científicos de datos, tenemos ciertas suposiciones sobre los datos con los que trabajamos y modelamos, y que el *unit testing* que necesitamos debe estar enfocado en los datos.

Esta librería te permite hacer pruebas unitarias para comprobar que las suposiciones que tenemos sobre los datos se siguen sosteniendo con nuevos datos (o con los mismos después de hacer transformaciones o *pipelines* de preprocesamiento).

Los objetivos son:

+ Que quede explícito hacia otros en el equipo cuáles son las suposiciones que tenemos de los datos
+ Validar nuestras suposiciones como parte del día a día como científicos de datos (en *unit testing*)
+ Tener confianza de que los datos con los que estamos trabajando cumplen con las suposiciones bajo las cuales construimos todo nuestro *pipeline* de ETL y modelado.

¿Qué es diferente en esta librería que `unittest` no haya cubierto?

Recuerda que *Unit testing* viene del mundo de ingeniería de *software* en donde lo que queremos probar es el código. En esta librería un fallo en una prueba unitaria no necesariamente implica que el código está mal, sino que tal vez los datos están mal, y que de ser así puede ser posible que inclusive los datos al llegar a tu organización ya estaban "mal".

Marbles nos permite dar un contexto sobre esa prueba unitaria, sobre las validaciones que estas haciendo a tus datos y también saber qué hacer bajo ciertas circunstancias.

Esta librería está construida sobre `unittest` no sobre `pytest` razón por la cual vimos antes `unittest`. Dado que está construida "sobre" *unittest* se puede ampliar la funcionalidad de pruebas que ya estaban escritas en *unittest* para mejorar los mensajes de salida y brindar contexto.

Para ocupar *marbles* como *unit testing*:

+ Necesitas instalar en tu ambiente virtual de pyenv/virtualenv/conda/anaconda de la clase un `pip install marbles`.
+ En lugar de importar `unittest` tendrás que importar `marbles.core`.
+ En lugar de correr las pruebas con `python -m unittest` hay que correrlas con `python -m marbles`.

Dado que en marbles lo más importante es el contexto, los mensajes de salida cuando una prueba falla, incluyen más información.

1. Agrega el código "alrededor" de donde se originó la falla.
2. Agrega la visualización de los valores en las variables locales (las públicas), para tener contexto de cómo estaba el "estado del mundo" en el momento de la falla. Esto evita tener que estar poniendo prints por todos lados <- qué por cierto es una muy mala práctica para hacer debugueo!.
3. Agrega una **nota** generada por el autor de la prueba unitaria para tener el contexto correcto.  

La diferencia entre el mensaje de una prueba unitaria normal de *unit testing* y la nota de marbles, consiste en que la primera debe ser un mensaje corto, concreto y no ambiguo del error, mientras que la segunda es el contexto asociado a lo que estamos probando; es aquí donde deberíamos poner la severidad del error, o qué es lo normal de esperar en esa prueba.

Marbles también agrega sus propios métodos de `assert` a través del módulo `mixins`.

![](./images/pointer.png) Ver el script `test_mixins.py`.

![](./images/pointer.png) Marbles se acomoda muy bien al *pipeline* para validar que los datos que vas a procesar cumplen las suposiciones del EDA. Puedes validar que una variable tiene un rango permitible de valores nulos, o rangos de valores que esperas, etc.

#### Bulwark

`pip install bulwark`

Esta librería nos permite hacer pruebas sobre suposiciones que tenemos de los datos en forma y tipo, por lo que está más enfocada a la parte del ETL y DataFrames.

Esta librería ocupa decoradores sobre las funciones para hacer explícitas las suposiciones que estamos haciendo sobre los datos.

Por ejemplo:

```
import bulwark.decorators as dc

    @dc.IsShape((-1, 10))
    @dc.IsMonotonic(strict=True)
    @dc.HasNoNans()
    def compute(df):
        # complex operations to determine result
        ...
    return result_df
```
Fuente: [Bulwark](https://github.com/zaxr/bulwark)

Ejemplo en el *script* `test_bulwark.py` (`python test_bulwark.py`)

#### Hypothesis

`pip install hypothesis`

Esta librería está enfocada en verificar *propiedades* en los datos. Dado que casi siempre pensamos en "corto" sobre las pruebas que tenemos que realizar a los datos, esta librería nos ayuda a encontrar *corner cases*.

Funciona generando datos aleatorios que cumplen con las especificaciones que nosotros definimos, verifica que las pruebas se siguen cumpliendo con estos nuevos datos. Si encuentra una muestra que "rompe" la prueba, la hará más pequeña hasta encontrar cuál es el problema. Guarda ese ejemplo para después para no olvidar el problema que causó en tu código en el futuro.

La definición de las pruebas en este sentido consiste en decidir y definir qué garantias o propiedades debe cumplir el código siempre, sin importar los datos que entren. Por ejemplo: Si borras un objeto ya no es visible en ningún lado, si serializas y deserializas un objeto debe ser exactamente el mismo.

Al igual que Bulwark, funciona con decoradores sobre las funciones que quieres probar.

Ejemplo en el *script* `test_hypothesis.py` (`python -m unittest test_hypothesis`)

#### Feature forge

`pip install featureforge`

Esta librería está pensada para procesos de ML y sobretodo `sklearn`
, aunque enfocada en la parte de generación de *features*.

Esta librería nos permitie verificar que las supociones que tenemos de los datos durante su *pipeline* de transformación se sostiene.


### Referencias

+ [Unittest documentación](https://docs.python.org/3/library/unittest.html)
+ [Numpy unit test](https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.testing.html)
+ [Pandas unit test](https://pandas.pydata.org/pandas-docs/stable/reference/general_utility_functions.html)
+ [Marbles API](https://marbles.readthedocs.io/en/stable/quickstart.html)
+ [Marbles: PyData Amsterdam 2018](https://www.youtube.com/watch?v=enlNiRSt9nk)
+ [PyData conference Seatle 2015: Testing for Data Scientists](https://www.youtube.com/watch?v=GEqM9uJi64Q)
+ [PyData conference: Unit testing for data scientists](https://www.youtube.com/watch?v=Da-FL_1i6ps)
+ [Python mocking 101: Faking it before you make it](https://www.fugue.co/blog/2016-02-11-python-mocking-101)
+ [Bulwark](https://github.com/zaxr/bulwark)
+ [Bulwark API](https://bulwark.readthedocs.io/en/latest/api.html)
+ [Hypothesis](https://hypothesis.readthedocs.io/en/latest/)
+ [FeatureForge git repo](https://github.com/machinalis/featureforge)
+ [FeatureForge Documentation](https://feature-forge.readthedocs.io/en/latest/)
+ [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf)
+ [PyTest](https://docs.pytest.org/en/latest/)
+ [API PyTest](https://docs.pytest.org/en/latest/reference.html#)
