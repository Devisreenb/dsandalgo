def ispali(arr):
    if arr=="":
        return True
    new =""
    arr=  arr.lower()
    for i in arr:
        if i.isalnum():
            new+=i
        
    if new == new[::-1]:
        return True
    else:
        return False

ipt ="A man, a plan, a canal: Panama"
print(ispali(ipt))