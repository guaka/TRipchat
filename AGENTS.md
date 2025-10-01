# Repository Guidelines

## Project Structure & Module Organization
TRipchat is a static single-page application. All HTML, styling, and scripted behavior live in `index.html`, with inline ES module imports for Leaflet and `nostr-tools`. Keep related features grouped with clear comment blocks, and favor dedicated helper functions within the same script block for map, relay, and UI logic. Add new assets under `assets/` if you introduce images or fonts, and reference them with relative paths.

## Local Development & Build
Run a lightweight server so browser security policies allow module imports:
- `python3 -m http.server 5173` – serve the site for manual testing.
- `npx serve .` – alternative static server with caching headers. Update the Content Security Policy (CSP) meta tag if you add new CDNs or websocket targets.

## Coding Style & Naming
Use four-space indentation and trailing semicolons in JavaScript for consistency with the existing file. Prefer `const`/`let` over `var`, camelCase for variables and functions, and kebab-case for CSS classes. Group CSS by component (map, notes, stats) and keep selectors scoped. When adding modules, load them via `<script type="module">` and document any globals attached to `window`.

## Testing & QA
There is no automated test suite yet. Before submitting changes, verify Leaflet renders the map, Nostr relays connect without console errors, stats counters update while interacting, and the CSP allows all required resources. Capture browser console logs for regressions and document manual test steps in the pull request.

## Commit & PR Workflow
No commit history is included, so adopt Conventional Commits (e.g., `feat: add relay health badges`) for clarity. Reference related issues in the body, explain UI changes with screenshots or screen recordings, and flag any CSP or dependency updates. For PRs, provide a short change summary, manual test notes, and rollback considerations so reviewers can evaluate quickly.

## Security & Configuration Tips
Never embed private Nostr keys in the repository or example snippets; rely on browser extensions or environment prompts. When adjusting relay endpoints, sanitize user input and document trusted defaults in the PR description.
