# TRipchat

TRipchat is a static, single-page travel chat that combines a Leaflet-powered map with Nostr relays so travelers can discover, filter, and discuss nearby notes. The site runs entirely in the browser and keeps all HTML, styling, and client logic inside `index.html`.

## Features
- Interactive world map with Leaflet tiles and clustered note pins.
- Nostr relay integration for publishing and streaming geotagged notes.
- Trustroots-focused filters (planned) to surface trusted community posts.
- Inline stats cards that summarize active relays, note counts, and recent activity.

## Getting Started
1. Install dependencies (none required; everything loads from CDNs).
2. Serve the project from the repo root so browsers allow ES module imports:
   ```bash
   python3 -m http.server 5173
   ```
   or
   ```bash
   npx serve .
   ```
3. Visit `http://localhost:5173` in a modern browser.

## Development Notes
- All script and style changes live in `index.html`; keep related blocks grouped and commented.
- Use four-space indentation, camelCase identifiers, and trailing semicolons in JavaScript.
- Add new assets under `assets/` and update the CSP meta tag if you rely on additional CDNs or websocket relays.
- Do **not** commit private keys. Prompt users for keys or rely on browser extensions for Nostr auth.

## Manual QA Checklist
- Map renders without console errors and tiles load across zoom levels.
- Nostr relays connect successfully; posting and receiving notes updates the UI.
- Filters and stats counters respond while interacting with the map and note list.
- CSP allows any new external scripts, styles, or websocket connections introduced.

## Roadmap
- Validate Trustroots NIP-05 identities before posting notes.
- Fetch Trustroots circles and expose them as filters in the UI.
- Add filter toggles to surface only Trustroots-verified notes.

## Contributing
Follow Conventional Commits (for example, `feat: add relay health badges`) and document manual test steps plus rollback considerations in pull requests. Include screenshots or recordings for any significant UI changes.
