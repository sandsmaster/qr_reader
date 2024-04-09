import segno

def get_qr(text):
    qr = segno.make_qr(text)
    img_path = r'C:\Users\Vager\Desktop\Slavi_QR\qr_codes\Roskilde.png'
    qr.save(img_path)


qr_text = r'http://192.168.8.200:8000/Roskilde'	

get_qr(qr_text)