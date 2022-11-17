miles_gallon = float(input())
dollars_gallon = float(input())

mile_value1 = 20 / miles_gallon * dollars_gallon
mile_value2 = 75 / miles_gallon * dollars_gallon
mile_value3 = 500 / miles_gallon * dollars_gallon

print(f'{mile_value1:.2f} {mile_value2:.2f} {mile_value3:.2f}')
