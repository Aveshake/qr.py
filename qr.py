import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=10
)

qr.add_data("https://www.google.com/search?q=logo&sca_esv=e92a91eafa47dfb8&sca_upv=1&udm=2&tbs=isz:l,itp:lineart&sxsrf=ADLYWIIqS36LsSxeAaN-hNiDNpfOv3DsMw:1719662031989&source=lnt&sa=X&ved=2ahUKEwjPqLOk4ICHAxVrxDgGHVABAQYQpwV6BAgCECc&biw=1366&bih=617&dpr=1#vhid=5QvIIT6XmpqIJM&vssid=mosaic")
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="white")
img.save("qrcode.png")
