# Login
You've been tasked by law enforcement to break into the secret safe of Nefarious Incorporated.

You've found the door to the safe room. But it's protected by a computerized login system...

root@13ea019f8a92:~# ./login
Error: ./login <password>

To get in you'll need the password...

But it looks like you can run commands on the login system. Maybe you can extract the password from the program?

# Solution
Very easy one, we could use a fancy tool like radare2 to reverse the executable, but for this one we can use a tool call `strings` in linux. Is a command line tool thar print the sequence of printable characters in a file. So with a simple `strings login` you'll find it.
