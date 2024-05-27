from django.db import models

# Create your models here.

class Login(models.Model):
    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Type=models.CharField(max_length=100)

class Department(models.Model):
    Dname=models.CharField(max_length=100)
    Phone=models.BigIntegerField()
    Email=models.CharField(max_length=100)


class Staff(models.Model):
    Sname = models.CharField(max_length=100)
    Phno = models.BigIntegerField()
    Email = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Dob = models.DateField()
    Designation=models.CharField(max_length=100)
    Photo = models.CharField(max_length=100)
    DEPARTMENT = models.ForeignKey(Department, on_delete=models.CASCADE)
    Post=models.CharField(max_length=100)
    Pin=models.IntegerField()
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)

class Ward(models.Model):
    Wname=models.CharField(max_length=100)
    Wnum= models.IntegerField()

class Wardmember(models.Model):
    Mname = models.CharField(max_length=100)
    Phno = models.BigIntegerField()
    Email = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Dob = models.DateField()
    Photo = models.CharField(max_length=100)
    WARD = models.ForeignKey(Ward, on_delete=models.CASCADE)
    Post=models.CharField(max_length=100)
    Designation=models.CharField(max_length=100)
    Pin=models.IntegerField()
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)


class User(models.Model):
    Uname = models.CharField(max_length=100)
    Phno = models.BigIntegerField()
    Email = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Dob = models.DateField()
    Photo = models.CharField(max_length=100)
    WARD = models.ForeignKey(Ward, on_delete=models.CASCADE)
    Post=models.CharField(max_length=100)
    Place=models.CharField(max_length=100)
    Hname=models.CharField(max_length=100)
    Pin=models.IntegerField()
    District=models.CharField(max_length=100)
    Sc=models.CharField(max_length=100)
    Idproof= models.CharField(max_length=100)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    Status=models.CharField(max_length=100)


class Certificate(models.Model):
    Category = models.CharField(max_length=100)
    Desc = models.CharField(max_length=100, db_column='Description')
    DEPARTMENT = models.ForeignKey(Department, on_delete=models.CASCADE)


class Birthregistration(models.Model):
    State = models.CharField(max_length=100)
    Dist = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Dob = models.DateField()
    Mother = models.CharField(max_length=100)
    Father = models.CharField(max_length=100)
    Hospital = models.CharField(max_length=100)
    Regno = models.IntegerField()
    Status = models.CharField(max_length=100)
    CERTIFICATE = models.ForeignKey(Certificate, on_delete=models.CASCADE)

class Birthcertificaterequest(models.Model):
    Date = models.DateField()
    Status = models.CharField(max_length=100)
    Bcertificate=models.CharField(max_length=100)
    BIRTH=models.ForeignKey(Birthregistration, on_delete=models.CASCADE)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)

class Deathregistration(models.Model):
    State = models.CharField(max_length=100)
    Dist = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Dod = models.DateField()
    Dob = models.DateField()
    Wife = models.CharField(max_length=100)
    Husband = models.CharField(max_length=100)
    Hospital = models.CharField(max_length=100)
    Regno = models.IntegerField()
    Status = models.CharField(max_length=100)
    CERTIFICATE = models.ForeignKey(Certificate, on_delete=models.CASCADE)

class Deathcertificaterequest(models.Model):
    Date = models.DateField()
    Status = models.CharField(max_length=100)
    Dcertificate=models.CharField(max_length=100)
    DEATH=models.ForeignKey(Deathregistration, on_delete=models.CASCADE)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)

class Scheme(models.Model):
    Scheme = models.CharField(max_length=100)
    Desc = models.CharField(max_length=100, db_column='Description')
    DEPARTMENT = models.ForeignKey(Department, on_delete=models.CASCADE)

class Jobcardrequest(models.Model):
    Date = models.DateField()
    Status = models.CharField(max_length=100)
    Rationcard = models.BigIntegerField()
    Head = models.CharField(max_length=100)
    Photo = models.CharField(max_length=300)
    Idproof = models.CharField(max_length=300)
    SCHEME=models.ForeignKey(Scheme, on_delete=models.CASCADE)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)

class Jobcard(models.Model):
    Validity = models.DateField()
    Cardno = models.CharField(max_length=25)
    Photo = models.CharField(max_length=100)
    Rationcard = models.BigIntegerField()
    Head = models.CharField(max_length=100)
    JOBCARDREQUEST = models.ForeignKey(Jobcardrequest, on_delete=models.CASCADE)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)


