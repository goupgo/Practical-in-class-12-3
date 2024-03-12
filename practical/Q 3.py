# ===YOU CAN ADD NEW CLASSES IN THE FOLLOWING PART========
class employDict:
    def __init__(self):
        self.employeeList = {'employeeID': [], 'employeeName': [], 'employeeSalary': [], 'employeeAge': []}
#=========================================================
class Main(employDict):
    #====EDIT THIS FUNCTION TO READ AND RETURN LIST EMPLOYEE========
    def InputListEmployee(self):
        quantity = int(input('Enter the number of employees: '))
        
        for _ in range(quantity):
            employeeID = int(input('\nEnter employees: '))
            employeeName = input('Enter name: ')
            employeeSalary = int(input('Enter salary: '))
            employeeAge = int(input('Enter age: '))
            
            self.employeeList['employeeID'].append(employeeID)
            self.employeeList['employeeName'].append(employeeName)
            self.employeeList['employeeSalary'].append(employeeSalary)
            self.employeeList['employeeAge'].append(employeeAge)
            
        return self.employeeList
        # end def

    #====================f1====================
    def f1(self):
        #=======DO NOT EDIT CODE BELOW===============
        employeeList = self.InputListEmployee()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        for IDs in range(len(employeeList['employeeID'])):
            print('\nEmployees', employeeList['employeeID'][IDs])
            print(employeeList['employeeName'][IDs])
            print(employeeList['employeeSalary'][IDs])
            print(employeeList['employeeAge'][IDs])
        # end def


    #====================f2====================
    def f2(self):
        #=======DO NOT EDIT CODE BELOW===============
        employeeList = self.InputListEmployee()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        employeeList['employeeAge'].reverse()
            
        for IDs in range(len(employeeList['employeeID'])):
            print('\nEmployees', employeeList['employeeID'][IDs])
            print(employeeList['employeeName'][IDs])
            print(employeeList['employeeSalary'][IDs])
            print(employeeList['employeeAge'][IDs])
        # end def



    #====================f3====================
    def f3(self):
        #=======DO NOT EDIT CODE BELOW===============
        employeeList = self.InputListEmployee()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        eligible_employees = [(name, salary) for name, age, salary in zip(employeeList['employeeName'], employeeList['employeeAge'], employeeList['employeeSalary']) if age >= 18]
        sorted_salaries = sorted(eligible_employees, key=lambda x: x[1], reverse=True)
        for name, salary in sorted_salaries:
            print(f"Employee: {name}, Salary: {salary}")
        # end def




#==================DO NOT CHANGE THE CODE BELOW=====================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (2 mark)")
        print(" 3. Test f3 (1 mark)")
        print(" Your selection (1 -> 3): ")
        choice = int(input())
        
        if choice == 1:
            self.f1()
        elif choice == 2:
            self.f2()
        elif choice == 3:
            self.f3()
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()

