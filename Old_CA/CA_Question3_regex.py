import re

string = '''Betty Botter bought a bit of butter
But, she said, this butter’s bitter
If I put it in my batter
It will make my batter bitter
But a bit of better butter
Will make my batter better
So ’twas better Betty Botter bought a bit of better butter'''

def re_view(pattern, string) :
    print(re.compile(pattern, re.M).sub("{\g<0>}", string.rstrip()))

# A
re_view(r"(butter|batter|better)$",string)

# B
print("\nB :: \n")
re_view(r"((butter|batter|better)$|Betty)",string)