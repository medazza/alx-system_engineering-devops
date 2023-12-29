# 0x06. Regular Expressions

Regular expressions, often abbreviated as "regex" or "regexp," are powerful tools for pattern matching and text manipulation. They provide a concise and flexible way to search, match, and manipulate strings based on specific patterns.

## Table of Contents
1. [Introduction to Regular Expressions](#introduction-to-regular-expressions)
2. [Basic Syntax](#basic-syntax)
3. [Common Metacharacters](#common-metacharacters)
4. [Matching Text](#matching-text)
5. [Modifiers](#modifiers)
6. [Character Classes](#character-classes)
7. [Quantifiers](#quantifiers)
8. [Anchors](#anchors)
9. [Groups and Alternation](#groups-and-alternation)
10. [Examples](#examples)
11. [Conclusion](#conclusion)

---

## Introduction to Regular Expressions

A regular expression is a sequence of characters that defines a search pattern. It can be used for various text-processing tasks like validation, searching, and replacing. Regular expressions are supported in many programming languages and text editors, making them a widely used tool.

## Basic Syntax

A regular expression is composed of normal characters and metacharacters, which have special meanings. Here are some basic syntax rules:

- Normal characters (e.g., letters, digits) match themselves.
- Metacharacters (e.g., `.` or `*`) have special meanings and control the pattern's behavior.
- Square brackets `[ ]` define a character class, matching any single character from the class.
- Parentheses `( )` are used for grouping and capturing.

## Common Metacharacters

- `.` (dot): Matches any character except a newline.
- `*`: Matches zero or more occurrences of the preceding character or group.
- `+`: Matches one or more occurrences of the preceding character or group.
- `?`: Matches zero or one occurrence of the preceding character or group.
- `\`: Escapes a metacharacter, making it match as a literal character.
- `|`: Alternation operator, used to match either of two patterns.
- `^`: Anchors the pattern to the start of a line or string.
- `$`: Anchors the pattern to the end of a line or string.

## Matching Text

Regular expressions can be used to:

- Find patterns within a text.
- Validate input data (e.g., email addresses, phone numbers).
- Extract information from strings.
- Replace text with other text.

## Modifiers

Modifiers change the way regular expressions are applied. Common modifiers include:

- `i`: Case-insensitive matching.
- `g`: Global matching (find all matches, not just the first one).
- `m`: Multiline mode (anchors `^` and `$` match the start/end of each line).

## Character Classes

Character classes define sets of characters to match. For example:

- `[abc]`: Matches 'a,' 'b,' or 'c.'
- `[0-9]`: Matches any digit.
- `[^0-9]`: Matches any character that is not a digit.

## Quantifiers

Quantifiers control the number of times a character or group should be matched:

- `*`: Matches 0 or more.
- `+`: Matches 1 or more.
- `?`: Matches 0 or 1.
- `{n}`: Matches exactly n times.
- `{n,}`: Matches at least n times.
- `{n,m}`: Matches between n and m times.

## Anchors

Anchors specify where in the text a match should occur:

- `^`: Matches the start of a line or string.
- `$`: Matches the end of a line or string.
- `\b`: Matches a word boundary.

## Groups and Alternation

Parentheses `( )` are used for grouping and capturing. The pipe symbol `|` is used for alternation:

- `(abc)`: Matches 'abc' and captures it as a group.
- `(abc|def)`: Matches 'abc' or 'def.'

## Examples

Here are some examples of regular expressions and what they match:

- `\d{3}-\d{2}-\d{4}`: Matches a Social Security Number (e.g., 123-45-6789).
- `^[A-Z][a-z]*$`: Matches a single word starting with an uppercase letter.
- `\b\d{4}\b`: Matches 4-digit numbers in a text.

## Conclusion

Regular expressions are a powerful tool for pattern matching and text manipulation. Learning to use them effectively can greatly enhance your text-processing capabilities. Experiment with different patterns and modifiers to become proficient in using regular expressions for your specific needs.

For more in-depth information and advanced patterns, refer to the documentation of your programming language or text editor of choice, as regex implementations may vary.