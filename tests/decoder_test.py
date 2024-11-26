from BarcodeDecoder import BarcodeDecoder
from PIL import Image
from numpy import asarray
import os
import json

decoder = BarcodeDecoder()

jd = json.decoder.JSONDecoder()
f = open("data/data_markup.json")
dm = jd.decode(f.read())['_via_img_metadata']

for res in dm:
    file = dm[res]['filename']
    img = Image.open('data/'+file)
    if not dm[res]['regions']:
        continue
    dec_res = decoder.decode(asarray(img))
    if not dec_res:
        print(file, "not decoded")
        continue
    if dec_res.type != dm[res]['regions'][0]['region_attributes']['type']:
        print(file, "wrong result:", dec_res.type, "expected:", dm[res]['regions'][0]['region_attributes']['type'])
