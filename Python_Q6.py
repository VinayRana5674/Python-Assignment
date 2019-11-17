input_number=input("Please enter a number--")
def divison_by_5_and_7_a(input_number):
    for i in range(1,input_number+1):
        if(i%5==0 and i%7==0):
            yield(i)
my_object=divison_by_5_and_7_a(int(input_number))
print(list(my_object))
