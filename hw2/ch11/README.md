# Linux Tutorial 11. Piping and Redirection
## Main Concepts
Programs automatically have 3 data streams connected to it
1. STDIN (0) - Standard input (data fed into the program)
2. STDOUT (1) - Standard output (data printed by the program, defaults to the terminal)
3. STDERR (2) - Standard error (for error messages, also defaults to the terminal)
- putting the corresponding number before the operator will send it to that stream
  - default is stream 1

** Visual Example**
! [Image of Data Streams]
(https://ryanstutorials.net/linuxtutorial/img/streams.png)

### Activities
**Redirection**
*STDOUT*
By default, we usually get output on screen. But, we have the availability to save it to a file to keep record, feed it to another system, or send it to someone else.
- > - indicates command line we want the programs output will be saved in a file
i.e.
$ ls
 Catering.txt  'Guest list'   README.md  'Vendors for Packages'
$ ls > 'Event Items'
$ cat 'Event Items'
- the output of ls is printed into the Event Items file
  - output is line by line, because it is the safest format for easier manipulation later

If we redirect a file hat does not exists, it is created automatically
- If we redirect to one that already exists, original content will be cleared and the new saved
  - we can get new data appended to the file by using >>
i.e.
$ wc -l 'Event Items' >> "Mary's Night under the Moon"
- prints the 'Event Items' title and line count to the new file

- < - sends the data the opposite direction
i.e.
$ wc -l < "Mary's Night under the Moon"
- read data from the file and print the line count to STDIN

Can combine two forms of Redirection
i.e.
$ wc -l < March.txt > Dates

*STDERR*
Use stream 2 to access STDERR
*error message*
$ ls -l 'Moon' invite.photo

*gives permissions and info*
$ ls -l 'Moon' invite.photo 2> errors.txt
- errors.txt has the lines of text errors received when trying to access certain file if cat-ted

- can save both to normal and error into single file.
  - you redirect STDERR to STDOUT and redirecting STDOUT to a file, no this by adding & in front of the stream number
i.e.
$ ls -l 'Moon' photo.invite > "Mary's Night under the Moon" 2>&1



**Piping**
Sends data from one program to another
- represented by |
  - feeds the output from the program on left as input to the program to the right; imagine putting both visual models together side by side
i.e.
*prints the first 3 files*
$ ls | head -3
Catering.txt
Dates
errors.txt

*pipes output to tail to get only the third file*
$ ls | head -3 | tail -1
errors.txt

*piping and redirection combined*
$ ls | head -3 | tail -1 > "Mary's Night under the Moon"
cat "Mary's Night under the Moon"
errors.txt

*sorting the listing of a directory so that all directories are listed
$ ls -l /etc |tail -n +2 | sort
drwxr-xr-x 1 USAPAWN 197121     0 Jan 28 12:43 pkcs11/
drwxr-xr-x 1 USAPAWN 197121     0 Jan 28 12:43 pki/
drwxr-xr-x 1 USAPAWN 197121     0 Jan 28 12:43 ssh/
...

*feeding output of program to program less  to view it easier
$ ls -l /etc | less
- output scrollable in full screen with line count at top

*identifies all files in home directory where the group has the permission for
$ ls -l ~ | grep '^.....w'
lrwxrwxrwx 1 USAPAWN 197121      32 Jan 23 16:55 Application Data -> /c/Users/USAPAWN/AppData/Roaming/

*creating a list of every user which owns a file in a given directory as well as how many files and directories they own
 ~/Documents/GitHub/csc221/hw2
$ ls -l ch11/ Catering | tail -n +2 | sed 's/\s\s*/ /g' | cut -d ' ' -f 3 | sort | uniq -c
ls: cannot access 'Catering': No such file or directory
      1
     10 USAPAWN
