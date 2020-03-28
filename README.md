# Módulo "My Courses"

Versión de Odoo: 12

URL del repositorio: https://github.com/a18paulapv/ModCursos

Este módulo sirve para gestionar alumnos, cursos y sus respectivas imparticiones, y saber así qué alumno asiste a cada curso y cuándo. Su objetivo es facilitar la gestión a institutos, colegios y academias.

Manejar este módulo es muy sencillo. Podemos gestionar los siguientes datos de un curso(Modelo: **courses.course**):

* **name** = En la interfaz hace referencia al nombre del curso. Por ejemplo: "Desarrollo de Aplicaciones Multiplataforma"

* **acronyms** = No es un campo obligatorio, sirve para indicar, si se desea, las siglas del nombre del curso para abreviar. Continuando con el ejemplo anterior sería: "DAM".

* **level**=En este campo se indica el nivel del curso(1º, 2º, 3º, ...) 

* **teach_ids**= Este campo, en la interfaz, muestra una lista con los alumnos que están asignados a ese curso.

Los cursos se pueden ver listados(con la vista *tree*) o agrupados por nivel(con la vista *kanban*)

El modelo **courses.student** que maneja la gestión de los alumnos se utiliza de una forma un poco diferente a los cursos, puesto que tiene herencia por delegación del modelo **"res.partner"**. Los datos que podemos manejar son los siguientes:

* **partner_id**: Cuando queremos crear un estudiante nos muestra una lista con los nombres que ya están declarados en el modelo padre.

* **date_start**: Con este campo indicamos cuando ingresamos un alumno(matrícula). Por defecto coge la fecha actual.
    
* **student_phone**: En este campo se puede introducir un teléfono de contacto.

* **date_birth**: Indicamos la fecha de nacimiento del alumno.

* **photo**: Muestra una foto del alumno. Muestra una automáticamente en cuanto escogemos el nombre del alumno, pues hace referencia a la imagen del modelo padre.

* **age**: Es un campo calculado que indica la edad del alumno, y no se guarda en la base de datos pues no es necesario.

* **is_assigned**: Este campo *boolean* indica si un alumno está asignado a un curso o no. Un alumno puede estar asignado únicamente a un curso. 

* **state**: Indica el estado de un estudiante. Solo hai dos posibilidades: "Available" y "Unavailable". Este estado lo cambiamos con los botones que aparecen en la parte superior de la vista *form* de cada alumno, que son: "Make Available" y "Make Locked". Esto serviría si queremos "dar de baja" un alumno por cualquier motivo, pero no queremos eliminarlo de nuestra base de datos, le damos a "Make Locked" y ya nos dejaría asignar dicho alumno a ningún curso(aunque esto no está implementado en mi módulo).

Para este modelo únicamente tenemos las vistas *tree* y *form*.

Las imparticiones las establecemos con el modelo **courses.teaching**, el cual relaciona los dos modelos anteriores. Los datos que utiliza son los siguientes:

* **student_id**: Hace referencia al estudiante.

* **course_id**: Hace referencia al curso.

* **date_start**: Indica la fecha de comiezo de la impartición del curso. Por defecto establece la fecha actual.

* **date_end**: Indica la fecha en la que termina la impartición del curso. Por defecto coge la fecha de nueve meses después de la fecha de inicio(270 días).

* **student_photo**: Muestra la foto del estudiante indicado.

* **course_level**: Muestra el nivel del curso indicado.

En este modelo además tenemos dos restricciones:

1. Para que la fecha en la que termina la impartición no sea anterior a la de comienzo, pues no tendría sentido.

2. Para que un estudiante únicamente pueda estar asignado a un solo curso que se esté impartiendo en ese momento. Si el curso al que estaba asignado ya ha terminado, podrá ser asignado a otro distinto.

Para este modelo además de las vistas *tree* y *form* tenemos la vista *calendar*.

Para cada modelo hay un elemento en el menú superior del módulo, mediante los cuales podremos acceder a sus vistas para gestionar cada uno de ellos. Podremos crear cursos y alumnos independientemente, o hacerlo a la vez que creamos también una impartición.


