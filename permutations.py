def permutations(input_list):
    if len(input_list) == 0:
        return [[]]
    else:
        moving_element = input_list[0]
        mega_arr = []
        permutated_list = permutations(input_list[1:])
        for list_index in range(len(permutated_list)):
            for list_element_index in range(len(permutated_list[list_index])):
                mega_arr.append(permutated_list[list_index][:list_element_index]+[moving_element]+permutated_list[list_index][list_element_index:])
            mega_arr.append(permutated_list[list_index]+[moving_element])
            mega_arr.append(permutated_list[list_index])
        return mega_arr

out_file = open("permutation_out.txt",'w')
out_arr = permutations("A B C".split())
print(len(out_arr))
out_file.write(str(out_arr))

#
# def permutations(input_list):
#     #print(input_list)
#     if len(input_list) == 1:
#         return [[input_list[0]],[]]
#     else:
#         moving_element = input_list[0]
#         mega_arr = []
#         permutated_list = permutations(input_list[1:])
#         for list_index in range(len(permutated_list)):
#             for list_element_index in range(len(permutated_list[list_index])):
#                 mega_arr.append(permutated_list[list_index][:list_element_index]+[moving_element]+permutated_list[list_index][list_element_index:])
#             mega_arr.append(permutated_list[list_index]+[moving_element])
        
#         for list_index in range(len(permutated_list)):
#             for list_element_index in range(len(permutated_list[list_index])):
#                 mega_arr.append(permutated_list[list_index][:list_element_index]+[]+permutated_list[list_index][list_element_index:])
#             mega_arr.append(permutated_list[list_index]+[])

#         return removeDuplicates(mega_arr)
#         return mega_arr

# def removeDuplicates(input_list):
#     if len(input_list) == 1:
#         return
#     list_index = 0
#     while list_index < len(input_list):
#         control_list = input_list[list_index]
#         list_index2 = list_index + 1
#         while list_index2 < len(input_list):
#             if len(control_list) == len(input_list[list_index2]):
#                 element_index = 0
#                 duplicate_flag = True
#                 while element_index < len(control_list):
#                     if control_list[element_index] != input_list[list_index2][element_index]:
#                         duplicate_flag = False
#                         break
#                     element_index += 1
#                 if duplicate_flag:
#                     del input_list[list_index2]
#             list_index2+=1
#         list_index+=1
#     return input_list