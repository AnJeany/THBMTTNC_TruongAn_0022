from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# ==================== HOME PAGE ====================
@app.route("/")
def home():
    return render_template('index.html')


# ==================== CAESAR CIPHER ====================
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    cipher = CaesarCipher()
    encrypted_text = cipher.encrypt_text(text, key)
    return render_template('result.html', cipher_name="Caesar", operation="Encryption", 
                           input_text=text, key=key, result_text=encrypted_text, return_url="/caesar")

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    cipher = CaesarCipher()
    decrypted_text = cipher.decrypt_text(text, key)
    return render_template('result.html', cipher_name="Caesar", operation="Decryption", 
                           input_text=text, key=key, result_text=decrypted_text, return_url="/caesar")


# ==================== VIGENERE CIPHER ====================
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    cipher = VigenereCipher()
    encrypted_text = cipher.vigenere_encrypt(text, key)
    return render_template('result.html', cipher_name="Vigenère", operation="Encryption", 
                           input_text=text, key=key, result_text=encrypted_text, return_url="/vigenere")

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    cipher = VigenereCipher()
    decrypted_text = cipher.vigenere_decrypt(text, key)
    return render_template('result.html', cipher_name="Vigenère", operation="Decryption", 
                           input_text=text, key=key, result_text=decrypted_text, return_url="/vigenere")


# ==================== RAIL FENCE CIPHER ====================
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    cipher = RailFenceCipher()
    encrypted_text = cipher.rail_fence_encrypt(text, key)
    return render_template('result.html', cipher_name="Rail Fence", operation="Encryption", 
                           input_text=text, key=key, result_text=encrypted_text, return_url="/railfence")

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    cipher = RailFenceCipher()
    decrypted_text = cipher.rail_fence_decrypt(text, key)
    return render_template('result.html', cipher_name="Rail Fence", operation="Decryption", 
                           input_text=text, key=key, result_text=decrypted_text, return_url="/railfence")


# ==================== PLAYFAIR CIPHER ====================
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    cipher = PlayFairCipher()
    matrix = cipher.create_playfair_matrix(key)
    encrypted_text = cipher.playfair_encrypt(text, matrix)
    return render_template('result.html', cipher_name="Playfair", operation="Encryption", 
                           input_text=text, key=key, result_text=encrypted_text, return_url="/playfair")

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    cipher = PlayFairCipher()
    matrix = cipher.create_playfair_matrix(key)
    decrypted_text = cipher.playfair_decrypt(text, matrix)
    return render_template('result.html', cipher_name="Playfair", operation="Decryption", 
                           input_text=text, key=key, result_text=decrypted_text, return_url="/playfair")


# ==================== TRANSPOSITION CIPHER ====================
@app.route("/transposition")
def transposition():
    return render_template('transposition.html')

@app.route("/transposition/encrypt", methods=['POST'])
def transposition_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    cipher = TranspositionCipher()
    encrypted_text = cipher.encrypt(text, key)
    return render_template('result.html', cipher_name="Transposition", operation="Encryption", 
                           input_text=text, key=key, result_text=encrypted_text, return_url="/transposition")

@app.route("/transposition/decrypt", methods=['POST'])
def transposition_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    cipher = TranspositionCipher()
    decrypted_text = cipher.decrypt(text, key)
    return render_template('result.html', cipher_name="Transposition", operation="Decryption", 
                           input_text=text, key=key, result_text=decrypted_text, return_url="/transposition")


# ==================== MAIN FUNCTION ====================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)