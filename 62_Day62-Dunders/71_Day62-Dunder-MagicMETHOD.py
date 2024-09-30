from emp import Employee
e=Employee("ashwina")
print(e) #<emp.Employee object at 0x000002290061D940>  without __str__
print(e.name)
print(len(e))
print(e) # with __str__ output: The name of employee is ashwina str (useful without using names of variables)
# if str not present repr will run
print(str(e))
print(repr(e))
e() #call method :make obj callable