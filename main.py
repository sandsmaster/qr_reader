import segno

qr = segno.make_qr(r'https://www.youtube.com/watch?v=jIQ6UV2onyI')
qr.save("qr_codes/cool_qr.png")