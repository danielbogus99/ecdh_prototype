from cryptography.hazmat.primitives.asymmetric import ec

# Step 1: Key generation
daniel_private_key = ec.generate_private_key(ec.SECP384R1())
yinon_private_key = ec.generate_private_key(ec.SECP384R1())

# Step 2: Public key exchange
daniel_public_key = daniel_private_key.public_key()
yinon_public_key = yinon_private_key.public_key()

# Step 3: Shared secret derivation
daniel_shared_secret = daniel_private_key.exchange(ec.ECDH(), yinon_public_key)
yinon_shared_secret = yinon_private_key.exchange(ec.ECDH(), daniel_public_key)

# Step 4: Output results
print("Daniel's Shared Secret:", daniel_shared_secret.hex())
print("Yinon's Shared Secret: ", yinon_shared_secret.hex())
print("Match:", daniel_shared_secret == yinon_shared_secret)
