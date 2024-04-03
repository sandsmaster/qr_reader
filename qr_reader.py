from qreader import QReader
from cv2 import QRCodeDetector, imread
from pyzbar.pyzbar import decode

qreader_reader= QReader()
    
def read_qr(img_path):
    img = imread(img_path)

    qreader_out = qreader_reader.detect_and_decode(image=img)
    print(f"{qreader_out[0]}")