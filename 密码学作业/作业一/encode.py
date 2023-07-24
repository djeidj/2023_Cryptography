import random
import analysis
def get_table():
    pre_image = [chr(x) for x in range(ord('a'), ord('z')+1)]
    image = [chr(x) for x in range(ord('a'), ord('z')+1)]
    random.seed()
    random.shuffle(image)

    table = {}
    for i in range(26):
        table[pre_image[i]] = image[i]
    
    return table

def get_cipher_text(plaintext):
    ciphertext = ''
    table = get_table()
    # analysis.print_dict(table)

    for i in plaintext:
        if i in table:
            ciphertext += table[i]
        else:
            ciphertext += i
    
    return ciphertext 

if __name__ == '__main__':
    plaintext = input('输入明文：')
    plaintext = plaintext.lower()
    ciphertext = get_cipher_text(plaintext)
    file = open('jj.txt','w+')
    file.write(ciphertext)
    file.close
    print(ciphertext)