# Level 4: Anchors and Boundaries

Anchors and boundaries in regular expressions allow you to match patterns at specific positions in the text.

## Start and End Anchors

1. `^` (caret): Matches the start of a line.
   Example: `^Hello` matches "Hello" only at the beginning of a line.

2. `$` (dollar): Matches the end of a line.
   Example: `world$` matches "world" only at the end of a line.

## Word Boundaries

3. `\b`: Matches a word boundary (the position between a word character and a non-word character).
   Example: `\bcat\b` matches "cat" as a whole word, but not in "category".

4. `\B`: Matches a position that is not a word boundary.
   Example: `\Bcat\B` matches "cat" in "concatenate", but not in "category" or "scatter".

## String Boundaries

5. `\A`: Matches the start of the string (similar to ^, but works for multiline strings).

6. `\Z`: Matches the end of the string or just before the newline at the end of the string.

7. `\z`: Matches the end of the string (similar to $, but works for multiline strings).

## Lookaround Assertions

8. Negative Lookbehind `(?<!...)`: Asserts that what precedes the current position does not match the pattern.
   Example: `(?<!^)\bun` matches "un" at the start of a word, but not at the beginning of a line.

9. Negative Lookahead `(?!...)`: Asserts that what follows the current position does not match the pattern.
   Example: `ing\b(?!$)` matches "ing" at the end of a word, but not at the end of a line.

These lookaround assertions allow for more complex matching based on context without including the looked-at characters in the match.

## Examples

- `^Start`: Matches "Start" at the beginning of a line.
- `End$`: Matches "End" at the end of a line.
- `\bword\b`: Matches "word" as a whole word.
- `\Binter\B`: Matches "inter" when it's in the middle of a word (e.g., "winter").
- `\ABegin`: Matches "Begin" at the start of the entire string.
- `Finish\Z`: Matches "Finish" at the end of the string or just before the final newline.

Practice using these anchors, boundaries, and lookaround assertions to create more precise patterns that match at specific positions in the text!