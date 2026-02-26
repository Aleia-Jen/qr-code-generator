QR Code Generator (Python)

This project demonstrates a simple Python-based QR code generator for creating scannable links for professional portfolio integration.

Purpose

The script converts URL inputs into QR code images for use in resumes, portfolios, or documentation. It was developed to generate LinkedIn and GitHub QR codes for professional use.

Features

The application accepts valid URLs and converts them into high-error-correction QR code images to improve scan reliability. Generated codes are exported as PNG image files.

Technologies Used

Python 3
qrcode library (with Pillow support)

Example Use Case

QR codes were generated for professional portfolio links, including LinkedIn and GitHub profiles.

How to Run

pip install qrcode[pil]
python generate_qr.py
