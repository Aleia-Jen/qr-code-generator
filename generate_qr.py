import qrcode

def generate_qr(url, filename):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as {filename}")

if __name__ == "__main__":
    linkedin_url = "https://linkedin.com/in/jenkinsaleia"
    github_url = "https://github.com/Aleia-Jen"

    generate_qr(linkedin_url, "linkedin_qr.png")
    generate_qr(github_url, "github_qr.png")
