# Hidden Files
This crocodile has many secrets. If you poke him enough, he will reveal the secret of his people.

# Solution
As the title sugest, there are files hidden in the picture. So we first use a tool called `binwalk` and it will show us information hidden in the picture. We see there is a Zip archive data, so we just use `unzip` on the picture and there we go, `flag.png` appears.
