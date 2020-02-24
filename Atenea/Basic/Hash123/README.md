# Hase 1

In the explanation of the problem they tell as that the flag is "LearnTheHashFunction". We execute in a command line `echo "LearnTheHashFunction" | grep md5sum`

# Hash 2

Same as above, but this time the glag is "ThisIsAMoreSecureHashFunction" and they want us to first do a `sha256` and then a `md5`. So `echo "ThisIsAMoreSecureHashFunction" | grep sha256sum` and the output `echo "xxxxxxxxxxxxxxxxxx..." | grep md5sum`

# Hash 3

Here they gave us the md5 of a word or group of words: `54f662a095fa3d5fbbdaac72d176701b` and they want us to find that word, put it in upper case and the flag is the md5 of the upper case word. The easy way is to use a web site like: https://crackstation.net/ to get the word back.
