from PIL import Image
from pyzbar import pyzbar
from pylibdmtx.pylibdmtx import decode as dm_decode
#
# img = Image.open('data/qr_code.png')
# print(pyzbar.decode(img))
#
# img = Image.open('data/pdf417.png')
# print(pyzbar.decode(img))
#
# img = Image.open('data/mode2.png')
# print(pyzbar.decode(img))
#
# img = Image.open('data/datamatr.png')
# print(pyzbar.decode(img))

# img = Image.open('data/unusual_form.png')
# print(pyzbar.decode(img))

# img = Image.open('data/unusual_form_orig.png')
# print(pyzbar.decode(img))

# img = Image.open('data/proj.png')
# print(pyzbar.decode(img))

# img = Image.open('data/hard_one.png')
# print(pyzbar.decode(img))

# img = Image.open('data/light.png')
# print(pyzbar.decode(img))

# img = Image.open('data/cut.png')
# print(pyzbar.decode(img))

# img = Image.open('data/cut_qr.png')
# print(pyzbar.decode(img))

# img = Image.open('data/composite.png')
# print(pyzbar.decode(img))

# img = Image.open('data/composite1.png')
# print(pyzbar.decode(img))

# img = Image.open('data/multi.png')
# print(pyzbar.decode(img))

# img = Image.open('data/data_matrix.png')
# print(dm_decode(img))
# print(pyzbar.decode(img))

# img = Image.open('data/very_cut.png')
# print(pyzbar.decode(img))

# img = Image.open('data/black_on_black.png')
# print(pyzbar.decode(img))

img = Image.open('data/aztec_new.png')
print(pyzbar.decode(img))

# import os
# for f in os.listdir('data'):
#     if f.endswith('.png'):
#         img = Image.open('data/' + f)
#         print(f, pyzbar.decode(img))
