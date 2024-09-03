# Level 7: Flags and Options

Flags and options in regular expressions modify how the pattern is interpreted and matched. In Python's re module, these flags can be set using either inline flags or as arguments to re functions.

## Common Flags

1. `re.IGNORECASE` or `(?i)`: Makes the pattern case-insensitive.
   Example: `(?i)python` matches "Python", "PYTHON", "python", etc.

2. `re.MULTILINE` or `(?m)`: Makes `^` and `$` match the start/end of each line.
   Example: `(?m)^Start` matches "Start" at the beginning of any line in a multiline string.

3. `re.DOTALL` or `(?s)`: Makes the dot (.) match any character, including newlines.
   Example: `(?s).*` matches an entire string, including newlines.

4. `re.VERBOSE` or `(?x)`: Allows you to write more readable patterns by ignoring whitespace and allowing comments.
   Example:
   ```python
   pattern = re.compile(r"""
       \d{3}  # Match three digits
       -      # followed by a hyphen
       \d{4}  # followed by four digits
   """, re.VERBOSE)
   ```

5. `re.ASCII` or `(?a)`: Makes `\w`, `\W`, `\b`, `\B`, `\d`, `\D`, `\s`, and `\S` perform ASCII-only matching.

## Combining Flags

You can combine multiple flags using the bitwise OR operator `|` or by listing them in the inline flag group.

Example: `re.compile(pattern, re.IGNORECASE | re.MULTILINE)`
Inline equivalent: `(?im)pattern`

## Using Flags in Python

```python
import re