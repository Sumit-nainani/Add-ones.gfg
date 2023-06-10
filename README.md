# ADD ONES

approach:
    this problem is based on prefix sum,we will assign the max value to the array,
    then the value decrease by one at the index before updtaes[i] for each index.
    then add the value of a[i+1]-k for each index.
    n=3 k=4
    updates: 1 1 2 3
    a: 4  4  4 
      -1 -1 
      -1  0
    a: 2  3  4