# Memoria
## Entrega 1
### 1. Propuesta general de diseño
 Propuesta de una interfaz sencilla estilo *stackoverflow* pero con comentarios de estilo *reddit* en varios niveles segun quien responde a quien. 
 
 El sistema de votacion puede ser estilo *reddit* o *stackoverflow* indistintamente, con enfoque en los puntos para el orden y como forma de recompensar al usuario, de esta forma como los comentarios mas votados aparecen primero no sera necesario que el usuario se tenga que leer todo.

 Un esquema simple de como apareceran los comentarios a una pregunta:
- Pregunta
  - Respuesta 1 
  - Respuesta 2 
    - Comentario a la respuesta 2 (👍)
  - Respuesta 3
    - Comentario a la respuesta 2 (👎)
  
#### 1.1 Diseño de las preguntas
Las preguntas podrian ser simples o se puede contemplar la opcion de agregar imagenes o texto enriquecido, se valorara segun complejidad durante el desarrollo del proyecto.

#### 1.2 Tipos de usuarios
En cuanto al la estructura de paginas podremos diferenciar entre las paginas para usuarios logeados y las de usuarios anonimos, a pesar que dentro de los logueados puedan existir distintos roles, los dos gradnes grupos son los anteriormente mensionados.

Un usuario no logueado:
- Podra ver las preguntas que hacen otros usuarios
- Al hacer click en una pregunta podra ver las respuestas a esta
- Se le dara la posibilidad de crearse una cuenta o iniciar sesion
- No se le permitira hacer nuevas preguntas o responderlas
- No podra votar las preguntas/respuestas
- No podra reportar preguntas/respuestas

Un usuario logueado podra realizar las actividades propias de su rol.

Por lo tanto se podra acceder a la pagina raiz o "inicio" sin estar logueado para tener una vision general de la aplicacion o a una pregunta en concreto, pero para hacer cualquier otra accion se tendra que estar logueado. El funcionamiento sera identico al de *StackOverflow*, de esta forma no sera necesario trabajar demasiado en la UX.

#### 1.3 Funciones de los usuarios

Dentro de los usuarios existen distintos roles:
- Discusion: Es el usuario standard, puede crear y responder preguntas.
- Moderador: Se encarga de atender los reportes sobre las preguntas y los comentarios.
- Administrador: Es un rol especial que solo lo tendra el primer usuario creado "admin"

Un usuario Moderador no podra publicar preguntas/respuestas y un Discusion no podra moderar.

#### 1.4 Elementos principales

La base de las aplicacion son las preguntas con respuestas a modo de resolucion y comentarios a la respuestas valorandolas, segun si son utiles o no. La dinamica es extremadamente parecida a la de *StackOverflow*.

- Pregunta (El usuario plantea un problema):
  - Tiene un titulo y un cuerpo
  - Puede ser votada (Positivo o Negativo)
  - Tiene un Autor
  - Tiene una fecha de creacion
- Respuestas (Los usuarios proponen soluciones):
  - Solo tienen cuerpo
  - Pueden ser votadas (Positivo o Negativo)
  - Tienen un autor
  - Siempre tienen una única pregunta asociada
  - Tienen una fecha de creacion
  - Otros usuarios con rol "Discusion" podrán valorar mediante comentarios si es útil o no.
- Comentario (Valoracion de una respuesta)
  - Solo tienen cuerpo y una mayor restriccion de longitud
  - Tienen asociado una valoracion sobre la respuesta *positiva, negativa o neutra*
  - Se mostrará la fecha de creacion y su autor
  - Tendran un tamñano mas reducido en pantalla
  - Se sombrearan según la valoracion
  - Podran ser votados para resaltar los mas útiles

#### 1.5 Respuesta
Para responder a una pregunta realizada por un usuario, se ha creado una macro, llamada respuesta y que, como es de esperar, contiene la respuesta a una pregunta realizada por un usuario.
En el fichero respuesta.html podemos encontrar:
  -En primer lugar, los imports tanto de la macro input como de los botones y del contenedor de respuestas creado.
  -Posteriormente, se visualizará "Respuesta" y, a continuación, el contenido concreto de la respuesta.
  -Una vez visualizado este, el usuario visualizará por pantalla las acciones que puede realizar. Estas son: Votar, responder, añadir un comentario, dar feedback(positivo, negativo o neutro) y, por último, reportar la respuesta.
  -Además, al final aparecerá el nombre del usuario que ha respondido junto con la fecha y la hora en la que lo hizo.
  Estos datos se sacarán del backend.
