from qreader import QReader
from cv2 import QRCodeDetector, imread
from pyzbar.pyzbar import decode

qreader_reader= QReader()

for img_path in (r'C:\Users\Vager\Desktop\Slavi_QR\qr_codes\cool_qr.png',):
    # Read the image
    img = imread(img_path)

    qreader_out = qreader_reader.detect_and_decode(image=img)
    print(f"{qreader_out[0]}")
