import os,sys
import codecs

path = 'C:\\Users\\KULSUM\\Desktop\\18-10-27-0826'
mylist = os.listdir(path)

for file in mylist:

  data = file.replace(".xml", "\n")
  data_modified = data.replace("_", " ")

  file = codecs.open("testfile.txt","+a","utf-8")
  file.write(data_modified)
  file.close()



  
   