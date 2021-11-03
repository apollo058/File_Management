import glob
import zipfile
import os

video_name = 'video'

img_save_path = '/mnt/c/Users/apoll/Desktop/Google/python_test/test/' + video_name + '/'
os.chdir(img_save_path)

img_zip = zipfile.ZipFile(video_name + '.zip', 'w')

for(path, dir, files) in os.walk('.'):
    for file in files:
        if file.endswith('.jpg'):
            img_zip.write(os.path.join(path, file))
            os.remove(os.path.join(path, file))
            print("delete : " + os.path.join(path, file))
    if len(os.listdir(path)) == 0:
        os.rmdir(path)
img_zip.close()