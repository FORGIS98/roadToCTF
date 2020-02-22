# Virus
We were able to capture the internet communication of virus a most wanted internet criminal. Can you figure out virus's password so we can log into his server?

# Solution
.pcap files contain the packet data of a network. This files can be open with tools like wireshark. So, we open wireshark, and load the .pcac file. Then we filter all the info and we only take `TELNET` info. Then we follow the `TCP Stream` and read the client information (in red usually). After a minute you'll find the password somewhere in the `TCP Stream`.
