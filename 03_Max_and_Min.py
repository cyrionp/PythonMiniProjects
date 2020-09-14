numbers=input("Input numbers with spaces: ")
listNumbers=numbers.split(" ")
listNumbers.sort()
print(f"Max: {listNumbers[-1]} Min: {listNumbers[0]}")
