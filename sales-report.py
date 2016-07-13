"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""
#create an empty list to contain sales persons names
salespeople = []
#create an empty list to contain num of melons sold
melons_sold = []

#initiate access to txt doc with sales report info
f = open("sales-report.txt")
#per line within the sales report
for line in f:
    #strip away any \n or white space to the right of each line
    line = line.rstrip()
    #split each word in the line with a bar
    entries = line.split("|")
    #index 0 of the list, per line, is the sales persons name
    salesperson = entries[0]
    #index 2 of the list, per line is an integer of the num of melons sold
    melons = int(entries[2])

    #if the salesperson is already within the salespeople list
    if salesperson in salespeople:
        #position is the index at which each salesperson name is located
        position = salespeople.index(salesperson)
        #the number of melons sold is incremented within the melons sold list
        # per each salesperson as their name is encountered
        melons_sold[position] += melons
    #otherwise
    else:
        #if the salesperson name is not in the list, add it to their list
        salespeople.append(salesperson)
        #and add the number of melons sold to its own corresponding list
        melons_sold.append(melons)

#per index across the range and length of the salespeople list
for i in range(len(salespeople)):
    #print the salespersons name and number of melons sold total, for each
    print "{} sold {} melons".format(salespeople[i], melons_sold[i])
