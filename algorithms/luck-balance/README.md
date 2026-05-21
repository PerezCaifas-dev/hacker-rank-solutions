# Luck Balance

## 🧩 Problem

Lena is preparing for an important coding competition that is preceded by a number of sequential preliminary contests. Initially, her luck balance is 0. She believes in "saving luck", and wants to check her theory. Each contest is described by two integers, L[i] and T[i]:

- L[i] is the amount of luck associated with a contest. If Lena wins the contest, her luck balance will decrease by L[i]; if she loses it, her luck balance will increase by L[i].

- T[i] denotes the contest's importance rating. It's equal to  if the contest is important, and it's equal to 0 if it's unimportant.

Example 
k = 2
L = [5,1,4]
T = [1,1,0]

``` text 
Contest     L[i]        T[i]
1           5           1
2           1           1
3           4           0
```
If Lena loses all of the contests, her will be 5+1+4 = 10. Since she is allowed to lose 2 important contests, and there are only 2 important contests, she can lose all three contests to maximize her luck at 10.

If k = 1, she has to win at least  of the  important contests. She would choose to win the lowest value important contest worth . Her final luck will be 5 + 4 - 1 = 8.
