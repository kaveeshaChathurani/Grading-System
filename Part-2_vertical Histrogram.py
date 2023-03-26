# I declare that my work contains no examples of misconduct, such as plagiarism, or concllusion.
 
# Any code taken from other sources is referenced within my code solution.

# Student ID: 20210267
 
# Date: 7/12/2021 




# Part 2 - Vertical Histogram (extension)
Progress = 0
Progress_module_trailer = 0
Module_retriever = 0
Exclude = 0




# Function
def pro(Pass_credit, Defer_credit, Fail_credit, Progress, Progress_module_trailer, Module_retriever, Exclude):
    if (Pass_credit == 120):

        print("Progress")
        
        
        return 1

    elif (Pass_credit == 100 and (Defer_credit == 20 or Fail_credit == 20)):
        print("Progress (module trailer)")
        

        
        return 2

    elif (Fail_credit < 80):
        print("Do not progress - module retriever")
        

       
        return 3

    elif (Fail_credit >= 80):
        print("Exclude")
       

        

        return 4


# Progress function

try:
    program = 0

    while program < 10:

        Pass_credit = int(input("Please enter your credit at pass: "))
        if Pass_credit in [20 * i for i in range(7)]:
            Defer_credit = int(input("Please enter your credit at defer:"))
            if Defer_credit in [20 * i for i in range(7)]:
                Fail_credit = int(input("Please enter your credit at fail:"))
                if Fail_credit in [20 * i for i in range(7)]:
                    if Pass_credit + Defer_credit + Fail_credit == 120:
                        word = pro(Pass_credit, Defer_credit, Fail_credit, Progress, Progress_module_trailer,
                                   Module_retriever, Exclude)

                        if (word == 1):
                            Progress += 1

                        elif (word == 2):
                            Progress_module_trailer += 1

                        elif (word == 3):
                            Module_retriever += 1

                        elif (word == 4):
                            Exclude += 1

                        print(" ")
                        print("Would you like to enter another set of data?")
                        yesq = input("Enter 'y' for yes or 'q' to quit and view results:")
                        print(" ")

                        if (yesq == "q"):
                            program = 11
                            print(" ")
                            print("------------------------------------------------------------------------")
                            print(" ")
                            print("Horizontal Histogram")
                            print(" ")
                            print("Progress", Progress, ":", end=" ")
                            for i in range(0, Progress):
                                print("*", end=" ")
                            print("")
                            print("Trailer", Progress_module_trailer, ":", end=" ")
                            for i in range(0, Progress_module_trailer):
                                print("*", end=" ")
                            print("")
                            print("Retriever", Module_retriever, ":", end=" ")
                            for i in range(0, Module_retriever):
                                print("*", end=" ")
                            print("")
                            print("Excluded", Exclude, ":", end=" ")
                            for i in range(0, Exclude):
                                print("*", end=" ")
                            print("")
                            print(" ")
                            print(Progress + Progress_module_trailer + Module_retriever + Exclude, "outcomes in total.")

                            print("------------------------------------------------------------------------")
                            print(" ")
                            print("Vertical Histogram")#https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops#:~:text=You%20can%20use,Improve%20this%20answer
                            print(" ")
                            print("Progress", Progress, "|", "Trailer", Progress_module_trailer, "|", "Retriever",
                                  Module_retriever, "|", "Excluded", Exclude)

                            for i in range(max(Progress, Progress_module_trailer, Module_retriever, Exclude)):
                                print("  {0}            {1}            {2}              {3} ".format(
                                    '*' if i < Progress else ' ',
                                    '*' if i < Progress_module_trailer else ' ',
                                    '*' if i < Module_retriever else ' ',
                                    '*' if i < Exclude else ' '
                                ))

                            print(Progress + Progress_module_trailer + Module_retriever + Exclude, "outcomes in total.")
                            print("------------------------------------------------------------------------")
                            print(" ")
                            

                        elif (yesq == "y"):
                          program = 1
                    else :
                        print("Total incorret")
                else:
                    print("Out of range")
            else:
                print("Out of range")
        else:
            print("Out of range")
   


except ValueError:
    print("Integer required")

except NameError:
    print("")


