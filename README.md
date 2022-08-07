## Airflow

Airflow se usa para automatizar trabajos programáticamente dividiéndolos en subtareas. Permite su planificación y monitorización desde una herramienta centralizada. Los casos de uso más comunes son la automatización de ingestas de datos, acciones de mantenimiento periódicas y tareas de administración.

<br>

### Creando y seteando Entorno virtual
```
python3 -m venv .venv
source .venv/bin/activate
```

### Instalando dependencias de apache-airflow
```
pip install "apache-airflow[postgres, password]"
pip freeze > requirements.txt
pip install -r requirements.txt
```

### Creando la App y Base de datos en Heroku 

```
heroku create
Creating app... done, ⬢ ...

heroku addons:create heroku-postgresql:hobby-dev
Creating heroku-postgresql:hobby-dev on ⬢ ...
```

### Configuraciones de Apache Airflow en Heroku
```
 heroku config:set AIRFLOW__CORE__SQL_ALCHEMY_CONN=....
 heroku config:set AIRFLOW__CORE__LOAD_EXAMPLES=False
 heroku config:set AIRFLOW_HOME=/app
 heroku config:set AIRFLOW__CORE__FERNET_KEY=...
```

### Desplegando Apache Airflow en Heroku
```
git push heroku main
```

```
chmod -R 777
```

````
docker-compose up webserver
````

https://airflow.apache.org/docs/apache-airflow/stable/modules_management.html#additional-modules-in-airflow

````
airflow info
````