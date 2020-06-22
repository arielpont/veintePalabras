# veintePalabras

Es un juego CLI (command-line interface) dónde los usuarios pueden jugar a crear una historia de forma secuencial. El concepto de esta aplicación está basado en el juego de palabras ["Cadaver Exquisito"](https://es.wikipedia.org/wiki/Cad%C3%A1ver_exquisito) dóndo cada jugador debe escribir una palabra pudiendo solamente visualizar lo escrito por el anterior jugador. Tamando este concepto se adaptó para que cada usuario puede visualizar las últimas 20(veinte) palabras de la historia que se va formando.

## ¿Cómo preparar el entorno para trabajar?

Antes de ejecutar los siguientes comandos es necesario tener instalado [Python 3](https://www.python.org/downloads/) en nuestro ordenador.

1. Instalamos "pipenv". 

+ Windows:  
``` pip install pipenv ```.  

+ MacOs o Linux:  
``` pip3 install pipenv ```.   

2. Instalamos nuestro entorno virtual tomando las dependencias del "Pipfile.lock".  

``` pipenv install --ignore-pipfile ```

## Referencias

1. [Crear un entorno virtual con Pipenv](https://realpython.com/pipenv-guide/)
2. [Convenciones](https://www.python.org/dev/peps/pep-0008/#introduction)
