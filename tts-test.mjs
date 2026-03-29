import { TTSClient } from 'C:/Users/TL/AppData/Roaming/npm/node_modules/openclaw/dist/index.js';

async function test() {
  try {
    const client = new TTSClient();
    const result = await client.synthesize({ text: '微臣狄仁杰，待命', voice: 'male-qn-qingse' });
    console.log('SUCCESS');
    console.log(JSON.stringify(result));
  } catch(e) {
    console.log('ERROR:', e.message);
    console.log('STACK:', e.stack);
  }
}
test();
