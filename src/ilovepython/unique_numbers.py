n = int(input("enter the number of ele: "))
elements_list: list[int] = []
for i in range(n):
    ele = int(input("enter element: "))
    elements_list.append(ele)

print("the list is", elements_list)

unique_elements = set(elements_list)
print("unique elements are", unique_elements)
