// homomorphicEncryption.js

const paillier = require('paillier-bigint');

// Generate Paillier keys
const { publicKey, privateKey } = paillier.generateRandomKeysSync(512);

// Encrypt function
function encrypt(number) {
  return publicKey.encrypt(BigInt(number));
}

// Decrypt function
function decrypt(encryptedNumber) {
  return privateKey.decrypt(encryptedNumber).toString();
}

module.exports = { encrypt, decrypt };
