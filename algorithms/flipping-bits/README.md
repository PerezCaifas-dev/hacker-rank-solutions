You will be given a list of 32 bit unsigned integers. Flip all the bits (1 -> 0 and 0 -> 1) and return the result as an unsigned integer.

*Example*
n = 9<sup>10</sup>

9<sup>10</sup> = 1001<sup>2</sup>. We're working with 32 bits, so:
00000000000000000000000000001001<sup>2</sup> = 9<sup>10</sup>
11111111111111111111111111110110<sup>2</sup> = 4294967286<sup>10</sup>

Return 4294967286.

*Sample Input 0*

```
3
2147483647
1
0
```

*Sample Output 0*

```
2147483648
4294967294
4294967295
```