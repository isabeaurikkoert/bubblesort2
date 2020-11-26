listToSort = [3,6,9,7,1,3,2,6]
z = len(listToSort)

for probeer in range(z):

  for j in range(z - 1):  
     if listToSort[j] > listToSort[j + 1]: 
       listToSort[j], listToSort[j + 1] = listToSort[j + 1], listToSort[j]

print(listToSort)
