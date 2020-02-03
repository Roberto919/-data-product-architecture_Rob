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

AWS tiene muchos (muchos muchos!) servicios, y sigue siendo la primera solución de servicios de la nube utilizada en la industria.

Nosotros nos concentraremos en algunos servicios que nos ayudarán a levantar un *cluster* con servicios de MapReduce -EMR-, 

### CI/CD

+ *Continuous Integration* CI
+ *Continuous Delivery* CD
