# Independent Study
This independent study required solving challenging algorithmic problems of varying difficulties
from online sources, including HackerRank, Leetcode, and CodeChef. The solutions to these
problems had to pass the online judge provided in the afore mentioned online sources.

## Ashton and String
### Problem Statement
Ashton appeared for a job interview and is asked the following question. Arrange all the distinct substrings of a given string in lexicographical order and concatenate them. Print the character of the concatenated string. It is assured that given value of will be valid i.e.
there will be a character. Can you help Ashton out with this?
For example, given the string s= abcd, its distinct substrings are [a, ab, abc, abcd, b, bc, bcd, c, cd, d]. Sorted and concatenated, they make the string. If k = 5 then, the answer is b, the 5th character of the 1-indexed concatenated string.

### Implementation
The solution to this problem requires using a suffix array and the longest common prefixes. After finding distinct substrings, sorting strings using the merge sort can have the worst time complexity of O(N$ logN). To improve this, suffix arrays can be used. Suffix strings are part of a string and can be sorted using indexes. 
Let us take an example: BANANA
1 | BANANA
2 | ANANA
3 | NANA
4 | ANA
5 | NA
6 | A
After sorting the suffixes, we get – 6A
4 | ANA
2 | ANANA
1 | BANANA 
5 | NA
3 | NANA
Once we sort the suffixes, we get the prefix string of each string and generate all possible substrings. For example, NANA will make [N, NA, NAN, NANA]. Notice that all the substrings are produced in the correct lexicographical order that needs to be concatenated. By going through the sorted suffixes array and generating all the substring for each suffix, we get all substrings in the order required for concatenation. We skip any duplicates. For example, A and ANA have one character as a common prefix, so the first character in ANA is omitted. Once we have all the substrings, we concatenate them and print out the kth value.
