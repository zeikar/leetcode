# LeetCode

**A study log, and the tool that made it work.**

Every problem here has two halves: a solution file in this repo, and a study
note in [Issues](https://github.com/zeikar/leetcode/issues) covering what the
problem asked, what was tried, what failed, and why the working idea works. The
notes are published at **https://zeikar.dev/leetcode/**.

Studying this way needs something that will not just hand over the answer — so
that ships here too.

## leetcode-study — a Claude Code plugin for studying LeetCode

[![Claude Code plugin](https://img.shields.io/badge/Claude_Code-plugin-d97757)](plugin/)

Claude gives **one hint level at a time, then stops and waits** — topic tags
held back until you ask for them, and a wrong submission answered with the
smallest input that breaks it rather than a rewritten function. The most recent
notes below came out of sessions like that.

```
/plugin marketplace add zeikar/leetcode
/plugin install leetcode-study@leetcode-study
```

[**What a session looks like →**](plugin/)

## Solved problems

Generated from the issues by
[`update-index.yml`](.github/workflows/update-index.yml) — don't edit by hand.
Recording a solved problem is a separate skill in `.claude/skills/`, kept local
rather than shipped in the plugin because it is built around this repo's issue
template, index workflow and commit convention.

<!-- PROBLEMS:START -->

**157 solved** — Easy 13 · Medium 77 · Hard 67

| # | Problem | Difficulty | Solution |
| ---: | --- | --- | --- |
| 1 | [Two Sum](https://zeikar.dev/leetcode/posts/1/) | Easy | [two-sum.py](two-sum.py) |
| 2 | [Add Two Numbers](https://zeikar.dev/leetcode/posts/121/) | Medium | [add-two-numbers.py](add-two-numbers.py) |
| 4 | [Median of Two Sorted Arrays](https://zeikar.dev/leetcode/posts/8/) | Hard | [median-of-two-sorted-arrays.py](median-of-two-sorted-arrays.py) |
| 15 | [3Sum](https://zeikar.dev/leetcode/posts/17/) | Medium | [3sum.py](3sum.py) |
| 20 | [Valid Parentheses](https://zeikar.dev/leetcode/posts/41/) | Easy | [valid-parentheses.py](valid-parentheses.py) |
| 23 | [Merge k Sorted Lists](https://zeikar.dev/leetcode/posts/7/) | Hard | [merge-k-sorted-lists.py](merge-k-sorted-lists.py) |
| 29 | [Divide Two Integers](https://zeikar.dev/leetcode/posts/99/) | Medium | [divide-two-integers.py](divide-two-integers.py) |
| 32 | [Longest Valid Parentheses](https://zeikar.dev/leetcode/posts/2/) | Hard | [longest-valid-parentheses.py](longest-valid-parentheses.py) |
| 40 | [Combination Sum II](https://zeikar.dev/leetcode/posts/135/) | Medium | [combination-sum-ii.py](combination-sum-ii.py) |
| 41 | [First Missing Positive](https://zeikar.dev/leetcode/posts/6/) | Hard | [first-missing-positive.py](first-missing-positive.py) |
| 42 | [Trapping Rain Water](https://zeikar.dev/leetcode/posts/10/) | Hard | [trapping-rain-water.py](trapping-rain-water.py) |
| 49 | [Group Anagrams](https://zeikar.dev/leetcode/posts/122/) | Medium | [group-anagrams.py](group-anagrams.py) |
| 57 | [Insert Interval](https://zeikar.dev/leetcode/posts/104/) | Medium | [insert-interval.py](insert-interval.py) |
| 61 | [Rotate List](https://zeikar.dev/leetcode/posts/40/) | Medium | [rotate-list.py](rotate-list.py) |
| 65 | [Valid Number](https://zeikar.dev/leetcode/posts/5/) | Hard | [valid-number.py](valid-number.py) |
| 71 | [Simplify Path](https://zeikar.dev/leetcode/posts/149/) | Medium | [simplify-path.py](simplify-path.py) |
| 84 | [Largest Rectangle in Histogram](https://zeikar.dev/leetcode/posts/4/) | Hard | [largest-rectangle-in-histogram.py](largest-rectangle-in-histogram.py) |
| 85 | [Maximal Rectangle](https://zeikar.dev/leetcode/posts/15/) | Hard | [maximal-rectangle.py](maximal-rectangle.py) |
| 97 | [Interleaving String](https://zeikar.dev/leetcode/posts/81/) | Medium | [interleaving-string.py](interleaving-string.py) |
| 103 | [Binary Tree Zigzag Level Order Traversal](https://zeikar.dev/leetcode/posts/152/) | Medium | [binary-tree-zigzag-level-order-traversal.py](binary-tree-zigzag-level-order-traversal.py) |
| 124 | [Binary Tree Maximum Path Sum](https://zeikar.dev/leetcode/posts/63/) | Hard | [binary-tree-maximum-path-sum.py](binary-tree-maximum-path-sum.py) |
| 128 | [Longest Consecutive Sequence](https://zeikar.dev/leetcode/posts/147/) | Medium | [longest-consecutive-sequence.py](longest-consecutive-sequence.py) |
| 129 | [Sum Root to Leaf Numbers](https://zeikar.dev/leetcode/posts/153/) | Medium | [sum-root-to-leaf-numbers.py](sum-root-to-leaf-numbers.py) |
| 131 | [Palindrome Partitioning](https://zeikar.dev/leetcode/posts/148/) | Medium | [palindrome-partitioning.py](palindrome-partitioning.py) |
| 138 | [Copy List with Random Pointer](https://zeikar.dev/leetcode/posts/39/) | Medium | [copy-list-with-random-pointer.py](copy-list-with-random-pointer.py) |
| 139 | [Word Break](https://zeikar.dev/leetcode/posts/83/) | Medium | [word-break.py](word-break.py) |
| 149 | [Max Points on a Line](https://zeikar.dev/leetcode/posts/13/) | Hard | [max-points-on-a-line.py](max-points-on-a-line.py) |
| 152 | [Maximum Product Subarray](https://zeikar.dev/leetcode/posts/27/) | Medium | [maximum-product-subarray.py](maximum-product-subarray.py) |
| 169 | [Majority Element](https://zeikar.dev/leetcode/posts/90/) | Easy | [majority-element.py](majority-element.py) |
| 173 | [Binary Search Tree Iterator](https://zeikar.dev/leetcode/posts/53/) | Medium | [binary-search-tree-iterator.py](binary-search-tree-iterator.py) |
| 174 | [Dungeon Game](https://zeikar.dev/leetcode/posts/28/) | Hard | [dungeon-game.py](dungeon-game.py) |
| 199 | [Binary Tree Right Side View](https://zeikar.dev/leetcode/posts/80/) | Medium | [binary-tree-right-side-view.py](binary-tree-right-side-view.py) |
| 201 | [Bitwise AND of Numbers Range](https://zeikar.dev/leetcode/posts/101/) | Medium | [bitwise-and-of-numbers-range.py](bitwise-and-of-numbers-range.py) |
| 214 | [Shortest Palindrome](https://zeikar.dev/leetcode/posts/33/) | Hard | [shortest-palindrome.py](shortest-palindrome.py) |
| 215 | [Kth Largest Element in an Array](https://zeikar.dev/leetcode/posts/150/) | Medium | [kth-largest-element-in-an-array.py](kth-largest-element-in-an-array.py) |
| 218 | [The Skyline Problem](https://zeikar.dev/leetcode/posts/110/) | Hard | [the-skyline-problem.py](the-skyline-problem.py) |
| 224 | [Basic Calculator](https://zeikar.dev/leetcode/posts/14/) | Hard | [basic-calculator.py](basic-calculator.py) |
| 230 | [Kth Smallest Element in a BST](https://zeikar.dev/leetcode/posts/52/) | Medium | [kth-smallest-element-in-a-bst.py](kth-smallest-element-in-a-bst.py) |
| 231 | [Power of Two](https://zeikar.dev/leetcode/posts/97/) | Easy | [power-of-two.py](power-of-two.py) |
| 239 | [Sliding Window Maximum](https://zeikar.dev/leetcode/posts/9/) | Hard | [sliding-window-maximum.py](sliding-window-maximum.py) |
| 264 | [Ugly Number II](https://zeikar.dev/leetcode/posts/140/) | Medium | [ugly-number-ii.py](ugly-number-ii.py) |
| 268 | [Missing Number](https://zeikar.dev/leetcode/posts/67/) | Easy | [missing-number.py](missing-number.py) |
| 273 | [Integer to English Words](https://zeikar.dev/leetcode/posts/125/) | Hard | [integer-to-english-words.py](integer-to-english-words.py) |
| 279 | [Perfect Squares](https://zeikar.dev/leetcode/posts/86/) | Medium | [perfect-squares.py](perfect-squares.py) |
| 284 | [Peeking Iterator](https://zeikar.dev/leetcode/posts/58/) | Medium | [peeking-iterator.py](peeking-iterator.py) |
| 287 | [Find the Duplicate Number](https://zeikar.dev/leetcode/posts/105/) | Medium | [find-the-duplicate-number.py](find-the-duplicate-number.py) |
| 295 | [Find Median from Data Stream](https://zeikar.dev/leetcode/posts/11/) | Hard | [find-median-from-data-stream.py](find-median-from-data-stream.py) |
| 301 | [Remove Invalid Parentheses](https://zeikar.dev/leetcode/posts/42/) | Hard | [remove-invalid-parentheses.py](remove-invalid-parentheses.py) |
| 312 | [Burst Balloons](https://zeikar.dev/leetcode/posts/124/) | Hard | [burst-balloons.py](burst-balloons.py) |
| 315 | [Count of Smaller Numbers After Self](https://zeikar.dev/leetcode/posts/12/) | Hard | [count-of-smaller-numbers-after-self.py](count-of-smaller-numbers-after-self.py) |
| 336 | [Palindrome Pairs](https://zeikar.dev/leetcode/posts/29/) | Hard | [palindrome-pairs.py](palindrome-pairs.py) |
| 337 | [House Robber III](https://zeikar.dev/leetcode/posts/18/) | Medium | [house-robber-iii.py](house-robber-iii.py) |
| 368 | [Largest Divisible Subset](https://zeikar.dev/leetcode/posts/87/) | Medium | [largest-divisible-subset.py](largest-divisible-subset.py) |
| 399 | [Evaluate Division](https://zeikar.dev/leetcode/posts/62/) | Medium | [evaluate-division.py](evaluate-division.py) |
| 403 | [Frog Jump](https://zeikar.dev/leetcode/posts/50/) | Hard | [frog-jump.py](frog-jump.py) |
| 410 | [Split Array Largest Sum](https://zeikar.dev/leetcode/posts/64/) | Hard | [split-array-largest-sum.py](split-array-largest-sum.py) |
| 416 | [Partition Equal Subset Sum](https://zeikar.dev/leetcode/posts/23/) | Medium | [partition-equal-subset-sum.py](partition-equal-subset-sum.py) |
| 433 | [Minimum Genetic Mutation](https://zeikar.dev/leetcode/posts/151/) | Medium | [minimum-genetic-mutation.py](minimum-genetic-mutation.py) |
| 452 | [Minimum Number of Arrows to Burst Balloons](https://zeikar.dev/leetcode/posts/103/) | Medium | [minimum-number-of-arrows-to-burst-balloons.py](minimum-number-of-arrows-to-burst-balloons.py) |
| 476 | [Number Complement](https://zeikar.dev/leetcode/posts/144/) | Easy | [number-complement.py](number-complement.py) |
| 514 | [Freedom Trail](https://zeikar.dev/leetcode/posts/108/) | Hard | [freedom-trail.py](freedom-trail.py) |
| 517 | [Super Washing Machines](https://zeikar.dev/leetcode/posts/123/) | Hard | [super-washing-machines.py](super-washing-machines.py) |
| 525 | [Contiguous Array](https://zeikar.dev/leetcode/posts/102/) | Medium | [contiguous-array.py](contiguous-array.py) |
| 535 | [Encode and Decode TinyURL](https://zeikar.dev/leetcode/posts/55/) | Medium | [encode-and-decode-tinyurl.py](encode-and-decode-tinyurl.py) |
| 546 | [Remove Boxes](https://zeikar.dev/leetcode/posts/25/) | Hard | [remove-boxes.py](remove-boxes.py) |
| 563 | [Binary Tree Tilt](https://zeikar.dev/leetcode/posts/19/) | Easy | [binary-tree-tilt.py](binary-tree-tilt.py) |
| 592 | [Fraction Addition and Subtraction](https://zeikar.dev/leetcode/posts/145/) | Medium | [fraction-addition-and-subtraction.py](fraction-addition-and-subtraction.py) |
| 600 | [Non-negative Integers without Consecutive Ones](https://zeikar.dev/leetcode/posts/49/) | Hard | [non-negative-integers-without-consecutive-ones.py](non-negative-integers-without-consecutive-ones.py) |
| 624 | [Maximum Distance in Arrays](https://zeikar.dev/leetcode/posts/138/) | Medium | [maximum-distance-in-arrays.py](maximum-distance-in-arrays.py) |
| 647 | [Palindromic Substrings](https://zeikar.dev/leetcode/posts/88/) | Medium | [palindromic-substrings.py](palindromic-substrings.py) |
| 650 | [2 Keys Keyboard](https://zeikar.dev/leetcode/posts/141/) | Medium | [2-keys-keyboard.py](2-keys-keyboard.py) |
| 664 | [Strange Printer](https://zeikar.dev/leetcode/posts/143/) | Hard | [strange-printer.py](strange-printer.py) |
| 699 | [Falling Squares](https://zeikar.dev/leetcode/posts/37/) | Hard | [falling-squares.py](falling-squares.py) |
| 703 | [Kth Largest Element in a Stream](https://zeikar.dev/leetcode/posts/134/) | Easy | [kth-largest-element-in-a-stream.py](kth-largest-element-in-a-stream.py) |
| 719 | [Find K-th Smallest Pair Distance](https://zeikar.dev/leetcode/posts/136/) | Hard | [find-k-th-smallest-pair-distance.py](find-k-th-smallest-pair-distance.py) |
| 763 | [Partition Labels](https://zeikar.dev/leetcode/posts/46/) | Medium | [partition-labels.py](partition-labels.py) |
| 765 | [Couples Holding Hands](https://zeikar.dev/leetcode/posts/26/) | Hard | [couples-holding-hands.py](couples-holding-hands.py) |
| 778 | [Swim in Rising Water](https://zeikar.dev/leetcode/posts/44/) | Hard | [swim-in-rising-water.py](swim-in-rising-water.py) |
| 785 | [Is Graph Bipartite?](https://zeikar.dev/leetcode/posts/61/) | Medium | [is-graph-bipartite.py](is-graph-bipartite.py) |
| 787 | [Cheapest Flights Within K Stops](https://zeikar.dev/leetcode/posts/100/) | Medium | [cheapest-flights-within-k-stops.py](cheapest-flights-within-k-stops.py) |
| 790 | [Domino and Tromino Tiling](https://zeikar.dev/leetcode/posts/21/) | Medium | [domino-and-tromino-tiling.py](domino-and-tromino-tiling.py) |
| 799 | [Champagne Tower](https://zeikar.dev/leetcode/posts/84/) | Medium | [champagne-tower.py](champagne-tower.py) |
| 801 | [Minimum Swaps To Make Sequences Increasing](https://zeikar.dev/leetcode/posts/116/) | Hard | [minimum-swaps-to-make-sequences-increasing.py](minimum-swaps-to-make-sequences-increasing.py) |
| 834 | [Sum of Distances in Tree](https://zeikar.dev/leetcode/posts/32/) | Hard | [sum-of-distances-in-tree.py](sum-of-distances-in-tree.py) |
| 835 | [Image Overlap](https://zeikar.dev/leetcode/posts/157/) | Medium | [image-overlap.py](image-overlap.py) |
| 840 | [Magic Squares In Grid](https://zeikar.dev/leetcode/posts/131/) | Medium | [magic-squares-in-grid.py](magic-squares-in-grid.py) |
| 857 | [Minimum Cost to Hire K Workers](https://zeikar.dev/leetcode/posts/51/) | Hard | [minimum-cost-to-hire-k-workers.py](minimum-cost-to-hire-k-workers.py) |
| 860 | [Lemonade Change](https://zeikar.dev/leetcode/posts/137/) | Easy | [lemonade-change.py](lemonade-change.py) |
| 878 | [Nth Magical Number](https://zeikar.dev/leetcode/posts/22/) | Hard | [nth-magical-number.py](nth-magical-number.py) |
| 885 | [Spiral Matrix III](https://zeikar.dev/leetcode/posts/128/) | Medium | [spiral-matrix-iii.py](spiral-matrix-iii.py) |
| 895 | [Maximum Frequency Stack](https://zeikar.dev/leetcode/posts/45/) | Hard | [maximum-frequency-stack.py](maximum-frequency-stack.py) |
| 912 | [Sort an Array](https://zeikar.dev/leetcode/posts/106/) | Medium | [sort-an-array.py](sort-an-array.py) |
| 930 | [Binary Subarrays With Sum](https://zeikar.dev/leetcode/posts/130/) | Medium | [binary-subarrays-with-sum.py](binary-subarrays-with-sum.py) |
| 943 | [Find the Shortest Superstring](https://zeikar.dev/leetcode/posts/74/) | Hard | [find-the-shortest-superstring.py](find-the-shortest-superstring.py) |
| 959 | [Regions Cut By Slashes](https://zeikar.dev/leetcode/posts/132/) | Medium | [regions-cut-by-slashes.py](regions-cut-by-slashes.py) |
| 983 | [Minimum Cost For Tickets](https://zeikar.dev/leetcode/posts/85/) | Medium | [minimum-cost-for-tickets.py](minimum-cost-for-tickets.py) |
| 991 | [Broken Calculator](https://zeikar.dev/leetcode/posts/48/) | Medium | [broken-calculator.py](broken-calculator.py) |
| 1105 | [Filling Bookcase Shelves](https://zeikar.dev/leetcode/posts/114/) | Medium | [filling-bookcase-shelves.py](filling-bookcase-shelves.py) |
| 1140 | [Stone Game II](https://zeikar.dev/leetcode/posts/142/) | Medium | [stone-game-ii.py](stone-game-ii.py) |
| 1202 | [Smallest String With Swaps](https://zeikar.dev/leetcode/posts/59/) | Medium | [smallest-string-with-swaps.py](smallest-string-with-swaps.py) |
| 1249 | [Minimum Remove to Make Valid Parentheses](https://zeikar.dev/leetcode/posts/43/) | Medium | [minimum-remove-to-make-valid-parentheses.py](minimum-remove-to-make-valid-parentheses.py) |
| 1284 | [Minimum Number of Flips to Convert Binary Matrix to Zero Matrix](https://zeikar.dev/leetcode/posts/75/) | Hard | [minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix.py](minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix.py) |
| 1289 | [Minimum Falling Path Sum II](https://zeikar.dev/leetcode/posts/107/) | Hard | [minimum-falling-path-sum-ii.py](minimum-falling-path-sum-ii.py) |
| 1306 | [Jump Game III](https://zeikar.dev/leetcode/posts/20/) | Medium | [jump-game-iii.py](jump-game-iii.py) |
| 1307 | [Verbal Arithmetic Puzzle](https://zeikar.dev/leetcode/posts/68/) | Hard | [verbal-arithmetic-puzzle.py](verbal-arithmetic-puzzle.py) |
| 1392 | [Longest Happy Prefix](https://zeikar.dev/leetcode/posts/73/) | Hard | [longest-happy-prefix.py](longest-happy-prefix.py) |
| 1395 | [Count Number of Teams](https://zeikar.dev/leetcode/posts/112/) | Medium | [count-number-of-teams.py](count-number-of-teams.py) |
| 1396 | [Design Underground System](https://zeikar.dev/leetcode/posts/56/) | Medium | [design-underground-system.py](design-underground-system.py) |
| 1397 | [Find All Good Strings](https://zeikar.dev/leetcode/posts/30/) | Hard | [find-all-good-strings.py](find-all-good-strings.py) |
| 1411 | [Number of Ways to Paint N × 3 Grid](https://zeikar.dev/leetcode/posts/34/) | Hard | [number-of-ways-to-paint-n-3-grid.py](number-of-ways-to-paint-n-3-grid.py) |
| 1416 | [Restore The Array](https://zeikar.dev/leetcode/posts/66/) | Hard | [restore-the-array.py](restore-the-array.py) |
| 1444 | [Number of Ways of Cutting a Pizza](https://zeikar.dev/leetcode/posts/70/) | Hard | [number-of-ways-of-cutting-a-pizza.py](number-of-ways-of-cutting-a-pizza.py) |
| 1446 | [Consecutive Characters](https://zeikar.dev/leetcode/posts/24/) | Easy | [consecutive-characters.py](consecutive-characters.py) |
| 1460 | [Make Two Arrays Equal by Reversing Subarrays](https://zeikar.dev/leetcode/posts/115/) | Easy | [make-two-arrays-equal-by-reversing-subarrays.py](make-two-arrays-equal-by-reversing-subarrays.py) |
| 1463 | [Cherry Pickup II](https://zeikar.dev/leetcode/posts/89/) | Hard | [cherry-pickup-ii.py](cherry-pickup-ii.py) |
| 1481 | [Least Number of Unique Integers after K Removals](https://zeikar.dev/leetcode/posts/94/) | Medium | [least-number-of-unique-integers-after-k-removals.py](least-number-of-unique-integers-after-k-removals.py) |
| 1492 | [The kth Factor of n](https://zeikar.dev/leetcode/posts/126/) | Medium | [the-kth-factor-of-n.py](the-kth-factor-of-n.py) |
| 1508 | [Range Sum of Sorted Subarray Sums](https://zeikar.dev/leetcode/posts/117/) | Medium | [range-sum-of-sorted-subarray-sums.py](range-sum-of-sorted-subarray-sums.py) |
| 1514 | [Path with Maximum Probability](https://zeikar.dev/leetcode/posts/146/) | Medium | [path-with-maximum-probability.py](path-with-maximum-probability.py) |
| 1542 | [Find Longest Awesome Substring](https://zeikar.dev/leetcode/posts/36/) | Hard | [find-longest-awesome-substring.py](find-longest-awesome-substring.py) |
| 1568 | [Minimum Number of Days to Disconnect Island](https://zeikar.dev/leetcode/posts/133/) | Hard | [minimum-number-of-days-to-disconnect-island.py](minimum-number-of-days-to-disconnect-island.py) |
| 1575 | [Count All Possible Routes](https://zeikar.dev/leetcode/posts/76/) | Hard | [count-all-possible-routes.py](count-all-possible-routes.py) |
| 1631 | [Path With Minimum Effort](https://zeikar.dev/leetcode/posts/60/) | Medium | [path-with-minimum-effort.py](path-with-minimum-effort.py) |
| 1641 | [Count Sorted Vowel Strings](https://zeikar.dev/leetcode/posts/3/) | Medium | [count-sorted-vowel-strings.py](count-sorted-vowel-strings.py) |
| 1642 | [Furthest Building You Can Reach](https://zeikar.dev/leetcode/posts/95/) | Medium | [furthest-building-you-can-reach.py](furthest-building-you-can-reach.py) |
| 1653 | [Minimum Deletions to Make String Balanced](https://zeikar.dev/leetcode/posts/113/) | Medium | [minimum-deletions-to-make-string-balanced.py](minimum-deletions-to-make-string-balanced.py) |
| 1663 | [Smallest String With A Given Numeric Value](https://zeikar.dev/leetcode/posts/47/) | Medium | [smallest-string-with-a-given-numeric-value.py](smallest-string-with-a-given-numeric-value.py) |
| 1671 | [Minimum Number of Removals to Make Mountain Array](https://zeikar.dev/leetcode/posts/65/) | Hard | [minimum-number-of-removals-to-make-mountain-array.py](minimum-number-of-removals-to-make-mountain-array.py) |
| 1685 | [Sum of Absolute Differences in a Sorted Array](https://zeikar.dev/leetcode/posts/98/) | Medium | [sum-of-absolute-differences-in-a-sorted-array.py](sum-of-absolute-differences-in-a-sorted-array.py) |
| 1735 | [Count Ways to Make Array With Product](https://zeikar.dev/leetcode/posts/54/) | Hard | [count-ways-to-make-array-with-product.py](count-ways-to-make-array-with-product.py) |
| 1857 | [Largest Color Value in a Directed Graph](https://zeikar.dev/leetcode/posts/31/) | Hard | [largest-color-value-in-a-directed-graph.py](largest-color-value-in-a-directed-graph.py) |
| 1883 | [Minimum Skips to Arrive at Meeting On Time](https://zeikar.dev/leetcode/posts/38/) | Hard | [minimum-skips-to-arrive-at-meeting-on-time.py](minimum-skips-to-arrive-at-meeting-on-time.py) |
| 1937 | [Maximum Number of Points with Cost](https://zeikar.dev/leetcode/posts/139/) | Medium | [maximum-number-of-points-with-cost.py](maximum-number-of-points-with-cost.py) |
| 1982 | [Find Array Given Subset Sums](https://zeikar.dev/leetcode/posts/71/) | Hard | [find-array-given-subset-sums.py](find-array-given-subset-sums.py) |
| 1987 | [Number of Unique Good Subsequences](https://zeikar.dev/leetcode/posts/72/) | Hard | [number-of-unique-good-subsequences.py](number-of-unique-good-subsequences.py) |
| 2009 | [Minimum Number of Operations to Make Array Continuous](https://zeikar.dev/leetcode/posts/35/) | Hard | [minimum-number-of-operations-to-make-array-continuous.py](minimum-number-of-operations-to-make-array-continuous.py) |
| 2045 | [Second Minimum Time to Reach Destination](https://zeikar.dev/leetcode/posts/111/) | Hard | [second-minimum-time-to-reach-destination.py](second-minimum-time-to-reach-destination.py) |
| 2053 | [Kth Distinct String in an Array](https://zeikar.dev/leetcode/posts/118/) | Easy | [kth-distinct-string-in-an-array.py](kth-distinct-string-in-an-array.py) |
| 2108 | [Find First Palindromic String in the Array](https://zeikar.dev/leetcode/posts/91/) | Easy | [find-first-palindromic-string-in-the-array.py](find-first-palindromic-string-in-the-array.py) |
| 2134 | [Minimum Swaps to Group All 1's Together II](https://zeikar.dev/leetcode/posts/119/) | Medium | [minimum-swaps-to-group-all-1s-together-ii.py](minimum-swaps-to-group-all-1s-together-ii.py) |
| 2147 | [Number of Ways to Divide a Long Corridor](https://zeikar.dev/leetcode/posts/57/) | Hard | [number-of-ways-to-divide-a-long-corridor.py](number-of-ways-to-divide-a-long-corridor.py) |
| 2149 | [Rearrange Array Elements by Sign](https://zeikar.dev/leetcode/posts/92/) | Medium | [rearrange-array-elements-by-sign.py](rearrange-array-elements-by-sign.py) |
| 2172 | [Maximum AND Sum of Array](https://zeikar.dev/leetcode/posts/77/) | Hard | [maximum-and-sum-of-array.py](maximum-and-sum-of-array.py) |
| 2193 | [Minimum Number of Moves to Make Palindrome](https://zeikar.dev/leetcode/posts/69/) | Hard | [minimum-number-of-moves-to-make-palindrome.py](minimum-number-of-moves-to-make-palindrome.py) |
| 2265 | [Count Nodes Equal to Average of Subtree](https://zeikar.dev/leetcode/posts/158/) | Medium | [count-nodes-equal-to-average-of-subtree.py](count-nodes-equal-to-average-of-subtree.py) |
| 2321 | [Maximum Score Of Spliced Array](https://zeikar.dev/leetcode/posts/78/) | Hard | [maximum-score-of-spliced-array.py](maximum-score-of-spliced-array.py) |
| 2360 | [Longest Cycle in a Graph](https://zeikar.dev/leetcode/posts/79/) | Hard | [longest-cycle-in-a-graph.py](longest-cycle-in-a-graph.py) |
| 2392 | [Build a Matrix With Conditions](https://zeikar.dev/leetcode/posts/129/) | Hard | [build-a-matrix-with-conditions.py](build-a-matrix-with-conditions.py) |
| 2402 | [Meeting Rooms III](https://zeikar.dev/leetcode/posts/96/) | Hard | [meeting-rooms-iii.py](meeting-rooms-iii.py) |
| 2405 | [Optimal Partition of String](https://zeikar.dev/leetcode/posts/127/) | Medium | [optimal-partition-of-string.py](optimal-partition-of-string.py) |
| 2461 | [Maximum Sum of Distinct Subarrays With Length K](https://zeikar.dev/leetcode/posts/154/) | Medium | [maximum-sum-of-distinct-subarrays-with-length-k.py](maximum-sum-of-distinct-subarrays-with-length-k.py) |
| 2551 | [Put Marbles in Bags](https://zeikar.dev/leetcode/posts/109/) | Hard | [put-marbles-in-bags.py](put-marbles-in-bags.py) |
| 2841 | [Maximum Sum of Almost Unique Subarray](https://zeikar.dev/leetcode/posts/82/) | Medium | [maximum-sum-of-almost-unique-subarray.py](maximum-sum-of-almost-unique-subarray.py) |
| 2971 | [Find Polygon With the Largest Perimeter](https://zeikar.dev/leetcode/posts/93/) | Medium | [find-polygon-with-the-largest-perimeter.py](find-polygon-with-the-largest-perimeter.py) |
| 3016 | [Minimum Number of Pushes to Type Word II](https://zeikar.dev/leetcode/posts/120/) | Medium | [minimum-number-of-pushes-to-type-word-ii.py](minimum-number-of-pushes-to-type-word-ii.py) |
| 3414 | [Maximum Score of Non-overlapping Intervals](https://zeikar.dev/leetcode/posts/156/) | Hard | [maximum-score-of-non-overlapping-intervals.py](maximum-score-of-non-overlapping-intervals.py) |
| 3871 | [Count Commas in Range II](https://zeikar.dev/leetcode/posts/155/) | Medium | [count-commas-in-range-ii.py](count-commas-in-range-ii.py) |

<!-- PROBLEMS:END -->
