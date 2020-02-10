![](./docs/images/itam_logo.png)
<br>

M. Sc. Liliana Millán Núñez liliana.millan@itam.mx

Febrero 2020

### Agenda

+ Formatos de almacenamiento
  + Parquet
  + Avro
+ Formatos de compresión para almacenamiento distribuido
+ ETL
+ Pipelines (data)


### Formatos de almacenamiento

#### [Parquet](https://parquet.apache.org/)


-   Proyecto de Apache.
-   **Formato columnar preferido para manejar set de datos de gran escala**:
    -   Funciona mejor para *queries* que solo requieren un pequeño subconjunto del total de columnas de una tabla -de no ser así es mejor ocupar el formato por renglón tradicional-.
    -   No tiene que hacer la decompresión y I/O de columnas que no forman parte del *query*.
    -   Es eficiente en compresión porque normalmente la entropía -0 homogéneo, 1 heterogéneo- en una columna es más baja que la entropía por renglón -diferentes atributos-.
-   Permite regresar solo los atributos requeridos.
-   Eficiencia en compresión -por naturalieza-, es posible definir el nivel de compresión por columna.
-   Diseñado para soportar estructuras de datos complejas: mapas, arreglos, etc.
-   Guarda los metadatos del archivo al final del mismo.
-   Puede leer y escribir con los API de avro ＼(＾O＾)／.
-   Utiliza un *encoding* de esquema eficiente.
-   Soporta tipos de datos primitivos, lógicos y *nested*.
-   Al igual que avro, es *compressible* y *splittable*, características importantes en sistemas de archivos distribuidos ya que son más eficientes en tareas de *MapReduce*.

**Ejemplo:**

![](./docs/images/columnar_format.png) Fuente: [NoSQL Database Concepts, Bhaskar Gunda](https://www.slideshare.net/BhaskarGunda/nosqldatabaseconcepts-64494185)

**Ejercicio 1:** ¿Cómo quedaría la siguiente tabla con un formato columnar?

![](./docs/images/db_ex.png)
<br>

#### [AVRO](https://avro.apache.org/)

-   Proyecto de Apache.
- Este **no** es un formato columnar, es un formato de renglón.
-   Un lenguaje de serialización de datos neutral: los datos son descritos a través de un esquema independiente de lenguaje.
-   Guarda el esquema de los los datos -tipos de datos: numérico, string, etc.- en el *header* de cada archivo para que siempre pueda ser leído al mismo tiempo que los datos. Este formato es de tipo *compressible* y *splittable*, características importantes en sistemas de archivos distribuidos ya que son más eficientes en tareas de *MapReduce*.
-   Permite guardar la evolución del esquema ya que el esquema al momento de leer los datos puede ser diferente al momento de escritura -alguna manipulación en los datos puede cambiar su esquema original-.
-   Los esquemas de avro se escriben en JSON o en Avro IDL (C-ish) generalmente.
-   Utiliza tipos de datos simples y complejos: enums, arrays, maps, unions [Avro Data Types](https://avro.apache.org/docs/1.8.1/spec.html)
-   Una de las ventajas más grandes de avro, además de que guarda el esquema, es que se puede leer por otros formatos más adelante en el proceso. Por ejemplo: Es posible leer un avro en Spark y guardarlo como parquet ＼(＾O＾)／.


**Comparaciones entre Avro y Parquet**

Las siguientes comparaciones se realizaron con 2 datasets reales en un spark 1.6, la comparación completa la puedes encontrar [aquí](https://blog.cloudera.com/blog/2016/04/benchmarking-apache-parquet-the-allstate-experience/):

-   *Dataset* 1: Contiene 3 columnas y 82.8 millones de registros en formato CSV con un tamaño original de 3.6GB.
-   *Dataset* 2: Contiene 103 columnas con 694 millones de registros en formato CSV con un tamaño original de 194GB.

1. Cargar los datos:

+ *Dataset* 1

![](./docs/images/narrow_avro_parquet.png)
<br>

+ *Dataset* 2

![](./docs/images/wide_avro_parquet.png) <br>

2. Conteo de observaciones de una columna:

+ *Dataset* 1

![](./docs/images/narrow_row_count.png)
<br>

+ *Dataset* 2

![](./docs/images/wide_row_count_avro_parquet.png)
<br>

3. GroupBy

+ *Dataset* 1

![](./docs/images/narrow_group_by_avro_parquet.png)
<br>

+ *Dataset* 2

![](./docs/images/wide_group_by_avro_parquet.png)
<br>

4. Map simple

+ *Dataset* 1

![](./docs/images/narrow_map_avro_parquet.png)
<br>

+ *Dataset* 2

![](./docs/images/wide_map_avro_parquet.png)
<br>

5. Espacio en disco

+ Dataset 1

![](./docs/images/narrow_disk_space_avro_parquet.png)
<br>

+ *Dataset* 2

![](./docs/images/wide_disk_space_avro_parquet.png)
<br>

##### **Compresión**

En hadoop es importante seleccionar correctamente el formato de archivo que mejor sirva al propósito de lo que queremos hacer, seleccionar el formato incorrecto nos llevará a tener un desempeño pobre en Hadoop.

Normalmente los archivos en HDFS son almacenados en formato comprimido -recordemos que ocupamos HDFS para guardar grandes cantidades de datos!- pero debemos tener cuidado con el formato de compresión ya que hay algunos que no son *splittable* o que son *splittable* pero no secuencial -esto le podría dar en la torre a algún *set* de datos de serie de tiempo!-.

-   **Snappy:** Formato de compresión de Google optimizado para hacer compresiones rápidas con un nivel de compresión razonable, no es *splittable* por lo que requiere de ocuparse con algún formato que lo sea -avro, parquet-.

-   **LZO:** También está optimizado para hacer compresiones rápidas con un nivel de compresión razonable, a diferencia de `snappy`, este formato si es *splittable*. Su desventaja es que no viene como parte de la distribución de Hadoop por lo que hay que hacer otra instalación :(. Formato recomendado para archivos de texto plano.

-   **GZip:** Provee muy buen nivel de compresión a costa de la velocidad de compresión -2.5 veces lo que tarde Snappy, pero casi reduce a la mitad de lo de snappy-. Es igual de bueno en desempeño de lecturas sobre Hadoop pero al igual que snappy no es *splittable* por lo que requiere de ocuparse con algún formato que lo sea -avro, parquet-

-   **bzip2:** Provee un nivel de compresión excelente -9% mejor que GZip- pero es mucho más lento que cualquier otro formato, además de que en desempeño de lectura/escritura ya que en promedio puede tardar 10 veces más que Gzip. Este formato es *splittable* sin embargo no es recomendado para ocuparse en Hadoop por el performance mencionado, se recomienda ocupar solo si es necesario reducir el espacio ocupado en hadoop → eso solo ocurriría si se ocupa Hadoop como simple almacenador de datos.

-   Si utilizamos avro y/o parquet haremos que cualquier formato de compresión se haga *splittable* ＼(＾O＾)／.

Se recomienda tener un solo formato de archivo en el cluster, y la recomendación incluye ocupar uno que permita guardar esquema, eso solo nos deja avro o parquet. Es posible leer y escribir parquet desde los API de avro, pero no es tan sencillo de parquet a avro.


### ETL

*Extract Transform Load*