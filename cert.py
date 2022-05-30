import pandas as pd
import numpy as np
from PIL import Image, ImageFont, ImageDraw 
import os 


ticket = Image.open("Sample.png")
draw = ImageDraw.Draw(ticket)

font = ImageFont.truetype("arial", 50)
draw.text((1400, 575),"John Doe",(0,0,0),font=font,align='left')
draw.text((1250, 670),"Kampus Run",(0,0,0),font=font,align='left')


ticket.save("result.png")