########### Question 14 #########         
#********** UNIT CONVERTER **********

value = float(input("Enter a length: "))
unit_from = input("Enter the unit to convert from (inch, yard, mile, km, m, cm): ")
unit_to = (
    input("Enter the unit to convert to (inch, yard, mile, km, m, cm): ")
    .strip()                     
    .lower()
)      ###.strip() means space/blank/whitespace remover.

if unit_from == "inch":
    if unit_to == "yard":
        result = value * 0.0278
    elif unit_to == "mile":
        result = value * 0.00002
    elif unit_to == "km":
        result = value * 0.00003
    elif unit_to == "m":
        result = value * 0.0254
    elif unit_to == "cm":
        result = value * 2.54
    else:
        result = None

if unit_from == "yard":
    if unit_to == "inch":
        result = value * 36
    elif unit_to == "mile":
        result = value * 0.000589
    elif unit_to == "km":
        result = value * 0.0009
    elif unit_to == "m":
        result = value * 0.9144
    elif unit_to == "cm":
        result = value * 91.44
    else:
        result = None

if unit_from == "mile":
    if unit_to == "inch":
        result = value * 36360
    elif unit_to == "yard":
        result = value * 1760
    elif unit_to == "km":
        result = value * 1.6093
    elif unit_to == "m":
        result = value * 1609.344
    elif unit_to == "cm":
        result = value * 160934.4
    else:
        result = None

if unit_from == "km":
    if unit_to == "inch":
        result = value * 39370
    elif unit_to == "mile":
        result = value * 0.6214
    elif unit_to == "yard":
        result = value * 1093.61
    elif unit_to == "m":
        result = value * 1000
    elif unit_to == "cm":
        result = value * 100000
    else:
        result = None

if unit_from == "m":
    if unit_to == "inch":
        result = value * 39.37
    elif unit_to == "mile":
        result = value * 0.0006
    elif unit_to == "km":
        result = value * 0.001
    elif unit_to == "yard":
        result = value * 1.0936
    elif unit_to == "cm":
        result = value * 100
    else:
        result = None

if unit_from == "cm":
    if unit_to == "inch":
        result = value * 0.3937
    elif unit_to == "mile":
        result = value * 0.000015
    elif unit_to == "km":
        result = value * 0.000012
    elif unit_to == "m":
        result = value * 0.01
    elif unit_to == "yard":
        result = value * 0.0109
    else:
        result = None

if result is not None:
    print(f"{value} {unit_from} is equal to {result} {unit_to}")
else:
    print("Invalid unit entered.")
