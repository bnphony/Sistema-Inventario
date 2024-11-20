<div align="center">
  
  # Sistema de Inventario
</div>

<div align="center">
  <img src="https://raw.githubusercontent.com/bnphony/Calificar-Series/master/static/img/category_list.PNG" width="80%" alt="Category List">

  ![GitHub](https://img.shields.io/github/last-commit/bnphony/Sistema-Inventario)
  [![Django](https://img.shields.io/badge/Framework-Django-green)](https://www.djangoproject.com/)
  [![Python](https://img.shields.io/badge/Code-Python-fd81f)](https://www.python.org/)
  [![DataTables](https://img.shields.io/badge/Tables-DataTables-397ed3)](https://datatables.net/)
  [![Bootstrap 5](https://img.shields.io/badge/Framework-Bootstrap%205-7952b3)](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
  [![PostgreSQL](https://img.shields.io/badge/DB-PostgreSQL-6598c3)](https://www.postgresql.org/)
  [![JavaScript](https://img.shields.io/badge/Code-JavaSript-orange)](https://developer.mozilla.org/es/docs/Web/JavaScript)
  [![JQuery](https://img.shields.io/badge/Code-JQuery-0769ad)](https://jquery.com/)  

</div>

## Indice

- [Calificar Series](#calificar-series)
  - [Descripción](#descripción)
     - [Tecnologías](#tecnologías)
  - [Dominio](#dominio)
     - [Categoría](#categoría)
     - [Serie](#serie)
     - [Episodio](#episodio)
     - [Usuario](#usuario)
     - [Usuario Token](#usuario-token)
  - [Funciones](#funciones)
  - [Autor](#autor)
     - [Contacto](#contacto)
  - [Licencia de Uso](#licencia-de-uso)
 
## Descripción
Sistema de Inventarios y generación de reportes, utilizando DJANGO 3.0. Funciones Principales:
- Gestionar Usuarios.
- Gestionar Categorías.
- Gestionar Productos.
- Gestionar Clientes.
- Gestionar Ventas.
- Generar reportes de ventas.
- Exportar en formato Excel y PDF los reportes de ventas.
- Visualizar el porcentaje de ventas utilizando gráficos de barras y de sectores (pastel).

   
### Tecnologías

- Lenguaje del lado del Servidor: [Python](https://www.python.org/) - Interactuar con la base de datos, gestionar las peticiones del usuario.
- Web Framework: [Django](https://www.djangoproject.com/) - Facilitar el desarrollo web.
- Interacción con la Interfaz: [Java](https://www.java.com/es/) y [JQuery](https://jquery.com/) - Agregar comportamiento a los componentes de la UI.
- Cuadros de Confirmación: [jquery-confirm](https://craftpip.github.io/jquery-confirm/) - Cuadros de dialogos animados para confirmar procesos.
- Iconos: [Font Awesome](https://fontawesome.com/) - Mejorar la experiencia de usuario.
- Dashboard: [AdminLTE](https://adminlte.io/) - Plantilla para el Panel de Administración.
- Tablas de Información: [DataTables](https://datatables.net/) - Facilita la presentación e interación con la información, utilizando tablas responsivas.
- Selección de Fechas: [DateRangePicker](https://www.daterangepicker.com/) - Mejorar la experiencia del usuario al ingresar fechas en los formularios.
- Framework de Diseño: [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) - Facilitar una interfaz agradable y responsiva.
- Caja de Selección: [Select2](https://select2.org/) - Facilitar la presentación de información en las cajas de selección.
  
## Dominio

Gestionar usuarios, categorías, productos, clientes, ventas, generar reportes.
- Un usuario puede crearse una cuenta, iniciar sesión, restablecer su contraseña utilizando su email.
- Los usuarios creados a partir del sistema no tienen permisos de administrador.
- Un usuario puede crear, actualizar, listar, eliminar categorías.
- Un usuario puede crear, actualizar, listar, eliminar productos, cada productos pertenece a una categoría.
- Un usuario puede crear, actualizar, listar, eliminar clientes.
- Un usuario puede crear, actualizar, listar, eliminar, imprimir en pdf las ventas.
- Cada venta contiene información sobre los productos vendidos y sobre el cliente que compra dichos productos.
- Un usuario puede generar reportes de las ventas acorde a un rango de fechas y exportarlos en formato excel o pdf.

### Usuario

| Campo      | Tipo    | Descripción                 |
|------------|---------|-----------------------------|
| id         | UUID    | Identificar único           |
| image      | Varchar | Imagen del Usuario          |
| token      | UUID    | Token de Acceso del Usuario |
| username   | Varchar | Nombre de Usuario           |
| first_name | Varchar | Primer Nombre del Usuario   |
| last_name  | Varchar | Apellido del Usuario        |
| email      | Varchar | Email del Usuario           |
| password   | Varchar | Contraseña del Usuario      |

### Categoría

| Campo         | Tipo    | Descripción                 |
|---------------|---------|-----------------------------|
| id            | UUID    | Identificar único           |
| nombre        | Varchar | Nombre de la Categoría      |
| desc          | Varchar | Descripción de la Categoría |
| user_creation | Usuario | Usuario de la Categoría     |

### Producto

| Campo  | Tipo      | Descripción            |
|--------|-----------|------------------------|
| id     | UUID      | Identificar único      |
| nombre | Varchar   | Nombre del Producto    |
| image  | Varchar   | Imagen del Producto    |
| stock  | Integer   | Cantidad del Producto  |
| pvp    | Decimal   | Precio del Producto    |
| cat    | Categoría | Categoría del Producto |

### Cliente

| Campo         | Tipo     | Descripción                     |
|---------------|----------|---------------------------------|
| id            | UUID     | Identificar único               |
| nombres       | Varchar  | Nombres del Cliente             |
| apellidos     | Varchar  | Apellidos del Cliente           |
| dni           | Varchar  | Cédula del Cliente              |
| date_birthday | DateTime | Fecha de Nacimiento del Cliente |
| address       | Varchar  | Dirección del Cliente           |
| gender        | Varchar  | Género del Cliente              |

### Venta

| Campo       | Tipo     | Descripción                  |
|-------------|----------|------------------------------|
| id          | UUID     | Identificar único            |
| date_joined | DateTime | Fecha de Creación            |
| subtotal    | Decimal  | Precio Sub-total de la Venta |
| iva         | Decimal  | IVA de la Venta              |
| total       | Decimal  | Precio Total de la Venta     |
| cli         | Cliente  | Cliente de la Venta          |

### Descripción de la Venta

| Campo    | Tipo     | Descripción                                     |
|----------|----------|-------------------------------------------------|
| id       | UUID     | Identificar único                               |
| price    | Decimal  | Precio del Producto                             |
| cant     | Integer  | Cantidad a vender                               |
| subtotal | Decimal  | Precio Sub-total de la venta de este producto/s |
| sale     | Venta    | Venta de la Descripción de la Venta             |
| prod     | Producto | Producto de la Descripción de la Venta          |

## Funciones
<table>
  
  <tr>
    <td width="50%">
      <h3 align="center">Creación de una Cuenta de Usuario</h3>
      <div align="center">
        <img src="https://raw.githubusercontent.com/bnphony/Calificar-Series/master/static/img/create_account.PNG" width="80%" alt="Create Account">
        <p>
          - El nombre del usuario debe ser unico. <br/>- La contraseña debe contener numeros y letras.
        </p>
      </div>
    </td>
    <td width="50%">
      <h3 align="center">Iniciar Sesión</h3>
      <div align="center">
        <img src="https://raw.githubusercontent.com/bnphony/Calificar-Series/master/static/img/login.PNG" width="80%" alt="Login">
        <p>
          - Solo los usuarios registrados en la base de datos pueden acceder utilizando su nombre de usuario y contraseña.
        </p>
      </div>
    </td>
  </tr>
  
  <tr>
    <td witdh="100%" colspan="2">
      <h3 align="center">Resetear Contraseña</h3>
      <div align="center">
        <img src="https://raw.githubusercontent.com/bnphony/Calificar-Series/master/static/img/recover_password.PNG" width="40%" alt="Reset Password 1">
        <img src="https://raw.githubusercontent.com/bnphony/Calificar-Series/master/static/img/recover_password_2.PNG" width="40%" alt="Reset Password 2">
        <p>
          - Ingresar el nombre de usuario único para verificar en la base datos y tener acceso para cambiar la contraseña.<br/>
          - Las 2 contraseñas deben coincidir y debe utilizar numeros y letras.
        </p>
      </div>
    </td>
  </tr>

  
  <tr>
    <td width="100%" colspan="2">
      <h3 align="center">Lista de Categorías</h3>
      <div align="center">
        <img src="https://raw.githubusercontent.com/bnphony/Calificar-Series/master/static/img/category_list.PNG" width="80%" alt="Category List">
        <p>
          - Crear una nueva Categoría.<br/>
          - La imagen de fondo de cada categoría se coloca automáticamente utilizando los logos de las seres/películas que estén registradas dentro de esa categoría.
        </p>
      </div>
    </td>
  </tr>
  <tr>
    <td width="100%" colspan="2">
      <h3 align="center">Lista de Categorías</h3>
      <div align="center">
        <img src="https://raw.githubusercontent.com/bnphony/Calificar-Series/master/static/img/create_serie.PNG" width="80%" alt="Create Serie">
        <p>
          - Registrar una serie/película: nombre, logo, número de capítulos (esto crea los nodos para cada capítulo). <br/>
          - Iconos Verdes de la derecha: Subir/Descargar los datos de las series y capítulos de la categoría actual.
        </p>
      </div>
    </td>
  </tr>
  <tr>
    <td width="100%" colspan="2">
      <h3 align="center">Actualizar/Eliminar Serie</h3>
      <div align="center">
        <img src="https://raw.githubusercontent.com/bnphony/Calificar-Series/master/static/img/update_delete_serie.PNG" width="80%" alt="Update/Delete Serie">
        <p>
          - Actualizar o Eliminar la información de una serie asi como todos sus capitulos.          
        </p>
      </div>
    </td>
  </tr>
  <tr>
    <td witdh="100%" colspan="2">
      <h3 align="center">Valoración de Capítulos Interactivo</h3>
      <div align="center">
        <img src="https://raw.githubusercontent.com/bnphony/Calificar-Series/master/static/img/serie_interactive.PNG" width="80%" alt="Serie Interactive">
        <p>
          - El usuario puede arrastrar los nodos para asignar la nota correspondiente a cada capitulo. <br/>
          - El promedio general de la aserie se va actualizando automaticamente. <br/>
          - Los nodos formas una grafíca, facilitando la valoración general. <br/>
          - Doble Click en un nodo: abrir modal de configuración del capítulo. <br/>
          - Click Derecho en un nodo: confirmar la eliminación del capítulo. <br/>
        </p>
      </div>
    </td>
  </tr>
  <tr>
    <td width="100%" colspan="2">
      <h3 align="center">Información Breve del Capítulo</h3>
      <div align="center">
        <img src="https://raw.githubusercontent.com/bnphony/Calificar-Series/master/static/img/tooltip.PNG" width="80%" alt="Tooltip">
        <p>
          - Al pasar el mouse sobre encima de un nodo: presentación del título, la imagen y un poco de la descripción del capítulo.
        </p>
      </div>
    </td>
  </tr>
  <tr>
    <td width="100%" colspan="2">
      <h3 align="center">Gráfico de Resultados</h3>
      <div align="center">
        <img src="https://raw.githubusercontent.com/bnphony/Calificar-Series/master/static/img/resultados.PNG" width="80%" alt="Results">
        <p>
          - Gráfico de barras horizontal, ordenado descendentemente, presentando las mejores series/películas de la categoría actual.<br/>
          - Botón de 'Descargar': descargar el gráfico de barras en formato .svg pero con las imagenes incrustadas.
        </p>
      </div>
    </td>
  </tr>
</table>


## Autor
Codificado por [Bryan Jhoel Tarco Taipe](https://github.com/bnphony)

### Contacto
<a href="https://www.linkedin.com/in/bryan-tarco01" rel="noopener noreferrer" target="_blank">
  <img align="center" src="https://github.com/bnphony/Portafolio/blob/deployed/static/img/linkedin_icon.png" alt="LinkedIn" height="40" width="40" />
</a>
<a href="https://github.com/bnphony" rel="noopener noreferrer" target="blank">
  <img align="center" src="https://github.com/bnphony/Portafolio/blob/deployed/static/img/github_icon.png" alt="GitHub" height="40" width="40" />
</a>
<a href="mailto: bryan.tarco01@gmail.com" target="_blank">
  <img align="center" src="https://github.com/bnphony/Portafolio/blob/deployed/static/img/email_icon.png" alt="Email" height="40" width="40" />
</a>



## Licencia de Uso
Este repositorio y todo su contenido está licenciado bajo licencia **Creative Commons**. Por favor si compartes, usas o modificas este proyecto cita a su
autor, y usa las mismas condiciones para su uso docente, formativo o educativo y no comercial.
