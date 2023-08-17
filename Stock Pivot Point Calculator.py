def calculate_pivot_points(high, low, close):
    pivot = (high + low + close) / 3
    first_support = 2 * pivot - high
    first_resistance = 2 * pivot - low
    second_support = pivot - (high - low)
    second_resistance = pivot + (high - low)
    
    fibonacci_support = pivot - 0.382 * (high - low)
    fibonacci_resistance = pivot + 0.382 * (high - low)
    
    return {
        "Pivot": pivot,
        "First Support": first_support,
        "First Resistance": first_resistance,
        "Second Support": second_support,
        "Second Resistance": second_resistance,
        "Fibonacci Support": fibonacci_support,
        "Fibonacci Resistance": fibonacci_resistance
    }

if __name__ == "__main__":
    high = float(input("Enter the High price: "))
    low = float(input("Enter the Low price: "))
    close = float(input("Enter the Close price: "))
    
    pivot_points = calculate_pivot_points(high, low, close)
    
    print("\nSupport levels (GREEN):")
    for level, value in pivot_points.items():
        if "Support" in level:
            print(f"\033[32m{level}: {value:.2f}\033[0m")
    
    print("\nResistance levels (RED):")
    for level, value in pivot_points.items():
        if "Resistance" in level:
            print(f"\033[31m{level}: {value:.2f}\033[0m")
    
    print("\n")
    print("Pivot Point (BLUE):")
    print(f"\033[34mPivot: {pivot_points['Pivot']:.2f}\033[0m")
    
    print("\n")
    print("Fibonacci levels:")
    print("\n")
    
    for level, value in pivot_points.items():
        if "Fibonacci" in level:
            print(f"{level}: {value:.2f}")
