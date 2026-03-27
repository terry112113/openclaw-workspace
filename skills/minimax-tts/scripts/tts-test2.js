const https = require('https');
const fs = require('fs');

const API_KEY = 'sk-cp-e_kZnDB6jUSF6tmnzHCzpQajNFsUN9nGyZdywv13Z8oCgS059F6u0k72-n_EFFLPMdwiUDeAqqciSjsmv5gEvTiR69RrcahlVBLc8Vyr5QW-2IL35zCGUiY';

function generateTTS(text, outputPath, voiceId, speed, pitch) {
    return new Promise((resolve, reject) => {
        const data = JSON.stringify({
            model: 'speech-2.8-hd',
            text: text,
            stream: false,
            voice_setting: {
                voice_id: voiceId,
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
                        resolve();
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

async function main() {
    const text = "寇可往，我亦可往！";
    const outputPath = "C:\\Users\\TL\\.openclaw\\tts-han4.mp3";
    
    // Try male_qn_jingying with slightly higher pitch for more dramatic effect
    await generateTTS(text, outputPath, 'male_qn_jingying', 0.85, 0);
    console.log('[TTS] Saved to:', outputPath);
}

main().catch(err => {
    console.error('[TTS] Error:', err.message);
    process.exit(1);
});
