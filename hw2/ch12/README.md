# Linux Tutorial 12. Process Management
## Main Concepts

Program- series of instructions that tell the computer what to do
- instructions are copied into memory
- space is allocated for variables and other stuff required to mange execution

**Running a Program**
*TOP*
top -tells what is currently happening on the system
$ top
Tasks: 174 total, 3 running, 171 sleeping, 0 stopped
KiB Mem: 4050604 total, 3114428 used, 936176 free
Kib Swap: 2104476 total, 18132 used, 2086344 free

 PID USER %CPU %MEM COMMAND
6978 ryan 3.0  21.2 firefox
  11 root 0.3   0.0 rcu_preempt
6601 ryan 2.0   2.4 kwin

### Activities
*PS*
Processes- shows processes running on current terminal
- adding the argument aux will show a complete in-dept system view

Closing a Process
Use kill to act as a force quit
kill- [signal] <PID>
  - for example when a browser crashes, use this to act close it

*Jobs*
Use to lists currently running background jobs
*waits to prompt after 5 seconds
$ sleep 5
  - adding an & to the end to run in background to notify
    - assigns process a job number and lets us continue to work while process still runs
  - CTRL- z -current foreground process will be paused and moved into the background
$ fg <job number>
