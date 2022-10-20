a = int(input("Üçgenin 1. kenarı:"))
b = int(input("Üçgenin 2. kenarı:"))
c = int(input("Üçgenin 3. kenarı:"))
if a==b and b==c:
    print("eşkenar")
elif a==b or a==c or b==c:
    print("ikizkenar")
else:
    print("çeşitkenar")