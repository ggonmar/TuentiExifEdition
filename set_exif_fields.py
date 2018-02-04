import os
import piexif
from shutil import copyfile
#os.system("cls");

exifField={ 'dateTaken':['Exif',36867], 
			'dateDigitalized':['Exif',36868],
			'datetime':['0th',306], 
			'userComment':['Exif',37510], 
			'origin':['Exif',37500]}


	
def setNewExif(path, date, comment):
 	try:
	#	For debugging purposes, do the change on a copy of the file
	#	copyfile(path, path + "_(modified).jpg")
	#	path=path + "_(modified).jpg"

		exif_dict = piexif.load(path)
		exif_dict.pop("thumbnail")

		exif_dict=editExif(exif_dict, exifField['dateTaken'],date)
		exif_dict=editExif(exif_dict, exifField['dateDigitalized'],date)
		exif_dict=editExif(exif_dict, exifField['datetime'],date)
		exif_dict=editExif(exif_dict, exifField['userComment'],comment)
		exif_dict=editExif(exif_dict, exifField['origin'],"Tuenti")
		
		exif_bytes=piexif.dump(exif_dict)
		piexif.insert(exif_bytes, path)
	except:
		print "Error changing file though correct date format"
		

	
	


def get_all_fields(path):

	exif_dict = piexif.load(path)
	exif_dict.pop("thumbnail")
	for ifd_name in exif_dict:
		print("\n{0} IFD:".format(ifd_name))
		for key in exif_dict[ifd_name]:
			try:
				print(key, exif_dict[ifd_name][key][:10])
			except:
				print(key, exif_dict[ifd_name][key])


def get_field(path, key1, key2):
	exif_dict = piexif.load(path)
	try:
		return exif_dict[key1][key2]
	except:
		return "Value for "+ key1 + "-" + key2 + " not found"

				
def editExif(exif_dict, key, value):
	exif_dict[key[0]][key[1]]=value
	return exif_dict
	
	
def repeat_to_length(string_to_expand, length):
   return (string_to_expand * ((length/len(string_to_expand))+1))[:length]