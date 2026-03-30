// EdgeTTS direct wrapper for OpenClaw TTS
// Bypasses the broken provider registry
const { EdgeTTS } = require('C:/Users/TL/AppData/Roaming/npm/node_modules/openclaw/node_modules/node-edge-tts');
const path = require('path');
const fs = require('fs');
const crypto = require('crypto');

const VOICE = 'zh-CN-XiaoxiaoNeural';
const OUTPUT_FORMAT = 'audio-24khz-48kbitrate-mono-mp3';

async function generateTTS(text, outputPath) {
  const tts = new EdgeTTS({
    voice: VOICE,
    lang: 'zh-CN',
    outputFormat: OUTPUT_FORMAT,
    rate: '+0%',
    pitch: '-2Hz'
  });
  
  await tts.ttsPromise(text, outputPath);
  return outputPath;
}

// CLI interface
const text = process.argv[2] || '你好，这是狄仁杰的语音测试。';
const output = process.argv[3] || path.join(process.env.TEMP || 'C:\\Users\\TL\\AppData\\Local\\Temp', `tts_${crypto.randomBytes(4).toString('hex')}.mp3`);

generateTTS(text, output)
  .then(f => {
    console.log('OK:' + f);
    process.exit(0);
  })
  .catch(e => {
    console.error('ERROR:' + e.message);
    process.exit(1);
  });
