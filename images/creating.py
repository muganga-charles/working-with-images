#open a particular image from path
from PIL import Image
#forexample //img = Image.open('images/creating.png')
# an object of Image type is returned and stored in img variable)
try: 
    img  = Image.open(path) 
except IOError:
    pass