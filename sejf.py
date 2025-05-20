count = 0
for i in range(2, 10, 2):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 5):
             if i + j + k + l == 21:
                print(i, j, k, l)
                count += 1
print(f"Počet cifer:{count}.")
# cifry se nesmí opakovat.