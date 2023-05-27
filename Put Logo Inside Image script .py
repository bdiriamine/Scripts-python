from PIL import Image
import os

filename_Logo = input("Enter Logo with extension :")
folder_Name_NEW = input("Enter new Folder Name :")

logo_Img = Image.open(filename_Logo)
logo_width , logo_height = logo_Img.size
if not os.path.exists(folder_Name_NEW):
            os.mkdir(folder_Name_NEW)
for filname in os.listdir('.'):
    if not(filname.endswith('.png') or filname.endswith('.jpg') or filname == filename_Logo):
        continue
    img = Image.open(filname)
    width,height = img.size
    ## Add logo  to image 
    img.paste(logo_Img,(width -logo_width ,height-logo_height))
    img.save(os.path.join(folder_Name_NEW, filname))
    print("logo puted succesfuly",filname)
print("done")