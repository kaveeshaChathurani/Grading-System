# I declare that my work contains no examples of misconduct, such as plagiarism, or concllusion.
 
# Any code taken from other sources is referenced within my code solution.

# Student ID: 20210267
 
# Date: 7/12/2021 


#Part 1 - Main Version 

Progress = 0
Progress_module_trailer = 0
module_retriever = 0
Exclude = 0

version = int(input("Student or Staff  - "))
print("   ")
#  Student version
if (version == 1):
    Progress = 0
    Progress_module_trailer = 0
    module_retriever = 0
    Exclude = 0


    def progression(pass_credit, defer_credit, fail_credit):

        if (pass_credit == 120):
            print("Progress")

        elif (pass_credit == 100 and (defer_credit == 20 or fail_credit == 20)):
            print("Progress (module trailer)")

        elif (fail_credit < 80):
            print("Do not progress – module retriever")

        elif (fail_credit > 60):
            print("Exclude")


    try:
        pass_credit = int(input("Enter your credits at pass:"))
        if pass_credit in [20 * i for i in range(7)]:
            defer_credit = int(input("Enter your credits at defer:"))
            if defer_credit in [20 * i for i in range(7)]:
                fail_credit = int(input("Enter your credits at fail:"))
                if fail_credit in [20 * i for i in range(7)]:
                    if pass_credit + defer_credit + fail_credit == 120:
                        num = progression(pass_credit, defer_credit, fail_credit)
                    else:
                        print("Total incorrect")
                else:
                    print("Out Of range")
            else:
                print("Out of range")
        else:
            print("Out of range")

    except ValueError:
        print("Integer required")
    except NameError:
        print("")
# Staff version
elif (version == 2):

    Progress = 0
    Progress_module_trailer = 0
    module_retriever = 0
    Exclude = 0


    def progression(pass_credit, defer_credit, fail_credit, Progress, Progress_module_trailer, module_retriever,
                    Exclude):

        if (pass_credit == 120):
            print("Progress")

            return 1

        elif (pass_credit == 100 and (defer_credit == 20 or fail_credit == 20)):
            print("Progress (module trailer)")

            return 2

        elif (fail_credit < 80):
            print("Module retriever")

            return 3

        elif (fail_credit > 60):
            print("Exclude")

            return 4


    try:
        program = 0
        while program < 5:

            pass_credit = int(input("Enter your credits at pass:"))
            if pass_credit in [20 * i for i in range(7)]:
                defer_credit = int(input("Enter your credits at defer:"))
                if defer_credit in [20 * i for i in range(7)]:
                    fail_credit = int(input("Enter your credits at fail:"))
                    if fail_credit in [20 * i for i in range(7)]:
                        if pass_credit + defer_credit + fail_credit == 120:
                            word = progression(pass_credit, defer_credit, fail_credit, Progress,
                                               Progress_module_trailer, module_retriever, Exclude)
                            if (word == 1):
                                Progress += 1

                            elif (word == 2):
                                Progress_module_trailer += 1

                            elif (word == 3):
                                module_retriever += 1

                            elif (word == 4):
                                Exclude += 1

                            print("  ")
                            print("Would you like to enter another set of data?")
                            yesq = input("Enter 'y' for yes or 'q' to quit and view results: ")
                            print("  ")

                            if (yesq == "q"):
                                program = 10
                                print("------------------------")
                                print("Horizontal Histogram")#https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops#:~:text=You%20can%20use,Improve%20this%20answer
                                print("Progress ", Progress, " :", end=" ")
                                for i in range(0, Progress):
                                    print("*", end=" ")
                                print("")
                                print("Trailer  ", Progress_module_trailer, " :", end=" ")
                                for i in range(0, Progress_module_trailer):
                                    print("*", end=" ")
                                print("")
                                print("Retriever", module_retriever, " :", end=" ")
                                for i in range(0, module_retriever):
                                    print("*", end=" ")
                                print("")
                                print("Excluded ", Exclude, " :", end=" ")
                                for i in range(0, Exclude):
                                    print("*", end=" ")
                                print("")
                                print("     ")
                                print(Progress + Progress_module_trailer + module_retriever + Exclude,
                                      "outcomes in total.")
                                print("  ")

                                print("------------------------")



                            elif (yesq == "y"):
                                program = 0

                        else:
                            print("Total incorrect")
                    else:
                        print("Out Of range")
                else:
                    print("Out of range")
            else:
                print("Out of range")

    except ValueError:
        print("Integer required")

    except NameError:
        print("")
else:

    print("Only enter '1' or '2' ")
