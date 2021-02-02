#include "GFButton.h"

GFButton sensorT = GFButton(3);

void setup() {  
  Serial.begin(9600);
  sensorT.setHoldHandler(on_hold); //Funcion callback del boton segun la libreria
  //Reconfiguracion del tiempo de espera
  sensorT.setHoldTime(1200); //-----> 1200 ms
  sensorT.setDebounceTime(100); //Temporizador de rebotes
}

void loop() {
  sensorT.process(); //Metodo del boton de acuerdo a la libreria
}

//Event handler para solo actuar cuando el tiempo de espera se cumpla (1200 ms)
void on_hold(GFButton & button)
{
  if (button.isFirstHold()) //El metodo se llama varias veces, pero cuando es la primera vez, se activa la bandera isFirstHold, donde se desarrolla el codigo
  {
    //Al cumplirse...
    Serial.write(0x0d); //Limpiamos el serial por cualquier ruido
    Serial.println(F("1")); //Escribimos 1 como bandera de activacion para la UI
    delay(3000); //Esperamos 3 segundos para asegurarnos de que no volvera a entrar al ciclo de activacion
    Serial.println(F("0")); //Escribimos un cero como bandera de reinicio
  }
}
