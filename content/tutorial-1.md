# Level 1: Basic Patterns

In this level, you'll learn how to match simple literal characters, use the dot (.) wildcard, and introduce the * quantifier.

## Literal Characters

To match a specific character or sequence of characters, simply use those characters in your pattern. For example:

- `'hello'` matches the exact string "hello"
- `'python'` matches the exact string "python"

## Dot (.) Wildcard

The dot (.) is a special character that matches any single character except a newline. For example:

- `'h.llo'` matches "hello", "hallo", "h3llo", etc.
- `'py...n'` matches "python", "pyplot", "pycon", etc.

## Asterisk (*) Quantifier

The asterisk (*) quantifier matches zero or more occurrences of the previous character or group. For example:

- `'ab*c'` matches "ac", "abc", "abbc", "abbbc", etc.
- `'.*'` matches any string, including an empty string

## Using re.search()

To use these patterns in Python, you can use the `re.search()` function:
