# You start with an array A of size N. Initially all elements of the array A are zero. 
# You will be given K positive integers. Let j be one of these integers, you have to add 1 to all A[i], where i ≥ j. Your task is to print the array A after all these K updates are done.
# Note: 1-based indexing is used everywhere in this question.

class Solution:
    def update(self, a, n, updates, k):
        # Your code goes here
        for i in range(n):
            a[i]=k
        for i in range(k):
            if updates[i]-2>=0:
                a[updates[i]-2]-=1
        for i in range(n-2,-1,-1):
            a[i]+=a[i+1]-k

