<h2><a href="https://leetcode.com/problems/minimum-array-end">Minimum Array End</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>You are given two integers <code>n</code> and <code>x</code>. You have to construct an array of <strong>positive</strong> integers <code>nums</code> of size <code>n</code> where for every <code>0 &lt;= i &lt; n - 1</code>, <code>nums[i + 1]</code> is <strong>greater than</strong> <code>nums[i]</code>, and the result of the bitwise <code>AND</code> operation between all elements of <code>nums</code> is <code>x</code>.</p>

<p>Return the <strong>minimum</strong> possible value of <code>nums[n - 1]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, x = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<p><code>nums</code> can be <code>[4,5,6]</code> and its last element is 6.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 2, x = 7</span></p>

<p><strong>Output:</strong> <span class="example-io">15</span></p>

<p><strong>Explanation:</strong></p>

<p><code>nums</code> can be <code>[7,15]</code> and its last element is 15.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n, x &lt;= 10<sup>8</sup></code></li>
</ul>


Approach/Solution:

Approach
As the AND over all elements of the list should be x. Therefore, the samllest number that can be placed inside the list is x (as AND of two or more number is less than or equals to the smallest number). So let the first element be x.

For example if x = 18, think of first element as '10010'

Also, as the AND over all element is x itself, thus binary representation of all numbers must have 1 at second last and 5th last position else the AND would get smaller than x.

Observation:
If I just maintain these two things:
1. The smallest number is x itself
2. All elements must have 1's at the positions where x had ones (postion from last)

Then we are surely getting AND of all items as x.

Now, just need to think what would be next greater element with these two constraints and that would do:

x is '10010', shouldn't next greater be '10011', what should be just next greater element, shouldn't it be 10110, the next one 10111 ans so on. It's like we are bound to place 1's at position where x has ones but where it is 0, think of placing numbers in order like, in the current example:

The smallest number x = '10010', 0's were places by 000 (0)
The next number '10011', 0' were placed by 001 (1)
The next number '10110', 0' were placed by 010 (2)
The next number '10111', 0' were placed by 011 (3)
The next number '11010', 0' were placed by 100 (4)
The next number '11011', 0' were placed by 101 (5)

ans so on.

Now in case all zeros within x is filled, think that x = '10010' can also be written as '00010010' so start filling zeros on the left as necessary.

Thus, find binary of x, and binary of (n-1) and in place of zeros of x, place the binart of (n-1). Done.

Complexity
Time complexity:
O(logn)

Space complexity:
O(logn)
