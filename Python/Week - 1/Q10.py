##Temperature converter + advice:Ask user for temperature in Celsius.Convert to Fahrenheit (°F = °C × 9/5 + 32),Then print advice:
##< 0 → "Very cold! Wear thick jacket"
##0–15 → "Cold. Wear jacket"
##16–25 → "Nice weather"
##25 → "Hot! Stay hydrated"

temperature = float(input("Enter temperature in Celsius: "))
f_temperature = (temperature * 9/5) + 32
print("Temperature in Fahrenheit:", f_temperature)
if temperature < 0:
    print("Very cold! Wear thick jacket.")
elif 0 <= temperature <= 15:
    print("Cold. Wear jacket.")
elif 16 <= temperature <= 25:
    print("Nice weather.")
else :
    print("Hot! Stay hydrated.")
