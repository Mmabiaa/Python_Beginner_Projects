def power (base, exp):
  if exp == 0:
  return 1
  return base * power(base, exp - 1)
base = int(input("Enter the base number: "))
exp = int(input("Enter the exponent: "))
print (power (base, exp))
