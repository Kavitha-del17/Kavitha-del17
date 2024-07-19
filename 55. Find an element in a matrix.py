test_file =[[4,5,6],
            [8,9,3],
            [7,1,2]]
print("The orginal list :"+ str(test_list))
res= any(7 in sub for sub in test_list)
print("Is 7 present in matrix ?:"+ str(res))
            
