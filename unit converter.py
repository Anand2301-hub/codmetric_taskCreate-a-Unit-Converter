def temperature_converter():
    """Convert between Celsius, Fahrenheit, and Kelvin"""
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    
    choice = input("Enter your choice (1-6): ")
    value = float(input("Enter the temperature value to convert: "))
    
    conversions = {
        '1': lambda c: (c * 9/5) + 32,
        '2': lambda f: (f - 32) * 5/9,
        '3': lambda c: c + 273.15,
        '4': lambda k: k - 273.15,
        '5': lambda f: (f - 32) * 5/9 + 273.15,
        '6': lambda k: (k - 273.15) * 9/5 + 32
    }
    
    if choice in conversions:
        result = conversions[choice](value)
        units = {
            '1': ("°C", "°F"),
            '2': ("°F", "°C"),
            '3': ("°C", "K"),
            '4': ("K", "°C"),
            '5': ("°F", "K"),
            '6': ("K", "°F")
        }
        print(f"\n{value:.2f}{units[choice][0]} = {result:.2f}{units[choice][1]}")
    else:
        print("Invalid choice!")

def distance_converter():
    """Convert between kilometers, miles, meters, and feet"""
    print("\nDistance Converter")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Meters to Feet")
    print("4. Feet to Meters")
    print("5. Kilometers to Meters")
    print("6. Miles to Feet")
    
    choice = input("Enter your choice (1-6): ")
    value = float(input("Enter the distance value to convert: "))
    
    conversions = {
        '1': lambda km: km * 0.621371,
        '2': lambda mi: mi * 1.60934,
        '3': lambda m: m * 3.28084,
        '4': lambda ft: ft * 0.3048,
        '5': lambda km: km * 1000,
        '6': lambda mi: mi * 5280
    }
    
    if choice in conversions:
        result = conversions[choice](value)
        units = {
            '1': ("km", "mi"),
            '2': ("mi", "km"),
            '3': ("m", "ft"),
            '4': ("ft", "m"),
            '5': ("km", "m"),
            '6': ("mi", "ft")
        }
        print(f"\n{value:.2f}{units[choice][0]} = {result:.2f}{units[choice][1]}")
    else:
        print("Invalid choice!")

def weight_converter():
    """Convert between kilograms, pounds, and ounces"""
    print("\nWeight Converter")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    print("3. Kilograms to Ounces")
    print("4. Pounds to Ounces")
    print("5. Ounces to Kilograms")
    print("6. Ounces to Pounds")
    
    choice = input("Enter your choice (1-6): ")
    value = float(input("Enter the weight value to convert: "))
    
    conversions = {
        '1': lambda kg: kg * 2.20462,
        '2': lambda lb: lb * 0.453592,
        '3': lambda kg: kg * 35.274,
        '4': lambda lb: lb * 16,
        '5': lambda oz: oz * 0.0283495,
        '6': lambda oz: oz * 0.0625
    }
    
    if choice in conversions:
        result = conversions[choice](value)
        units = {
            '1': ("kg", "lb"),
            '2': ("lb", "kg"),
            '3': ("kg", "oz"),
            '4': ("lb", "oz"),
            '5': ("oz", "kg"),
            '6': ("oz", "lb")
        }
        print(f"\n{value:.2f}{units[choice][0]} = {result:.2f}{units[choice][1]}")
    else:
        print("Invalid choice!")

def main():
    """Main program loop"""
    while True:
        print("\nUnit Converter")
        print("1. Temperature Converter")
        print("2. Distance Converter")
        print("3. Weight Converter")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            temperature_converter()
        elif choice == '2':
            distance_converter()
        elif choice == '3':
            weight_converter()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()