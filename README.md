# 🧾 Sistema de Inventario

Este proyecto es un sistema de gestión de inventario desarrollado con **Flask** utilizando el patrón de arquitectura **Hexagonal (Ports & Adapters)**. Permite gestionar productos, categorías e historiales de movimientos, con soporte para múltiples motores de base de datos: **MongoDB** y **MySQL**.

---

## 🚀 Funcionalidades principales

- 🔐 Autenticación de usuarios
- 📦 Gestión de productos (crear, actualizar, eliminar, listar)
- 🏷️ Gestión de categorías
- 📚 Registro de historial de movimientos
- 🔄 Persistencia con MongoDB y MySQL (intercambiable)
- 📊 Conteo total de registros por módulo
- 🧪 Separación clara entre capas de dominio, infraestructura y presentación

---

## 🛠️ Tecnologías utilizadas

- Python 3
- Flask
- MongoDB (`pymongo`)
- MySQL (`mysql-connector-python`)
- Jinja2
- Arquitectura Hexagonal

---

## ⚙️ Configuración del proyecto

1. **Clona el repositorio**:
    ```bash
    git clone https://github.com/maherrera603/inventory.git
    ```

2. **Navega a la carpeta del proyecto**:
    ```bash
    cd inventory
    ```

3. **Copia el archivo `.env.template` y renómbralo a `.env`**. Luego, agrega las variables correspondientes en este archivo.

4. **Crea un entorno virtual**:
    ```bash
    python -m venv venv
    ```

5. **Activa el entorno virtual**:
    ```bash
    venv\Scripts\Activate
    ```

6. **Instala las dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

7. **Configura la base de datos de MySQL**:
    - Usa el archivo `database.sql` para crear la base de datos y las tablas necesarias.
    - En el archivo `database.sql`, en la línea 19, encontrarás la inserción de datos del usuario. **Modifica los datos de usuario según sea necesario, excepto la contraseña (ya está encriptada) y el `role` (que debe permanecer como `ADMIN_ROLE`).**

8. **Configura la base de datos de MongoDB**:
    - Si no tienes MongoDB instalado, puedes seguir la guía oficial de instalación de [MongoDB](https://www.mongodb.com/docs/manual/installation/).
    - Asegúrate de tener un clúster de MongoDB en ejecución en tu máquina local o en una instancia remota.
    - Inserta los datos del usuario en MongoDB con el siguiente JSON (reemplaza los valores correspondientes según sea necesario):

    ```json
    {
        "name": "nombre_usuario",
        "lastname": "apellidos_usuario",
        "idnumber": "NoIdentificador",
        "phone": "telefono",
        "email": "email_usuario",
        "password": "$2b$12$7lcaKJDnt2TtRubIyT26C.q5inmMbX.E9QIQQaXjzDB6hJeZi8NEG",
        "role": "ADMIN_ROLE",
        "created_at": "2025-04-15T10:06:53Z",
        "updated_at": "2025-04-15T10:06:53Z"
    }
    ```

    **Importante**: No modifiques los valores de `password` ni `role`, ya que estos son los datos predeterminados y deben permanecer intactos. La contraseña ya está encriptada utilizando `bcrypt`. Modifica solo los valores de `lastname`, `idnumber`, `phone`, `email`, `created_at` y `updated_at` según sea necesario.

9. **Ejecuta la aplicación**:
    ```bash
    python main.py
    ```

10. **Contraseña para ingresar**:  
    ```text
    Prueba2025_*
    ```

---

## 🔄 Cambio de Base de Datos: MongoDB a MySQL

Si deseas cambiar la base de datos de **MongoDB** a **MySQL**, sigue estos pasos:

1. **Modifica las rutas en los controladores**:
    - Los archivos de rutas se encuentran en el directorio `app/routes/`. Por ejemplo, para el historial, el archivo podría ser `historyRoutes.py`, y para los productos, `productRoutes.py`.
    - Dentro de cada archivo de rutas, encontrarás las instancias de los **datasources** (que se encargan de interactuar con la base de datos). Por ejemplo, para MongoDB, verás algo como esto en el archivo `HistoryRoutes.py`:

    ```python
    historyDatasource = HistoryDatasourceImp(database)
    ```

    - Para cambiar de MongoDB a MySQL, solo necesitas cambiar el datasource a la implementación de MySQL. Por ejemplo:

    ```python
    # Cambio de MongoDB a MySQL
    from app.infrastructure.datasource.mysql.historyDatasourceImp import HistoryDatasourceImp
    historyDatasource = HistoryDatasourceImp(database)
    ```

2. **Reemplaza los `datasources` de MongoDB con los correspondientes de MySQL**:
    - Asegúrate de que en cada archivo de ruta, el datasource esté apuntando a la implementación de MySQL.
    - Los **repositorios** también deben ser actualizados si es necesario para adaptarse a las consultas SQL en lugar de las consultas de MongoDB.

3. **Verifica la configuración de la base de datos**:
    - En el archivo `.env`, asegúrate de tener las variables adecuadas para MySQL, como `MYSQL_HOST`, `MYSQL_USER`, `MYSQL_PASSWORD`, y `MYSQL_DB_NAME`.
    - MongoDB debería estar comentado o eliminado si no lo estás utilizando.

4. **Ejecuta la aplicación**:
    Después de hacer estos cambios, puedes ejecutar la aplicación con MySQL como base de datos:

    ```bash
    python main.py
    ```

Este cambio te permitirá trabajar con MySQL en lugar de MongoDB. Si tienes alguna pregunta o problema con la migración, no dudes en consultarnos.

---

¡Listo! Ahora tienes un archivo `README.md` completo que no solo incluye instrucciones de instalación y configuración, sino también cómo cambiar de base de datos entre MongoDB y MySQL.
