print ("Converting temp from Celsius to Fahrenheit")
Celsius=int(input("Enter Celsius:"))
if (Celsius >= 0):
   farenheit = 273 + Celsius
elif (Celsius <= 0):
   farenheit = Celsius - 273
else:
   print("Not valid") 
print("Temp in farenheit =",farenheit)