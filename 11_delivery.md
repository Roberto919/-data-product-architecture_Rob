![](./docs/images/itam_logo.png)

M. Sc. Liliana Millán Núñez liliana.millan@itam.mx

Mayo 2020

## Delivery

### Agenda

+ SFTP
+ API
  + Flask
+ Dashboard

### SFTP

Acrónimo de *Secure File Transfer Protocol*. Este tipo de *delivery* implica que tenemos que depositar un archivo (normalmente csv) en un servidor remoto en un lugar particular las predicciones cada $x$ tiempo.

Si esta es la forma de entrega recuerda establecer un estándar en el nombre de los archivos para que sea muy claro qué se entregó cuándo. Por ejemplo, si estas entregando las predicciones de quién hará churn en esta semana, el nombre debería quedar algo asi: `churn_20200501_predictions.csv`.

Para que esto funcione previamente se deberá haber definido junto con el cliente el formato y tipo de datos que van en el csv para que no se modifique.

### API

Acrónimo de *Application Programming Interface*. Un(a) API nos permite poder acceder a desarrollo de alguien más de manera programática. Donde alguien más puede ser una empresa, una ONG, un proyecto escolar, etc. Nos permiten compartir datos entre diferentes piezas de *software*, en particular a través de Internet.

Por ejemplo: La mayoría de sus proyectos utilizan una API a través de la cuál obtienen los datos que necesitan para sus productos de datos.

![](./images/pointer.png) La forma más eficiente de integrar nuestro trabajo como científicos de datos a una empresa/proceso es utilizar una API para "exponer" las predicciones de nuestro modelo. De esta manera, el área de sistemas "solo" tiene que hacer una petición a la API para obtener los resultados del modelo.

También preferimos ocupar APIs porque de esta manera nos aseguramos que el desarrollo o implementación de los modelos están bien hechos -los hicimos nosotros con nuestras herramientas de trabajo: R, Sklearn, PySpark, etc.- y que no hubo ningún cambio en el código que pueda ser problema. --> ¡No queremos que ingenieros de software implementen nuestra solución!.

#### Protocolos para API

+ SOAP: Acrónimo de *Simple Object Access Protocol*, en este protocolo el intercambio de datos se realiza a través de mensajes a través de Internet. Los mensajes SOAP están en formato XML y se utilizan sobre métodos de HTTP: POST, PUT, GET, DELETE, HEAD.  

+ REST: Acrónimo de *Representational State Transfer*, en este protocolo también conocido como *RESTful* el intercambio de datos se realiza entre servidor y cliente y hay varios formatos de entrega: JSON, XML, texto plano, etc., aunque el más utilizado es JSON. Dado que no hay un formato estándar, es más flexible que el protocolo SOAP y por lo tanto más utilizado, en un estudio del 2017, 81% de los APIs hosteados por [Programmingweb](https://www.programmableweb.com/news/which-api-types-and-architectural-styles-are-most-used/research/2017/11/26) eran REST vs 9% SOAP.

Cabe mencionar que el protocolo SOAP aún es muy utilizado en empresas financieras donde la comunicación entre sistemas legacy se realiza a través del protocolo SOAP.

El protocolo REST, también ocupa los métodos de HTTP para la transferencia de datos: PUT, POST, GET, etc.

+ Otros como GraphQL que empieza a tener cierta popularidad (desarrollada por Facebook).


#### Historia

Los API como tal existen desde el año 2000 y en los primeros 10 años, eran las grandes empresas las que tenían API como SalesForce, Amazon, Flickr, Facebook, Google, Foursquare, Instagram.

Hoy en día hay APIs en casi todos los sectores de la industria.

Desde 2014 las API correspondientes a servicios de datos, financieros, analítica hay ido en aunmeto.

El top 5 para 2019: Facebook, Google maps, Twitter, YouTube, Accuweather.

Seguro para el análisis de 2020 las API más llamadas serán de datos relacionados a COVID-19.


#### HTTP Methods

También conocidos como verbos, cada uno de estos métodos tiene un estatus de respuesta específico. Por ejemplo, el famoso 404 (Not Found) de cuando no encuentras una página -o recurso- es un posible estatus correspondiente a haber hecho un método POST o GET o PUT o DELETE.  

+ POST: Corresponde a una operación Create, se utiliza para crear nuevos recursos o exponer nuevos recursos.
+ GET: Corresponde a una operación Read, se utiliza para leer un recurso, este recurso se regresa en un formato de XML o JSON.
+ PUT: Corresponde a una operación Update, se utliza para que el recurso existente ahora tenga una actualización. También es posible que esta operación pueda Crear un recurso si la URI que se envía desde el cliente no existe.
+ DELETE: Corresponde a una operación Delete, se utiliza para eliminar un recurso existente.

|Método|Estatus OK|Estatus no OK|
|:----------|:-------------|:-----------|
|POST|201 (CREATED)|404 (NOT FOUND)<br>409 (BAD CONFLICT) el recurso ya existe|
|GET|200 (OK)|404 (NOT FOUND)<br>400 (BAD REQUEST)|
|PUT|200 (OK)<br> 201 si se creó|204 (NO CONTENT)<br>404 (NOT FOUND)|
|DELETE|200 (OK)|404 (NOT FOUND)|


#### Frameworks para API

Existen varios *frameworks* para desarrollar una API, en particular para python hay varias opciones: Flask, Bottle, Django, entre otros.

Ocuparemos Flask porque es muy sencillo de implementar y trae lo mínimo necesario para hacer una API por lo que si necesitamos más cosas necesitaremos agregar extensiones a Flask (de Flask) o bien si ya te sientes con más confianza a conceptos de ingeniería de software pasarnos a Djando.

Si en tu equipo de trabajo hay un ingenieró de datos entonces la opción uno debería ser Django que trae todo lo que pudieras necesitar: seguridad en las llamdas, soporte para aguantar n llamadas por segundo, tiempo de respuesta, etc. 

### Referencias

+ [Flask Documentacion](https://flask.palletsprojects.com/en/1.1.x/)
+
