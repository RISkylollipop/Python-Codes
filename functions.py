numbers = [3,4,2,6,7,79,9,3, 2, 3, 4, 4, 5, 6, 6, 21,1,0,5,12,9]

uniques = [];
for number in numbers:
    if number not in uniques:
        uniques.append(number)
uniques.sort()
print(uniques)
