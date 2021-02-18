![](./images/itam_logo.png)

M. Sc. Liliana Millán Núñez liliana.millan@itam.mx

Febrero 2021

## Checkpoint 2: Ingestión y almacenamiento automatizado

Los datos de *Food Inspections* se actualizan de manera diaria, y contienen inspecciones realizadas desde el 2 de enero de 2020.

Necesitas leer lo que significa cada campo en el dataset [aquí](https://data.cityofchicago.org/api/assets/BAD5301B-681A-4202-9D25-51B2CAE672FF) y cómo utilizar la API [aquí](https://dev.socrata.com/foundry/data.cityofchicago.org/4ijn-s7e5).

Para poder ingestar estos datos a través de la API tendrás que generar un token, la explicación de cómo generar este token viene en la documentación mencionada anteriormente.

### Objetivos

+ Hacer la ingesta inicial de los datos de inspecciones de establecimientos de comida de la ciudad de Chicago.
+ Almacenar los datos históricos en S3.
+ Hacer la ingesta continua de los datos de inspecciones de establecimientos de comida de la ciudad de Chicago.
+ Almacenar ingestiones de nuevos datos en S3.


### Requerimientos

+ Python >= 3.7.4
+ Instalar el paquete `SODAP` (actualizar tu `requirements.txt`), y utilizar la clase `Socrata` para utilizar la API de inspecciones de establecimientos de comida de Chicago
+ Instalar el paquete `boto3` (actualizar tu `requirements.txt`)
+ Instalar `PyYAML` (actualizar tu `requirements.txt`)
+ Pickle


### Notas

Por *default* cada *endpoint* de la API solo te permite bajar 1,000 registros a la vez, por lo que tienes que definir un límite de 300,000 registros para poder bajar todos los datos históricos en la ingesta inicial.


### ¿Qué tienes que hacer?

Una vez que hayas leído la documentación de la API y cómo generar un cliente puedes iniciar esta sección.

Un script en tu carpeta `src/utils/` que se llame `general.py` que tiene la función `get_s3_credentials()` que lee de tu archivo `credentials.yaml` que se encuentra en tu carpeta `conf/local` las credenciales de aws y te las devuelve.

Un script en tu carpeta `src/pipeline` que se llame `ingesta_almacenamiento.py` a través del cual llamaremos a la API de inspecciones a establecimientos de comida de Chicago para cumplir con los objetivos del proyecto. Este script debe tener las siguientes funciones:  

+ `get_client`: Esta función regresa un cliente que se puede conectar a la API de inspecciones de establecimiento dándole un token previamente generado.

+ `ingesta_inicial`: Esta función recibe como parámetros el cliente con el que nos podemos comunicar con la API, y el límite de registros que queremos obtener al llamar a la API. Regresa una lista de los elementos que la API regresó.

+ `get_s3_resource`: Esta función regresa un resource de S3 para poder guardar datos en el bucket (checar script de `aws_boto_s3`).

+ `guardar_ingesta`: Esta función recibe como parámetros el nombre de tu bucket de S3, la ruta  en el bucket en donde se guardarán los datos y los datos ingestados en pkl.

El nombre del bucket es `data-product-architecture-equipo-n`

#### Para la ingesta inicial

La ruta del bucket es: `ingestion/initial/historic-inspections-2020-02-02.pkl`

![](./images/pointer.png) Necesitarás cambiar el `2020-02-02.pkl` por la fecha en la que hiciste la consulta inicial a la API de manera dinámica, leer la siguiente parte.

#### Para la ingesta consecutiva

La ruta del bucket es:
`ingestion/consecutive/consecutive-inspections-2020-11-03.pkl`

El **sufijo** de los archivos que se almacenan en el bucket debe llevar la fecha del día en la que se hizo la ingestión, se debe obtener de manera dinámica a través de la función `today` del paquete `datetime.time`

+ `ingesta_consecutiva`: Esta función recibe como parámetros el cliente con el que nos podemos comunicar con la API, la fecha de la que se quieren obtener nuevos datos al llamar a la API y el límite de registros para obtener de regreso.

El límite debe ser 1,000.


![](./images/pointer.png) Tendrás que conectarte a la API de Food Inspections y bajar los datos:
  + La primera vez que bajes los datos será histórico, todos los que existan.
  + La siguentes veces: lunes por la madrugada (4 am) sólo serán solicitando los días de la semana pasada -lunes a domingo-.


### Fecha revisión

**Martes 23 febrero 2021 23:59:59 CST**

+ Actualizar el `README.md` para incluir:
  + Información sobre versión de python y cómo instalar su `requirements.txt`.
  + Información de dónde está su EDA.
  + Información de cómo funciona su proceso de ingestión (resumen).
+ Actualizar `requirements.txt` con las librerías nuevas requeridas.
+ Correré su proceso de ingestión y verificaré que se generan las ingestas iniciales y las consecutivas.

![](./images/pointer.png) Tu script `ingesta_almacenamiento.py` **no** debe tener un `main`, solo debe tener las funciones mencionadas. Puedes probar tu script ejecutando desde línea de comando u otro script de python o un script de bash con tus diferentes funciones.

**Parte 2**

+ Agregar mi llave pública a su Bastión, verificaré que tengo acceso y que tengo un usuario `lmillan`

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCrry88D1cPQEDtNC5F5r9NntP3uwsw/FkVvsu3G84C8H+Ojpii1+uyOEmVpyXcP9Myx2w8kUFDbTPxwmTCm4WFQK4njg7IpF31Fvf6+sexFMV1RuDgRCmEQlKo20lfaWTd/fmuEYu30FOXoMGYw/G1RzM6hTLMiorOIGZwEGruZDhQSCZ64fk3Clzwfk4ShBeJUN/8REFOO0gbCm1XSdO+dqJFhc9fpFT163XMWuEsB4Z2YySbgW6+2jTvIRUcfVIMTFexLbSfwbGoYyVusdtgzmHNNNsnPP3jHIPMRe3WSyQEUpUOtrpvGlx1bxsumpNQOgIwomgTnq5aC6m9hE/CsHASbB+SDUm3Q1iK2SI1lPd7ArU/Bpdvh7Ld8marNGPZiy+oke8Z/lwURIuCvI3jPGsnLec+q1uAYuqdk1bVHjJAoA4LFyzkggvyral09wveop8BluXtHfEBNakp9n48pGbVkwZkopmPXu1u/wjTtNzb41vrI3JVGwJ7OJgWXoE= silil@turing
```
