#format specifiers{valus:flags} format a value based on what flag are inserted

price1 = 5568450.35433
price2 = -86616423.46
price3 = 1298656.98

print(f"price 1 is  {price1:.2f}")#.2 is udes to round the decimal digit f represent floating point num
print(f"price 2 is  {price2:.2f}")
print(f"price 3 is  {price3:.2f}")

print(f"price 1 is  {price1:10}")#gives 10 space
print(f"price 2 is  {price2:10}")
print(f"price 3 is  {price3:10}")


print(f"price 3 is  {price3:010}")#add 0 in space

print(f"price 3 is  {price3:<10}")#left justified

print(f"price 3 is  {price3:>10}")#right justified

print(f"price 3 is  {price3:^10}")#centre align

print(f"price 1 is  {price1:+}")#gives + sign
print(f"price 2 is  {price2:+}")#negative num remains negative
print(f"price 3 is  {price3:+}")

print(f"price 1 is  {price1:+,.2f}")#
print(f"price 2 is  {price2:+,.2f}")
print(f"price 3 is  {price3:+,.2f}")
