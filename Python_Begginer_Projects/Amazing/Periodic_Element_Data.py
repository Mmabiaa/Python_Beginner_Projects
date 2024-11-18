import periodictable

# Prompt the user to input the atomic number
Atomic_Number = int(input('Enter the atomic number of the element: '))

# Use the `periodictable` module to get the element by its atomic number
element = periodictable.elements[Atomic_Number - 1]  # Indexing starts at 0, so subtract 1

# Display the element's information
print("Name:", element.name)
print('----------------------')
print("Symbol:", element.symbol)
print('----------------------')
print("Atomic mass:", element.mass)
print('----------------------')
print("Atomic density:", element.density)
print('----------------------')