El acceso a la respuesta se realizará desde "/respuesta".
Cuando deseemos implementar esta macro, lo primero que debemos de realizar es un import de ella.
Y, cuando queramos ver el contenido de la respuesta lo llamaremos utilizando {{ respuesta.contenidoRespuesta }}.
Por si además se desea crear una nueva respuesta, se ha implementado un botón "Crear respuesta", que se visualizará despues del contenido de la respuesta.


#### 1.6 Respuesta (Votaciones)
Para llevar a cabo las votaciones de las preguntas y las respuestas se han creado dos macros correspondientes con los botones para votos positivos y para votos negativos. Dichas macros se encuentran en el fichero "buttons.html", obteniendo cada una de ellas características especiales como el color de fondo (verde en caso de voto positivo y rojo en caso de voto negativo) y el texto que contiene (vote Up en caso de voto positivo y vote Down en caso de voto negativo), tambien se realiza una llamada en cada caso al método correspondiente cuando es pulsado (voteUp() en caso de voto positivo y voteDown() en caso de voto negativo). Los metodos a los que se llaman cuando se pulsa el boton se encuentran en el fichero votos.py, en el que se ha creado la clase Voto con cuatro metodos posibles: El primero "voteUp" hará que se sume un punto positivo a los votos de la pregunta/respuesta. El segundo "unvoteUp" se llamará en caso de querer anular el punto positivo de la pregunta/respuesta en caso de haber sumado previamente dicho punto. El tercero "voteDown" hara que se sume un punto negativo a los votos de la pregunta/respuesta. Por ultimo, el cuarto "unvoteDown" se llamará en caso de querer anular el punto negativo de la pregunta/respuesta en caso de haber sumado previamente dicho punto. Adicionalmente, se ha creado un Endpoint para actualizar las votaciones de las preguntas/respuestas, quedando tambien reflejado en el frontend.


#### 1.8 Creaccion de preguntas

El usuario tendra la opcion de poder crear preguntas, para ello se ha creado un template (el cual extiende de "base.html") llamado crear_preguntas.html.
En este archivo encontramos los siguientes componentes:
  - Un import de la macro de los botones, en el cual agregamos "submit_button" y "reset_button", este ultimo se ha creado para poder vaciar los campos del formulario al crear la pregunta.
  - Un formulario con sus respectivos labels (Titulo de la pregunta y Detalles de la pregunta), inputs ("titulo" de tipo text, "detalles" de tipo textarea) y buttons (Enviar Pregunta y Vaciar Campos).
    - El boton "Enviar Pregunta" es de tipo "submit_button", su funcion sera gruardar: el nombre del usuario que ha realizado la pregunta, la fecha cuando se ha realizado la pregunta, el titulo de la pregunta y el detalle/descripcion de la pregunta.
    - El boton "Vaciar Campos" es de tipo "reset_button", su función es resetear (vaciar) los campos del formulario.
Para acceder a la creaccion de preguntas se hace desde "/crear_preguntas".



### 2. Consideraciones de para el desarrollo
#### 2.1 Docker
Por su simplicidad se han decidido modificar los ficheros de instalacion e inicio y asi permitir el desarrollo sin necesiadad de reinicios.
Se ha asumido que los desarrolladores actuales han instalado las imagenes, por lo que se ha comentado las lineas de *"/practica-dms-2022-2023/components/dms2223auth/bin/dms2223auth-create-admin"* para que no se intente volver a crear el usuario admin.
Si se requiriese reinstalar la maquina habria que desomentarlas o no sera posible loguearse en la aplicacion.

Ademas para permitir la compatibilidad con WSL2 se ha editado *" practica-dms-2022-2023/docker/config/dev.yml" liena 33* para enlazar el puerto 8080 de Docker con el 8080 de Windows.
#### 2.2 Modo debug
Para agilizar el desarrollo se ha configurado Jinja/Flask para actualizarsa cada vez que se produce un cambio en el frontend, asi no sera necesario reiniciar el servicio o la maquina docker cada vez que haga un cambio a la web. 
Para ello se ha modificado:

- *practica-dms-2022-2023/components/dms2223frontend/install.sh*: Se ha comentado la eliminacion del directorio temporal, es posible que requiera ser descomentado para nuevas instalacions.
- *practica-dms-2022-2023/components/dms2223frontend/bin/dms2223frontend*: Se ha añadido:
```
app.config["TESTING"] = True
app.testing=True
app.config.update(
    TEMPLATES_AUTO_RELOAD = True
)
```
Esto permite la recarga automatica de templates y codigo de las peticiones del mismo archivo. 
Es recomendable eliminar estas lineas en un futuro despliegue.

