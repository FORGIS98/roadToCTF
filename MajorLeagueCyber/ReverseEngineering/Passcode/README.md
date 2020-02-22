# Passcode
Ok you're in the secret safe room. The safe itself looks physically intimidating but it has a small key pad.

On the safe it looks like they switched the password for a passcode....

root@13ea019f8a92:~# ./passcode
Please enter your passcode: 12345678
[ACCESS DENIED]

To break into the safe you'll need to figure out the passcode. Maybe this program is like the door and saves the keycode inside of itself somehow.

The passcode is the flag.

# Solution
For this one we are going to use radare2, first of all we use `rabin2 -I passcode` and `rabin2 -z passcode` for basic information. Then we go to radare2 and execute a full analysis with the command `aaaa`. Then we seek the main `s main` and use the "graphical" view to see how the program flows with the command `VV`. Finally, we read and find that our input is compare to an hexadecimal number `cmp eax, 0x13371337` where `eax` is our input. Then we take the hex number and change it to decimal and we are done.
