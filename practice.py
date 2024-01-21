import sys
import csv

inputFile = sys.argv[1]
outputFile = sys.argv[2]
student = []

with open(inputFile, 'r') as file:
    
    output_file = open(sys.argv[2], 'w')
    writer = csv.writer(output_file)
    writer.writerow(['first', 'last', 'house'])
    output_file.close()
    
    for line in file:
        
        name1, name2, house = line.split(', ')
        student.append({'name1':name1, 'name2':name2, 'house':house})
        output_file = open(sys.argv[2], 'w')
        writer = csv.writer(output_file)
        writer.writerow(['first', 'last', 'house'])
        output_file.close()
