### Florería :sunflower: :white_flower:

El siguiente proyecto cuenta con 6 endpoints con la finalidad de ejemplificar un CRUD mediante el uso de la clase APIView. El proyecto esta basando en el tema de una florería que requiere almacenar en una base de datos lo siguiente:

- El nombre de la planta/árbol
- Si es una planta/árbol que requiera estar en el sol, en sombra o en media sombra.
- Si es necesario regar la planta/árbol
- El tamaño de crecimiento de la planta

## Instalación :desktop_computer:

+ **Clonar el repositorio** :link:

      `git clone https://github.com/LoadING-718/floreria.git`
  
+ **Creación de ambiente virtual** :wrench:
      `py -m venv venv`
      _ _No olvides activar tu ambiente virtual_ _
  
+ **Instalación de liberías** :card_index_dividers:
      `pip install -r requirements.txt`
  
+ **Conexión a base de datos en Postgresql**  :electric_plug:
      _ _Si cuentas con pgAdmin para Postgres, crea una base de datos nueva y agrega los tus datos correspondientes a los siguientes objetos en el siguiente formato que se encuentra en settings.py del proyecto_ _
  
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

+ **Migrations** :page_with_curl:

  En tu terminal ejecuta los siguientes comandos en el orden correspondiente.
        `python manage.py migrate`
        `python manage.py makemigrations plantas`
        `python manage.py migrate plantas`
  
+ **Abrir el puerto de los endpoints** :chains:
  
        `python manage.py runserver` o `python manage.py runserver 0.0.0.0:8000`
  
+ **Utiliza el siguiente JSON para probar tu endpoint**  :placard:
        {
          "name":"Jacaranda",
          "light":"Sol",
          "irrigation":"Si",
          "alto": "50m"
        }
        _ _Recuerda que puedes usar cualquier gestor de APIs de tu preferencia, (ejem. Postman, Thunder Client, tu navegador, etc.)_ _
  
+ **Listo** :four_leaf_clover:
      _ _Ahora puedes usar el proyecto y probar cada uno de los enpoints_ _

