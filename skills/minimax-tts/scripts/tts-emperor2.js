const https = require('https');
const fs = require('fs');
const { execSync } = require('child_process');

const API_KEY = 'sk-cp-e_kZnDB6jUSF6tmnzHCzpQajNFsUN9nGyZdywv13Z8oCgS059F6u0k72-n_EFFLPMdwiUDeAqqciSjsmv5gEvTiR69RrcahlVBLc8Vyr5QW-2IL35zCGUiY';

function generateTTS(text, voiceId, speed, pitch) {
    return new Promise((resolve, reject) => {
        const data = JSON.stringify({
            model: 'speech-2.8-hd',
            text: text,
            stream: false,
            voice_setting: { voice_id: voiceId, speed: speed, vol: 1, pitch: pitch },
            audio_setting: { sample_rate: 32000, bitrate: 128000, format: 'mp3', channel: 1 }
        });

        const options = {
            hostname: 'api.minimaxi.com', path: '/v1/t2a_v2', method: 'POST',
            headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${API_KEY}`, 'Content-Length': Buffer.byteLength(data) }
        };

        const req = https.request(options, (res) => {
            let body = '';
            res.on('data', c => body += c);
            res.on('end', () => {
                try {
                    const json = JSON.parse(body);
                    if (json.data && json.data.audio) resolve(Buffer.from(json.data.audio, 'hex'));
                    else reject(new Error(JSON.stringify(json)));
                } catch (e) { reject(e); }
            });
        });
        req.on('error', reject);
        req.write(data);
        req.end();
    });
}

async function main() {
    // 寇可往（低沉有力）我亦可往（上扬有力）！
    const parts = [
        { text: "寇可往——", voice: 'audiobook_male_2', speed: 0.75, pitch: -3 },  // 沉稳
        { text: "我亦可往！", voice: 'audiobook_male_2', speed: 0.9, pitch: 0 }    // 上扬
    ];

    const files = [];
    for (let i = 0; i < parts.length; i++) {
        const p = `C:\\Users\\TL\\.openclaw\\tts_seg_${i}.mp3`;
        const buf = await generateTTS(parts[i].text, parts[i].voice, parts[i].speed, parts[i].pitch);
        fs.writeFileSync(p, buf);
        files.push(p);
        console.log(`[TTS] Part ${i+1} done`);
    }

    // 用 PowerShell 合并 MP3
    const output = 'C:\\Users\\TL\\.openclaw\\tts-han5.mp3';
    try {
        execSync(`powershell -Command "Get-ChildItem 'C:\\Users\\TL\\.openclaw\\tts_seg_*.mp3' | ForEach-Object { [System.IO.File]::ReadAllBytes($_.FullName) } | Set-Content '${output}' -AsByteStream"`, { stdio: 'inherit' });
    } catch (e) {
        // 简单拼接
        const all = Buffer.concat(files.map(f => fs.readFileSync(f)));
        fs.writeFileSync(output, all);
    }
    console.log('[TTS] Combined to:', output);
    
    // 清理
    files.forEach(f => { try { fs.unlinkSync(f); } catch(e) {} });
}

main().catch(console.error);
