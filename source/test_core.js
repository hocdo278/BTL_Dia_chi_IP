const fs = require('fs');
const html = fs.readFileSync(process.argv[2], 'utf8');
const core = html.split('// ==== CORE BEGIN ====')[1].split('// ==== CORE END ====')[0];
const api = new Function(core + ';return { runAll, bruteForce, canon };')();
const { runAll, bruteForce, canon } = api;
const tests = JSON.parse(html.split('/*TESTS_BEGIN*/')[1].split('/*TESTS_END*/')[0]);
let bad = 0;
for (const t of tests) {
  const p = runAll(t.input, true).results, q = runAll(t.input, false).results, b = bruteForce(t.input).results;
  const ok = canon(p) === canon(t.expected) && canon(q) === canon(t.expected) && canon(b) === canon(t.expected);
  if (!ok) { bad++; console.log('FAIL', t.name, t.input); }
}
console.log('testcase nhung trong trang:', tests.length, 'sai:', bad);
let seed = 12345; const rnd = () => (seed = (seed * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff;
let n = 0, nonEmpty = 0, sameTree = 0;
for (let i = 0; i < 3000; i++) {
  const len = 1 + Math.floor(rnd() * 14), al = ['0', '01', '0125', '0123456789', '12'][Math.floor(rnd() * 5)];
  let s = ''; for (let j = 0; j < len; j++) s += al[Math.floor(rnd() * al.length)];
  const a = runAll(s, true), b = runAll(s, false), c = bruteForce(s);
  if (canon(a.results) !== canon(c.results) || canon(b.results) !== canon(c.results)) { console.log('MISMATCH', s); process.exit(1); }
  if (a.stats.tries > b.stats.tries) { console.log('prune tang tries?', s); process.exit(1); }
  n++; if (c.results.length) nonEmpty++;
}
console.log('3000 chuoi ngau nhien: quay lui (co/khong tia) = vet can. Co nghiem:', nonEmpty);
const s100 = '1'.repeat(100);
const pr = runAll(s100, true), np = runAll(s100, false);
console.log('n=100 toan so 1: co tia nut =', pr.stats.calls, ', khong tia nut =', np.stats.calls);
const sample = runAll('25525511135', true);
console.log('mau de bai:', sample.results.join(' '), '| nut', sample.stats.calls, 'thu', sample.stats.tries, 'loai', sample.stats.rejects, 'tia', sample.stats.prunes);
