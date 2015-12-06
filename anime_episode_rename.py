import os ,  time, sys


def rename_files(dir, anime_name, extention):
	files_list = os.listdir(dir)
	os.chdir(dir)
	new_file_name  = 1
	files_date_creation = []
	file_date_created =""
	for old_file_name in files_list :
		print old_file_name
		file_date_created = time.ctime(os.path.getctime(old_file_name))
		files_date_creation.append(file_date_created +"-" +old_file_name)
		print "last modified: %s" % time.ctime(os.path.getmtime(old_file_name))
		print "created: %s" % time.ctime(os.path.getctime(old_file_name))
		print

		
	files_date_creation.sort()
	for filee in files_date_creation:
		file_name = filee.split("-")[1]
		for old_file_name in files_list:
			if old_file_name == file_name :
				os.rename(old_file_name,anime_name + str(new_file_name)+'.'+ extention)
				print old_file_name + '-->' + str(new_file_name)
				new_file_name +=1
		print filee
		print

def main ():
	data_dir = sys.argv[1]
	anime_name = sys.argv[2]
	extention = sys.argv[3]
	rename_files(data_dir, anime_name, extention)



if __name__ == "__main__" :
	main()
