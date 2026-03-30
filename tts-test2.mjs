import { TTSClient } from 'file:///C:/Users/TL/AppData/Roaming/npm/node_modules/openclaw/dist/index.js';
const client = new TTSClient();
const r = await client.synthesize({ text: '微臣待命', voice: 'male-qn-qingse' });
console.log(JSON.stringify(r));
