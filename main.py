import cv2
import re
import pyotp

# Load the QR code image
image = cv2.imread('download.png')
# Initialize the QR code detector
detector = cv2.QRCodeDetector()
# Detect and decode the QR code
val = detector.detectAndDecode(image)

def get_secret_key(uri):
    # Extract the secret key from the OTPAuth URI
    # Example uri = otpauth://totp/Stripe: quantum@stripe.com?secret=mtsnk5haka5j3pgpsz5f6wdj&issuer=Stripe
    match = re.search(r'secret=([^&]+)', uri)
    if match:
        secret_key = match.group(1)
        return secret_key
    else:
        raise ValueError("Secret key not found in the OTPAuth URI.")


# Get the secret key from the decoded QR code
key = get_secret_key(val[0])


# Initialize the TOTP object
totp = pyotp.TOTP(key)
# Generate the Google Authenticator code
google_code = totp.now()
print(google_code)
