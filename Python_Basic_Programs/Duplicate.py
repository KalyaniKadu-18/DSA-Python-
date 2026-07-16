#Duplicate in string
#str = "Programming"
duplicate = " "
for ch in str:
    if ch not in duplicate:
       if str.count(ch)>1:
          print(ch)
       duplicate += ch 