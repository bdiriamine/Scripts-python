import os 
import shutil

current_dir = os.path.dirname(os.path.realpath(__file__))

print(current_dir)
for filname in os.listdir(current_dir):
    #organize images 
    if filname.endswith((".png","jpg","webp","svg","gif")):
        print(filname)
        if not os.path.exists("img"):
            os.mkdir('img')
        shutil.copy(filname, "img")
        os.remove(filname)
        print("done")
     #organize Codes 
    if filname.endswith((".py","css","html","ts")):
        print(filname)
        if not os.path.exists("Codes"):
            os.mkdir('Codes')
        shutil.copy(filname, "Codes")
        os.remove(filname)
        print("done")
     #organize documents 
    if filname.endswith((".rar","pdf","zip","ts","docx","scv","xls")):
        print(filname)
        if not os.path.exists("documents"):
            os.mkdir('documents')
        shutil.copy(filname, "documents")
        os.remove(filname)
        print("done")
    #organize Video 
    if filname.endswith((".mp4","webm")):
        print(filname)
        if not os.path.exists("Videos"):
            os.mkdir('Videos')
        shutil.copy(filname, "Videos")
        os.remove(filname)
        print("done")
        #organize music 
    if filname.endswith((".mp3")):
        print(filname)
        if not os.path.exists("music"):
            os.mkdir('music')
        shutil.copy(filname, "music")
        os.remove(filname)
        print("done")
        #organize Programmes 
    if filname.endswith((".exe")):
        print(filname)
        if not os.path.exists("Programmes"):
            os.mkdir('Programmes')
        shutil.copy(filname, "Programmes")
        os.remove(filname)
        print("done")