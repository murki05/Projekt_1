def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def read_data_from_file(ki.txt):
    data = []
    try:
        with open(ki.txt, 'r') as file:
            for line in file:
                data.append(line.strip())
        return data
    except FileNotFoundError:
        print(f"A(z) {ki.txt} fájl nem található.")
        return None

def simple_swap_sort(arr, reverse=False):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if (not reverse and arr[j] > arr[j + 1]) or (reverse and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def bubble_sort(arr, reverse=False):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (not reverse and arr[j] > arr[j + 1]) or (reverse and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertion_sort(arr, reverse=False):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and ((not reverse and arr[j] > key) or (reverse and arr[j] < key)):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr, reverse=False):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if (not reverse and arr[j] < arr[min_idx]) or (reverse and arr[j] > arr[min_idx]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def custom_sort(arr, reverse=False):
    pass

def main():
    filename = "ki.txt"
    data = read_data_from_file(filename)

    if data is None:
        return

    is_numeric = all(is_number(item) for item in data)

    if is_numeric:
        data = [float(item) for item in data]
    else:
        data = [str(item) for item in data]

    print("Az adatok beolvasása után:")
    print(data)

    while True:
        print("\nVálassz rendezési algoritmust:")
        print("1. Egyszerű cserés rendezés")
        print("2. Buborékrendezés")
        print("3. Beszúrásos rendezés")
        print("4. Minimum/maximumkiválasztásos rendezés")
        print("5. Saját rendezési algoritmus")
        print("0. Kilépés")
        choice = input("Választás (0-5): ")

        if choice == "0":
            break
        elif choice in ("1", "2", "3", "4", "5"):
            reverse = input("Növekvő (n) vagy csökkenő (c) rendezés? ").lower() == "c"

            if choice == "1":
                simple_swap_sort(data, reverse)
            elif choice == "2":
                bubble_sort(data, reverse)
            elif choice == "3":
                insertion_sort(data, reverse)
            elif choice == "4":
                selection_sort(data, reverse)
            elif choice == "5":
                custom_sort(data, reverse)

            print("\nRendezés után:")
            print(data)
        else:
            print("Érvénytelen választás!")

    while True:
        new_item = input("\nÚj elem hozzáadása (üres sor befejezi): ")
        if not new_item:
            break
        if is_numeric:
            if is_number(new_item):
                data.append(float(new_item))
            else:
                print("Érvénytelen adat!")
        else:
            data.append(new_item)

        print("\nAz adatok frissítése után:")
        print(data)

    with open(filename, 'w') as file:
        for item in data:
            file.write(str(item) + "\n")

if __name__ == "__main__":
    main()
