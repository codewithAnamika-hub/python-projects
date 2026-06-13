a=input("enter the name of student");
print(a)
b=int(input("enter the no. of maths"))
c=int(input("enter the no. of english"))
d=int(input("enter the no. of hindi"))
e=int(input("enter the no. of science"))
f=int(input("enter the no.of s.s.t"))
total=b+c+d+e+f
print(total)
percentage=total/5
print(percentage)
if(percentage>=33):
  print("pass")
else:
    print("fail")
