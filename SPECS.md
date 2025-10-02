# TRipchat Specifications

## Overview
TRipchat is a web-based visualization tool for travel chat on Nostr. It displays location-based messages from the Nostr network in a map interface, inspired by Trustroots design principles.

## Core Features

### Map Visualization
- Interactive map using Leaflet.js
- Dark/light theme support
- Geohash-based location markers
- Clickable markers showing note content
- Geohash area highlighting

### Note Display
- Real-time note streaming from Nostr relays
- Note persistence with expiration times (1h, 24h, 7d, 30d)
- Username display with NIP-05 verification
- Clickable timestamps showing raw Nostr data
- Hashtag processing and linking

### Filtering System
- **Search Filter**: Text search across content, usernames, hashtags
- **Geohash Filter**: Location-based filtering
- **Verified Filter**: Show only NIP-05 verified users
- **URL Hash Support**: Clean URLs like `#hitch&geohash=u1`

### Posting
- Compose new notes with geohash location
- Private key management (nsec/hex)
- NIP-05 verification for Trustroots users
- Hashtag extraction from search filter
- Multiple relay publishing

### User Interface
- Responsive design for mobile/desktop
- Dark mode toggle
- Clean, modern styling
- Keyboard shortcuts (Enter to post)
- Auto-scroll to new messages

## Technical Details

### Nostr Integration
- Uses nostr-tools library for key management
- Connects to multiple Nostr relays
- Supports Kind 1 events (text notes)
- NIP-05 verification support

### Data Storage
- LocalStorage for user preferences
- Profile caching for usernames
- Theme persistence

### URL Structure
- `#hitch` - Direct hashtag filter
- `#hitch&geohash=u1` - Hashtag + geohash
- `#hitch&nip05=true` - Hashtag + verified filter

## Browser Support
- Modern browsers with WebSocket support
- ES6+ JavaScript features
- CSS Grid and Flexbox

## Embeddable iframe

### Overview
A separate HTML file that can be embedded on external sites like Trustroots and Hitchwiki. Provides read-only access to TRipchat data with customizable display options.

### Features
- **Read-only mode**: No posting or user interaction
- **Same URL parameters**: Supports all TRipchat hash location parameters
- **Customizable display**: Optional map and/or notes display
- **Responsive**: Adapts to iframe container size
- **Lightweight**: Minimal dependencies for embedding

### URL Parameters
- `#hitch` - Filter by hashtag
- `#hitch&geohash=u1` - Hashtag + geohash filter
- `#hitch&nip05=true` - Hashtag + verified filter
- `?showMap=true` - Display map (default: true)
- `?showNotes=true` - Display notes list (default: true)
- `?theme=dark` - Force dark theme
- `?height=400` - Set iframe height

### Implementation
- Separate `embed.html` file
- Same Nostr relay connections
- Simplified UI without compose form and without filter
- Show link to `index.html` (with same parameters)
- Configurable via URL parameters
- Cross-origin iframe friendly

### Use Cases
- **Trustroots**: Show travel-related notes on location pages
- **Hitchwiki**: Display hitchhiking notes for specific areas
- **Other sites**: Embed travel chat in location-based content

## Dependencies
- Leaflet.js (map visualization)
- nostr-tools (Nostr protocol)
- No build process required (static HTML)
