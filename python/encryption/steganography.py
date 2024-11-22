# steganography.py

from PIL import Image

# Simple steganography - hiding text in the least significant bits of an image
def encode_message(input_image_path, output_image_path, message):
    image = Image.open(input_image_path)
    binary_message = ''.join([format(ord(char), '08b') for char in message])
    data_index = 0

    for x in range(image.width):
        for y in range(image.height):
            pixel = list(image.getpixel((x, y)))
            for n in range(3):
                if data_index < len(binary_message):
                    pixel[n] = int(format(pixel[n], '08b')[:-1] + binary_message[data_index], 2)
                    data_index += 1
            image.putpixel((x, y), tuple(pixel))
    
    image.save(output_image_path)

def decode_message(image_path):
    image = Image.open(image_path)
    binary_message = ''
    
    for x in range(image.width):
        for y in range(image.height):
            pixel = list(image.getpixel((x, y)))
            for n in range(3):
                binary_message += format(pixel[n], '08b')[-1]

    # Convert binary string to text
    decoded_chars = [chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8)]
    return ''.join(decoded_chars).rstrip('\x00')

if __name__ == "__main__":
    encode_message('input.png', 'output.png', 'Secret Message!')
    print(decode_message('output.png'))
    