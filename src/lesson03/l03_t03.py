# -*- coding: UTF-8 -*-

response = input("Enter a string: ")
lower = 0
capital = 0
if response:
    for l in response:
        if str.isalpha(l):
            if str.islower(l):
                lower += 1
            else:
                capital += 1
    lower = round((lower * 100) / len(response), 2)
    capital = round((capital * 100) / len(response), 2)

print("String contains {} characters, {}% lower letters and {}% capital "
      "ones.".format(len(response), lower, capital))
