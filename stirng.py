a=input()
ans=""
n=5
for i in range(0,len(a)-1,+2):
    ans=ans+((a[i])* int(a[i+1]))
if len(ans)>n:
    print(ans[n-1])
else:
    print('-1')