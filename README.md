# Nutrihelp

## Instalar

0. Depende de pip y virtualenv.
1. `virtualenv -p python3 .venv`
1. `source .venv/bin/activate`
1. pip install -r requirements.txt

## Iniciar

1. `source .venv/bin/activate` # Desde el root del proyecto
2. `cd nutrihelp`
3. `python manage.py migrate`
4. `python manage.py runserver 0.0.0.0:8000`

## Desactivar el entorno virtual

1. deactivate
