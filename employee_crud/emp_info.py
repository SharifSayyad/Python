class Employee:
    def __init__(self,eid,enm,eag,eadr,esal,edeg):
        self.empId=eid,
        self.empName=enm,
        self.empAge=eag,
        self.empAddress=eadr,
        self.empSalary = esal,
        self.empDegignation=edeg

    def __str__(self):
        return f'\n {self.__dict__}'

    def __repr__(self):
        return str(self)
