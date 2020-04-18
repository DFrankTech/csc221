# Linux Tutorial 13. Bash Scripting
## Activities
*Script*
Tell you what to say and do
- gets interpreted
echo - prints message to screen

- top
  View real-time data about processes running on the system.
- ps
  Get a listing of processes running on the system.
- kill
  End the running of a process.
- jobs
  Display a list of current jobs running in the background.
- fg
  Move a background process into the foreground.
- ctrl + z
  Pause the current foreground process and move it into the background.

*Tips*
which <program>
Tells path to particular program
$ which bash
/usr/bin/bash

*Variables*
A container for a simple piece of data
$0 - The name of the script
$1 - $9 - Any command line arguments given to the script $1 is the first argument, $2 the second and so on
$# - How many command line arguments were given to the script
$* - All of the command line arguments

data- prints data

*If Statements*
if [] then else fi
