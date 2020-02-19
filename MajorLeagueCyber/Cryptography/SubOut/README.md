# Sub Out
The substitution cipher is the kind of challenge that you'd find inside of a cereal box. The ones with the puzzles and the decoder rings.

Except it gets more complicated if you don't have the decoder ring!

## Solution
So this one is a big change, try and repeat. So you have the ciphertext, and what you have to try is to find a pattern, something that tells you information about the text. Here we have `izu` that is repeated many times, so we can thing that `izu` means `the`. And we are on a good path, because looking at the las line `izu rpjm ky "izux jpp pksue zjhhkpx uoug jriug".` we find our well known `the flag is "..."` and that's a format we know. With that in mind, we change `i` with `t`, `z` with `h` and so on. We do it in all the text, and we read again and look for a word that sounds familiar and we change more letters. And so on, that's what the script does, we change the variable `abc` to change the letters of the ciphertext and make the real plain text.
