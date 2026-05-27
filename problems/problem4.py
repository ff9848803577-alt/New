name = input("Enter your name:")

print(f"Good morning {name}") # here if we use f string we can use string name's entered value in any string by using curly braces and the variable name inside it. It is a very useful way to format strings in python.

letter = ''' Dear <|Name|>,
You are selected!
<|Date|>'''

print (letter.replace("<|Name|>", "Bikki").replace("<|Date|>", "20 sept"))


