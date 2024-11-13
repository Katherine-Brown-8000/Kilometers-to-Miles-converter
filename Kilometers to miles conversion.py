metric = str(input("Enter K for Kilometers or M for Miles: "))
distant = float(input("Enter distance: "))


if metric == "K":
    km = distant * 0.62137119
    print(f"The distance in miles is {km:.2f}")
elif metric == "M":
    mk = distant * 1.609344
    print(f"distance in kilometers is {mk:.2f}")
