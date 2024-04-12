# Florería :sunflower::white_flower:

El siguiente proyecto cuenta con 6 endpoints con la finalidad de ejemplificar un CRUD mediante el uso de la clase APIView. El proyecto esta basando en el tema de una florería que requiere almacenar en una base de datos lo siguiente:

- El nombre de la planta/árbol
- Si es una planta/árbol que requiera estar en el sol, en sombra o en media sombra.
- Si es necesario regar la planta/árbol
- El tamaño de crecimiento de la planta

## Instalación :desktop_computer:

+ **Clonar el repositorio** :link:
  
`git clone https://github.com/LoadING-718/floreria.git`
  
+ **Creación de ambiente virtual** :wrench:

 _Para versión 3.11 de python_

`py -m venv venv`

  
:loudspeaker: _No olvides activar tu ambiente virtual_

_Activación para Windows PowerShell_

`venv/Scripts/Activate.ps1`

_Activación para bash_

`venv/bin/activate`

_Pudes consultar la documentación de ambientes virtuales de python en el siguiente link_

https://docs.python.org/es/3.11/library/venv.html#module-venv
  
+ **Instalación de liberías** :card_index_dividers:

`pip install -r requirements.txt`
  
+ **Conexión a base de datos en Postgresql**  :electric_plug: <br>

  _Si cuentas con pgAdmin para Postgres, crea una base de datos nueva y agrega los tus datos correspondientes a los siguientes objetos en el siguiente formato que se encuentra en settings.py del proyecto_ 
        
        
        DATABASES = {
            'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'Aquí_el_nombre_de_tu_base_de_datos',
            'USER':'Aquí_tu_usuario_de_postgres',
            'PASSWORD': 'Aquí_tu_contraseña_de_postgres',
            'HOST':'localhost',
            'PORT':'5432',
            }
        }

## Uso :joystick:

+ **Migrations** :page_with_curl:


  En tu terminal ejecuta los siguientes comandos en el orden correspondiente.
  
`python manage.py migrate`

`python manage.py makemigrations plantas`

`python manage.py migrate plantas`


+ **Abrir el puerto de los endpoints** :chains:

`python manage.py runserver`

ó 
  
`python manage.py runserver 0.0.0.0:8000`
  
+ **JSON para endpoint**  :placard:
 
        {
          "name":"Jacaranda",
          "light":"Sol",
          "irrigation":"Si",
          "alto": "50m"
        }

  _Recuerda que puedes usar cualquier gestor de APIs de tu preferencia, (ejem. Postman, Thunder Client, tu navegador, etc.)_  
  
+ **Listo** :four_leaf_clover::four_leaf_clover::four_leaf_clover::four_leaf_clover:

  _Ahora puedes usar el proyecto y probar cada uno de los enpoints_

