const https = require('https');
const fs = require('fs');

const API_KEY = 'sk-cp-e_kZnDB6jUSF6tmnzHCzpQajNFsUN9nGyZdywv13Z8oCgS059F6u0k72-n_EFFLPMdwiUDeAqqciSjsmv5gEvTiR69RrcahlVBLc8Vyr5QW-2IL35zCGUiY';

const VOICE_ID = 'dib扎';  // 帝王风格

function generateTTS(text, outputPath, voiceId = 'speech-2.8', speed = 0.85, pitch = -1) {
    return new Promise((resolve, reject) => {
        const data = JSON.stringify({
            model: voiceId,
            text: text,
            stream: false,
            voice_setting: {
                voice_id: VOICE_ID,
                speed: speed,
                vol: 1,
                pitch: pitch
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
    console.log('Usage: node tts-v2.js "text" "/path/to/output.mp3"');
    process.exit(1);
}

// Try speech-2 model instead of speech-2.8-hd for more natural variation
generateTTS(text, outputPath, 'speech-2', 0.85, -1)
    .then((p) => {
        console.log(`[TTS] Saved to: ${p} (speech-2 model)`);
        process.exit(0);
    })
    .catch((err) => {
        console.error('[TTS] Error:', err.message);
        process.exit(1);
    });
