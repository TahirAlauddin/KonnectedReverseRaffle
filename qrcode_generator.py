import qrcode

def create_qrcode(number, filename='qrcode.png'):
    # Convert the number to string as QR code data
    number_str = str(number)
    
    # Create a qr code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to qr code object
    qr.add_data(number_str)
    qr.make(fit=True)
    
    # Create an image from the qr code object
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image to a file
    img.save(filename)

# Example usage:
create_qrcode(15, 'qrcode.png')
