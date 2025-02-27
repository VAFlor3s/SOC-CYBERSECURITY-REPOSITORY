from PIL import Image
import io
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes



    
def image_to_bytes(img_path):
    with open(img_path,'rb') as image:
        return image.read()
    
def encrypt_image(image_bytes, key):
    iv= get_random_bytes(16)
    cipher= AES.new(key, AES.MODE_CBC, iv)
    padded_data= pad(image_bytes,AES.block_size)
    encrypt_data= cipher.encrypt(padded_data)
    return iv+encrypt_data

def decrypt_image(encrypt_data, key):
    iv= encrypt_data[:16]
    encrypt_bytes= encrypt_data[16:]
    cipher= AES.new(key, AES.MODE_CBC, iv)
    decrypt_data= unpad(cipher.decrypt(encrypt_bytes), AES.block_size)
    return decrypt_data

def save_enc_img(encrypt_data, output_path):
    with open(output_path,'wb') as file:
        file.write(encrypt_data)


def save_dec_img(decrypt_data, output_path):
    img= Image.open(io.BytesIO(decrypt_data))
    img.save(output_path,format='PNG')

key= get_random_bytes(16)
image_path ="C:\\Users\\Usuario\\Downloads\\info.png"
encryp_img_path= "C:\\Users\\Usuario\\Downloads\\cifrada.bin"
decryp_img_path= "C:\\Users\\Usuario\\Downloads\\descifrada.png"

first= image_to_bytes(image_path)
encrypt= encrypt_image(first,key)
save = save_enc_img(encrypt, encryp_img_path)
decrypt = decrypt_image(encrypt,key)
save_dec= save_dec_img(decrypt,decryp_img_path)


