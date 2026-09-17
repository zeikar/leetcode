# LeetCode

**A study log, and the tool that made it work.**

Every problem here has two halves: a solution file in this repo, and a study
note in [Discussions](https://github.com/zeikar/leetcode/discussions/categories/posts) covering what the
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

Generated from the notes by
[`update-index.yml`](.github/workflows/update-index.yml) — don't edit by hand.
Recording a solved problem is a separate skill in `.claude/skills/`, kept local
rather than shipped in the plugin because it is built around this repo's note
form, index workflow and commit convention.

<!-- PROBLEMS:START -->

**161 solved** — Easy 14 · Medium 79 · Hard 68

| # | Problem | Difficulty | Solution |
| ---: | --- | --- | --- |
| 1 | [Two Sum](https://zeikar.dev/leetcode/posts/160/) | Easy | [two-sum.py](solutions/two-sum.py) |
| 2 | [Add Two Numbers](https://zeikar.dev/leetcode/posts/279/) | Medium | [add-two-numbers.py](solutions/add-two-numbers.py) |
| 4 | [Median of Two Sorted Arrays](https://zeikar.dev/leetcode/posts/167/) | Hard | [median-of-two-sorted-arrays.py](solutions/median-of-two-sorted-arrays.py) |
| 15 | [3Sum](https://zeikar.dev/leetcode/posts/175/) | Medium | [3sum.py](solutions/3sum.py) |
| 20 | [Valid Parentheses](https://zeikar.dev/leetcode/posts/199/) | Easy | [valid-parentheses.py](solutions/valid-parentheses.py) |
| 23 | [Merge k Sorted Lists](https://zeikar.dev/leetcode/posts/166/) | Hard | [merge-k-sorted-lists.py](solutions/merge-k-sorted-lists.py) |
| 29 | [Divide Two Integers](https://zeikar.dev/leetcode/posts/257/) | Medium | [divide-two-integers.py](solutions/divide-two-integers.py) |
| 32 | [Longest Valid Parentheses](https://zeikar.dev/leetcode/posts/161/) | Hard | [longest-valid-parentheses.py](solutions/longest-valid-parentheses.py) |
| 40 | [Combination Sum II](https://zeikar.dev/leetcode/posts/293/) | Medium | [combination-sum-ii.py](solutions/combination-sum-ii.py) |
| 41 | [First Missing Positive](https://zeikar.dev/leetcode/posts/165/) | Hard | [first-missing-positive.py](solutions/first-missing-positive.py) |
| 42 | [Trapping Rain Water](https://zeikar.dev/leetcode/posts/169/) | Hard | [trapping-rain-water.py](solutions/trapping-rain-water.py) |
| 49 | [Group Anagrams](https://zeikar.dev/leetcode/posts/280/) | Medium | [group-anagrams.py](solutions/group-anagrams.py) |
| 57 | [Insert Interval](https://zeikar.dev/leetcode/posts/262/) | Medium | [insert-interval.py](solutions/insert-interval.py) |
| 61 | [Rotate List](https://zeikar.dev/leetcode/posts/198/) | Medium | [rotate-list.py](solutions/rotate-list.py) |
| 65 | [Valid Number](https://zeikar.dev/leetcode/posts/164/) | Hard | [valid-number.py](solutions/valid-number.py) |
| 71 | [Simplify Path](https://zeikar.dev/leetcode/posts/307/) | Medium | [simplify-path.py](solutions/simplify-path.py) |
| 84 | [Largest Rectangle in Histogram](https://zeikar.dev/leetcode/posts/163/) | Hard | [largest-rectangle-in-histogram.py](solutions/largest-rectangle-in-histogram.py) |
| 85 | [Maximal Rectangle](https://zeikar.dev/leetcode/posts/174/) | Hard | [maximal-rectangle.py](solutions/maximal-rectangle.py) |
| 97 | [Interleaving String](https://zeikar.dev/leetcode/posts/239/) | Medium | [interleaving-string.py](solutions/interleaving-string.py) |
| 103 | [Binary Tree Zigzag Level Order Traversal](https://zeikar.dev/leetcode/posts/310/) | Medium | [binary-tree-zigzag-level-order-traversal.py](solutions/binary-tree-zigzag-level-order-traversal.py) |
| 124 | [Binary Tree Maximum Path Sum](https://zeikar.dev/leetcode/posts/221/) | Hard | [binary-tree-maximum-path-sum.py](solutions/binary-tree-maximum-path-sum.py) |
| 128 | [Longest Consecutive Sequence](https://zeikar.dev/leetcode/posts/305/) | Medium | [longest-consecutive-sequence.py](solutions/longest-consecutive-sequence.py) |
| 129 | [Sum Root to Leaf Numbers](https://zeikar.dev/leetcode/posts/311/) | Medium | [sum-root-to-leaf-numbers.py](solutions/sum-root-to-leaf-numbers.py) |
| 131 | [Palindrome Partitioning](https://zeikar.dev/leetcode/posts/306/) | Medium | [palindrome-partitioning.py](solutions/palindrome-partitioning.py) |
| 138 | [Copy List with Random Pointer](https://zeikar.dev/leetcode/posts/197/) | Medium | [copy-list-with-random-pointer.py](solutions/copy-list-with-random-pointer.py) |
| 139 | [Word Break](https://zeikar.dev/leetcode/posts/241/) | Medium | [word-break.py](solutions/word-break.py) |
| 149 | [Max Points on a Line](https://zeikar.dev/leetcode/posts/172/) | Hard | [max-points-on-a-line.py](solutions/max-points-on-a-line.py) |
| 152 | [Maximum Product Subarray](https://zeikar.dev/leetcode/posts/185/) | Medium | [maximum-product-subarray.py](solutions/maximum-product-subarray.py) |
| 169 | [Majority Element](https://zeikar.dev/leetcode/posts/248/) | Easy | [majority-element.py](solutions/majority-element.py) |
| 173 | [Binary Search Tree Iterator](https://zeikar.dev/leetcode/posts/211/) | Medium | [binary-search-tree-iterator.py](solutions/binary-search-tree-iterator.py) |
| 174 | [Dungeon Game](https://zeikar.dev/leetcode/posts/186/) | Hard | [dungeon-game.py](solutions/dungeon-game.py) |
| 199 | [Binary Tree Right Side View](https://zeikar.dev/leetcode/posts/238/) | Medium | [binary-tree-right-side-view.py](solutions/binary-tree-right-side-view.py) |
| 201 | [Bitwise AND of Numbers Range](https://zeikar.dev/leetcode/posts/259/) | Medium | [bitwise-and-of-numbers-range.py](solutions/bitwise-and-of-numbers-range.py) |
| 214 | [Shortest Palindrome](https://zeikar.dev/leetcode/posts/191/) | Hard | [shortest-palindrome.py](solutions/shortest-palindrome.py) |
| 215 | [Kth Largest Element in an Array](https://zeikar.dev/leetcode/posts/308/) | Medium | [kth-largest-element-in-an-array.py](solutions/kth-largest-element-in-an-array.py) |
| 218 | [The Skyline Problem](https://zeikar.dev/leetcode/posts/268/) | Hard | [the-skyline-problem.py](solutions/the-skyline-problem.py) |
| 224 | [Basic Calculator](https://zeikar.dev/leetcode/posts/173/) | Hard | [basic-calculator.py](solutions/basic-calculator.py) |
| 230 | [Kth Smallest Element in a BST](https://zeikar.dev/leetcode/posts/210/) | Medium | [kth-smallest-element-in-a-bst.py](solutions/kth-smallest-element-in-a-bst.py) |
| 231 | [Power of Two](https://zeikar.dev/leetcode/posts/255/) | Easy | [power-of-two.py](solutions/power-of-two.py) |
| 239 | [Sliding Window Maximum](https://zeikar.dev/leetcode/posts/168/) | Hard | [sliding-window-maximum.py](solutions/sliding-window-maximum.py) |
| 264 | [Ugly Number II](https://zeikar.dev/leetcode/posts/298/) | Medium | [ugly-number-ii.py](solutions/ugly-number-ii.py) |
| 268 | [Missing Number](https://zeikar.dev/leetcode/posts/225/) | Easy | [missing-number.py](solutions/missing-number.py) |
| 273 | [Integer to English Words](https://zeikar.dev/leetcode/posts/283/) | Hard | [integer-to-english-words.py](solutions/integer-to-english-words.py) |
| 279 | [Perfect Squares](https://zeikar.dev/leetcode/posts/244/) | Medium | [perfect-squares.py](solutions/perfect-squares.py) |
| 284 | [Peeking Iterator](https://zeikar.dev/leetcode/posts/216/) | Medium | [peeking-iterator.py](solutions/peeking-iterator.py) |
| 287 | [Find the Duplicate Number](https://zeikar.dev/leetcode/posts/263/) | Medium | [find-the-duplicate-number.py](solutions/find-the-duplicate-number.py) |
| 295 | [Find Median from Data Stream](https://zeikar.dev/leetcode/posts/170/) | Hard | [find-median-from-data-stream.py](solutions/find-median-from-data-stream.py) |
| 301 | [Remove Invalid Parentheses](https://zeikar.dev/leetcode/posts/200/) | Hard | [remove-invalid-parentheses.py](solutions/remove-invalid-parentheses.py) |
| 312 | [Burst Balloons](https://zeikar.dev/leetcode/posts/282/) | Hard | [burst-balloons.py](solutions/burst-balloons.py) |
| 315 | [Count of Smaller Numbers After Self](https://zeikar.dev/leetcode/posts/171/) | Hard | [count-of-smaller-numbers-after-self.py](solutions/count-of-smaller-numbers-after-self.py) |
| 336 | [Palindrome Pairs](https://zeikar.dev/leetcode/posts/187/) | Hard | [palindrome-pairs.py](solutions/palindrome-pairs.py) |
| 337 | [House Robber III](https://zeikar.dev/leetcode/posts/176/) | Medium | [house-robber-iii.py](solutions/house-robber-iii.py) |
| 368 | [Largest Divisible Subset](https://zeikar.dev/leetcode/posts/245/) | Medium | [largest-divisible-subset.py](solutions/largest-divisible-subset.py) |
| 399 | [Evaluate Division](https://zeikar.dev/leetcode/posts/220/) | Medium | [evaluate-division.py](solutions/evaluate-division.py) |
| 403 | [Frog Jump](https://zeikar.dev/leetcode/posts/208/) | Hard | [frog-jump.py](solutions/frog-jump.py) |
| 410 | [Split Array Largest Sum](https://zeikar.dev/leetcode/posts/222/) | Hard | [split-array-largest-sum.py](solutions/split-array-largest-sum.py) |
| 416 | [Partition Equal Subset Sum](https://zeikar.dev/leetcode/posts/181/) | Medium | [partition-equal-subset-sum.py](solutions/partition-equal-subset-sum.py) |
| 433 | [Minimum Genetic Mutation](https://zeikar.dev/leetcode/posts/309/) | Medium | [minimum-genetic-mutation.py](solutions/minimum-genetic-mutation.py) |
| 452 | [Minimum Number of Arrows to Burst Balloons](https://zeikar.dev/leetcode/posts/261/) | Medium | [minimum-number-of-arrows-to-burst-balloons.py](solutions/minimum-number-of-arrows-to-burst-balloons.py) |
| 476 | [Number Complement](https://zeikar.dev/leetcode/posts/302/) | Easy | [number-complement.py](solutions/number-complement.py) |
| 514 | [Freedom Trail](https://zeikar.dev/leetcode/posts/266/) | Hard | [freedom-trail.py](solutions/freedom-trail.py) |
| 517 | [Super Washing Machines](https://zeikar.dev/leetcode/posts/281/) | Hard | [super-washing-machines.py](solutions/super-washing-machines.py) |
| 525 | [Contiguous Array](https://zeikar.dev/leetcode/posts/260/) | Medium | [contiguous-array.py](solutions/contiguous-array.py) |
| 535 | [Encode and Decode TinyURL](https://zeikar.dev/leetcode/posts/213/) | Medium | [encode-and-decode-tinyurl.py](solutions/encode-and-decode-tinyurl.py) |
| 546 | [Remove Boxes](https://zeikar.dev/leetcode/posts/183/) | Hard | [remove-boxes.py](solutions/remove-boxes.py) |
| 563 | [Binary Tree Tilt](https://zeikar.dev/leetcode/posts/177/) | Easy | [binary-tree-tilt.py](solutions/binary-tree-tilt.py) |
| 592 | [Fraction Addition and Subtraction](https://zeikar.dev/leetcode/posts/303/) | Medium | [fraction-addition-and-subtraction.py](solutions/fraction-addition-and-subtraction.py) |
| 600 | [Non-negative Integers without Consecutive Ones](https://zeikar.dev/leetcode/posts/207/) | Hard | [non-negative-integers-without-consecutive-ones.py](solutions/non-negative-integers-without-consecutive-ones.py) |
| 624 | [Maximum Distance in Arrays](https://zeikar.dev/leetcode/posts/296/) | Medium | [maximum-distance-in-arrays.py](solutions/maximum-distance-in-arrays.py) |
| 647 | [Palindromic Substrings](https://zeikar.dev/leetcode/posts/246/) | Medium | [palindromic-substrings.py](solutions/palindromic-substrings.py) |
| 650 | [2 Keys Keyboard](https://zeikar.dev/leetcode/posts/299/) | Medium | [2-keys-keyboard.py](solutions/2-keys-keyboard.py) |
| 664 | [Strange Printer](https://zeikar.dev/leetcode/posts/301/) | Hard | [strange-printer.py](solutions/strange-printer.py) |
| 699 | [Falling Squares](https://zeikar.dev/leetcode/posts/195/) | Hard | [falling-squares.py](solutions/falling-squares.py) |
| 703 | [Kth Largest Element in a Stream](https://zeikar.dev/leetcode/posts/292/) | Easy | [kth-largest-element-in-a-stream.py](solutions/kth-largest-element-in-a-stream.py) |
| 719 | [Find K-th Smallest Pair Distance](https://zeikar.dev/leetcode/posts/294/) | Hard | [find-k-th-smallest-pair-distance.py](solutions/find-k-th-smallest-pair-distance.py) |
| 763 | [Partition Labels](https://zeikar.dev/leetcode/posts/204/) | Medium | [partition-labels.py](solutions/partition-labels.py) |
| 765 | [Couples Holding Hands](https://zeikar.dev/leetcode/posts/184/) | Hard | [couples-holding-hands.py](solutions/couples-holding-hands.py) |
| 778 | [Swim in Rising Water](https://zeikar.dev/leetcode/posts/202/) | Hard | [swim-in-rising-water.py](solutions/swim-in-rising-water.py) |
| 785 | [Is Graph Bipartite?](https://zeikar.dev/leetcode/posts/219/) | Medium | [is-graph-bipartite.py](solutions/is-graph-bipartite.py) |
| 787 | [Cheapest Flights Within K Stops](https://zeikar.dev/leetcode/posts/258/) | Medium | [cheapest-flights-within-k-stops.py](solutions/cheapest-flights-within-k-stops.py) |
| 790 | [Domino and Tromino Tiling](https://zeikar.dev/leetcode/posts/179/) | Medium | [domino-and-tromino-tiling.py](solutions/domino-and-tromino-tiling.py) |
| 799 | [Champagne Tower](https://zeikar.dev/leetcode/posts/242/) | Medium | [champagne-tower.py](solutions/champagne-tower.py) |
| 801 | [Minimum Swaps To Make Sequences Increasing](https://zeikar.dev/leetcode/posts/274/) | Hard | [minimum-swaps-to-make-sequences-increasing.py](solutions/minimum-swaps-to-make-sequences-increasing.py) |
| 834 | [Sum of Distances in Tree](https://zeikar.dev/leetcode/posts/190/) | Hard | [sum-of-distances-in-tree.py](solutions/sum-of-distances-in-tree.py) |
| 835 | [Image Overlap](https://zeikar.dev/leetcode/posts/315/) | Medium | [image-overlap.py](solutions/image-overlap.py) |
| 836 | [Rectangle Overlap](https://zeikar.dev/leetcode/posts/317/) | Easy | [rectangle-overlap.py](solutions/rectangle-overlap.py) |
| 840 | [Magic Squares In Grid](https://zeikar.dev/leetcode/posts/289/) | Medium | [magic-squares-in-grid.py](solutions/magic-squares-in-grid.py) |
| 857 | [Minimum Cost to Hire K Workers](https://zeikar.dev/leetcode/posts/209/) | Hard | [minimum-cost-to-hire-k-workers.py](solutions/minimum-cost-to-hire-k-workers.py) |
| 860 | [Lemonade Change](https://zeikar.dev/leetcode/posts/295/) | Easy | [lemonade-change.py](solutions/lemonade-change.py) |
| 878 | [Nth Magical Number](https://zeikar.dev/leetcode/posts/180/) | Hard | [nth-magical-number.py](solutions/nth-magical-number.py) |
| 885 | [Spiral Matrix III](https://zeikar.dev/leetcode/posts/286/) | Medium | [spiral-matrix-iii.py](solutions/spiral-matrix-iii.py) |
| 895 | [Maximum Frequency Stack](https://zeikar.dev/leetcode/posts/203/) | Hard | [maximum-frequency-stack.py](solutions/maximum-frequency-stack.py) |
| 912 | [Sort an Array](https://zeikar.dev/leetcode/posts/264/) | Medium | [sort-an-array.py](solutions/sort-an-array.py) |
| 930 | [Binary Subarrays With Sum](https://zeikar.dev/leetcode/posts/288/) | Medium | [binary-subarrays-with-sum.py](solutions/binary-subarrays-with-sum.py) |
| 943 | [Find the Shortest Superstring](https://zeikar.dev/leetcode/posts/232/) | Hard | [find-the-shortest-superstring.py](solutions/find-the-shortest-superstring.py) |
| 959 | [Regions Cut By Slashes](https://zeikar.dev/leetcode/posts/290/) | Medium | [regions-cut-by-slashes.py](solutions/regions-cut-by-slashes.py) |
| 983 | [Minimum Cost For Tickets](https://zeikar.dev/leetcode/posts/243/) | Medium | [minimum-cost-for-tickets.py](solutions/minimum-cost-for-tickets.py) |
| 991 | [Broken Calculator](https://zeikar.dev/leetcode/posts/206/) | Medium | [broken-calculator.py](solutions/broken-calculator.py) |
| 1105 | [Filling Bookcase Shelves](https://zeikar.dev/leetcode/posts/272/) | Medium | [filling-bookcase-shelves.py](solutions/filling-bookcase-shelves.py) |
| 1140 | [Stone Game II](https://zeikar.dev/leetcode/posts/300/) | Medium | [stone-game-ii.py](solutions/stone-game-ii.py) |
| 1202 | [Smallest String With Swaps](https://zeikar.dev/leetcode/posts/217/) | Medium | [smallest-string-with-swaps.py](solutions/smallest-string-with-swaps.py) |
| 1249 | [Minimum Remove to Make Valid Parentheses](https://zeikar.dev/leetcode/posts/201/) | Medium | [minimum-remove-to-make-valid-parentheses.py](solutions/minimum-remove-to-make-valid-parentheses.py) |
| 1284 | [Minimum Number of Flips to Convert Binary Matrix to Zero Matrix](https://zeikar.dev/leetcode/posts/233/) | Hard | [minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix.py](solutions/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix.py) |
| 1289 | [Minimum Falling Path Sum II](https://zeikar.dev/leetcode/posts/265/) | Hard | [minimum-falling-path-sum-ii.py](solutions/minimum-falling-path-sum-ii.py) |
| 1306 | [Jump Game III](https://zeikar.dev/leetcode/posts/178/) | Medium | [jump-game-iii.py](solutions/jump-game-iii.py) |
| 1307 | [Verbal Arithmetic Puzzle](https://zeikar.dev/leetcode/posts/226/) | Hard | [verbal-arithmetic-puzzle.py](solutions/verbal-arithmetic-puzzle.py) |
| 1392 | [Longest Happy Prefix](https://zeikar.dev/leetcode/posts/231/) | Hard | [longest-happy-prefix.py](solutions/longest-happy-prefix.py) |
| 1395 | [Count Number of Teams](https://zeikar.dev/leetcode/posts/270/) | Medium | [count-number-of-teams.py](solutions/count-number-of-teams.py) |
| 1396 | [Design Underground System](https://zeikar.dev/leetcode/posts/214/) | Medium | [design-underground-system.py](solutions/design-underground-system.py) |
| 1397 | [Find All Good Strings](https://zeikar.dev/leetcode/posts/188/) | Hard | [find-all-good-strings.py](solutions/find-all-good-strings.py) |
| 1411 | [Number of Ways to Paint N × 3 Grid](https://zeikar.dev/leetcode/posts/192/) | Hard | [number-of-ways-to-paint-n-3-grid.py](solutions/number-of-ways-to-paint-n-3-grid.py) |
| 1416 | [Restore The Array](https://zeikar.dev/leetcode/posts/224/) | Hard | [restore-the-array.py](solutions/restore-the-array.py) |
| 1444 | [Number of Ways of Cutting a Pizza](https://zeikar.dev/leetcode/posts/228/) | Hard | [number-of-ways-of-cutting-a-pizza.py](solutions/number-of-ways-of-cutting-a-pizza.py) |
| 1446 | [Consecutive Characters](https://zeikar.dev/leetcode/posts/182/) | Easy | [consecutive-characters.py](solutions/consecutive-characters.py) |
| 1460 | [Make Two Arrays Equal by Reversing Subarrays](https://zeikar.dev/leetcode/posts/273/) | Easy | [make-two-arrays-equal-by-reversing-subarrays.py](solutions/make-two-arrays-equal-by-reversing-subarrays.py) |
| 1463 | [Cherry Pickup II](https://zeikar.dev/leetcode/posts/247/) | Hard | [cherry-pickup-ii.py](solutions/cherry-pickup-ii.py) |
| 1477 | [Find Two Non-overlapping Sub-arrays Each With Target Sum](https://zeikar.dev/leetcode/posts/320/) | Medium | [find-two-non-overlapping-sub-arrays-each-with-target-sum.py](solutions/find-two-non-overlapping-sub-arrays-each-with-target-sum.py) |
| 1481 | [Least Number of Unique Integers after K Removals](https://zeikar.dev/leetcode/posts/252/) | Medium | [least-number-of-unique-integers-after-k-removals.py](solutions/least-number-of-unique-integers-after-k-removals.py) |
| 1492 | [The kth Factor of n](https://zeikar.dev/leetcode/posts/284/) | Medium | [the-kth-factor-of-n.py](solutions/the-kth-factor-of-n.py) |
| 1508 | [Range Sum of Sorted Subarray Sums](https://zeikar.dev/leetcode/posts/275/) | Medium | [range-sum-of-sorted-subarray-sums.py](solutions/range-sum-of-sorted-subarray-sums.py) |
| 1514 | [Path with Maximum Probability](https://zeikar.dev/leetcode/posts/304/) | Medium | [path-with-maximum-probability.py](solutions/path-with-maximum-probability.py) |
| 1542 | [Find Longest Awesome Substring](https://zeikar.dev/leetcode/posts/194/) | Hard | [find-longest-awesome-substring.py](solutions/find-longest-awesome-substring.py) |
| 1568 | [Minimum Number of Days to Disconnect Island](https://zeikar.dev/leetcode/posts/291/) | Hard | [minimum-number-of-days-to-disconnect-island.py](solutions/minimum-number-of-days-to-disconnect-island.py) |
| 1575 | [Count All Possible Routes](https://zeikar.dev/leetcode/posts/234/) | Hard | [count-all-possible-routes.py](solutions/count-all-possible-routes.py) |
| 1621 | [Number of Sets of K Non-Overlapping Line Segments](https://zeikar.dev/leetcode/posts/319/) | Medium | [number-of-sets-of-k-non-overlapping-line-segments.py](solutions/number-of-sets-of-k-non-overlapping-line-segments.py) |
| 1631 | [Path With Minimum Effort](https://zeikar.dev/leetcode/posts/218/) | Medium | [path-with-minimum-effort.py](solutions/path-with-minimum-effort.py) |
| 1641 | [Count Sorted Vowel Strings](https://zeikar.dev/leetcode/posts/162/) | Medium | [count-sorted-vowel-strings.py](solutions/count-sorted-vowel-strings.py) |
| 1642 | [Furthest Building You Can Reach](https://zeikar.dev/leetcode/posts/253/) | Medium | [furthest-building-you-can-reach.py](solutions/furthest-building-you-can-reach.py) |
| 1653 | [Minimum Deletions to Make String Balanced](https://zeikar.dev/leetcode/posts/271/) | Medium | [minimum-deletions-to-make-string-balanced.py](solutions/minimum-deletions-to-make-string-balanced.py) |
| 1663 | [Smallest String With A Given Numeric Value](https://zeikar.dev/leetcode/posts/205/) | Medium | [smallest-string-with-a-given-numeric-value.py](solutions/smallest-string-with-a-given-numeric-value.py) |
| 1671 | [Minimum Number of Removals to Make Mountain Array](https://zeikar.dev/leetcode/posts/223/) | Hard | [minimum-number-of-removals-to-make-mountain-array.py](solutions/minimum-number-of-removals-to-make-mountain-array.py) |
| 1685 | [Sum of Absolute Differences in a Sorted Array](https://zeikar.dev/leetcode/posts/256/) | Medium | [sum-of-absolute-differences-in-a-sorted-array.py](solutions/sum-of-absolute-differences-in-a-sorted-array.py) |
| 1735 | [Count Ways to Make Array With Product](https://zeikar.dev/leetcode/posts/212/) | Hard | [count-ways-to-make-array-with-product.py](solutions/count-ways-to-make-array-with-product.py) |
| 1857 | [Largest Color Value in a Directed Graph](https://zeikar.dev/leetcode/posts/189/) | Hard | [largest-color-value-in-a-directed-graph.py](solutions/largest-color-value-in-a-directed-graph.py) |
| 1883 | [Minimum Skips to Arrive at Meeting On Time](https://zeikar.dev/leetcode/posts/196/) | Hard | [minimum-skips-to-arrive-at-meeting-on-time.py](solutions/minimum-skips-to-arrive-at-meeting-on-time.py) |
| 1937 | [Maximum Number of Points with Cost](https://zeikar.dev/leetcode/posts/297/) | Medium | [maximum-number-of-points-with-cost.py](solutions/maximum-number-of-points-with-cost.py) |
| 1982 | [Find Array Given Subset Sums](https://zeikar.dev/leetcode/posts/229/) | Hard | [find-array-given-subset-sums.py](solutions/find-array-given-subset-sums.py) |
| 1987 | [Number of Unique Good Subsequences](https://zeikar.dev/leetcode/posts/230/) | Hard | [number-of-unique-good-subsequences.py](solutions/number-of-unique-good-subsequences.py) |
| 2009 | [Minimum Number of Operations to Make Array Continuous](https://zeikar.dev/leetcode/posts/193/) | Hard | [minimum-number-of-operations-to-make-array-continuous.py](solutions/minimum-number-of-operations-to-make-array-continuous.py) |
| 2045 | [Second Minimum Time to Reach Destination](https://zeikar.dev/leetcode/posts/269/) | Hard | [second-minimum-time-to-reach-destination.py](solutions/second-minimum-time-to-reach-destination.py) |
| 2053 | [Kth Distinct String in an Array](https://zeikar.dev/leetcode/posts/276/) | Easy | [kth-distinct-string-in-an-array.py](solutions/kth-distinct-string-in-an-array.py) |
| 2108 | [Find First Palindromic String in the Array](https://zeikar.dev/leetcode/posts/249/) | Easy | [find-first-palindromic-string-in-the-array.py](solutions/find-first-palindromic-string-in-the-array.py) |
| 2134 | [Minimum Swaps to Group All 1's Together II](https://zeikar.dev/leetcode/posts/277/) | Medium | [minimum-swaps-to-group-all-1s-together-ii.py](solutions/minimum-swaps-to-group-all-1s-together-ii.py) |
| 2147 | [Number of Ways to Divide a Long Corridor](https://zeikar.dev/leetcode/posts/215/) | Hard | [number-of-ways-to-divide-a-long-corridor.py](solutions/number-of-ways-to-divide-a-long-corridor.py) |
| 2149 | [Rearrange Array Elements by Sign](https://zeikar.dev/leetcode/posts/250/) | Medium | [rearrange-array-elements-by-sign.py](solutions/rearrange-array-elements-by-sign.py) |
| 2172 | [Maximum AND Sum of Array](https://zeikar.dev/leetcode/posts/235/) | Hard | [maximum-and-sum-of-array.py](solutions/maximum-and-sum-of-array.py) |
| 2193 | [Minimum Number of Moves to Make Palindrome](https://zeikar.dev/leetcode/posts/227/) | Hard | [minimum-number-of-moves-to-make-palindrome.py](solutions/minimum-number-of-moves-to-make-palindrome.py) |
| 2265 | [Count Nodes Equal to Average of Subtree](https://zeikar.dev/leetcode/posts/316/) | Medium | [count-nodes-equal-to-average-of-subtree.py](solutions/count-nodes-equal-to-average-of-subtree.py) |
| 2321 | [Maximum Score Of Spliced Array](https://zeikar.dev/leetcode/posts/236/) | Hard | [maximum-score-of-spliced-array.py](solutions/maximum-score-of-spliced-array.py) |
| 2360 | [Longest Cycle in a Graph](https://zeikar.dev/leetcode/posts/237/) | Hard | [longest-cycle-in-a-graph.py](solutions/longest-cycle-in-a-graph.py) |
| 2392 | [Build a Matrix With Conditions](https://zeikar.dev/leetcode/posts/287/) | Hard | [build-a-matrix-with-conditions.py](solutions/build-a-matrix-with-conditions.py) |
| 2402 | [Meeting Rooms III](https://zeikar.dev/leetcode/posts/254/) | Hard | [meeting-rooms-iii.py](solutions/meeting-rooms-iii.py) |
| 2405 | [Optimal Partition of String](https://zeikar.dev/leetcode/posts/285/) | Medium | [optimal-partition-of-string.py](solutions/optimal-partition-of-string.py) |
| 2461 | [Maximum Sum of Distinct Subarrays With Length K](https://zeikar.dev/leetcode/posts/312/) | Medium | [maximum-sum-of-distinct-subarrays-with-length-k.py](solutions/maximum-sum-of-distinct-subarrays-with-length-k.py) |
| 2472 | [Maximum Number of Non-overlapping Palindrome Substrings](https://zeikar.dev/leetcode/posts/318/) | Hard | [maximum-number-of-non-overlapping-palindrome-substrings.py](solutions/maximum-number-of-non-overlapping-palindrome-substrings.py) |
| 2551 | [Put Marbles in Bags](https://zeikar.dev/leetcode/posts/267/) | Hard | [put-marbles-in-bags.py](solutions/put-marbles-in-bags.py) |
| 2841 | [Maximum Sum of Almost Unique Subarray](https://zeikar.dev/leetcode/posts/240/) | Medium | [maximum-sum-of-almost-unique-subarray.py](solutions/maximum-sum-of-almost-unique-subarray.py) |
| 2971 | [Find Polygon With the Largest Perimeter](https://zeikar.dev/leetcode/posts/251/) | Medium | [find-polygon-with-the-largest-perimeter.py](solutions/find-polygon-with-the-largest-perimeter.py) |
| 3016 | [Minimum Number of Pushes to Type Word II](https://zeikar.dev/leetcode/posts/278/) | Medium | [minimum-number-of-pushes-to-type-word-ii.py](solutions/minimum-number-of-pushes-to-type-word-ii.py) |
| 3414 | [Maximum Score of Non-overlapping Intervals](https://zeikar.dev/leetcode/posts/314/) | Hard | [maximum-score-of-non-overlapping-intervals.py](solutions/maximum-score-of-non-overlapping-intervals.py) |
| 3871 | [Count Commas in Range II](https://zeikar.dev/leetcode/posts/313/) | Medium | [count-commas-in-range-ii.py](solutions/count-commas-in-range-ii.py) |

<!-- PROBLEMS:END -->
