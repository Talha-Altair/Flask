from PIL import Image
   
import os

PATH = "D:/PROJECTS/static/uploads"
Copy_to_path="D:/PROJECTS/static/uploads"

for filename in os.listdir(PATH):
    img = Image.open(os.path.join(PATH, filename))
    img = img.resize((50,50), Image.ANTIALIAS)
    img.save(Copy_to_path+filename+'Thumb1.png')
    img = img.resize((80,60), Image.ANTIALIAS)
    img.save(Copy_to_path+filename+'Thumb2.png')

os.rename(Copy_to_path+filename+'Thumb1.png','Thumb1.png')
os.rename(Copy_to_path+filename+'Thumb2.png','Thumb2.png')


