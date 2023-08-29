"""
liste içerisindeki verilerin index numaralarına göre 
tek ve çift olacak şekilde ayrı ayrı tekrardan listelenmesi örneği
"""


students = ["John", "Mark", "Venessa", "Mariam"]
  
A = []
B = []
    
for index,student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)
        
print("A listesi:", A) 
print("B listesi:", B)
  

