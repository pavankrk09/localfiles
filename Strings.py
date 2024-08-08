# Problem : We have a string - A,B,D,E,E, F,G,H,IK,M, N, OO, PP, QQ, ZZ , X,Y,Z,9,4,3,1,5,6,7,8, 1.1.0.2

# Write logic to 
# 1. Sort in Ascending Order and Print
# 2. Sort in Descending Order and Print  
# 3. Extract Numbers only and Sort in Ascending Order and Print (Descending also)
# 4. Extract string only and Sort in Ascending Order and Print (Descending also)
# 5. Remove all duplicates and Sort ASC and Desc
# Remember these are 5 Separate Tasks and not 1. If you stuck in one start other But i need this let me know when you can complete same 

def main():
    String=["E","E","F","G","H","IK","M","N","OO","PP","QQ","ZZ","X","Y","Z","A","B","D","9","4","3","1","5","6","7","8","1.1","0.2"]
    #Sorting the list in Ascending order 
    String.sort()
    print(f"Printing the String in Sorted Order in Ascending Order: {String}")

    #sorting the list in Descending order
    String.sort(reverse=True)
    print(f"Printing the String in Sorted Order in Descending Order: {String}")

    #extracting numbers from the list
    #numbers=[int(i) for i in String if i.isdigit()]
    numbers=[float(i) if '.' in i else int(i) for i in String if i.replace('.','',1).isdigit()]
    #sorting numbers in ascending order
    numbers.sort()
    print(f"Extracting Numbers from the list and printing in Sorted order:{numbers}")
    
    #sorting numbers in descending order
    numbers.sort(reverse=True)
    print(f"Extracting Numbers from the list and printing in Sorted order(Descending):{numbers}")

    #removing duplicates
    remove_duplicates=list(set(String))
    remove_duplicates.sort()
    #printing in ascending order
    print(f" Removing duplicates from the list and displaying in sorted order: {remove_duplicates}")

    #printing in descending order
    remove_duplicates.sort(reverse=True)
    print(f" Removing duplicates from the list and displaying in sorted order(Descending order): {remove_duplicates}")


    #extracting the string
    String=[i for i in String if i.isalpha()]
    String.sort()

    #printing in sorted order
    print(f"After removing duplicates from the list and only Extracting the alpha charcter: {String}")

    #sorting in descending order
    String.sort(reverse=True)

    #printing in descending order
    print(f"After removing duplicates from the list and only Extracting the alpha charcter(descending): {String}")



if __name__=="__main__":
    main()