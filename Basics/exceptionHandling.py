try:
    age = int(input("Enter Age: "))
    print("Born in "+str(2023-age))
except ValueError:
    print('Invalid value')