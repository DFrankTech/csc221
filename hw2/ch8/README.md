# Linux Tutorial 8. Permissions
## Activities

**View Permissions:**
~/Documents
$ ls -l GitHub
total 4
drwxr-xr-x 1 USAPAWN 197121 0 Feb 12 10:17 csc221/

**Changing Permissions**
chmod [permissions][path]
Who are we changing the permission for? [ugoa] - user (or owner), group, others, all
- granting or revoking the permission - indicated with either a plus ( + ) or minus ( - )
- permission being setting - read ( r ), write ( w ) or execute ( x )

ls -l frog.png
- list the current permissions

chmod g+x frog.png
- group has the permission to execute the file

chmod u-w frog.png
- users can write to the file only
