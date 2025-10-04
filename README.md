# TRipchat

A web-based visualization tool for travel chat on Nostr. Displays location-based messages from the Nostr network in a map interface, inspired by Trustroots design principles.

## Features

### Core Functionality
- **Interactive Map**: Leaflet-powered world map with clustered note pins
- **Nostr Integration**: Real-time streaming from multiple Nostr relays
- **Location-based Notes**: Geohash-tagged messages with clickable markers
- **User Verification**: NIP-05 verified profiles with Trustroots/Hitchwiki links
- **Smart Filtering**: Search, geohash, and verified user filters
- **Note Persistence**: Configurable expiration times (1h, 24h, 7d, 30d)
- **Responsive Design**: Works on mobile and desktop with dark/light themes

### Embeddable Widget
- **`embed.html`**: Read-only iframe widget for external sites
- **URL Parameters**: `#hitch&geohash=u1&nip05=true` for filtering
- **Customizable**: Show/hide map and notes via URL parameters
- **Cross-origin Safe**: Designed for embedding on Trustroots, Hitchwiki, etc.

## Quick Start

1. **Serve the project** (required for ES modules):
   ```bash
   python3 -m http.server 5173
   # or
   npx serve .
   ```

2. **Visit** `http://localhost:5173` in a modern browser

3. **Embed** by including `embed.html` in an iframe with URL parameters

## URL Structure

- `#hitch` - Filter by hashtag
- `#hitch&geohash=u1` - Hashtag + geohash location
- `#hitch&nip05=true` - Show only verified users
- `?theme=dark` - Force dark theme
- `?showMap=false` - Hide map (embed only)

## Technical Details

- **Static HTML**: No build process, everything in `index.html`
- **Dependencies**: Leaflet.js, nostr-tools (loaded from CDNs)
- **Relays**: `relay.nomadwiki.org`, `relay.trustroots.org`
- **Storage**: LocalStorage for preferences and profile caching
- **Security**: CSP-protected, no private key storage

## Development

- **Code Style**: 4-space indentation, camelCase, trailing semicolons
- **File Structure**: Keep related code grouped with clear comments
- **Testing**: Manual QA checklist in browser console
- **Contributing**: Use Conventional Commits, include screenshots for UI changes

## Roadmap

- Trustroots circle integration and filtering
- Enhanced NIP-05 verification
- Mobile-optimized note composition
- Additional relay support

## Manual QA Checklist

- [ ] Map renders without console errors
- [ ] Nostr relays connect successfully
- [ ] Note posting and receiving works
- [ ] Filters and stats update correctly
- [ ] CSP allows all required resources
- [ ] Embed works in iframe context