name=input("Enter your name :")

marks=[]
for i in range(4):
    mark=int(input("Enter your marks :"))
    marks.append(mark)
sum=0
larg=0
small=marks[0]

for i in marks:
    sum=sum+i
    if i > larg:
        larg=i
    if i < small:
        small=i
avg=sum/len(marks)
print("              ")
print("-----------------student report-----------------------")
print("\n")
print("Name :",name.capitalize())
print("Total sum :",sum)
print("Average :",avg)
print("largest mark :",larg)
print("lowest mark :",small)