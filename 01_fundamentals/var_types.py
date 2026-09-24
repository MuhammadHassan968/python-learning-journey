name = 'hassan'
age = 21
height = 182.5
is_student = True


#Printing variable values
print(name)
print(age)
print(height)
print(is_student)


#Printing variable types
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


# Type Conversions

# string -> int 
age_text = "21"
age_int=int(age_text)
print(age_int)
print(type(age_int))

# int -> float
num_int = 70.2 
num_float=float(num_int)
print(num_float)
print(type(num_float))

# int -> string  
count = 100
str_count = str(count)
print(count)
print(type(count))


#Operators
num1 = 56
num2 = 45


#Arithmetic
print("Add ", num1+num2)
print("subtract ", num1-num2)
print("Multiply ", num1*num2)
print("division ", num1/num2)
print("reminder", num1%num2)
print("num 1 rasises to power num2  ", num1**num2)


#Comparisons
print(num1>num2)
print(num1<num2)
print(num1==num2)
print(num1>=num2)
print(num1<=num2)
print(num1!=num2)


#Logic
if num1>50 and num2<50 :
    print (" condition is true ")
elif num1>50 or num2<50 :
     print (" one condition is true ") 
else : 
     not is_student 


student_name =input ("Enter student name : ")
Age =input ("Enter student age : ")
math_marks =input ("Enter math marks : ")
eng_marks =input ("Enter eng marks : ")
python_marks =input ("Enter python marks : ")

Total_marks = math_marks+eng_marks+python_marks
Average_marks=(Total_marks/300)*100

print("Total Marks : ", Total_marks)
print("Average Marks : ", Average_marks)