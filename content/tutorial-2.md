# Level 2: Character Classes

Character classes allow you to match any one of a set of characters. They are defined using square brackets [].

## Basic Character Classes

- `[aeiou]` matches any single vowel
- `[0-9]` matches any single digit
- `[a-z]` matches any single lowercase letter
- `[A-Z]` matches any single uppercase letter

## Negated Character Classes

You can negate a character class by putting a ^ symbol after the opening bracket:

- `[^aeiou]` matches any character that is not a vowel

## Combining Character Classes

You can combine multiple ranges or individual characters:

- `[a-zA-Z]` matches any single letter, uppercase or lowercase
- `[0-9a-fA-F]` matches any hexadecimal digit

## Predefined Character Classes

Python's re module provides some predefined character classes:

- `\d` matches any digit (equivalent to [0-9])
- `\D` matches any non-digit (equivalent to [^0-9])
- `\w` matches any alphanumeric character (equivalent to [a-zA-Z0-9_])
- `\W` matches any non-alphanumeric character
- `\s` matches any whitespace character (space, tab, newline, etc.)
- `\S` matches any non-whitespace character

Note: When using these predefined classes in a string, you need to escape the backslash, e.g., "\\d" or use a raw string r"\d".

## Examples

Here are some examples of using character classes:

1. Match any vowel: `[aeiou]`
2. Match any consonant: `[^aeiou]`
3. Match any letter: `[a-zA-Z]`
4. Match any hexadecimal digit: `[0-9a-fA-F]`
5. Match any non-digit: `\D`
6. Match any alphanumeric character: `\w`
7. Match any whitespace: `\s`
8. Match any non-letter: `[^a-zA-Z]`

Practice using these character classes to create more flexible patterns!