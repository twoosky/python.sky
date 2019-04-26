#4
# reverse 이용
customer = ["Jane", "Mark", "Tom", "Amy", "Bob "]

def reverseList1(a):
    customer = a.reverse()
def reverseList2(b):
    temp = []
    for i in range(len(b), -1):
        temp.append(b[i])
    customer =  temp

reverseList1(customer)
print(customer)
reverseList2(customer)
print(customer)
