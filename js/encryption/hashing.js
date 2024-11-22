// hashing.js

const crypto = require('crypto');

// Hashing function using SHA-256
function hash(text) {
  return crypto.createHash('sha256').update(text).digest('hex');
}

// Hashing function using MD5 (not recommended for sensitive data)
function hashMD5(text) {
  return crypto.createHash('md5').update(text).digest('hex');
}

module.exports = { hash, hashMD5 };
console.log("Hashing true")