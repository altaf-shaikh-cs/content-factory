// Resolve the Gemini API key without it ever passing through a command line,
// a log, or an agent transcript.
//   1. GEMINI_API_KEY / GOOGLE_API_KEY in the environment
//   2. macOS Keychain, service "GEMINI_API_KEY"
import { execFileSync } from 'node:child_process';

export function getKey() {
  const env = process.env.GEMINI_API_KEY || process.env.GOOGLE_API_KEY;
  if (env) return { key: env, source: 'env' };
  try {
    const key = execFileSync('security',
      ['find-generic-password', '-a', process.env.USER, '-s', 'GEMINI_API_KEY', '-w'],
      { encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] }).trim();
    if (key) return { key, source: 'keychain' };
  } catch { /* not stored */ }
  return { key: null, source: null };
}

export function requireKey() {
  const { key, source } = getKey();
  if (!key) {
    console.error('No Gemini API key found. Store it once (the value is typed at a prompt,\n'
      + 'never echoed, and never enters a shell history or an agent transcript):\n\n'
      + '  security add-generic-password -a "$USER" -s GEMINI_API_KEY -w\n\n'
      + 'Or export GEMINI_API_KEY in your shell profile.');
    process.exit(2);
  }
  return { key, source };
}
