##### RegexOnDebianUbuntu
# Regular Expressions On Debian and Ubuntu 

<details markdown='1'>
<summary>
0. Specs
</summary>
---
### 0.0. Info
Well I know Regex is (almost) the same on every system, but this site is for Debian and Ubuntu, so it is named as.

### 0.1. Resources:
Book: 978-0-13-475706-3 Learning Regular Expressions by Ben Forta  
Book: 978-1-4842-3875-2 Regex Quick Syntax Reference by Zsolt Nagy  
Book: 978-1-449-31943-4Regular Expressions Cookbook by Jan Goyvaerts and Steven Levithan

<br>
</details>

<details markdown='1'>
<summary>
1. Basics
</summary>
---
### 1.1. A string itself
Obviously every string is a match for itself
- go: go
- dog: dog

### 1.2. Or Operator 
| or []

- (c|b|t)ook → cook  
- (c|b|t)ook → book  
- (c|b|t)ook → took  
- [cbt]ook → cook  
- [cbt]ook → book  
- [cbt]ook → took  

### 1.3. Ranges
- [a-z] → any lowercase letter  
- [A-Z] → any uppercase letter  
- [0-9] → any single digit number, including 0  
- [d-g] → d e f g (just one of them)  
- [M-R] → M N O P Q R (just one of them)  
- [a-zA-Z] → any letter (lower or uppercase)  
- [a-zA-Z0-9] → any letter or number (single digit)  
- [0-9a-fA-F] → a hexadecimal digit  

### 1.4. Exception
- [^a-z] → anything but not a lowercase letter
- [^A-Z] → anything but not an uppercase letter
- [^0-9] → anything but not a single digit number

### 1.5. Character Classes
- . →  Anything
- \d → any digit
- \D → anything other than a digit (any non-digit)
- \w → any letter or digit (any alphanumeric character)
- \W → anything other than letters and digits (any non-alphanumeric character)
- \s → any whitespace including CR, LF, tab
- \S → anything other than whitespaces
- \r → Carriage Return (CR)
- \n → Line Feed (LF)
- \t → Tab
- \b → Word boundary (start or end of a word)

### 1.6. Escape Characters
Any operator or quantifier can be escaped with \ to resemble itself

- \\. → .
- \\[ → [ 
- \\] → ]
- \\( → (
- \\) → )
- \\* → *
- \\+ → +
- \\\ → \
- \\. → .

When used in a bracket, \ is not necessary

- [().\\] → ( ) . or \

<br>
</details>

<details markdown='1'>
<summary>
2. Quantifiers and Boundaries
</summary>
---
### 2.1. * Quantifier
A * quantifier after a character or group means 0 or more occurences of it.

- goal* → goa goal goall goalll goallll ...
- co(me)* → co come  comeme comememe comememe ...
- [a-zA-Z]* → any string made from alphabet letters or an empty string

### 2.2. + Quantifier
A + quantifier after a character or group means 1 or more occurences of it.

- goal+ → goal goall goalll goallll ...
- co(me)+ → come  comeme comememe comememe ...
- [a-zA-Z]+ → any string made from alphabet letters

### 2.3. ? Quantifier
A ? quantifier after a character or group means 0 or 1 occurences of it.

- goal? → goa goal
- co(me)? → co come
- [a-zA-Z][a-zA-Z]? → any 1 or 2 alphabet letters

### 2.4. {} Quantifier
Could be in {m} {n,} or {p,r} forms, m, n, p, r are all whole numbers

They come after a character or group and mean:
1. Exactly m occurences 
2. n or more occurences
3. p to r occurences

- set{3} → settt
- set{3,} → settt setttt settttt ...
- se{2,5} → sett settt setttt settttt
- [a-zA-Z]{3}[0-9]{1,3} → any 3 letters followed by 1 to 3 digits

### 2.5. Greedy and Lazy Quantifiers
By default, a quantifier matches as many of characters as possible. 

When we try the regex:

```
\(.*\)
```

(find anything in paranthesis) on the following 

```
abc(def)ghi(jkl)mno
```

instead of matching `(def)` and `(jkl)`, it matches `(def)ghi(jkl)`. This is called greedy matchings. So quantifiers are greedy by default.

