// asymmetricEncryption.js

const crypto = require('crypto');

// Generate a pair of keys (public and private)
const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', {
  modulusLength: 2048,
});

// Encrypt function
function encrypt(text) {
  const encrypted = crypto.publicEncrypt(
    publicKey,
    Buffer.from(text, 'utf8')
  );
  return encrypted.toString('hex');
}

// Decrypt function
function decrypt(encryptedText) {
  const decrypted = crypto.privateDecrypt(
    privateKey,
    Buffer.from(encryptedText, 'hex')
  );
  return decrypted.toString('utf8');
}

module.exports = { encrypt, decrypt };
