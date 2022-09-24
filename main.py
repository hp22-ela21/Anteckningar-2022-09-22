################################################################################
# main.py: Demonstration of event detection for Raspberry Pi with a callback 
#          routine for toggling a led connected to pin 17 when a button
#          connected to pin 27 is pressed (rising edge).
################################################################################
import gpio

# Global members:
led1 = gpio.output(17) # Led connected to pin 17.

def interrupt_routine(pin):
   """
   interrupt_routine: Routine for toggling the led when the button is pressed.
                      This routine is called when an event occurs.

                      - pin: The pin number where the event was detected.
   """
   global led1 
   led1.toggle()
   return

def main():
   """
   main: Connects a button to pin 27 and enables event detection at rising edge.
         A callback routine named interrupt_routine is called when the button
         is pressed to toggle a led connected to pin 17.
    
   """
   button1 = gpio.input(27)
   button1.enable_event_detection(gpio.RISING_EDGE, interrupt_routine)
   while True:
      pass
   return

################################################################################
# If this file is the startup file of the project (indicated via the variable
# name), the main function is called to start the program.
################################################################################
if __name__ == "__main__":
   main()