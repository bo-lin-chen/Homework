# open the file
path = r"C:\Users\lin\Desktop\hw2_data.txt"
f = open(path, 'r')
# null hash
my_dict={}
# remove \n
line=f.read().splitlines()
# if key exist --> number + 1
# if not add key in hash and set 1
for i in range(0,len(line)):
    if line[i] not in my_dict:
        my_dict[line[i]]=1
    else:
        my_dict[line[i]]=my_dict[line[i]]+1
# show the result
dict_number=len(my_dict)
print("There are %s kinds of words." %dict_number)
print("Each word repeat times: ")
for j,k in my_dict.items():
    print("%s : %s" %(j,k))
