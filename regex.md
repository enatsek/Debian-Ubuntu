##### Regex
# Regular Expressions Tutorial 

<details markdown='1'>
<summary>
0. Specs
</summary>

---
### 0.1. The What

Regular expressions, often abbreviated as regex or regexp, are sequences of characters that define search patterns in text. They are widely used in programming and text processing for tasks like searching, replacing, and validating input.

### 0.2. The Environment

Regex and its usage are independent of operating systems. I tested these patterns on Debian and Ubuntu, but they should work on any Linux, Unix-like, or other operating systems that support standard regex syntax.


### 0.3. Resources:

- Book: 978-0-13-475706-3 *Learning Regular Expressions* by Ben Forta
- Book: 978-1-4842-3875-2 *Regex Quick Syntax Reference* by Zsolt Nagy
- Book: 978-1-449-31943-4 *Regular Expressions Cookbook* by Jan Goyvaerts and Steven Levithan

<br>
</details>

<details markdown='1'>
<summary>
1. Basics
</summary>

---
### 1.1. A String Itself

Obviously, every string is a match for itself.
- Pattern: `go` → Matches: `go`
- Pattern: `dog` → Matches: `dog`

### 1.2. OR Operator: `|` or `[]`

- `(c|b|t)ook` → `cook`
- `(c|b|t)ook` → `book`
- `(c|b|t)ook` → `took`
- `[cbt]ook` → `cook`
- `[cbt]ook` → `book`
- `[cbt]ook` → `took`

### 1.3. Ranges

- `[a-z]` → any lowercase letter
- `[A-Z]` → any uppercase letter
- `[0-9]` → any single digit number, including 0
- `[d-g]` → `d`, `e`, `f`, or `g` (just one of them)
- `[M-R]` → `M`, `N`, `O`, `P`, `Q`, or `R` (just one of them)
- `[a-zA-Z]` → any letter (lowercase or uppercase)
- `[a-zA-Z0-9]` → any letter or number (single digit)
- `[0-9a-fA-F]` → a hexadecimal digit

### 1.4. Negation (Exception)

- `[^a-z]` → any character except a lowercase letter
- `[^A-Z]` → any character except an uppercase letter
- `[^0-9]` → any character except a single digit number

### 1.5. Character Classes

- `.` → Any single character (except newline in most contexts)
- `\d` → any digit (equivalent to `[0-9]`)
- `\D` → any non-digit character (equivalent to `[^0-9]`)
- `\w` → any word character (letter, digit, or underscore; equivalent to `[a-zA-Z0-9_]`)
- `\W` → any non-word character
- `\s` → any whitespace character (space, tab, newline, carriage return)
- `\S` → any non-whitespace character
- `\r` → Carriage Return (CR)
- `\n` → Line Feed (LF)
- `\t` → Tab
- `\b` → Word boundary (zero-width position at the start or end of a word)

### 1.6. Escape Characters
Any operator or quantifier can be escaped with \ to resemble itself

