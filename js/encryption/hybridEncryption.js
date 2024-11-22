// hybridEncryption.js

const crypto = require('crypto');

// Generate RSA keys
const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', {
  modulusLength: 2048,
});

// Symmetric encryption with AES
const algorithm = 'aes-256-cbc';
const key = crypto.randomBytes(32);
const iv = crypto.randomBytes(16);

// Encrypt function
function encrypt(text) {
  // Symmetrically encrypt the message
  const cipher = crypto.createCipheriv(algorithm, key, iv);
  let encryptedMessage = cipher.update(text, 'utf8', 'hex');
  encryptedMessage += cipher.final('hex');

  // Asymmetrically encrypt the AES key
  const encryptedKey = crypto.publicEncrypt(publicKey, key);

  return {
    encryptedMessage,
    encryptedKey: encryptedKey.toString('hex'),
    iv: iv.toString('hex'),
  };
}

// Decrypt function
function decrypt(encryptedMessage, encryptedKeyHex, ivHex) {
  const iv = Buffer.from(ivHex, 'hex');
  const encryptedKey = Buffer.from(encryptedKeyHex, 'hex');

  // Asymmetrically decrypt the AES key
  const key = crypto.privateDecrypt(privateKey, encryptedKey);

  // Symmetrically decrypt the message
  const decipher = crypto.createDecipheriv(algorithm, key, iv);
  let decrypted = decipher.update(encryptedMessage, 'hex', 'utf8');
  decrypted += decipher.final('utf8');

  return decrypted;
}

module.exports = { encrypt, decrypt };
