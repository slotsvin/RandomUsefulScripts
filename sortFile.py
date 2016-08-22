import time

filename = input("Enter file name/location: ")

start = time.time()

print("Sorting file", filename)

with open(filename, 'r') as f:
    lines = f.readlines()
    if "\n" not in lines[-1]:
        lines[-1] += "\n"

lines = sorted(lines)

with open(filename, 'w') as f:
    f.writelines(lines)

print("Done sorting lines in", filename)

print(time.time() - start)