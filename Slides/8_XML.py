import xml.etree.ElementTree as ET

data = '''<person>
   <name>Chuck</name>
   <phone type="intl">
      +1 734 303 4456
    </phone>
    <email hide="yes"/>
 </person>'''

# creating tree object for XML
tree = ET.fromstring(data)

# print name
print("Name : ",tree.find('name').text)
# print attributes
print("Attr : ", tree.find('email').get('hide'))
print("Attr : ", tree.find('phone').get('type'))
print("Phone : ", tree.find('phone').text)



# multiple complex elements
input = '''<stuff>
       <users>
           <user x="2">
               <id>001</id>
               <name>Chuck</name>
           </user>
           <user x="7">
               <id>009</id>
               <name>Brent</name>
           </user>
       </users>
   </stuff>'''

stuff = ET.fromstring(input)
users = stuff.findall('users/user')
print("Total users : ", len(users))
for item in users :
    print("Name : ", item.find("name").text)
    print("id : ", item.find("id").text)
    print("Attri : ", item.get('x'))