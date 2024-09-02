from ecdsa import SigningKey, VerifyingKey, SECP256k1

# Tạo một khóa ký
signing_key = SigningKey.generate(curve=SECP256k1)
verifying_key = signing_key.get_verifying_key()

# Thông điệp cần ký
message = b"hello"

# Ký thông điệp
signature = signing_key.sign(message)

# Xác minh chữ ký
try:
    verifying_key.verify(signature, message)
    print("Chữ ký hợp lệ.")
except:
    print("Chữ ký không hợp lệ.")

# In thông tin để kiểm tra
print("Thông điệp:", message.decode())
print("Chữ ký:", signature.hex())