Any special character (operator or quantifier) can be escaped with `\` to match its literal value.

- `\.` → `.`
- `\[` → `[`
- `\]` → `]`
- `\(` → `(`
- `\)` → `)`
- `\*` → `*`
- `\+` → `+`
- `\\` → `\`
- `\.` → `.`

When used inside a character class `[]`, the backslash is not always necessary for these characters, but it's good practice to escape them for clarity. Inside a character class, most characters lose their special meaning.

- `[().\\]` → matches `(`, `)`, `.`, or `\`

<br>
</details>

<details markdown='1'>
<summary>
2. Quantifiers and Boundaries
</summary>

---
### 2.1. `*` Quantifier (Zero or More)

A `*` quantifier after a character or group means **0 or more occurrences** of it.

- `goal*` → `goa`, `goal`, `goall`, `goalll`, `goallll`...
- `co(me)*` → `co`, `come`, `comeme`, `comememe`, `comemememe`...
- `[a-zA-Z]*` → any string made from alphabet letters or an empty string

### 2.2. `+` Quantifier (One or More)

A `+` quantifier after a character or group means **1 or more occurrences** of it.

- `goal+` → `goal`, `goall`, `goalll`, `goallll`... (not `goa`)
- `co(me)+` → `come`, `comeme`, `comememe`, `comemememe`... (not `co`)
- `[a-zA-Z]+` → any non-empty string made from alphabet letters

### 2.3. `?` Quantifier (Zero or One)

A `?` quantifier after a character or group means **0 or 1 occurrence** of it.

- `goal?` → `goa`, `goal`
- `co(me)?` → `co`, `come`
- `[a-zA-Z][a-zA-Z]?` → any 1 or 2 alphabet letters

### 2.4. `{}` Quantifier (Exact Count or Range)

Can be in `{m}`, `{n,}`, or `{p,r}` forms, where `m`, `n`, `p`, `r` are whole numbers.

They come after a character or group and mean:
1. Exactly `m` occurrences
2. `n` or more occurrences
3. `p` to `r` occurrences (inclusive)

- `set{3}` → `settt` (exactly 3 't's)
- `set{3,}` → `settt`, `setttt`, `settttt`... (3 or more 't's)
- `se{2,5}` → `sett`, `settt`, `setttt`, `settttt` (2 to 5 't's)
- `[a-zA-Z]{3}[0-9]{1,3}` → any 3 letters followed by 1 to 3 digits

### 2.5. Greedy vs. Lazy Quantifiers

By default, quantifiers are **greedy**—they match as many characters as possible.

For example, with the regex:

```
\(.*\)
```

(applied to find anything in parentheses) on the text:

```
abc(def)ghi(jkl)mno
```

To make quantifiers **lazy** (matching the minimum possible), add `?` after the quantifier:
```
\(.*?\)
```
This regex will match `(def)` and `(jkl)` separately.

Lazy versions of quantifiers:
- `*` → `*?`
- `+` → `+?`
- `{n,}` → `{n,}?`


### 2.6. Word Boundary: `\b`

`\b` denotes a zero-width position at the beginning or end of a word (where word characters are adjacent to non-word characters).

- `\bget` → words starting with "get" (e.g., "get", "getting", but not "forget")
- `get\b` → words ending with "get" (e.g., "get", "forget", but not "getting")
- `\bget\b` → "get" as a whole word

### 2.7. Line Boundaries: `^` and `$`

`^` defines the start of a line.  
`$` defines the end of a line.

- `^Log:[\s\w]+` → All lines starting with "Log:"
- `^[0-9]{3}` → All lines starting with 3 digits
- `.*END$` → All lines ending with "END"
- `^Begin[\s\w]+End$` → All lines starting with "Begin" and ending with "End"

<br>
</details>

<details markdown='1'>
<summary>
3. Subexpressions and Backreferences
</summary>

---
### 3.1. Subexpressions

A subexpression is a group of characters or operators in parentheses. They are used to apply quantifiers to entire expressions or for capturing.

- `dis(like)` → matches "dislike"
- `dis(like)*` → matches "dis", "dislike", "dislikelike", "dislikelikelike"...
- `dis(like)+` → matches "dislike", "dislikelike", "dislikelikelike"...
- `dis(like)?` → matches "dis" and "dislike"
- `dis(like){2}` → matches "dislikelike"
- `dis(like){2,}` → matches "dislikelike", "dislikelikelike"...
- `dis(like){2,4}` → matches "dislikelike", "dislikelikelike", "dislikelikelikelike"

Subexpressions can be nested:

- `log((in)|(out))` → matches "login" and "logout"

### 3.2. Backreferences

A backreference is in the format of a backslash followed by a digit, like `\1`, `\2`, `\3`. It refers to the text matched by a previous capturing group (subexpression).

For example, this regex matches repeating words:

```
[\s]+(\w+)[\s]+\1[\s]+
```

- `[\s]+(\w+)[\s]+` matches: one or more spaces, followed by one or more word characters (captured as group 1), followed by one or more spaces.
- `\1` matches exactly the same text that was captured by the first group `(\w+)`.

Another example would be matching repeating word couples:

```
[\s]+(\w+)[\s]+(\w+)[\s]+\1[\s]+\2[\s]+
```

Here, `\1` refers to the first word, and `\2` refers to the second word.

Backreferences are particularly useful in find-and-replace operations. In the repeating word example, to replace duplicate words with a single instance, you would use `\1` as the replacement pattern.


<br>
</details>

<details markdown='1'>
<summary>
4. Regex Examples
</summary>

---

Please note: these examples are not perfect. You may find or write more robust versions for production use.

### 4.1. Email Address: `abc.def@email.duck.com.nz`

```
\w+[\w\.]*@\w+[\w\.]*\.\w+
```

**Name Part:**

- Starts with a letter or digit: `\w+`
- May be followed by any number of letters, digits, or dots: `[\w\.]*`
- Then the `@` symbol

**Domain Part:**

- Starts with a letter or digit: `\w+`
- May be followed by any number of letters, digits, or dots: `[\w\.]*`
- Then a literal dot: `\.`
- Ends with the TLD: `\w+`

### 4.2. Date Format: `02/02/2020`, `1\5\12`, `1-11-1995`, `31.12.2020`
```
\d{1,2}[-\/.]\d{1,2}[-\/.]\d{2,4}
```

- 1 or 2 digit day field: `\d{1,2}`
- Separator `-`, `/`, or `.`: `[-\/.]`
- 1 or 2 digit month field: `\d{1,2}`
- Separator `-`, `/`, or `.`: `[-\/.]`
- 2 to 4 digit year field: `\d{2,4}`


### 4.3. Basic IP Address: `192.168.1.110`

```
(\d{1,3}\.){3}\d{1,3}
```

- 3 repetitions of (1 to 3 digits followed by a dot): `(\d{1,3}\.){3}`
- Followed by 1 to 3 digits: `\d{1,3}`

**Note:** This regex matches invalid IP addresses too, like `300.288.11.11`, since it doesn't validate that each octet is between 0-255.

### 4.4. Better IP Address (Validates 0-255 Range)
```
((25[0-5]|2[0-4]\d|1\d{2}|\d{1,2})\.){3}(25[0-5]|2[0-4]\d|1\d{2}|\d{1,2})
```

This pattern validates that each octet is between 0-255:
- `25[0-5]` → 250-255
- `2[0-4]\d` → 200-249
- `1\d{2}` → 100-199
- `\d{1,2}` → 0-99

</details>