class Jobcardmembers(models.Model):
    Name=models.CharField(max_length=100)
    Gender=models.CharField(max_length=100)
    Photo=models.CharField(max_length=300)
    Age=models.IntegerField()
    Relation=models.CharField(max_length=100)
    Adharno=models.CharField(max_length=100)
    Bank=models.CharField(max_length=100)
    JOBCARD=models.ForeignKey(Jobcard, on_delete=models.CASCADE)


class Workrequest(models.Model):
    Date = models.DateField()
    Sdate = models.CharField(max_length=100, default='NA')
    Edate = models.CharField(max_length=100, default='NA')
    Status = models.CharField(max_length=100)
    Area=models.IntegerField()
    Taxreciept =models.CharField(max_length=300)
    JOBCARD=models.ForeignKey(Jobcard, on_delete=models.CASCADE)
    SCHEME = models.ForeignKey(Scheme, on_delete=models.CASCADE)




class EmployeemateReq(models.Model):
    Sslc = models.CharField(max_length=300)
    Email = models.CharField(max_length=300)
    Status=models.CharField(max_length=100)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    USER=models.ForeignKey(User, on_delete=models.CASCADE)
    JOBCARDMEMBERS = models.ForeignKey(Jobcardmembers, on_delete=models.CASCADE)
    # JOBCARD = models.ForeignKey(Jobcard, on_delete=models.CASCADE)


class Employee(models.Model):
    Date = models.DateField()
    Status = models.CharField(max_length=100)
    JOBCARDMEMBERS=models.ForeignKey(Jobcardmembers, on_delete=models.CASCADE)
    # SCHEME = models.ForeignKey(Scheme, on_delete=models.CASCADE)


class Employeemate(models.Model):
    Date= models.DateField()
    validity=models.DateField()
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    EMPLOYEEMATEREQ= models.ForeignKey(EmployeemateReq,on_delete=models.CASCADE)

class Attendance(models.Model):
    Date = models.DateField()
    Status = models.CharField(max_length=100)
    # Photo=models.CharField(max_length=100)
    # JOBCARD=models.ForeignKey(Jobcard, on_delete=models.CASCADE)
    EMPLOYEEMATE=models.ForeignKey(Employeemate, on_delete=models.CASCADE)
    # EMPLOYEE= models.ForeignKey(Employee, on_delete=models.CASCADE)
    JOBCARDMEMMBERS = models.ForeignKey(Jobcardmembers, on_delete=models.CASCADE)
    WORKREQUEST = models.ForeignKey(Workrequest, on_delete=models.CASCADE)



class Plan(models.Model):
    Plan = models.CharField(max_length=100)
    Desc=models.CharField(max_length=100, db_column='Description')
    Photo=models.CharField(max_length=100)


class Planrequest(models.Model):
    Sdate = models.DateField()
    Edate = models.DateField()
    Status = models.CharField(max_length=100)
    PLAN= models.ForeignKey(Plan, on_delete=models.CASCADE)
    MEMBER=models.ForeignKey(Wardmember, on_delete=models.CASCADE)



class PlanNotification(models.Model):
    title = models.CharField(max_length=100)
    Desc=models.CharField(max_length=100, db_column='Description')
    Date = models.DateField()
    PLANREQUEST= models.ForeignKey(Planrequest, on_delete=models.CASCADE)
    WARD = models.ForeignKey(Ward, on_delete=models.CASCADE)


class Notification(models.Model):
    title = models.CharField(max_length=100)
    Desc=models.CharField(max_length=100, db_column='Description')
    Date = models.DateField()
    WARD = models.ForeignKey(Ward, on_delete=models.CASCADE)

class Complaint(models.Model):
    Title = models.CharField(max_length=100)
    Desc=models.CharField(max_length=100, db_column='Description')
    Type = models.CharField(max_length=100)
    Reply= models.CharField(max_length=100)
    Phno = models.BigIntegerField()
    Email = models.CharField(max_length=100)
    Date = models.DateField()



class WorkAllocation(models.Model):
    Date = models.DateField()
    WORKREQUEST = models.ForeignKey(Workrequest, on_delete=models.CASCADE)
    JOBCARDMEMMBERS = models.ForeignKey(Jobcardmembers, on_delete=models.CASCADE)
    Status = models.CharField(max_length=100)


class Forwardedwrkrequest(models.Model):
    EMPLOYEEMATE=models.ForeignKey(Employeemate, on_delete=models.CASCADE)
    WORKREQUEST=models.ForeignKey(Workrequest, on_delete=models.CASCADE)


