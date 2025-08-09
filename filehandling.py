import os
import csv
os.makedirs('output',exist_ok = True )
os.makedirs('output/csv',exist_ok= True)
class student:
    def __init__(self):
        self.stud = []
    def getdetails(self):
        self.name = input("Enter the name:")
        self.age = input("Enter the age")
        self.u_id = input("enter your university id ")
    
    def showdetails(self):
        print(f'{self.name}\n{self.age}')


obj = student()

obj.getdetails()
obj.showdetails()
