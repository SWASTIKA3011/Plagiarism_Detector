# this is file 1 which has to be checked 
file1 = open(r"/Users/swastika/Desktop/PFDS Project/Plagiarism_Detector.py/text1.txt")  

 # this is file 2 which has to compared to 
file2 = open(r"/Users/swastika/Desktop/PFDS Project/Plagiarism_Detector.py/text2.txt")

# no of lines that are copied 
sen=0 

# no of totals lines in file 
count=0 

#iterating  the file 2
for line1 in file2: 
    #converting strings in list of strings    
    data2=line1.split(".")   
    #iterating the file 1 
for line in file1:
    #converting strings in list of strings           
    data1=line.split(".")  
    #going sentence to sentence     
    for i in data1:  
        #no of total lines in comaring if the sentence is already  file         
        count=count+1          
        if i in data2: 
            #membership operator  in comaring if the sentence is already in  file         
            print("copied sentence is :" ,i) 
            sen=sen+1

#findingpercentage 
percet=(sen/count)*100 
print("percentage of plagiarism is :-> ",percet,"%")