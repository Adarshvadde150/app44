import io
from PIL import Image
import base64
from .db import Db,Account
accounts=Account()
database=Db()
def image_object(myfile):
    image1 = Image.open(myfile)
    image2 = io.BytesIO()
    image1.save(image2, format="png")
    image2 = base64.b64encode(image2.getvalue()).decode("utf-8")
    return image2
def image_object1(myfile):
    image1 = Image.open(myfile)
    image2 = io.BytesIO()
    image1.save(image2, format="png")
    image2 = base64.b64encode(image2.getvalue()).decode("utf-8")
    return image2
def alldata(all):
    id=all['id']
    name=all['name']
    bod=all['bod']
    address=all['address']
    email=all['email']
    number=all['number']
    return id,name,bod,address,email,number


                
