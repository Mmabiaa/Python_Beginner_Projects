import qrcode

def Main():
    data = input("Enter a URL or text: ").strip().lower()
    filename = input('Enter the filename: ').strip()

    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)

    image = qr.make_image(fill_color='black', back_color = 'white')
    image.save(filename)

    print(f"QR code saved as {filename}")
Main()
# Author - Mmabiaa
