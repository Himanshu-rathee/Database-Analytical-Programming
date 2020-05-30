import xml.etree.ElementTree as ET
import pandas as pd
import sys
import csv

# Part - 1
# function to import the xml file; pass file name with path as parameter
def importXMl(file) :
    tree = ET.parse(file)
    root = tree.getroot()
    return root

try:
    people = importXMl("./people.xml")
except ET.ParseError:
    print("Formatting error in XML file")
else:
    print("Other type of error {}" .format(sys.exc_info()[2]))

# Part - 2
#to get all child tags  of root & attributes
resident_s = people.findall("Resident")

for resident in range(1,len(resident_s),2):
    print(resident_s[resident].find('Name').text)
    print(resident_s[resident].find('EmailAddress').text)
    print(resident_s[resident].find('PhoneNumber').text)
    print(resident_s[resident].find('./Address/City').text)

# Part -3
import csv

# open a file for writing
Resident_data = open('people.csv', 'w')

# create the csv writer object
csvwriter = csv.writer(Resident_data)
resident_head = []
count = 0
for member in people.findall('Resident'):
    resident = []
    address_list = []
    if count == 0:
        name = member.find('Name').tag
        resident_head.append(name)
        PhoneNumber = member.find('PhoneNumber').tag
        resident_head.append(PhoneNumber)
        EmailAddress = member.find('EmailAddress').tag
        resident_head.append(EmailAddress)
        Address = member[3].tag
        resident_head.append(Address)
        csvwriter.writerow(resident_head)
    count = count + 1

    name = member.find('Name').text
    resident.append(name)
    PhoneNumber = member.find('PhoneNumber').text
    resident.append(PhoneNumber)
    EmailAddress = member.find('EmailAddress').text
    resident.append(EmailAddress)
    Address = member[3][0].text
    address_list.append(Address)
    City = member[3][1].text
    address_list.append(City)
    StateCode = member[3][2].text
    address_list.append(StateCode)
    PostalCode = member[3][3].text
    address_list.append(PostalCode)
    resident.append(address_list)
    csvwriter.writerow(resident)
Resident_data.close()

# extra-converting csv to df and getting values from it:
resident_df = pd.read_csv('./people.csv',index_col=0)
print(resident_df.head())
print(resident_df.loc[2,["Name","EmailAddress"]])

