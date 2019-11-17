class Reverselter:
    def __init__(self,l):
        x=len(l)
        for i in range(x-1,-1,-1):
            print(l[i])
my_list=[8343,43432,3434,434]
Reverselter(my_list)
