import RPi.GPIO as GPIO, time, playSound

detectPin = 14
ledPin = 21
delay = 5

def detectCallback(inputpin):
  #if movement detected
  if GPIO.input(inputpin):
    print('true')
    GPIO.output(ledPin,GPIO.HIGH)
    playSound.playRandomSound()
    time.sleep(delay)
  else:
    print('false')
    GPIO.output(ledPin,GPIO.LOW)

try:
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(ledPin,GPIO.OUT)
  GPIO.setup(detectPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.add_event_detect(detectPin, GPIO.BOTH, callback = detectCallback)
  while True:
   time.sleep(0.1)

finally:
  print('Goodbye')
  GPIO.cleanup()
