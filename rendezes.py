def read_data_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data_line = file.readline()
        data = data_line.split(';')
        return [item.strip() for item in data]
    except FileNotFoundError:
        print("The file does not exist.")
        return None

def is_numeric(data):
    return all(item.replace(".", "", 1).isdigit() for item in data)

def bubble_sort(data, ascending=True):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ascending:
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
            else:
                if data[j] < data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]

def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

def insert_element(data, element):
    data.append(element)
    bubble_sort(data)

def main():
    filename = "ki.txt"
    data = read_data_from_file(filename)

    if data is None:
        return

    if is_numeric(data):
        data = [float(item) for item in data]

    print("Data read from file:", data)
    ascending = input("Do you want to sort in ascending order? (y/n): ").lower() == 'y'

    bubble_sort(data, ascending)
    print("Sorted data using Bubble Sort:", data)

    merge_sort(data.copy())
    print("Sorted data using Merge Sort:", data)

    new_element = input("Enter a new element to insert: ")
    if is_numeric([new_element]):
        new_element = float(new_element)
    insert_element(data, new_element)
    print("Updated data after insertion:", data)

if __name__ == "__main__":
    main()