import re


text= "hiree me so we can do great"
pattern="we"
match= re.search(pattern, text)

if match:
    print('match_result=', match.group())
else:
    print('no match')