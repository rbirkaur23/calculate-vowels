s="Education is the key to success"
s=s.upper()
count=0
for p in s:
  if p in "AEIOU":
    count=count+1
  print("Number of vowels are ",count)  
