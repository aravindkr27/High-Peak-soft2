f = open("sample_input.txt","r")
text = f.readlines()
d = {}
n = int(text[0][-2])
for i in range(4,len(text)):
    temp = "".join(j for j in text[i])
    texti = temp[:temp.find(":")]
    d[int(temp[temp.find(":")+2:len(temp)])] = texti
def print_ans(arr):
    fo = open("result.txt","w+")
    fo.write("The goodies selected for distribution are:\n\n")
    for i in arr:
        s = str(d[i])+": "+str(i)+"\n"
        fo.write(s)
    t = "\nAnd the difference between the chosen goodie with highest price and the lowest price is "+str(arr[-1]-arr[0])
    fo.write(t)
arr = sorted(d.keys())
n = 4
if n==1:
    print(d[arr[0]],":",arr[0]) 
elif n==len(arr):
    print_ans(arr)
else:
    least = 9999999
    for i in range(len(arr)-n):
        if arr[i:i+n][-1]-arr[i:i+n][0] < least:
            least = arr[i:i+n][-1]-arr[i:i+n][0]
            final_ans = arr[i:i+n]
    print_ans(final_ans)
