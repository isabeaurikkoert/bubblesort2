listToSort = [8,7,6,5,4,3,2,1]
z = len(listToSort)

for probeer in range(z):

  for j in range(z - 1):  
     if listToSort[j] > listToSort[j + 1]: 
       listToSort[j], listToSort[j + 1] = listToSort[j + 1], listToSort[j]

print(listToSort)