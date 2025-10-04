# TRipchat

A web-based visualization tool for travel chat on Nostr. Displays location-based messages from the Nostr network in a map interface.

## Features

- **Interactive Map**: Leaflet-powered world map with clustered note pins
- **Nostr Integration**: Real-time streaming from multiple Nostr relays
- **Location-based Notes**: Geohash-tagged messages with clickable markers
- **User Verification**: NIP-05 verified profiles with Trustroots/Hitchwiki links
- **Smart Filtering**: Search, geohash, and verified user filters
- **Embeddable Widget**: `embed.html` for external sites

## Quick Start

**Just open `index.html` in your browser!** No server required.

## URL Parameters

- `#hitch` - Filter by hashtag
- `#hitch&geohash=u1` - Hashtag + geohash location
- `#hitch&nip05=true` - Show only verified users
- `?theme=dark` - Force dark theme
- `?showMap=false` - Hide map (embed only)

## Technical Details

- **Static HTML**: No build process, everything in `index.html`
- **Dependencies**: Leaflet.js, nostr-tools (CDN-loaded)
- **Relays**: `relay.nomadwiki.org`, `relay.trustroots.org`
- **Storage**: LocalStorage for preferences and caching

## Development

- **Code Style**: 4-space indentation, camelCase, trailing semicolons
- **Testing**: Manual QA in browser console
- **Contributing**: Use Conventional Commits, include screenshots for UI changes