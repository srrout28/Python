stud=[['amit',89,98],['susmita',78,82],['ramit',90,95],['ayush',76,87],['banita',57,67],['khushi',54,87]]
res =[stud[i] for i in range(len(stud)) if(stud[i][1]+stud[i][2])/2>85]
print(res)
