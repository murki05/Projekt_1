def read_file(filename):
try:
with open(filename, 'r') as file:
lines = file.readlines()
return [line.strip() for line in lines]
except FileNotFoundError:
print("A megadott fájl nem található.")
return []

def is_numeric(value):
try:
float(value)
return True
except ValueError:
return False

def bubble_sort(data, reverse=False):
n = len(data)
for i in range(n):
for j in range(0, n - i - 1):
if (data[j] > data[j + 1] and not reverse) or (data[j] < data[j + 1] and reverse):
data[j], data[j + 1] = data[j + 1], data[j]

def main():
filename = input("Kérem, adja meg a fájl nevét: ")
data = read_file(filename)

if not data:
return

if all(is_numeric(item) for item in data):
data = [float(item) for item in data]
numeric = True
else:
numeric = False
print("Az adatok nem mind számok, szöveges adatok is vannak.")

print("Az adatok:", data)

while True:
choice = input("Válasszon rendezési módot (növekvő/csökkenő): ").lower()
if choice == 'növekvő':
bubble_sort(data)
break
elif choice == 'csökkenő':
bubble_sort(data, reverse=True)
break
else:
print("Érvénytelen választás. Kérem, válasszon növekvő vagy csökkenő rendezés közül.")

print("Rendezett adatok:", data)

if name == "main":
main()
