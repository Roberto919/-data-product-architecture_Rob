![](./docs/images/itam_logo.png)
<br>

### Infraestructura

M. Sc. Liliana Millán Núñez liliana.millan@itam.mx

Febrero 2020

### Agenda

+ Seguridad
  + *Tunneling*
  + SSH, llaves privadas, llaves públicas
+ AWS
  + S3
  + EMR
  + EC2
  + RDS
+ Configuración de tu *cluster*
+ Conceptos de CI/CD

### Seguridad

+ *Tunneling*

Concepto de redes, una forma de comunicación entre dos dispositivos de una forma "segura" a través de usar redes públicas consideras inseguras. Existen diferentes protocolos para poder realizar esta comunicación, uno de los más comunes es SSH (otro son las VPN).

+ SSH: *Secure Shell*

Un tipo particular -protocolo- de *tunneling* a través del cual podemos realizar *logins* y transferir archivos sobre redes no confiables ya que los datos que viajan a través de este tipo de *tunneling*, viajan encriptados. Este es el protocolo que se ocupa para usar los servicios de AWS.

![](./docs/images/ssh_tunneling.png)
<br>
Fuente: [SSH.COM](https://www.ssh.com/ssh/tunneling)

Este protocolo utiliza como método de autenticación un par de llaves: privada y pública- para dar acceso a las personas seleccionadas en los dispositivos seleccionados.

La generación de estas llaves está basada en algoritmos de encriptación asimétricos -existen dos llaves-, en particular la de SSH está basada en el algoritmo [RSA](https://www.di-mgt.com.au/rsa_alg.html) que utiliza números primos muy grandes como parte de su *core*.

**Llave pública:**

La llave que compartes con todo el mundo y que no tienes que recordar, solo la envías al administrador de la red que debe ponerla en el servidor de SSH. Aquellos que tienen tu llave pública pueden generar datos encriptados que solo el que tenga la llave privada podrá descifrar.

Una vez que la llave pública está en el servidor de SSH y verifica que es válida y correcta, la pone como una llave autorizada en el archivo *authorized_keys*.

**Llave privada:**

La otra parte de la llave, está **no** se debe compartir con nadie! ni copiar y pasar a otros dispositivos (es mejor un par de llaves por cada dispositivo), el que tiene esta llave es considerado el dueño de la llave pública.

#### SSH Keygen

Para crear este par de llaves necesitarás un programa que te las generes.

+ Linux `ssh-keygen`que ya viene en tu sistema operativos.
+ Mac, también tiene `ssh-keygen`.
+ Windows [PuTTYgen](https://docs.joyent.com/public-cloud/getting-started/ssh-keys/generating-an-ssh-key-manually/manually-generating-your-ssh-key-in-windows)

##### Linux

1. Abre tu terminal, y pon `ssh-keygen`. Esto iniciará la creación de un par de llaves.
2. El programa te pedirá la ruta y nombre del archivo donde quieres guardar la llave. Deja la que tiene por *default*, a menos que ya tengas una llave creada antes: `id_rsa.pub` e `id_rsa`. Puedes cambiarle el nombre sin problema.
3. Te pedirá una `passphrase` para generar la llave, que servirá como semilla aleatoria para poder generar las llaves. **No** se te vaya a olvidar este `passphrase` porque te lo pedirá cuando quieras conectarte a tu infraestructura de AWS.
4. Si todo se generó correctamente te mostrará un *output* "raro" con caracteres y te indicará que ocupó el algoritmo de RSA de 2048 bits utilizando SHA256 -genera un *hash* de 256 bits sin colisiones-.

![](./docs/images/pointer.png) Entonces necesitarán tener las llaves públicas de los miembros de sus equipos para que puedan compartir la misma infraestructura, y también la mía para que pueda meterme a verificar su infraestructura.

### AWS

Acrónimo de *Amazon Web Services*, los servicios de infraestructura en la nube de Amazon, que desde hace rato conforma la unidad de negocio más *profitable* de Amazon.

AWS tiene muchos (muchos muchos!) servicios, y sigue siendo la solución de servicios de la nube más utilizada en la industria. Otros proveedores son Microsoft con Azure, Google con *Google Cloud Platform*, IBM con IBM *Cloud Services*.

Nosotros nos concentraremos en algunos servicios que nos ayudarán a levantar un *cluster* con servicios de MapReduce -EMR-, y a tener un *cluster* con computadoras pequeñas que nos permitan tener una base de datos relacional -EC2, RDS respectivamente-.

También ocuparemos el servicio de almacentamiento de archivos de AWS, S3 que si bien no está definido como un DFS seguramente por debajo tiene muchas de las cosas de DFS. Para interactuar de manera más sencillas con algunos de estos servicios ocuparemos el CLI (*Command Line Interface*) de AWS que puedes instalar usando  `pip install awscli` en tu ambiente `pyenv` de esta materia.

Si tienes varias cuentas de AWS -tu trabajo y la escuela- puedes crear un archivo `credentials` (sin extensión) para almacenar todos los pares de `aws_access_key_id` y `aws_secret_access_key`. Este archivo se encuentra bajo el directorio `~/.aws` (este directorio se crea cuando instalas awscli). Cuando crees tu cuenta de AWS educativa tendrás que generar un par de access key de aws.

#### EC2

Este servicio de AWS nos permite crear instancias de computadoras con sistemas operativos instalados, y dependiendo de nuestras necesidades podemos escoger entre instancias optimizadas a procesamiento, a almacenamiento, a CPU, a memoria, etc. Debido a todas estas posibles combinaciones hay muchos tipos de instancias disponibles en AWS por lo que te servirá conocer los [tipos de instancia de EC2](https://aws.amazon.com/ec2/instance-types/).

+ VPC *Virtual Private Cloud*: Nos permite aprovisionar un espacio lógico en la nube de AWS para que podamos poner nuestras instancias EC2 a las que solo quienes definamos tengan acceso. Cuando cread una VPC tienes que definir un rango de direcciones IP4 en la forma de un *CIDR block (Classles Inter-Domain Routing)*, por ejemplo: `10.0.0.0/16`.

+ *Subnet*: Dentro de la VPC puedes crear un rango de direcciones para poner instancias EC2 específicas. El acceso a estas subredes se determina a través de los *Inbounds* y *Outbounds*.

+ IPs *Inbounds* y *Outbounds*: Las IPs *Inbound* indican las IPs que tienen acceso a una *subnet*, mientras que las *Outbound* indican las IPs hacia las que puede ser enviada la salida, un asterisco \* indica cualquier IP.

+ Redes públicas y privadas: Las redes privadas tienen definidas IPs específicas que tienen acceso a los recursos dentro de ella, una VPC genera una red privada.

+ *Elastic IPs*: Es una IP estática a través de la cual podemos acceder a nuestro VPC sin importar la IP interna a la VPC/Subnets. Esta IP es la misma para nosotros pero por abajo cambia dinámicamente a la instancia que se encuentre "levantada". Este tipo de IP se utiliza para asegurar que sin importar si una instancia está disponible o no, la accesibilidad a nuestra aplicación está asegurada. 

+ AMI *Amazon Machine Image*: Máquina de Amazon que ya tienen imagenes de sistemas operativos o configuraciones específicas instaladas. Por ejemplo, existe un AMI para *deep learning* en donde ya no te tienes que pelear con instalar las librerías en las versiones correctas o configurar los *drivers* de NVIDIA, etc.

La arquitectura que construiremos en DPA es la siguiente:

![](./docs/images/ec2_subnets.png)
<br>

![](./docs/images/ec2_architecture.png)
<br>

#### Creación de usuarios en buntu

[Pasos](https://www.cyberciti.biz/faq/create-a-user-account-on-ubuntu-linux/)

1. Como usuario `ubuntu` crea los usuarios de cada miembro del equipo.  
2. Crea cada usuario a través del comando `sudo adduser username`, conforme se crea el usuario ubuntu te pedirá un password **no** olvides ese password! cada usuario lo necesitará para conectarse al bastión. Entre los datos que te pedirá para el usuario está el nombre y otros datos particulares, no ingreses ninguno.

Para corroborar que el usuario fue creado puedes cambiar de usuario de  `ubuntu` al recién creado utilizando `sudo su username`.

#### Agregar credenciales


### CI/CD

+ *Continuous Integration* CI
+ *Continuous Delivery* CD


### Referencias, ligas de interés

+ [AWS VPC and Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html#vpc-subnet-basics)
+ [CIDR Block](https://tools.ietf.org/html/rfc4632)
