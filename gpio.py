################################################################################
# gpio.py: User friendly GPIO implementation for Raspberry Pi via classes
#          output and input. The library RPi.GPIO is used for GPIO control,
#          i.e. input and output signals, event detection etc.
################################################################################
import RPi.GPIO as GPIO # Import library as GPIO.
GPIO.setwarnings(False) # Disables unnecessary warnings.
GPIO.setmode(GPIO.BCM) # Using GPIO pin numbers.

# Parameters:
RISING_EDGE = GPIO.RISING 
FALLING_EDGE = GPIO.FALLING
BOTH_EDGES = GPIO.BOTH

class output:
   """
   output: Class for output devices connected to Raspberry Pi.

           - __pin    : The pin number the output device is connected to.
           - __enabled: Indicates if the output signal is high.

   """

   def __init__(self, pin):
      """
      __init__: Initiating new output device connected to specified pin.

                - pin: The pin number the output device is connected to.
      """
      self.__pin = pin
      self.__enabled = False
      GPIO.setup(self.__pin, GPIO.OUT)
      return

   def __del__(self):
      """
      __del__: Resets GPIO pin before output object is deleted.
      """
      GPIO.output(self.__pin, 0)
      GPIO.setup(self.__pin, GPIO.IN)
      self.__pin = None
      self.__enabled = None
      return

   def pin(self):
      """
      pin: Returns the pin number of the output device.
      """
      return self.__pin

   def enabled(self):
      """
      enabled: Indicates if the output signal is high.
      """
      return self.__enabled

   def on(self):
      """
      on: Sets output value to high on specified device.
      """
      GPIO.output(self.__pin, 1)
      self.__enabled = True
      return

   def off(self):
      """
      off: Sets output value to low on specified device.
      """
      GPIO.output(self.__pin, 0)
      self.__enabled = False
      return

   def toggle(self):
      """
      toggle: Toggles output value on specified device.
      """
      if self.__enabled:
         self.off()
      else:
         self.on()
      return

   def blink(self, blink_speed_ms):
      """
      blink: Blinks the output value of specified device
             with specified blink speed.
      
             - blink_speed_ms: The blink speed measured in milliseconds.
      """
      self.toggle()
      delay(blink_speed_ms)
      self.toggle()
      delay(blink_speed_ms)
      return

class input:
   """
   input: Class for input deviced connected to Raspberry Pi.

          - __pin          : The pin number of the input device.
          - __event_enabled: Indicated if event detection is enabled.
   """

   def __init__(self, pin):
      """
      __init__: Initiating input device at specified pin.

                - pin: The pin number the input device is connected to.
      """
      self.__pin = pin
      self.__event_enabled = False
      GPIO.setup(self.__pin, GPIO.IN)
      return

   def __del__(self):
      """
      __del__: Disables event detection before input object is deleted.
      """
      self.disable_event_detection()
      self.__pin = None 
      self.__event_enabled = None
      return

   def pin(self):
      """
      pin: Returns the pin number of the input device.
      """
      return self.__pin

   def event_enabled(self):
      """
      event_enabled: Indicates if event detection is enabled.
      """
      return self.__event_enabled

   def read(self):
      """
      read: Reads the input value of the device as high (1) or low (0).
      """
      return GPIO.input(self.__pin)

   def enable_event_detection(self, edge, callback, bouncetime_ms = 50):
      """
      enable_event_detection: Enables event detection for the input device.
                              When the event is occuring, the specified
                              callback routine is called. The bounce time
                              is used to protect against contact bounces.

                              - edge        : The specified edge to be detected
                                              (rising, falling or both).
                              - callback    : Callback function/routine to be
                                              called when the event is occuring.
                             - bouncetime_ms: Debounce time for protection against
                                              contact bounces (default = 50 ms).
      """
      GPIO.add_event_detect(self.__pin, edge, callback, bouncetime_ms)
      self.__event_enabled = True
      return

   def disable_event_detection(self):
      """
      disable_event_detection: Disables event detection for input device.
      """
      GPIO.remove_event_detect(self.__pin) 
      self.__event_enabled = False
      return

def delay(delay_time_ms):
   """
   delay: Generates specified delay time measured in milliseconds.

          - delay_time_ms: Delay time in milliseconds.
   """
   import time
   time.sleep(delay_time_ms / 1000.0)
   return






