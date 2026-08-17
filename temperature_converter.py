def celsius_to_all(c):
    f = (c * 9/5) + 32
    k = c + 273.15
    return f, k

def fahrenheit_to_all(f):
    c = (f - 32) * 5/9
    k = c + 273.15
    return c, k

def kelvin_to_all(k):
    c = k - 273.15
    f = (c * 9/5) + 32
    return c, f

def main():
    print("=== Temperature Conversion Program ===")
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").strip().upper()

    if unit == "C":
        f, k = celsius_to_all(temp)
        print(f"\n{temp}°C = {f:.2f}°F")
        print(f"{temp}°C = {k:.2f}K")

    elif unit == "F":
        c, k = fahrenheit_to_all(temp)
        print(f"\n{temp}°F = {c:.2f}°C")
        print(f"{temp}°F = {k:.2f}K")

    elif unit == "K":
        c, f = kelvin_to_all(temp)
        print(f"\n{temp}K = {c:.2f}°C")
        print(f"{temp}K = {f:.2f}°F")

    else:
        print("Invalid unit entered! Please enter C, F, or K.")

if __name__ == "__main__":
    main()
