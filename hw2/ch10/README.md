# Linux Tutorial 10. Grep and Regular Expressions
## Main Concepts
Regular Expressions- allow us to create patterns
- similar to wildcards
- usually used to identify and manipulate data
  - like if we wanted to identify every line with an email address or url in it

**eGrep**
egrep [command line options] <pattern> [path]
Program that searches a set of data and prints every line that contains a given pattern
- extension of grep program
- prints entire line with string
i.e.
egrep '50' Catering.txt
- prints lines with the string 50
        Sodas   50
Salad           50      *more added for dietary restrictions
Fries           50
Mashed Potatoes 50
etc.

egrep -n '50' Catering.txt
- adds line numbering as well

egrep -c '50' Catering.txt
- instead of printing lines, it just shows how many lines  had the 50 occurrence

**Building Blocks of Regular Expressions**
- . - single character
- ? - preceding character matches 0 or 1 times only
- * - preceding character matches 0 or more times
- + - preceding character matches 1 or more times
- {n} - preceding character matches exactly n times
- {n,m} - preceding character matches at least n times and not more than m times
- [agd] - character is one of those included within the square brackets
- [^agd] - character is not one of those included within the square brackets
- [c-f] - dash within the square brackets operates as a range. In this case it means either the letters c, d, e or f
- () - allows us to group several characters to behave as one
- | (pipe symbol) - the logical OR operation
- ^ - matches the beginning of the line
- $ - matches the end of the line

### Activities
i.e.
egrep '[aeiou]{2,}' Catering.txt
- print lines with 2 or more of the vowels listed in a row

egrep '2.+' Catering.txt
- print any line with a 2 in it that is not at the end of the line

egrep '2$' Catering.txt
- print lines where number 2 is the last character on the line

egrep 'or|is|go' Catering.txt
- print each line that contains either is, go, or or

egrep '^[A-K]' Catering.txt
- print lines with A-K un-alphabetically
