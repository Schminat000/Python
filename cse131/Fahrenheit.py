def main():

    fahrenheit = getTemperature()
    celsius = convert(fahrenheit)
    display(celsius)

def getTemperature():
    
    fahrenheit = float(input("What is the temperature in Fahrenheit? "))
    return fahrenheit

def convert(fahrenheit):
    
    celsius = (fahrenheit - 32) * (5/9)
    return celsius

def display(celsius):
    
    print(celsius)

if __name__ == "__main__":
    main()