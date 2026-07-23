'''
import heapq
class Patient:
    def __init__(self,id,name,disease,outorin,dept):
        self.id=id
        self.disease=disease
        set.outorin=outorin
        self.dept=dept

pts=[]
p1=Patient(1,'ann','cold','in','health')
p2=Patient(2,'annie','earinfection','in','ent')
p3=Patient(3,'anu','hypertension','in','cardiology')

heapq.heappush(pts,(2,p1))
heapq.heappush(pts,(3,p2))
heapq.heappush(pts,(1,p3))
'''


import heapq

class Patient:
    def __init__(self, id, name, disease, outorin, dept):
        self.id = id
        self.name = name
        self.disease = disease
        self.outorin = outorin
        self.dept = dept

pts = []
p1 = Patient(1, 'ann', 'cold', 'in', 'health')
p2 = Patient(2, 'annie', 'earinfection', 'in', 'ent')
p3 = Patient(3, 'anu', 'hypertension', 'in', 'cardiology')

heapq.heappush(pts, (2, p1.id, p1))
heapq.heappush(pts, (3, p2.id, p2))
heapq.heappush(pts, (1, p3.id, p3))

print("Patients in priority order:")
while pts:
    priority, _, patient = heapq.heappop(pts)
    print(f"Priority {priority}: id={patient.id} name={patient.name} "
          f"disease={patient.disease} status={patient.outorin} dept={patient.dept}")


