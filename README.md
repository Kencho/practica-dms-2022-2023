![pylint score](https://github.com/Kencho/practica-dms-2022-2023/workflows/pylint%20score/badge.svg)
![mypy typechecking](https://github.com/Kencho/practica-dms-2022-2023/workflows/mypy%20typechecking/badge.svg)

# DMS course project codebase, academic year 2022-2023

The goal of this project is to implement a basic questions and answers appliance deployed across several interconnected services.

## Autores
- Arturo Carretero Mateo
- Álvaro Díez Sáez
- Estela Victoria Ballester Delgado
## Manual de instalación
Para realizar el proceso de instalación en el equipo es necesario descargarlo de github a través de la ventana principal del repositorio. Para descargarlo se debe
clicar en `<> Code` y posteriormente en `Download ZIP`.

![man-instalación1.png](imagenes/man-instalación1.png)

Cuando se haya descargado el archivo es necesario descomprimir dicho archivo para las posteriores ejecuciones en el terminal.

Para poder llevar a cabo la ejecución es necesario acceder a la carpeta descomprimida que se descargó anteriormente.

![man-instalación3.PNG](imagenes/man-instalación3.PNG)

Una vez se está en dicha carpeta se deben introducir una serie de comandos. En el caso de que sea
la primera vez que se ejecuta el programa en el ordenador se debe usar el siguiente comando para crear las imágenes de Docker requeridas:

```bash
docker-compose -f docker/config/dev.yml build
```

Cuando ya se han creado dichas imágenes de Docker se ejecuta la aplicación con el comando:

```bash
docker-compose -f docker/config/dev.yml up -d
```

Y para detener y retirar los contenedores se debe introducir el comando:

```bash
docker-compose -f docker/config/dev.yml rm -sfv
```

Una vez ejecutados estos comandos se puede ver como se han ejecutado y detenido exitosamente.

![man-instalación2.PNG](imagenes/man-instalación2.PNG)

## Manual de uso
- [DMS course project codebase, academic year 2022-2023](#dms-course-project-codebase-academic-year-2022-2023)
  - [Autores](#autores)
  - [Manual de instalación](#manual-de-instalación)
  - [Manual de uso](#manual-de-uso)
  - [Manual](#manual)
  - [Discussion](#discussion)
    - [Ver listado de discusiones](#ver-listado-de-discusiones)
    - [Crear discussion](#crear-discussion)
    - [Crear respuestas a preguntas](#crear-respuestas-a-preguntas)
  - [Moderador](#moderador)
    - [Ver pregunta individual](#ver-pregunta-individual)
    - [Ver listado de reportes y resolverlos](#ver-listado-de-reportes-y-resolverlos)
  - [Creación de nuevos usuarios](#creación-de-nuevos-usuarios)
  - [Components](#components)
    - [Services](#services)
      - [`dms2223auth`](#dms2223auth)
      - [`dms2223backend`](#dms2223backend)
      - [`dms2223frontend`](#dms2223frontend)
    - [Libraries](#libraries)
      - [`dms2223core`](#dms2223core)
  - [Docker](#docker)
  - [Helper scripts](#helper-scripts)
  - [GitHub workflows and badges](#github-workflows-and-badges)
  - [Línea futura](#línea-futura)
    - [Patrón de diseño a aplicar en la línea futura](#patrón-de-diseño-a-aplicar-en-la-línea-futura)

## Manual
Para la primera entrega teniendo en cuenta que será solo la parte del front-end tendremos las siguientes funcionalidades siendo el usuario "admin".
<br>Según accedemos a nuestro servidor con la dirección "172.10.1.30" tendremos el siguiente login:

![img_1.png](imagenes/img_1.png)

Accederemos con la contraseña y usuario "admin - admin".
<br>Una vez dentro, para poder interactuar como si fuésemos otro usuario tendremos que ir al apartado de gestión de usuarios.

![img_2.png](imagenes/img_2.png)

En el panel de administración podremos modificar nuestro rol permitiendo acceder al de discusión y moderador pudiendo hacer sus acciones según el rol.
También podremos crear nuevos usuarios.

![img_3.png](imagenes/img_3.png)

Guardamos para continuar.
## Discussion
Accederemos Discussion, teniendo acceso a sus posibilidades y vistas a través de la barra superior.

![img_4.png](imagenes/img_4.png)

Una vez en discusión podremos ver que tendremos acceso a las discusiones.

![img_5.png](imagenes/img_5.png)

### Ver listado de discusiones
Una vez en las discusiones vemos que tenemos acceso a la lista de discusiones, además de crear preguntas.

![img_7.png](imagenes/img_7.png)

### Crear discussion
Podremos crear la discusión que estará formada por el titulo y el contenido de este, al guardar los cambios esta pregunta pasará a formar parte del listado.

![img_8.png](imagenes/img_8.png)

### Crear respuestas a preguntas 
Accediendo a las diferentes discusiones podremos crear las respuestas y comentarios, además de votarlos según el feedback que le queramos dar y reportarlos.

![img_9.png](imagenes/img_9.png)

## Moderador
A continuación, cambiaremos el rol a moderador.

![img_10.png](imagenes/img_10.png)

Accedemos a las funcionalidades y vistas de moderador.

![img_14.png](imagenes/img_14.png)

Tendremos acceso tanto a los reportes en la sección de informes y a las discusiones.

![img_12.png](imagenes/img_12.png)

En el apartado de discusiones podremos ver un listado de las discusiones actuales.
<br>Podremos acceder a cada una de ellas de manera individual.

![img_19.png](imagenes/img_19.png)

### Ver pregunta individual
Podremos ver la pregunta de manera individual, pero sin ciertas funcionalidades disponibles como la de votar, reportar, etc...

![img_17.png](imagenes/img_17.png)

### Ver listado de reportes y resolverlos
En el apartado de informes del moderador tendremos acceso a la lista de reportes.

![img_20.png](imagenes/img_20.png)

Accediendo a uno de ellos de forma individual podremos resolverlos

![img_21.png](imagenes/img_21.png)

Al aceptar el reporte ocultaremos las discusiones al resto de los usuarios.
## Creación de nuevos usuarios
Para la creacion de nuevos usuarios accederemos al apartado de admin en la barra superior.
<br>Seguidamente accederemos a la parte de gestión de usuarios.

![img_23.png](imagenes/img_23.png)

Una vez ahí, tendremos la posibilidad de crear usuarios.

![img_24.png](imagenes/img_24.png)

Para poder crear el usuario tendremos que poner su nombre y contraseña nueva.

![img_25.png](imagenes/img_25.png)

Una vez que lo hemos creado lo editaremos para asignar su correspondiente rol.

![img_26.png](imagenes/img_26.png)

Aquí podremos cambiar el rol del usuario procediendo a guardar los cambios.

![img_27.png](imagenes/img_27.png)


## Components

The source code of the components is available under the `components` directory.

### Services

The services comprising the appliance are:

#### `dms2223auth`

This is the authentication service. It provides the user credentials and rights functionalities of the application.

See the `README.md` file for further details on the service.

#### `dms2223backend`

This service provides the Q&A logic (definition of questions, answers/comments, etc.)

See the `README.md` file for further details on the service.

#### `dms2223frontend`

A frontend web service that allows to interact with the other services through a web browser.

See the `README.md` file for further details on the application.

### Libraries

These are auxiliar components shared by several services.

#### `dms2223core`

The shared core functionalities.

See the `README.md` file for further details on the component.

## Docker

The application comes with a pre-configured Docker setup to help with the development and testing (though it can be used as a base for more complex deployments).

To run the application using Docker Compose (`-d` "detaches" the standard I/O from the containers; i.e., they are run in background mode):

```bash
docker-compose -f docker/config/dev.yml up -d
```

When run for the first time, the required Docker images will be built. Should images be rebuilt, do it with:

```bash
docker-compose -f docker/config/dev.yml build
```

To stop and remove the containers:

```bash
docker-compose -f docker/config/dev.yml rm -sfv
```

By default data will not be persisted across executions. The configuration file `docker/config/dev.yml` can be edited to mount persistent volumes and use them for the persistent data.

To see the output of a container:

```bash
docker logs CONTAINER_NAME
# To keep printing the output as its streamed until interrupted with Ctrl+C:
# docker logs CONTAINER_NAME -f
```

To enter a running service as another subprocess to operate inside through a terminal:

```bash
docker exec -it CONTAINER_NAME /bin/bash
```

To see the status of the different containers:

```bash
docker container ps -a
```

## Helper scripts

The directory `scripts` contain several helper scripts.

- `verify-style.sh`: Runs linting (using pylint) on the components' code. This is used to verify a basic code quality. On GitHub, this CI pass will fail if the overall score falls below 7.00.
- `verify-type-correctness.sh`: Runs mypy to assess the type correctness in the components' code. It is used by GitHub to verify that no typing rules are broken in a commit.
- `verify-commit.sh`: Runs some validations before committing a changeset. Right now enforces type correctness (using `verify-type-correctness.sh`). Can be used as a Git hook to avoid committing a breaking change:
  Append at the end of `.git/hooks/pre-commit`:

  ```bash
  scripts/verify-commit.sh
  ```

## GitHub workflows and badges

This project includes some workflows configured in `.github/workflows`. They will generate the badges seen at the top of this document, so do not forget to update the URLs in this README file if the project is forked!

## Línea futura

Podemos llegar a pensar en numerosas mejoras futuras para nuestra aplicación como pueden ser:
Toques de atención a los usuarios llegando asi a bloquearlos si estos son reicidentes (dejando de tener acceso a nuestra aplicación) 
Posible mejora en cuanto a la funcionalidad de los usuarios, estos pudiendo editar su propio perfil asi modificando datos personales o bien que estos tengan acceso a un registro propio de elementos interactuados con la aplicación.
Destacar una nueva sección de discusiones en tendencia, en la que destacaremos las cuales han tenido una interacción mayor en un mismo día.
 
Tras un estudio de la posible mejor línea futura que puede tomar nuestra aplicación nos hemos decantado en mejorar la interacción de esta, mediante la sección de "tendencias" las cuales para pertenecer a esta han de tener un mayor número de actividades, dependiendo así de factores como pueden ser:
- Mayor número de respuestas.
- Mayor número de comentarios.
- Mayor número de votos por día.
	
Los pasos que hemos de tomar para poder llevar a cabo esta línea futura son:
- Un nuevo apartado en el home que permita el rápido acceso y visualización de la sección al usuario.
- El apartado realizado para tener acceso a las discusiones en tendencia que tenga un diseño que anime al usuario a interactuar con esta nueva sección.

![Captura.PNG](imagenes/Captura.PNG)

- Una vez dentro del apartado de tendencias podremos visualizarlas los titulos de las discusiones en orden de mayor actividad.

- Estableceremos 2 filtros sobre las discusiones en tendencias:
    - 1º Nos permitirá visualizarlas según la franja de tiempo (mese, semana, dia) 
    - 2º Nos permitirá visualizarlas según la localización (país y región)
- Podremos visualizar a primera vista el numero de interacciones actuales de la discusion además de las etiquetas relacionadas con ese tema

![Captura2.PNG](imagenes/Captura2.PNG)

- Una vez dentro de cada discusion en tendencia resaltaremos al lado del titulo que se encuentra en tendencia y su posicion concretamente

![Captura3.PNG](imagenes/Captura3.PNG)

### Patrón de diseño a aplicar en la línea futura

Hemos pensado que un posible patron de diseño que podríamos llegar a aplicar durante el desarrollo de las tendencias de las discusiones es el Método plantilla.
Este nos permitirá distinguir dos clases concretas de una clase abstractca `Discusiones` que serán: 
  - `Discusion_Estandar` la cual utilizará y tendrá funcionalidades "principales" que debe de tener todas las páginas de nuestra aplicación, como pueden ser: añadir comentario , respuesta , etc ...
  - `Discusion_Tendencia` la cual además de tener las funcionalidades principales de una discusion estandar tendrá unas propias de una discusion en tendencia, estas pueden ser: obtener ranking, obtener localidad , obtener numero de interacciones, obtener etiquetas, entre otras.
Para tener una idea mas clara de como utilizariamos el patron de diseño este sería un diagrama simplificado:

![image.PNG](imagenes/image.png)

Como podemos ver además de la estructura de herencia tendremos una parte invariable independientemente de la discusion que es el pie de discusión, el cual, independientemente del tipo de discusión que sea se mantendrá de forma estática