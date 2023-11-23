## DJANGO
    Framework = Conjunto de librerias ya realizadas. 
    Usos comunes = web, Backend
    El framework garantiza la funcionalidad de un proyecto
    
    Manejadores de dependencias {pip, conda}

    Enviroment {Locales y Virtuales}

    __init__.py -> Es para hacer importaciones
    urls.py -> Para hacer endpoints
    manage.py -> Correr comandos propios dentro del proyecto

    migracion = 

## BACKEND    
    El backend tambien se le conoce como API {APP PROGRAMMING INTERFACE}
    El backend los servicios que provee son {WEB, REST, WSDL, SOAP} 
    {ENDPOINT}
    GET -> Peticion
    POST -> Guardar
    PUT/PATCH -> Actualizar
    DELETE -> Borrar

    Estados de servicios Web {200 = OK} {400 = ERROR} {500 = ERROR SERVER}
    
    Lenguajes de Backend 
        JS con framework NODE
        PH con framework LARAVEL, VANILLA, YIZ
        C#
        Python con framework DJANGO, FLASK, FRONTAPI
    
    Lenguajes de Frontend
        JS con framework REACT, ANGULAR, JQUERY, VUE
    
    WEB
        HTML -> ESTRUCTURA
        CSS -> ESTILO   {FRAMEWORK BOOTSTRAP, TAILWIND}

    MOBILE
        REACT NATIVE
        SWIFT
        KOTLIN
        JAVA
        OBJECT C

    PLATAFORMAS CRUZADAS -> PERMITE QUE SE PUEDA PROVEER TANTO PARA IOS Y ANDROID {No siempre es 100% efectivo}  

    WINFORM
    Python
    C, C#, ...
    VISUAL STUDIO

## REGLAS DJANGO
	- DJANGO SE MODULARIZA EN UNA APP ; Las APP divide en partes ciertas funcionalidades del proyecto
    - ESCALABILIDAD DE DATOS
    - LA VIEW TIENDE A SER BASTANTE VOLATIL

    MODEL - TEMPLATE - VIEW
        MODEL -> DATABASE - SERVER      
        TEMPLATE -> VISTA DEL USUARIO
        VIEW -> APLICA LA LOGICA 
        
## INSTALL
    1. python -m install Django                         Correccion Django  - pip install django
    2. django-admin startproject NombreProyecto     
    3. python manage.py migrate -> realizar la primera migracion  - Debe de estar en la carpeta de clase
    4. python manage.py runserver -> levantar el servidor - 
    5. python manage.py startapp nombreapp -> crea una app dentro de la app

## EJEMPLO

## EJEMPLO
    Ejemplo del archivo views, no olvidar importar el HttpResponse
    
    Primer paso:
    from django.shortcut import render, HttpResponse

    Segundo paso:
    # Aqui se crearian las views
    def hola_mundo(request):
        return HttpRespnse(
            "<h1>HOLA MUNDO</h1>"
        )
    

    En las urls definir donde se define la ruta 
    Las URLS son unicas, NO se deben repetir
    Cada URL deben de una function, es decir parte de un controller de logica

    Enviar parametros dentro de una url
    
