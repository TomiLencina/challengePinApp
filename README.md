Challege PinApp

A continunacion les comparto mi repo, con la resolucion del challenge...

Contenido:
- Pruebas funcionales automatizadas para la web de PinApp, donde pude encontrar bugs y reportarlos.
- Pruebas funcionales y de integracion para la API de Rick And Morty.

# PRUEBAS AUTOMATIZADAS WEB
- Utilice arquitectura POM
- El desarrollo esta hecho en pyhon, utilizando gherkin y cucumber.
- Reportes de ejecucion en allure, se pueden visualizar el archivo html en Allure-report, o desde la terminal con el comando "allure serve report/"
- Todo el desarrollo esta dentro de la carpeta feature
- Los test case los pueden encontrar en la carpeta testCase

# PRUEBAS EN API
- Pruebas funcionales y de integracion
- Validando la respuesta de la api con escenarios correctos y otros erroneos


## Conclusiones en General
Aplique el proyecto a su pagina web. Realice validaciones funcionales de una de sus page y valide su footer tambien.
En el cual encontre 2 bugs a mi criterio bastantes criticos, aunque son faciles de arreglar...
BUG 1: El footer contiene una caja de texto a la cual le podes agregar tus inquietudes, a estas las deberias mandar con un boton submit, pero al clickearlo no ocurre nada (el boton estaría inactivo)
BUG 2: Los botones que deberian redirigir a redes sociales, el de Facebook no esta cumpliendo la redireccion.
