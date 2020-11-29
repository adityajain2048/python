try :
    age=int(input('Age = '))
    print(age)
    income=1000000
    price=income/age
except ValueError:
    print(" Invalid output ")
except ZeroDivisionError:
    print("Age cant be 0.")