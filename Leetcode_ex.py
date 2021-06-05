def check(s):
    count = 0
    vowel = ['a', 'e', 'i', 'o', 'u']
    for c in s:
        if(c in vowel):
            count+=1
    return count

print(check("hourly new day"))
