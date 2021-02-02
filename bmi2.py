weight = int(input("enter weight:"))
height = int(input("enter height:"))

BMI = ((weight)/((height/100)*(height/100)))

print('BMI: {:.1f};'.format(BMI))