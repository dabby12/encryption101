// index.js
const symmetric = require('./encryption/symmetricEncryption');
const asymmetric = require('./encryption/asymmetricEncryption');
const hash = require('./encryption/hashing');
const hybrid = require('./encryption/hybridEncryption');
const steg = require('./encryption/steganography');
const cipher = require('./encryption/blockAndStreamCipher');
const homo = require('./encryption/homomorphicEncryption');

// Example usage
const message = "Hello, World!";
console.log("Symmetric Encryption:", symmetric.encrypt(message));
console.log("Asymmetric Encryption:", asymmetric.encrypt(message));
console.log("SHA-256 Hash:", hash.hash(message));
console.log("MD5 Hash:", hash.hashMD5(message));
console.log("Hybrid Encryption:", hybrid.encrypt(message));
console.log("Steganography Encoded:", steg.encodeMessage("Carrier Text", "Hidden Message"));
console.log("AES Block Cipher Encryption:", cipher.aesEncrypt(message));
console.log("Homomorphic Encryption:", homo.encrypt(12345));
console.log('Current directory:', __dirname);
