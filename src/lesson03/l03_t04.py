# -*- coding: UTF-8 -*-

while True:
    try:
        response = input("Enter a number (int or float): ")
        response = float(response) if "." in response else int(response)
    except ValueError:
        print("Not a number, try again.")
        continue
    break

converted = "-" + str(response)[:0:-1] if response < 0 else str(response)[::-1]
converted = float(converted) if isinstance(response, float) else int(converted)

print("Converted number: {}, type: {}".format(converted, type(converted)))
