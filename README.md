# energy_rest_api

### Problema
Se requiere la creacion de un RESTful API que exponga un conjunto de 'endpoints' para manejar las operaciones CRUD sobre las entidades de Clientes, Puntos de Medida y Medidores.

### Solucion
Se crea una aplicacion Python que implementara los recursos correspondientes a los modelos Client, Socket y Device. Cada recurso expondra las cuatro operaciones CRUD, representadas en los REST Verbs POST, GET, PUT y DELETE respectivamente. 

### Configuracion del entorno de trabajo
* Sistema Operativo: Ubuntu 18.04 /WSL sobre Windows 10
* Editor: Visual Studio Code / Flake8
* Postman
* Virtualenv

### Componentes y Librerias utilizados
* Python==3.6.9
* Postgres==10
* Flask==1.1.2
* Flask-SQLAlchemy==2.4.3
* psycopg2==2.8.5
