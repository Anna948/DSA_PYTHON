class Customer:
    def __init__(self,id,name,place,phonenum,email,location):
        self.id=id
        self.name=name
        self.place=place
        self.phonenum=phonenum
        self.email=email
        self.location=location
        self.next=None
    def cus_info(self):
        print(f"id:{self.id} name:{self.name} place:{self.place} phonenum:{self.phonenum} email:{self.email} location:{self.location}")

customer = []
n=int(input("Enter the no of customers"))
for i in range(n):
    print("Enter details of customers")
    id=int(input("ID:"))
    name=input("Name:")
    place=input("place:")
    phonenum=int(input("phonenum:"))
    email=input("email:")
    location=input("location:")
    c=Customer(id ,name ,place ,phonenum ,email ,location)
    customer.append(c)

print("Customer details")
for c in customer:
    print(c.cus_info())