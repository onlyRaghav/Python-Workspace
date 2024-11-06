import numpy as np;

myfriends=np.array(["ivan","anshu","wani","anjani"])

print(type(myfriends))

for name in myfriends:
    print(name)

myfriends[0]="ivan sharma"
print(myfriends)
print(myfriends[0])
myfriends.sort()
print(myfriends)
myreverse=np.flip(myfriends)
print(myreverse)