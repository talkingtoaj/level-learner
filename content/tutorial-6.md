# Level 6: Lookahead and Lookbehind

Lookahead and lookbehind assertions in regular expressions allow you to create more complex patterns by looking ahead or behind the current position without including the looked-at characters in the match.

## Lookahead

1. Positive Lookahead `(?=...)`: Asserts that what follows the current position matches the pattern.
   Example: `\d+(?=\s*dollars)` matches numbers followed by "dollars" without including "dollars" in the match.

2. Negative Lookahead `(?!...)`: Asserts that what follows the current position does not match the pattern.
   Example: `\b\w+(?!\s+\d)` matches words not followed by numbers.

## Lookbehind

3. Positive Lookbehind `(?<=...)`: Asserts that what precedes the current position matches the pattern.
   Example: `(?<=\$)\d+` matches numbers preceded by a dollar sign without including the dollar sign.

4. Negative Lookbehind `(?<!...)`: Asserts that what precedes the current position does not match the pattern.
   Example: `(?<![@\w])\w+` matches words not preceded by @ or alphanumeric characters.

## Combining Lookaround Assertions

You can combine lookahead and lookbehind assertions for more complex matching:

Example: `(?<=\$)(\d+)(?=\.\d{2})` matches the dollar amount in "$10.99" without including the dollar sign or cents.

## Zero-width Assertions

Lookaround assertions are zero-width, meaning they don't consume characters in the string.

Practice using these lookaround assertions to create more sophisticated regex patterns that can match based on context!