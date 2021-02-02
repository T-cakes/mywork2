#This program calculates the user's BMI using their inputs
#author: Stephen Caulfield

#inputs for height and weight
weight = float (input ("enter weight: "))
height = float (input ("enter height: "))

#conversion of centimetres to metre squared
heightmetre = height/100
metresquared = heightmetre**2

#calculation of BMI
BMI = round(weight / metresquared, 2)

#BMI output
print("BMI is " + str(BMI))