# Anteckningar-2022-09-22
GPIO-implementering i Python via egenskapade klasser input och output.

Filen gpio.py innehåller funktionalitet för användarvänlig GPIO-implementering för Raspberry Pi via egenskapde klasser.
För att kontrollera hårdvaran (in- och utsignaler, eventdetektering med mera) används funktioner från biblioteket RPi.GPIO.

Filen main.py demonstrerar event-detektering i Python, där en callback-rutin kallas för att toggla en lysdiod ansluten till pin 17
vid nedtryckning av en tryckknapp ansluten till pin 27 (stigande flank).
