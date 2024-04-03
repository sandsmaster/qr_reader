import segno

def get_qr(text):
    qr = segno.make_qr(text)
    qr.save("qr_codes/cool_qr.png")