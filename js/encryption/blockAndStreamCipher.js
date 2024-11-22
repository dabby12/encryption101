// blockAndStreamCipher.js

const crypto = require('crypto');

// AES as a block cipher
function aesEncrypt(text) {
  const key = crypto.randomBytes(32);
  const iv = crypto.randomBytes(16);
  const cipher = crypto.createCipheriv('aes-256-cbc', key, iv);
  let encrypted = cipher.update(text, 'utf8', 'hex');
  encrypted += cipher.final('hex');
  return { encrypted, key: key.toString('hex'), iv: iv.toString('hex') };
}

// RC4 as a stream cipher
function rc4Encrypt(text, key) {
  const cipher = crypto.createCipher('rc4', key);
  let encrypted = cipher.update(text, 'utf8', 'hex');
  encrypted += cipher.final('hex');
  return encrypted;
}

module.exports = { aesEncrypt, rc4Encrypt };
