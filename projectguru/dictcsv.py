import csv
with open("Image/Emissions.csv") as file:
    # create a list of lists
    lis = [line.split() for line in file]
    # print the list items
    for i, x in enumerate(lis):
        print ("line{0} = {1}".format(i, x))


