import re

txt = "the rain in spain"
x = re.search("^The.*spain$", txt)
if x:
    print("YES! We have a match!")
else:
    print("No match")
