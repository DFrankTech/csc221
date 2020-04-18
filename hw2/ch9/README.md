# Linux Tutorial 9. Filters
## Activities
**Filter**
filter- program that accept textual data then formats it in a certain way
- takes raw data to manipulate

~/Documents/GitHub/csc221/hw2/ch9 (master)
$ cat Catering.txt
Number of Packages for Catering:

Cheeseburgers   10
Drinks          100
        Sodas   50
        Water   25
        Juices  25
...

**Head**
head [-number of lines to print] [path]
- prints the number of lines from the top
  -default lines printed is 10
i.e.
head -4 Catering.txt
- prints the first 4 lines

**Tail**
tail [-number of lines to print] [path]
- does the opposite of head. starts from bottom of files and prints the number of lines going up

**Sort**
sort [-options] [path]
- sorts items in file numbered then alphabetically
  - if there is tabbed items, they will be ordered alphabetically first

**NL**
nl [-options] [path]
- shows you the number of lines
i.e.
nl -s '. ' -w 10 Catering.txt
- shows number of lines in entire Document
  - includes spaces
- tabbed items are aligned

**WC**
wc [-options] [path]
- default gives a count of lines, words, then characters
  - -l only lines
  - -w only words
  - -m only characters
    - can be combined

**Cut**
cut [-options] [path]
- shows only certain fields from the columns
- defaults to using TAB as a separator
i.e.
cut -f 1 -d ' ' Catering.txt
- -f specifies which fields, in this case 1 column
- -d inputs the separator character (can be anything you want)
  - lets say we wanted 2 fields, separate them with commas
    i.e
    cut -f 1,2 -d ' ' Catering.txt

**Sed**
sed <expression> [path]
- Stream Editor; search for item and replace it
  - s/search/replace/g
  - g means global (optional) every instance of
  -identifies strings of characters

**Uniq**
uniq [options] [path]
- removes duplicate lines
  - only if lines are one after the other

**Tac**
tac [path]
- cat in reverse; prints file backwards
