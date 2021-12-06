# Proyecto Registro Marvel
 
_Para este proyecto les traigo un trabajo desarrollado en Flask, donde se puede ver un CRUD con una temática de Superhéroes_
 
 
### Pre-requisitos 📋
_Primeramente si es la primera ves que prueba con python, a continuación se muestran las librerías que se necesitan para desplegar el proyecto._
 
_Vamos a instalar Flask_
```
pip install flask
```
_Para MySQL utilizaremos:_
```
pip installFlask-MySQL
```
 
_Para Jinja2 utilizaremos:_
```
pip install jinja2
```
 
 
 
_Clonar repositorio en su computadora._
 
 
```
git clone https://github.com/juanprodrigues/Marvel-CRUD-Flask-Pyhon.git
```
 
### Instalación 🔧
 
_Para ejecutar el proyecto se necesitan las siguientes tecnologías._
 
```
Visual Studio Code
Python 3.9.0
Flask 2.0.2
Flask-MySQL 1.5.2
Jinja2 3.0.3
MySQL Workbench 8.0
```
 
 
## Ejecutando las el proyecto ⚙️
 
_Las principales características del proyecto  es un CRUD además se maneja archivos, en este caso fotos._
 
 
## Despliegue 📦
_Antes de desplegar la aplicación se tiene que crear la base de datos e ingresar la siguiente sentencia para crear las tablas necesarias_
```
#sentencia para crear la tabla en mysql
 CREATE TABLE `sistema`.`empleados` (
   `id` INT NOT NULL AUTO_INCREMENT,
   `nombre` VARCHAR(45) NULL,
  `correo` VARCHAR(45) NULL,
   `foto` VARCHAR(255) NULL,
  PRIMARY KEY (`id`));
```
_Luego completa con sus credenciales de User y Password dentro de app.py._
 ```
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='root'
app.config['MYSQL_DATABASE_BD']='sistema'
```
 
_Se puede visualizar en un puerto ejecutando la siguiente sentencia en la terminal._
 
```
pyton app.py
```
 
## Construido con 🛠️
 
_Las herramientas que utilice para crear el proyecto._
 
```
Visual Studio Code
Python 3.9.0
Flask 2.0.2
Flask-MySQL 1.5.2
Jinja2 3.0.3
MySQL Workbench 8.0
```
 
 
 
* [Visual Studio Code](https://code.visualstudio.com/) - Editor de codigo
* [Python ](https://www.python.org/) - Lenguaje principalñ
* [MySQL ](https://dev.mysql.com/downloads/workbench/) - Mptor de base de datos
 
 
 
## Mejoras para el futuro
_Un propósito que se puede añadir es el tema de roles,seguridad y enviar mail._
 
 
 Cualquier sugerencia o recomendacion se pueden comunicar al siguiente correo juanprodrigues.33@gmail.com
 
 
## Gracias por llegar hasta el final 🎁
 
* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien de tu equipo.
 
 
 
---
⌨️ con ❤️ por [Juan Pablo Rodriguez](https://github.com/juanprodrigues) 😊
 
 
## Algunas capturas del proyecto
_En la primer imagen se observa que se traen todos los elementos de la base de datos y se le dos botones como acción para Editar y/o eliminar ese personaje._
 
 _En la segunda creamos un personaje para luego guardarlo en la base de datos_
 
_Por último tenemos un formulario en el que persiste la base de datos y trae un personaje seleccionado por ID_
 
![alt listar](https://i.ibb.co/KFwnsRb/lista.png)
![alt crear](https://i.ibb.co/jrMmszs/crear.png)
![alt nnidificar](https://i.ibb.co/zr53Nbm/modificar.png)
 
 
 
 

