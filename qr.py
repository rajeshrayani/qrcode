import qrcode
data="www.youtube.com"
qr=qrcode.QRCode(
     version = 5,
     box_size = 10,
     border  = 5,
)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color='green',back_color='white')
img.save('raj.png')
img.show()
