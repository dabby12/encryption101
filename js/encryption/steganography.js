// steganography.js

const steganography = require('steganography');

// Encode hidden message
function encodeMessage(text, hiddenMessage) {
  const result = steganography.encode(text, hiddenMessage);
  return result;
}

// Decode hidden message
function decodeMessage(encodedText) {
  const hiddenMessage = steganography.decode(encodedText);
  return hiddenMessage;
}

module.exports = { encodeMessage, decodeMessage };
