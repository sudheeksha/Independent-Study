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
Index | Suffix
----- | ------
1 | BANANA
2 | ANANA
3 | NANA
4 | ANA
5 | NA
6 | A

After sorting the suffixes, we get – 6A
Index | Suffix
----- | ------
4 | ANA
2 | ANANA
1 | BANANA 
5 | NA
3 | NANA

Once we sort the suffixes, we get the prefix string of each string and generate all possible substrings. For example, NANA will make [N, NA, NAN, NANA]. Notice that all the substrings are produced in the correct lexicographical order that needs to be concatenated. By going through the sorted suffixes array and generating all the substring for each suffix, we get all substrings in the order required for concatenation. We skip any duplicates. For example, A and ANA have one character as a common prefix, so the first character in ANA is omitted. Once we have all the substrings, we concatenate them and print out the kth value.

## Insertion Sort Advanced Analysis
### Problem Statement 
Insertion Sort is a simple sorting technique which was covered in previous challenges. Sometimes, arrays may be too large for us to wait around for insertion sort to finish. Is there some other way we can calculate the number of shifts an Insertion Sort performs when
sorting an array?
If k\[i] is the number of elements over which the element of the array has to shift, then the total number of shifts will be k[1] + k[2]+...+k[n].

### Implementation 
An easy approach to this problem is to implement insertion sort and count the number of shifts. This approach would take +(,$) time. A better way to do this is to implement merge sort where number of shifts is incremented when a number in 2nd array is smaller than a number in 1st array. Here, the number of shifts equals the sum of values returned by merge sort of 1st and 2nd array. The shifts in each array are found and added and returned. Like merge sort, this occurs recursively till all the elements in the array are sorted, and each of their shifts is counted.
- First, the array to be sorted is passed. The array is divided into two halves by the merge sort function, and two new merge sort functions are called. This recursively divides the array into individual elements.
- During the merge sort process, each time if a value of the 2nd array is larger than the 1st array, the number of shifts it would have to make to its valid position is added to the counter.
- Once the sorting process ends, the count of shifts is returned. Recursively, all the shift counts are added.

## Jogging Cats
### Problem Statement
It's almost summertime, so Big Cat and Little Cat are getting in shape. They decide the core of their fitness plan is to start jogging every day.
Their city consists of N intersections connected by M bidirectional roads. The cats decide that their jogging route should be cyclic (i.e., starting and ending at the same intersection) and consist of 4 different roads.
The cats also love exploring new places, so each day they want to choose a new route to jog on that is not equal to any of their previous routes. Two routes are considered to be equal if their sets of component roads are equal.
Given a map of the city, can you help our heroic cats determine the maximum number of days they can go jogging so that every route traveled is different?
### Implementation
• The N nodes are split into two kinds of nodes – big nodes and small nodes 2
• To split the nodes, T = N3. If a node is bigger than T, then it is a big node. Otherwise, it is a small node.
• All the cycles can be now found using the following steps -
o For a cycle with four small nodes, using brute force, we find one node and then
two other neighbors and the fourth node that is adjacent to the neighbors.
o For a cycle with three nodes, using brute force, we find one node and then two
other neighbors and the fourth node that is adjacent to the neighbors; also, the
fourth node is a big node.
o For a cycle with two nodes that are not connected by an edge, using brute force,
find a small node, and two big nodes. The big nodes found should be such that it forms a three-length path with a small node, and the small node is in between the two big nodes.
o For a cycle with two nodes and a connected edge, we brute force and find two big nodes. We have to make sure that this forms a cycle.
o For a cycle with one node, brute force a small node and two big neighbors, and the fourth node should be such that it creates unordered end points.
o For a cycle with 0 nodes, brute force is used to find three big nodes that are connected.
### Time Complexity – The total time complexity is 0 56. ,78.
