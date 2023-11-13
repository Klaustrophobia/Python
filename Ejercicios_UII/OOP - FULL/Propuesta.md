Una empresa de Aseo y Mantenimientos requiere una base de datos para el manejo de sus contratos,
para esto se requiere la información de cada contrato la cual contiene, el empleado responsable,
la cantidad de metro cuadrados en los que se realizara el aseo, el cliente con sus respectivos datos 
generales, la fecha inicio y fin del contrato, precio por el cual se realiza el contrato, así
como el estado en el que se encuentra el contrato, por ejemplo un contrato puede estar en 
estado “En Espera”, “En Proceso”, “Finalizado”, en algunos casos puede estar “En Pausa”, pero un contrato 
no puede estar en dos estados al mismo tiempo, de estos estado se requiere la fecha en la inicio un estado
y la fecha en la que termino de estar en dicho estado.

Cada contrato necesariamente tiene que ser de uno de tres tipos, “Aseo Domiciliario”, “Aseo Empresarial” y “Aseo de Áreas Verdes”,
para el caso que sea de aseo domiciliario se requiere que se especifique si se requiere lavado y planchado, requiere cocinar, cantidad 
de habitaciones, cantidad de baños. 

Para el caso del aseo empresarial si se requiere servicio de mesero, cantidad de habitaciones, cantidad de baños, requiere el uso de químicos.

Para el caso de aseo de áreas verdes si se requiere el uso de químicos, requiere el talado de Arboles,
requiere mantenimiento de flores de jardín.

Cada contrato contara con el personal que trabajara en él, se va tener una persona que será el responsable 
y pueden tener n empleados mas ayudándole, de los empleados se requiere sus datos generales
y el cargo para el que fue contratado así como el cargo que esta realizando en el contrato.

Cada persona tendra un salario por lo cual el precio del contrato sera el 100% mas que el costo del salario total

En cada contrato la utilidad se calcula diferente basado en lo siguiente
    utilidad para domicilio es 40% si hay mas de dos empleados en caso contrario 30%
    utilidad para empresarial es 60% si hay se requieren meseros caso contrario 50%
    utilidad para areas verdes es 50% si son mas de 40 metros caso contrario 80%
para cada empleado calcular el impuesto de su sueldo el cual sera 12% si gana mas de 5000 y 500 si gana menos