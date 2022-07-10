from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v

while True:
  pot_value = pot.read()
  value = round(((pot_value * 3.31) / 4095) * 5, 2)
  print(value)
  sleep(0.1)