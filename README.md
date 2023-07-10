# Detalles del proyecto

## Primeros pasos para correr el proyecto con docker

Primero se debe crear un archivo `.env` en la raíz del proyecto, para este paso por razones de seguridad comparto la información que debe contener el archivo `.env` en el correo 

Ya que tengamos la configuración del archivo .`.env` debemos ejecutar los siguientes comandos uno tras otros hasta que la terminal termine cada proceso (igual en la raíz del proyecto o la carpeta contenedora que nos de github al clonar el proyecto):

```sh
docker compose up -d flask_db
docker compose logs
docker compose up --build flask_app
```
En este punto la terminal deberia arrojarnos algo como:

`Running on http://127.0.0.1:4000`

`Running on http://172.19.0.3:4000`

Para mas fácil podemos usar la url `http://127.0.0.1:4000` en el navegador de su preferencia para abrir una interfaz minima que nos dara la opción de subir un archivo en csv o colocar el email donde se enviara el correo con el reporte de este, cabe mencionar que sino se coloca un correo, este de momento me llegara a mi por lo que en caso de colocar un correo asegurese de que sea real. 

```sh
docker exec -it flask_db psql -U postgres
(postgres=#) \dt
(postgres=#) select * from transactions;
```

GET /show_data


![Paso 1](https://github.com/Benji-Mtz/flask-csv/tree/main/static/readme/1.png)
