import os,sys
import codecs

# get the directory dynamically
path =  os.path.join(os.getcwd())
mylist = os.listdir(path)

for file in mylist:

  data = file.replace(".xml", "\n")
  data_modified = data.replace("_", " ")

  file = codecs.open("testfile.txt","+a","utf-8")
  # writing new line
  file.write(data_modified+"\n")
  file.close()



  
   