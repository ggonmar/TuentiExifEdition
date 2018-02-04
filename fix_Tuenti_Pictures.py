from datetime import datetime
import os
import set_exif_fields
import logging
from datetime import datetime
from datetime import timedelta

os.system("cls");

path="C:\Users\Fotos_Tuenti"

extension="*.jpg"

success=0
fail=0
for root, dirs, files in os.walk(path):
    for name in files:
		dDateTaken=""
		
		if name.endswith(".jpg"):
			print "File Found: " + name
			sDateTaken=name[0:19]		
			try:
				dDateTaken = datetime.strptime(sDateTaken, '%Y-%m-%d %H-%M-%S')		
				sExifDate = dDateTaken.strftime('%Y:%m:%d %H:%M:%S')
				comment= root.rsplit("\\",1).pop()
				
				print "\tFile accepted. Proceeding..."
				print "\tDate to input: " + sExifDate	
				#print "\tComment to include:\t" + comment
				set_exif_fields.setNewExif(root + "\\" + name, sExifDate, comment)
				success+=1
				
				f= open("success.txt","a")
				f.write(str(success) + ".- File " + name + " successfully modified\n" )
				f.close()
				
			except:
				print "\tFile with no date in name. Debug mode.."
				fail+=1
				f= open("errors.txt","a")
				f.write(str(fail) +".- Error encountered with file " + name+ "\n" )
				f.close()
				pass

			print ""

text="Successfully changed: " + str(success)
print text

f= open("success.txt", "a")
f.write(set_exif_fields.repeat_to_length("-",len(text))+"\n")
f.write(text)
f.close()
text="Files with problems: " + str(fail)
print text
f= open("errors.txt","a")
f.write(set_exif_fields.repeat_to_length("-",len(text))+"\n")
f.write(text)
f.close()
