from PIL import Image
import sys

# Function to hide a message in an image
def hide_message(image_path, message, output_path):
    try:
        # Open the image
        img = Image.open(image_path)
        pixels = img.load()

        # Convert message to binary
        binary_message = ''.join(format(ord(char), '08b') for char in message)
        message_length = len(binary_message)

        # Check if the message can fit in the image
        width, height = img.size
        if message_length > width * height * 3:
            print("[-] Error: Message too long to hide in the image.")
            return

        # Embed the message in the LSB of each pixel
        index = 0
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]

                # Modify the LSB of each color channel
                if index < message_length:
                    r = (r & ~1) | int(binary_message[index])
                    index += 1
                if index < message_length:
                    g = (g & ~1) | int(binary_message[index])
                    index += 1
                if index < message_length:
                    b = (b & ~1) | int(binary_message[index])
                    index += 1

                pixels[x, y] = (r, g, b)

        # Save the output image
        img.save(output_path)
        print(f"[*] Message hidden successfully in {output_path}")

    except Exception as e:
        print(f"[-] Error: {e}")

# Function to extract a message from an image
def extract_message(image_path):
    try:
        # Open the image
        img = Image.open(image_path)
        pixels = img.load()

        # Extract the LSBs from each pixel
        binary_message = ""
        width, height = img.size
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                binary_message += str(r & 1)
                binary_message += str(g & 1)
                binary_message += str(b & 1)

        # Convert binary to text
        message = ""
        for i in range(0, len(binary_message), 8):
            byte = binary_message[i:i+8]
            message += chr(int(byte, 2))
            if message.endswith("\x00"):  # Stop at null character (if used)
                break

        print(f"[*] Extracted message: {message.split('\\x00')[0]}")

    except Exception as e:
        print(f"[-] Error: {e}")

# Main function
def main():
    print("Steganography Tool")
    choice = input("Choose an option:\n1. Hide a message in an image\n2. Extract a message from an image\nEnter your choice (1 or 2): ")

    if choice == "1":
        image_path = input("Enter the input image path: ")
        message = input("Enter the secret message: ")
        output_path = input("Enter the output image name: ")
        hide_message(image_path, message, output_path)
    elif choice == "2":
        image_path = input("Enter the steganographic image path: ")
        extract_message(image_path)
    else:
        print("[-] Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
