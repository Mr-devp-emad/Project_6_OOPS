class Employee:
    def __init__(self, name, employee_id, position):
        self.name = name
        self.employee_id = employee_id
        self.position = position
    
    def get_employee_info(self):
        return f"Employee: {self.name} (ID: {self.employee_id}, Position: {self.position})"


class Department:
    def __init__(self, name, department_id):
        self.name = name
        self.department_id = department_id
        self.employees = []  # List to store employee references
    
    def add_employee(self, employee):
        """Add an employee to the department"""
        self.employees.append(employee)
    
    def remove_employee(self, employee):
        """Remove an employee from the department"""
        if employee in self.employees:
            self.employees.remove(employee)
    
    def get_department_info(self):
        """Get department information including its employees"""
        info = f"Department: {self.name} (ID: {self.department_id})\n"
        info += "Employees in department:\n"
        for employee in self.employees:
            info += f"- {employee.get_employee_info()}\n"
        return info


# Example usage
if __name__ == "__main__":
    # Create employees
    emp1 = Employee("Ahmed Zia", "E016", "Software Engineer")
    emp2 = Employee("Saeed Abrar", "E036", "Project Manager")
    
    # Create department
    dept = Department("Engineering", "D001")
    
    # Add employees to department
    dept.add_employee(emp1)
    dept.add_employee(emp2)
    
    # Display department information
    print(dept.get_department_info())
    
    # Remove an employee
    dept.remove_employee(emp1)
    print("\nAfter removing an employee:")
    print(dept.get_department_info())
