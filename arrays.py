def main():
    new_list = [1, 2, 3]
    result = new_list[0]

    if 1 in new_list:
        print(True)

    for i in new_list:
        if i == 1:
            print(True)
            break

    numbers1 = [1, 2, 3, 4, 5]
    numbers2 = [6, 7, 8, 9]
    numbers1.append(6)
    numbers1.pop(5)
    numbers1.extend(numbers2)
    print(numbers1)


if __name__ == "__main__":
    main()
