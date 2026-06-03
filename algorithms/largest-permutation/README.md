# Largest Permutation

## 🧩 Problem

You are given an unordered array of unique integers incrementing from 1. You can swap any two elements a limited number of times. Determine the largest lexicographical value array that can be created by executing no more than the limited number of swaps.

**Example**

arr = [1,2,3,4]

k = 1

``` text 
[2,1,3,4]
[3,2,1,4]
[4,2,3,1]
```

The highest value of the four (including the original) is [4,2,3,1]. If k>=2, we can swap to the highest possible value: [4,3,2,1].