## DJANGO
    Es un web Framework, para back-end server-side web framework.
    Django follows the MVT design pattern (Model View Template)

## MTV design pattern
    Is a software design pattern, it's a collection of three important components; Model, View, Template.

    Model -> Helps to hablde database, it's a data access layer which handles the data.

        1. The Model provides data from DB.

        2. In Django, the data is delivered as an Object Relational Mapping (ORM) which is a technique designed to make it easier to work with DB

        3.Django, with ORM, makes it easier to communicate with the DB, without having to write complex SQL statements.

        4. The models are usually located in a file called models.py


    Template -> Is a presentation layer which handles UI part completely.

        1. A template is a file where you describe how the result should be represented.

        2. Template are often .html files, with HTML code describing the layout of a web page, but it can also be in other file formats to present other results, but we will concentrate on .html files.

        3. Django uses standart html to describe the layut, but uses Django tags to add logic.

        4. The templates of an application is located in a folder named templates.
        

    View -> Is used to execute the business logic and interact with model to carry data and renders a template.

        1. A View is a function or method that takes http requests as arguments, imports the relevant model(s), and finds out what data to send to the template, and returns the final result.

        2. The Views are usually located in a file called view.py


## MVC Architectal pattern
    Is an architectural pattern that separates an application into three main logical components: the model, the view, and the controller.
    Each of these components are built to hablde specific development aspects of an application.
    MVC is one of the most frequentl used industry-standard web development framework to create scalable and extensible projects

    Model -> The model component corresponds to all the data-related logic that user works with

        1. This can represent either the data that is beibg transferred between the View and Controller componentes or any other business logic-related data.

        EX: A player object will retrieve the player information from the DB, manipulate it and update it data back to the db or use it to render data.

    View ->The view component is used for all the UI logic of the application.

        EX: The player view will incluide all the UI componentes such as text boxes, dropdowns, etc. that the final user interacts with.


    Controller -> Controllers act as an interface between Model and View components to process all the business logic and incoming request, manipulate data using the Model component and interact with the Views to render the final output.

        EX: The player controller will handle all the interactions and inputs from the Player view and update the database using the Player Model. The same controller will be used to view the Player data.

                                  Model
                                    ^
                                    |
                                    v
                    CLIENT <-> CONTROLLER
                                    ^
                                    |
                                    v
                                  View

## Comandos para Python
OBS: 
'-m' es una opción que permite ejecutar un módulo como un script. 
'venv' es un módulo incorporado en Python que se utiliza para crear entornos virtuales.

    ACTUALIZACION DE GESTION DE PAQUETES EN PYTHON
        pip --version 
        python  -m pip install --upgrade pip
    
    CREAR ENTORNOS VIRTUALES CON PYTHON
        python -m venv NOMBRE_DEL_ENTORNO_VIRTUAL_A_CREAR

    ACTIVAR EL ENTORNO VIRTUAL
        Ubicarse en la caperta del Venv\scripts
        Luego agregar '\activate' para activarlo

    INSTALAR DJANGO
        Ubicarse en la carpeta del proyecto
        pip install django

    VER PIP INSTALADOS
        pip list

