string= input('Enter a string\n')

string=string.lower()
count={}

for ch in string:
    if ch not in ' !@#$%^&*()_+=' and ch in count:
        count[ch] = count[ch]+1
    else:
        count[ch]=1

print('The most frequent character is '+max(count, key=count.get))