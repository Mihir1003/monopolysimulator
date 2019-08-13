while True:
    x= raw_input("Enter list item or type done to start calculations...(please do not type non integer questions i am too lazy too code-in a validator)")
    lists=[]
    if x != "done":
        lists.append(float(x))
    else:
        break

l = x.len()
t=0.0
product=1.0
while t<l:
    product=product*x[t]
    t=t+1

t=0.0
summation=0.0
while t<l:
    summation=summation+x[t]
    t=t+1.0

answer= (product^(1/l)+(summation/l))/2
print answer
