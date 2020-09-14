numbers=input("Input integers with spaces: ")
listNumbers=numbers.split(" ")
listNumbers.sort()
print(f"Max: {listNumbers[-1]} Min: {listNumbers[0]}")
