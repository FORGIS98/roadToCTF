myBytes = [
  106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
  0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
  0o142, 0o131, 0o164, 0o63 , 0o163, 0o137, 0o67 , 0o141,
  '1' , 'c' , '8' , 'c' , '6' , '6' , '8' , 'b'
]

for x in myBytes:
    if(x not in ['1' , 'c' , '8' , 'c' , '6' , '6' , '8' , 'b']):
        print(chr(x), end="")
    else:
        print(x, end="")
