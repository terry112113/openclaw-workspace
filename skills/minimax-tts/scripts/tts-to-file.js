const https = require('https');
const fs = require('fs');
const path = require('path');

const API_KEY = 'sk-cp-e_kZnDB6jUSF6tmnzHCzpQajNFsUN9nGyZdywv13Z8oCgS059F6u0k72-n_EFFLPMdwiUDeAqqciSjsmv5gEvTiR69RrcahlVBLc8Vyr5QW-2IL35zCGUiY';

const VOICE_ID = 'audiobook_male_2';
const SPEED = 0.8;
const PITCH = -2;

function generateTTS(text, outputPath) {
    return new Promise((resolve, reject) => {
        const data = JSON.stringify({
            model: 'speech-2.8-hd',
            text: text,
            stream: false,
            voice_setting: {
                voice_id: VOICE_ID,
                speed: SPEED,
                vol: 1,
                pitch: PITCH
            },
            audio_setting: {
                sample_rate: 32000,
                bitrate: 128000,
                format: 'mp3',
                channel: 1
            }
        });

        const options = {
            hostname: 'api.minimaxi.com',
            path: '/v1/t2a_v2',
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${API_KEY}`,
                'Content-Length': Buffer.byteLength(data)
            }
        };

        const req = https.request(options, (res) => {
            let body = '';
            res.on('data', (chunk) => { body += chunk; });
            res.on('end', () => {
                try {
                    const json = JSON.parse(body);
                    if (json.data && json.data.audio) {
                        const audioBuffer = Buffer.from(json.data.audio, 'hex');
                        fs.writeFileSync(outputPath, audioBuffer);
                        resolve(outputPath);
                    } else {
                        reject(new Error(`API error: ${JSON.stringify(json)}`));
                    }
                } catch (e) {
                    reject(e);
                }
            });
        });

        req.on('error', reject);
        req.write(data);
        req.end();
    });
}

const text = process.argv.slice(2, -1).join(' ');
const outputPath = process.argv[process.argv.length - 1];

if (!text || !outputPath) {
    console.log('Usage: node tts-to-file.js "text" "/path/to/output.mp3"');
    process.exit(1);
}

generateTTS(text, outputPath)
    .then((path) => {
        console.log(`[TTS] Saved to: ${path}`);
        process.exit(0);
    })
    .catch((err) => {
        console.error('[TTS] Error:', err.message);
        process.exit(1);
    });
