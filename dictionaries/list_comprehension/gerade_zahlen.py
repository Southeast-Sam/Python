# Gerade Zahlen filtern
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
gerade_zahlen = [x for x in zahlen if x % 2 == 0]
print("Gerade Zahlen:", gerade_zahlen)