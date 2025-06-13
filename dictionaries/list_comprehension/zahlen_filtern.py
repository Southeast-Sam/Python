"""
# Gerade Zahlen filtern
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
gerade_zahlen = [x for x in zahlen if x % 2 == 0]
print("Gerade Zahlen:", gerade_zahlen)


zahlen = [zahl for zahl in range(30) if zahl % 3 == 0]
print(zahlen)
"""

# Gerade Quadrate
zahlen = [x**2 for x in range(1, 21) if x % 2 == 0]
print("Gerade Quadrate:", zahlen)