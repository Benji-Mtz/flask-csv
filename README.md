# Detalles del proyecto

## Primeros pasos para correr el proyecto con docker

Primero se debe crear un archivo `.env` en la raíz del proyecto, para este paso por razones de seguridad comparto la información que debe contener el archivo `.env` por separado

Ya que tengamos la configuración del archivo .`.env` debemos ejecutar los siguientes comandos uno tras otro en nuestra terminal hasta que termine cada proceso (igual en la raíz del proyecto o la carpeta contenedora que nos de github al clonar el proyecto):

```sh
$ docker compose up -d flask_db #levanta postgres
$ docker compose logs #para comprobar que postgres esta activo
$ docker compose up --build flask_app # levanta nuestro proyecto
```
En este punto la terminal deberia arrojarnos algo como:

`Running on http://127.0.0.1:4000`

`Running on http://172.19.0.3:4000`

Para mas fácil podemos usar la url `http://127.0.0.1:4000` en el navegador de su preferencia para abrir una interfaz minima que nos dara la opción de subir un archivo en csv o colocar el email donde se enviara el correo con el reporte de este, cabe mencionar que sino se coloca un correo no marcara error, pero me llegara a mi, por lo que en caso de colocar un correo asegurese de que sea suyo y/o real como se ve el las imagenes. 

![Paso 1](https://raw.githubusercontent.com/Benji-Mtz/flask-csv/main/static/readme/1.png)

![Paso 1](https://raw.githubusercontent.com/Benji-Mtz/flask-csv/main/static/readme/2.png)

Una vez cargado el csv (que por cierto dejo 3 ejemplos en la raiz del repositorio) y colocado el correo podrá ver la siguiente pantalla.
En esta pantalla tendrá un botón que dice **Reporte por GET y/o correo** y cuando de clic clik le mostrará el reporte y le llegará el reporte a su correo y es que nos lo proporciono

![Paso 1](https://raw.githubusercontent.com/Benji-Mtz/flask-csv/main/static/readme/3.png)

Imagen del reporte

![Paso 1](https://raw.githubusercontent.com/Benji-Mtz/flask-csv/main/static/readme/4.png)


## Base de datos

Si queremos ver la base de datos ya sea de ese único fichero csv u otros ficheros que haya usado en la aplicación podrá también ejecutar los siguientes comandos en la raiz del proyecto (en algúna terminal) y veremos el detalle de la tabla o registros.

```sh
$ docker exec -it flask_db psql -U postgres
(postgres=#) \dt
(postgres=#) select * from transactions;
```

Finalmente tendremos algo como vemos a continuación:

![Paso 1](https://raw.githubusercontent.com/Benji-Mtz/flask-csv/main/static/readme/5.png)
