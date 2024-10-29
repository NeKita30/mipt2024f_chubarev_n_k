from PIL import Image
from pyzxing import BarCodeReader


reader = BarCodeReader()
# print(reader.decode('data/qr_code.png'))
# print(reader.decode('data/pdf417.png'))
# print(reader.decode('data/mode2.png'))
# print(reader.decode('data/datamatr.png'))
# print(reader.decode('data/unusual_form.png'))
# print(reader.decode('data/unusual_form_orig.png'))
# print(reader.decode('data/proj.png'))
# print(reader.decode('data/hard_one.png'))
# print(reader.decode('data/light.png'))
# print(reader.decode('data/cut.png'))
# print(reader.decode('data/cut_qr.png'))
# print(reader.decode('data/composite.png'))
# print(reader.decode('data/composite1.png'))
# print(reader.decode('data/cut_cut.png'))
# print(reader.decode('data/multi_one.png'))

# print(results := reader.decode('data/multi.png'))
# img = Image.open('data/multi.png')
# for res in results:

from numpy import asarray
img = Image.open('data/very_cut.png')
numpydata = asarray(img)

print(reader.decode_array(numpydata))

