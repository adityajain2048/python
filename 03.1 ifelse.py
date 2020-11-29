name = input('Enter your name  ')
if len(name)<3:
    print('Name is too small')
elif len(name)>50:
    print('name is too big ')
else:
    print("Name is okay")