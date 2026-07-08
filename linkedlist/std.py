class Student:
    def __init__(self,roll_num,name,total):
        self.roll_num=roll_num
        self.name=name
        self.total=total
        self.next=None
    def std_info(self):
        print(f"Rollnum:{self.roll_num} name:{self.name} total {self.total}")
        
s1=Student(1,'Anna',543)
s2=Student(2,'Joe',543)
s3=Student(3,'Ann',543)
s4=Student(4,'Annie',543)
s5=Student(5,'Angie',543)
s1.next=s2
s2.next=s3
s3.next=s4
s4.next=s5
cur=s1
while cur:
    #print(cur.roll_num,cur.name,cur.total)
    cur.std_info()
    cur=cur.next
