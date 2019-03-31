# Import QRCode from pyqrcode 
import pyqrcode 


# String which represent the QR code 
s = input("enter url for QRCode")

# Generate QR code 
url = pyqrcode.create(s) 

# Create and save the png file naming "myqr.png" 
url.svg("myqr.svg", scale = 8) 