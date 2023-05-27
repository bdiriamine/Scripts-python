from PIL import Image
import os 

fit_size = int(input('entre size : '))
output_folder = input('entre output folder :')
if not os.path.exists(output_folder):
            os.mkdir(output_folder)
for filename in os.listdir('.'):
        if not filename.endswith((".png","jpg")):
                continue
        ## open image __ get image size ___resize
        image = Image.open(filename)
        width, height =image.size
        if width > fit_size and height > fit_size:
                if width > height:
                    height = int (( fit_size /width ) * height)
                    width = fit_size  
                else:
                    width = int (( fit_size /height  ) * width)
                    height  = fit_size  

                image = image.resize((width, height))
        image=image.save(os.path.join(output_folder,filename) )
        print('Resize success %s'%(filename))        
print("Fineshed")