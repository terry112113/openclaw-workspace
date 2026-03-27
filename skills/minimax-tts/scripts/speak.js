const https = require('https');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

const API_KEY = 'sk-cp-e_kZnDB6jUSF6tmnzHCzpQajNFsUN9nGyZdywv13Z8oCgS059F6u0k72-n_EFFLPMdwiUDeAqqciSjsmv5gEvTiR69RrcahlVBLc8Vyr5QW-2IL35zCGUiY';
const CACHE_DIR = 'C:/Users/TL/.openclaw/tts-cache/';
const PLAY_SCRIPT = 'C:/Users/TL/.openclaw/play-audio.ps1';

const VOICE_ID = 'audiobook_male_2';
const SPEED = 0.8;
const PITCH = -2;

const CACHED_PHRASES = [
    '准奏', '朕心甚慰', '微臣遵旨', '善', '朕卿所言极是',
    '退下吧', '来人', '宣', '早朝', '有事启奏', '无事退朝'
];

function playCached(phrase) {
    return new Promise((resolve, reject) => {
        const cmd = `powershell -ExecutionPolicy Bypass -File "${PLAY_SCRIPT}" -phrase "${phrase}"`;
        exec(cmd, (err, stdout, stderr) => {
            if (err) reject(err);
            else resolve(stdout);
        });
    });
}

function generateTTS(text) {
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
                        resolve(audioBuffer);
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

function playAudioFile(filePath) {
    return new Promise((resolve, reject) => {
        const cmd = `powershell -ExecutionPolicy Bypass -File "${PLAY_SCRIPT}" -phrase "${path.basename(filePath, '.mp3')}"`;
        exec(cmd, (err, stdout, stderr) => {
            if (err) reject(err);
            else resolve(stdout);
        });
    });
}

function findCached(text) {
    for (const phrase of CACHED_PHRASES) {
        if (text.includes(phrase)) {
            const filePath = path.join(CACHE_DIR, `${phrase}.mp3`);
            if (fs.existsSync(filePath)) {
                return phrase;
            }
        }
    }
    return null;
}

async function speak(text) {
    // First, check if text contains any cached phrase
    const cached = findCached(text);
    if (cached) {
        console.log(`[TTS] Playing cached: ${cached}`);
        await playCached(cached);
        return;
    }

    // Otherwise, generate TTS
    console.log(`[TTS] Generating: ${text.substring(0, 50)}...`);
    const audioBuffer = await generateTTS(text);
    
    // Save to temp file
    const tempFile = path.join(CACHE_DIR, `temp_${Date.now()}.mp3`);
    fs.writeFileSync(tempFile, audioBuffer);
    
    // Play it
    const phrase = path.basename(tempFile, '.mp3').replace('temp_', '');
    await playAudioFile(tempFile);
    
    // Clean up temp file after a delay
    setTimeout(() => {
        try { fs.unlinkSync(tempFile); } catch (e) {}
    }, 5000);
}

// Main
const text = process.argv.slice(2).join(' ');
if (!text) {
    console.log('Usage: node speak.js "text to speak"');
    process.exit(1);
}

speak(text).then(() => {
    console.log('[TTS] Done');
    process.exit(0);
}).catch(err => {
    console.error('[TTS] Error:', err.message);
    process.exit(1);
});
