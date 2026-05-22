# Beautiful Pairs

## 🧩 Problem

You are given two arrays, A and B, both containing N integers.

A pair of indices (i,j) is beautiful if the i<sup>th</sup> element of array A is equal to the j<sup>th</sup> element of array B. In other words, pair (i,j) is beautiful if and only if A[i] = B[j]. A set containing beautiful pairs is called a beautiful set.

A beautiful set is called pairwise disjoint if for every pair (l[i],r[j]) belonging to the set there is no repetition of either l[i] or r[i] values. For instance, if A = [10,11,12,5,14] and B = [8,9,11,11,5] the beautiful set [(1,2),(1,3),(3,4)] is not pairwise disjoint as there is a repetition of 1, that is l[0][0] = l[1][0].

Your task is to change exactly 1 element in B so that the size of the pairwise disjoint beautiful set is maximum.

**Example**

``` text 
4
1234
1233
```

**Sample Output**

``` text 
4
```

