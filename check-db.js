const s = require('sqlite3');
const db = new s.Database('C:/Users/TL/.openclaw/openclaw.db');
db.all("SELECT name FROM sqlite_master WHERE type='table'", [], (e,r) => {
  if(e) { console.log(e); }
  else { console.log(JSON.stringify(r)); }
  db.close();
});
