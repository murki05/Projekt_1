import random
while True:
    print("Válassz egy lehetőséget!")
    print("1. Véletlen számok generálása")
    print("2. Véletlen szöveg generálása")
    print("3. Számok ellenőrzése")
    print("4. Szöveg ellenőrzése")
    print("5. Kilépés")

    choice = input("Választott lehetőség (1/2/3/4/5): ")

    if choice == "1":
        lower_limit = int(input("Add meg az alsó határt: "))
        upper_limit = int(input("Add meg a felső határt: "))
        count = int(input("Add meg a számok darabszámát: "))
        numbers = [random.randint(lower_limit,upper_limit) for _ in range(count)]
        with open("ki.txt", "w") as f:
            f.write(";".join(map(str,numbers)))
        print("Számok generálva és kiírva a ki.txt-be.")

    elif choice == "2":
        count = int(input("Add meg a szövegek darabszámát: "))
        texts = [''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(1,20)))for _ in range(count)]
        with open("ki.txt", "w") as f:
            f.write(";".join(texts))
        print("Szövegek generálva és kiírva a ki.txt-be.")

    elif choice == "3":
        lower_limit = int(input("Add meg az alsó határt: "))
        upper_limit = int(input("Add meg a felső határt: "))
        with open("ki.txt","r") as f:
            data = f.read()
        numbers = [int(num) for num in data.split(";")]
        if all(lower_limit <= num <= upper_limit for num in numbers):
            print("A számok megfelelnek a feltételeknek.")
        else:
            print("A számok nem felelnek meg a feltételeknek.")

    elif choice == "4":
        with open("ki.txt","r") as f:
            data = f.read()
        texts = data.split(";")
        if all (1 <= len(text) <= 20 for text in texts):
            print("A szövegek megfelelnek a feltételeknek.")
        else:
            print("A szövegek nem felelnek meg a feltételeknek.")

    elif choice == "5":
        break
