import re
def re_new(pattern, replace, string) :
    print(re.sub(pattern, "{"+replace+"}", string))
    print("\n")

s = "The zoo had wild dogs, bobcats, lions, and other wild cats"
re_new("cat", "dog", s)


def re_view(pattern, string) :
    print(re.compile(pattern, re.M).sub("{\g<0>}", string.rstrip()))

re_view("o",s)