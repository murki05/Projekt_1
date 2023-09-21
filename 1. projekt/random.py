import random
while True:
    print("Válassz egy lehetőséget!")
    print("1. Véletlen számok generálása")
    print("2. Véletlen szöveg generálása")
    print("3. Számok ellenőrzése")
    print("4. Szöveg ellenőrzése")

    valasz = input("Választott lehetőség (1/2/3/4): ")

    if valasz == "1":
        also_hatar = int(input("Add meg az alsó határt: "))
        felso_hatar = int(input("Add meg a felső határt: "))
        szamol = int(input("Add meg a számok darabszámát: "))
        szamok = [random.randint(also_hatar, felso_hatar) for _ in range(szamol)]
        with open("ki.txt", "w") as f:
            file.write(";".join(map(str, szamok)))
        print("Számok generálva és kiírva a ki.txt-be.")

    elif valasz == "2":
        szamol = int(input("Add meg a szövegek darabszámát: "))
        szovegek = [''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(1,20)))for _ in range(szamol)]
        with open("ki.txt","w") as f:
            file.write(";".join(szovegek))
        print("Szövegek generálva és kiírva a ki.txt-be.")

    elif valasz == "3":
        also_hatar = int(input("Add meg az alsó határt: "))
        felso_hatar = int(input("Add meg a felső határt: "))
        with open("ki.txt","r") as f:
            data = file.read()
        szamok = [int(num) for num in data.split(";")]
        if all(also_hatar <= num <= felso_hatar for num in szamok):
            print("A számok megfelelnek a feltételeknek.")
        else:
            print("A számok nem felelnek meg a feltételeknek.")

    elif choice == "4":
        with open("ki.txt","r") as f:
            data = file.read()
        szovegek = data.split(";")
        if all (1 <= len(text) <= 20 for text in szovegek):
            print("A szövegek megfelelnek a feltételeknek.")
        else:
            print("A szövegek nem felelnek meg a feltételeknek.")