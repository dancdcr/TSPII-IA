# Indicaciones

El programa funciona como una interfaz entre 3 plataformas diferentes. Por ello, es necesario que se encuentren corriendo simultaneamente.  

# Proceso de activacion

El programa consiste en una interfaz de python, un arduino conectado al ordenador, y el uso del programa CoolTermWin.

## Carga del programa al Arduino

Primeramente, se requiere la carga del programa _"HoldPRoximitySensor"_ a la tarjeta de desarrollo, el cual se encargara de registrar los camios en el mismo
![enter image description here](https://raw.githubusercontent.com/dancdcr/TSPII-IA/main/img1.PNG)

## Uso de _CoolTermWin_

Para utuilizar el programa, se requiere tener una tarjeta Arduino conectada. Acto seguido, se requiere ir a la pestaña _"Connection"_, elegir _"Options"_, y elegir el puerto de comunicacion Serial en el que se encuentra el Arduino, asi como la velocidad de transferencia de datos del puerto serial. En el programa actual, el valor de _Baudrate_ es de 9,600.
![IMG](https://raw.githubusercontent.com/dancdcr/TSPII-IA/main/img2.PNG)
Una vez obtenido, se requiere presionar el boton _"Connect"_ para iniciar la transferencia de datos entre la tarjeta de desarrollo y el programa _"CoolTermWin"_
![IMG](https://raw.githubusercontent.com/dancdcr/TSPII-IA/main/img3.PNG)
Finalmente, en la pestaña _"Connection"_, al final, se elige la opcion _"Capture to Text File..."_ y se selecciona la opcion _"Start"_, o bien, se presiona _Ctrl+R_ para iniciar la captura de datos.
![IMG](https://raw.githubusercontent.com/dancdcr/TSPII-IA/main/img4.png)
Finalmente, se debe seleccionar el archivo __paymentFlag.txt_ dentro de la carpeta _"Proyecto"_ y sobreescribirlo para que se comience el proceso de registro sobre este archivo
![IMG](https://raw.githubusercontent.com/dancdcr/TSPII-IA/main/img5.PNG)

## Uso de la Interfaz de Usuario

Finalmente, se corre el archivo _UI.py_ y el programa se encuentra listo para usarse. Cabe mencionar que es requerida una camara web para poder utilizar el programa
![IMG](https://raw.githubusercontent.com/dancdcr/TSPII-IA/main/img6.PNG)
