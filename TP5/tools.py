from Crypto.Cipher import AES
from random import randint
from binascii import a2b_base64


def gen_rand_data(length=16):
    """Generate a random string of the given length"""
    return ''.join(chr(randint(0, 255)) for i in range(length))


def pkcs_7_pad(data, final_len=None):
    """Apply the PKCS#7 padding to data"""
    if final_len is None:
        final_len = (len(data) / 16 + 1) * 16
    padding_len = final_len - len(data)
    return data + chr(padding_len) * padding_len


def pkcs_7_unpad(data):
    """Remove the PKCS#7 padding from data"""
    padding_len = ord(data[len(data) - 1])
    for i in range(len(data) - padding_len, len(data)):
        if ord(data[i]) != padding_len:
            return data
    return data[:-padding_len]


def AES_128_ECB_encrypt(data, key, pad=False):
    """Encrypt the string data using AES_ECB using the provided key. Setting pad to True apply the PKCS#7 padding before encrypting"""
    cipher = AES.new(key, AES.MODE_ECB)
    if pad:
        data = pkcs_7_pad(data)
    return cipher.encrypt(data)


def AES_128_ECB_decrypt(data, key, unpad=False):
    """Decrypt the string data using AES_ECB using the provided key. Setting unpad to True remove the PKCS#7 padding after decrypting"""
    cipher = AES.new(key, AES.MODE_ECB)
    decr = cipher.decrypt(data)
    if unpad:
        decr = pkcs_7_unpad(decr)
    return decr


def xor_data(A, B):
    """return the string resulting from the XOR between A and B"""
    return ''.join(chr(ord(A[i]) ^ ord(B[i])) for i in range(len(A)))


def AES_128_CBC_encrypt(data, key, iv):
    """Encrypt the string data using AES_CBC using the provided key and iv. Always apply PKCS#7 padding."""
    data = pkcs_7_pad(data)
    block_count = len(data) / 16
    encrypted_data = ''
    prev_block = iv
    for b in range(block_count):
        cur_block = data[b * 16:(b + 1) * 16]
        encrypted_block = AES_128_ECB_encrypt(xor_data(cur_block, prev_block), key)
        encrypted_data += encrypted_block
        prev_block = encrypted_block
    return encrypted_data


def AES_128_CBC_decrypt(data, key, iv):
    """Decrypt the string data using AES_CBC using the provided key and iv. Always remove PKCS#7 padding."""
    block_count = len(data) / 16
    decrypted_data = ''
    prev_block = iv
    for b in range(block_count):
        cur_block = data[b * 16:(b + 1) * 16]
        decrypted_block = AES_128_ECB_decrypt(cur_block, key)
        decrypted_data += xor_data(decrypted_block, prev_block)
        prev_block = cur_block
    return pkcs_7_unpad(decrypted_data)


def encryption_oracle_chall11(data):
    """Encryption oracle for the challenge 11.
    Append 5-10 bytes (count chosen randomly) before data and 5-10 bytes after data.
    Then encrypt it using a random key, and either AES_ECB or AES_CBC at random"""
    should_encrypt_using_CBC = (randint(0, 1) == 0)
    key = gen_rand_data()

    data = gen_rand_data(randint(5, 10)) + data + gen_rand_data(randint(5, 10))

    if should_encrypt_using_CBC:
        iv = gen_rand_data()
        return "CBC", AES_128_CBC_encrypt(data, key, iv)
    else:
        return "ECB", AES_128_ECB_encrypt(data, key, True)


ecbsecretkey_12 = gen_rand_data(16)


def ECB_oracle_chall12(data):
    """Encryption oracle for the challenge 12.
    Append the decoded string from the challenge after data.
    Then encrypt it using AES_ECB with a random fixed key.
    In short return AES-128-ECB(data || unknown-string, random-key)."""
    global ecbsecretkey_12
    data = data + a2b_base64(
        'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg'+
        'aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq'+
        'dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg'+
        'YnkK')
    return AES_128_ECB_encrypt(data, ecbsecretkey_12, True)


ecbsecretkey_14 = gen_rand_data(16)


def ECB_oracle_chall14(data):
    """Encryption oracle for the challenge 14.
    Append a random prefix before data and the decoded string from the challenge after data.
    Then encrypt it using AES_ECB with a random fixed key.
    In short, return AES-128-ECB(random-prefix || data || target-bytes, random-key)."""
    global ecbsecretkey_14
    data = gen_rand_data(randint(3, 255)) + data + a2b_base64(
        'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg'+
        'aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq'+
        'dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg'+
        'YnkK')
    return AES_128_ECB_encrypt(data, ecbsecretkey_14, True)


key_16 = gen_rand_data()
iv_16 = gen_rand_data()


def encryption_oracle_chall16(data):
    """Encryption oracle for the challenge 16 (first function).
    First replace each ';' character in data with '%3b', and each '=' with '%3d'.
    Then append the given prefix and suffix to data (see challenge), and encrypt it with AES_CBC with a random fixed key and iv"""
    data = data.replace(';', '%3b')
    data = data.replace('=', '%3d')
    data = "comment1=cooking%20MCs;userdata=" + data + ";comment2=%20like%20a%20pound%20of%20bacon"
    return AES_128_CBC_encrypt(data, key_16, iv_16)


def decryption_oracle_chall16(data):
    """Decryption oracle for the challenge 16 (second function).
    Decrypt data using the fixed key and iv and return true if the string ';admin=true;' appears in the decrypted data."""
    return (AES_128_CBC_decrypt(data, key_16, iv_16).count(';admin=true;') > 0)
