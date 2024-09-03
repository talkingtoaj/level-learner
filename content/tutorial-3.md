# Level 3: Quantifiers

Quantifiers in regular expressions allow you to specify how many times a pattern should occur.

## Basic Quantifiers

1. `*` (asterisk): Matches 0 or more occurrences of the preceding character or group.
   Example: `a*b` matches "b", "ab", "aab", "aaab", etc.

2. `+` (plus): Matches 1 or more occurrences of the preceding character or group.
   Example: `a+b` matches "ab", "aab", "aaab", etc., but not "b".

3. `?` (question mark): Matches 0 or 1 occurrence of the preceding character or group.
   Example: `colou?r` matches both "color" and "colour".

## Specific Quantifiers

4. `{n}`: Matches exactly n occurrences of the preceding character or group.
   Example: `a{3}` matches exactly "aaa".

5. `{n,}`: Matches n or more occurrences of the preceding character or group.
   Example: `a{2,}` matches "aa", "aaa", "aaaa", etc.

6. `{n,m}`: Matches between n and m occurrences (inclusive) of the preceding character or group.
   Example: `a{2,4}` matches "aa", "aaa", and "aaaa".

## Greedy vs. Lazy Quantifiers

By default, quantifiers are greedy, meaning they match as much as possible. Adding a `?` after a quantifier makes it lazy, matching as little as possible.

- Greedy: `a.*b` in "aabab" matches "aabab"
- Lazy: `a.*?b` in "aabab" matches "aab"

Practice using these quantifiers to create more flexible and precise patterns!