To change the behaviour, that is matching the minimum, we can use the lazy versions of quantifiers by adding a ? to the end. Like:

```
\(.*?\)
```

This regex matches (def) and (jkl), and this is called lazy matching.

The lazy versions of the quantifiers are as follow:

- \*	→ \*?  
- \+	→ \+?  
- {n,} >	{n,};

### 2.6. Word Boundary: \b
\b denotes beginning or end of a word (characters surrounded by whitespaces).

- \bget → words starting with get
- get\b → words ending with get
- \bget\b → get as a whole word

### 2.7. Line Boundaries: ^ and $
^ defines the start of a line  
$ defines the end of a line  

- ^Log:[\s\w]+ → All the lines starting with Log:
- ^[0-9]{3} → All the lines starting with 3 digits
- .*END$ → All the lines ending with END
- ^Begin[\s\w]+End$ → All the lines starting with Begin and ending with End

<br>
</details>

<details markdown='1'>
<summary>
3. Subexpressions and Backreferences
</summary>
---
### 3.1. Subexpressions
A subexpression is a group of characters or operators in paranthesis. They are used to apply quantifiers to expressions.

- dis(like) → matches dislike 
- dis(like)* → matches dis, dislike, dislikelike, dislikelikelike, ...
- dis(like)+ → matches dislike, dislikelike, dislikelikelike, ...
- dis(like)? → matches dis and dislike
- dis(like){2} → matches dislikelike
- dis(like){2,} → matches dislikelike, dislikelikelike, dislikelikelikelike, ...
- dis(like){2,4} → matches dislikelike, dislikelikelike, dislikelikelikelike

Subexpressions can be nested

- log((in)|(out)) → matches login and logout

### 3.2. Backreferences
A backreference is in the format of a backslash followed by a digit, like \1 \2 \3. It refers to the subexpression in the relative position.

For example, the following regex matches the repeating words:

```
[\s]+(\w+)[\s]+\1[\s]+
```

[\s]+(\w+)[\s]+ matches a word, that is 1 or more whitespaces, followed by 1 or more characters, followed by 1 or more whitespaces. 

As the part (\w+) is the first subexpression in the regex, \1 matches to whatever it matches. So the regex matches the repeating word.

Another example would be matching repeating word couples:

```
[\s]+(\w+)[\s]+(\w+)[\s]+\1[\s]+\2[\s]+
```

The first (\w+) will be the first word as \1, and the second one will be the second word as \2.

Backreferences help a lot at find and replace operations. At the repeating word example, if we want to replace repeating words to a single one, for the replace part we would have to write \1 

<br>
</details>

<details markdown='1'>
<summary>
4. Regex Examples
</summary>
---
Please consider, this examples are not perfect. You or someone else can definitely find or write better versions. 

### 4.1. Email address   abc.def@email.duck.com.nz
```
\w+[\w\.]*@\w+[\w\.]*\.\w+
```

**Name Part:**  
it can only start with a letter or a digit \w+ then may follow any number of letters, digits and dots [\w\.]* then comes @

**Domain Part:**

it can only start with a letter or digit \w+ then may follow any number of letters, digits and dots [\w\.]* then comes . \\. and then comes the TLD part \w+

### 4.2. Date Format 02/02/2020  1\5\12 1-11-1995 31.12.2020
```
\d{1,2}[-\/.]\d{1,2}[-\/.]\d{2,4}
```

1 or 2 digit day field → \d{1,2}  
Separator - \ / or . → [-\/.]  
1 or 2 digit month field → \d{1,2}  
Separator - \ / or . → [-\/.]  
2 to 4 digit year field → \d{2,4}  

### 4.3. IP Address  192.168.1.110   (A better one is coming too)
```
(\d{1,3}\.){3}\d{1,3}
```

3 of (1 to 3 digit numbers, followed by a dot) → (\d{1,3}\.){3}
1 (1 to 3 digit numbers) → \d{1,3}

Actually this regex matches invalid IP addresses too, like:  300.288.11.11


### 4.4. A Better IP Adress
```
(((25[0-5])|(2[0-4]\d)|(1\d{2})|(\d{1,2}))\.)(((25[0-5])|(2[0-4]\d)|(1\d{2})|(\d{1,2})))
```

</details>

