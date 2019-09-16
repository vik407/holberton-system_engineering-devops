# SHELL REDIRECTIONS

0 - echo Hello, World

This script echo "Hello, World" with a new line to the standard output.

1- echo ""(Ôo)'"

This script display a confused smiley "(Ôo)' to the output.

2-cat /etc/passwd

This script display the content of the /etc/passwd

3-cat /etc/passwd /etc/hosts

This script display the contents of /etc/passwd and /etc/hosts

4-tail -n 10 /etc/passwd

This script display the last 10 lines in the file /etc/passwd

5-head /etc/passwd

This script display the first 10 lines in the file /etc/passwd

acta | tail --line=1

This script displays the third line in a file called iacta then tail show the space line up.

7-echo "Holberton School" > '*\'''"Holberton School"'''\*$?*****:)'

This script create a file called *\'"Holberton School"'\*$?*****:) and the text Holberton School append it at the file.

8-ls -la > ls_cwd_content

This script write the result of the command ls -la to a file called ls_cwd_content. It will create this file if it does not exist and will overwrite it if it does.

9-echo -en | tail -n 1 iacta >> iacta

This script duplicate the last line in the file iacta

10-find . -name '*.js' -type f -delete

This script will delete all regular files (excluding directories) that end with .js that are present in the current directory and all of its subfolders.

11-find -mindepth 1 -type d | wc -l

This script count the number of directories and subdirectories in the current directory while excluding the hidden . and .. directories.

12-ls -t | head

This script display the 10 newest files in the current directory, one per line, sorted from newest to oldest.

13-sort | uniq -u

This script take a list of words, one line and the output will be alphabetically sorted.

14-grep -i root /etc/passwd

This script display all lines in the file /etc/passwd that contain the pattern "root".

15-grep -i bin /etc/passwd | wc -l

This script display the physical number of lines that contain the pattern "bin" in the file /etc/passwd.

16-grep -iA 3 root /etc/passwd

This script lines in a file called /etc/passwd that contain the pattern "root" and 3 lines after them.

17-grep -iv bin /etc/passwd

This script display all lines from a file /etc/passwd that do not contain the pattern bin

18-grep -i "^[a-z]" /etc/ssh/sshd_config

This script display all lines in the file /etc/ssh/sshd_config that starts with a capital or lowercase letter

19 - tr Ac Ze

This script replace all characters A and c from input with the character Z and e.

20-tr -d cC

This script remove the letter c and C from input.

21-rev

This script take an input and reverse it.

22-cut -d':' -f1,6 /etc/passwd | sort

This script display the user and the forlder path from passwd file and sort it

100-empty_casks find . -empty -printf "%f\n"

This script finds all empty files and directories in the current directory and all sub-directories.

101-gifs find . -name "*.gif" -type f -printf "%f\n" | LC_ALL=C sort -fV | rev | cut -c 5-| rev

This script lists all the files with a .gif extension in the current directory and all its sub-directories.

102-acrostic cut -c 1 | tr -d '\n' | sort

This script decodes acrostics that use the first letter of each line.

103-the_biggest_fan tail -n +2 | cut -f1 | sort | uniq -c | sort -gr | rev | cut -d' ' -f1 | rev | head -11

This script parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.