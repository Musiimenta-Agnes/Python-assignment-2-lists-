#From this list, ['Sandra', 'Patricia', 'Phionah', 'Anitah'].

# a). Add the name Masha at the 4th position.
studen_list = ['Sandra','Patrica', 'Phionah', 'Anitah']
studen_list.insert(4, 'Masha')
print(studen_list)


# b). Update the name Phionah to Phionah Aladinah.

new_name = 'Phionah Aladinah'
index = 2
studen_list[index] = new_name
print(studen_list)


# c). Display the length of the students list. 
length = len(studen_list)
print(length)


# d). Print all the student names using a for loop.

for x in studen_list:
    print(x)



# 2. From the mark list [80,56,78,90].
# b). Calculate the total marks for the student marks variable and the answer should be 304.
marks = [80,56,78,90]
sum = 0
for x in marks:
    sum+=x
    print(sum)