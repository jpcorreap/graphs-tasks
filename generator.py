from random import randint


N = 10
M = 8

file = open("input/pal_readme.txt", "w")

file.write(f"{M} {N}\n")

for i in range(10):
    file.write(f"{randint(0, M-1)} {randint(0, N-1)}\n")

file.close()
print("Terminó")