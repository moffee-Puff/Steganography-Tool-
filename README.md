# Steganography Tool

A Python-based tool for hiding and extracting secret messages within image files using steganography. Built for Kali Linux, this tool allows you to embed text data into images and retrieve it without altering the visible appearance of the image.

---

## How It Works

Steganography is the practice of hiding information within another file, such as an image, without visibly altering it. This tool uses the **Least Significant Bit (LSB)** technique to embed and extract secret messages in PNG images.

### Key Features:
1. **Hide Text in an Image**:
   - The tool takes an input image and a secret message.
   - It encodes the message into the least significant bits of the image's pixel data.
   - The output is a new image that looks identical to the original but contains the hidden message.

2. **Extract Text from an Image**:
   - The tool reads the least significant bits of the image's pixel data.
   - It decodes the hidden message and displays it.

---

## How to Use

### Prerequisites
- Kali Linux (or any Linux distribution with Python 3).
- Python 3.x.
- The `Pillow` library (install using `pip`).

### Installation

1. **Install Required Libraries**:
   ```bash
   sudo apt update
   sudo apt install python3-pip
   pip3 install pillow

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/steganography-tool.git
   cd steganography-tool

3. **Run the Script**:
   ```bash
   python3 steganography.py

Usage
1. **Hide a Secret Message in an Image**
   ```bash
   python3 steganography.py

Choose the Hide option.

Enter the path to the input image (e.g., input.png).

Enter the secret message you want to hide.

Enter the output image name (e.g., output.png).

The tool will create a new image with the hidden message.

2. **Extract a Secret Message from an Image**: 
   ```bash
   python3 steganography.py

Choose the Extract option.

Enter the path to the steganographic image (e.g., output.png).

The tool will extract and display the hidden message.

Example Workflow
1. **Hide a Message**:
    ```bash
    $ python3 steganography.py
   Choose an option:
   1. Hide a message in an image
   2. Extract a message from an image
   Enter your choice (1 or 2): 1

   Enter the input image path: input.png
   Enter the secret message: This is a secret!
   Enter the output image name: output.png
   [*] Message hidden successfully in output.png

2. **Extract a Message**:
   ```bash
   $ python3 steganography.py
   Choose an option:
   1. Hide a message in an image
   2. Extract a message from an image
   Enter your choice (1 or 2): 2

   Enter the steganographic image path: output.png
   [*] Extracted message: This is a secret!
       
