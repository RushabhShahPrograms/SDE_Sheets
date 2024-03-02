'''
Write a program that will determine weather when the value of
temperature and humidity is provided by the user.
TEMPERATURE(C)                   HUMIDITY(%)             WEATHER
      >= 30                         >=90               Hot and Humid 
      >= 30                         < 90                   Hot
      <30                           >= 90              Cool and Humid
      <30                           <90                    Cool
'''

def determine_weather(temp,hum):
    if temp>=30:
        if hum>=90:
            return "Hot and Humid"
        else:
            return "Hot"
    else:
        if hum>=90:
            return "Cool and Humid"
        else:
            return "Cool"
        
temp = float(input("Enter the temperature in celsius: "))
hum = float(input("Enter the humidity in percentage: "))
result = determine_weather(temp,hum)
print(f"The  current weather is {result}")