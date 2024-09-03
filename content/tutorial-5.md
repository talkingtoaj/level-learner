# Level 5: Groups and Capturing

Groups in regular expressions allow you to treat multiple characters as a single unit. They are created by enclosing parts of a regex pattern in parentheses ().

## Basic Grouping

1. Parentheses `()` create a capturing group.
   Example: `(ab)+` matches one or more occurrences of "ab".

## Capturing Groups

2. Capturing groups store the matched content for later use.
   Example: In the pattern `(\d{3})-(\d{4})`, the first group captures the first three digits, and the second group captures the last four digits.

## Non-capturing Groups

3. `(?:...)` creates a non-capturing group. It groups the contents but doesn't store the match.
   Example: `(?:ab)+` matches one or more occurrences of "ab" without capturing.

## Named Groups

4. `(?P<name>...)` creates a named capturing group.
   Example: `(?P<area_code>\d{3})-(?P<number>\d{4})` captures the area code and number separately with names.

## Backreferences

5. `\1`, `\2`, etc., refer to captured groups by number.
   Example: `(\w+)\s+\1` matches repeated words.

6. `(?P=name)` refers to a named group.
   Example: `(?P<word>\w+)\s+(?P=word)` also matches repeated words.

## Alternation within Groups

7. `(a|b)` matches either "a" or "b".
   Example: `I like (cats|dogs)` matches "I like cats" or "I like dogs".

Practice using these grouping techniques to create more complex and powerful regex patterns!