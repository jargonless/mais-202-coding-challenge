import csv
import matplotlib.pyplot as plt

purposes = []
avg_rate = []

with open('data.csv','r',newline='') as csv_file:
    dataSet_reader = csv.DictReader(csv_file)

    for row in dataSet_reader:
        if len(purposes) == 0:
            purposes.append(row['purpose'])
            
        else:
            if row['purpose'] not in purposes:
                purposes.append(row['purpose'])

with open('data.csv','r',newline='') as file:
    reader = csv.DictReader(file)
    
    for i in range(len(purposes)):
        current_purpose = purposes[i]
        rate = 0
        counter = 0
        file.seek(0)
        
        for row in reader:
            if current_purpose == str(row['purpose']):
                rate += float(row['int_rate'])
                counter +=1
                
        if counter != 0:
            avg_rate.append((rate/float(counter)))
                
with open('output.csv','w',newline='') as output_file:
    fieldnames = [' ', 'purpose', 'avg_rate']
    output_writer = csv.DictWriter(output_file, fieldnames=fieldnames,delimiter=',')
    output_writer.writeheader()
        
    for i in range(len(purposes)):
        output_writer.writerow({' ':i, 'purpose':purposes[i], 'avg_rate':avg_rate[i]})

with open('output.csv','r',newline='') as output:
    output_reader = csv.reader(output)
    for line in output_reader:
        print(line)

x = []
y = []

x = purposes
y = avg_rate
plt.bar(x,y,label='Avg_rate')

plt.xlabel('purpose')
plt.ylabel('Average int_rate')
plt.title('Bart charts of average rate corresponding to loan purpose')
plt.legend()
plt.show()
   
input("Press ENTER to quit")
