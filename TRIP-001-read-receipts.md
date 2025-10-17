# TRIP-001: Read Receipt for NIP-04 Messages

**Status:** Draft  
**Kind:** 30004 (Parameterized Replaceable Event)  
**Created:** 2025-10-17  
**Author:** TRipchatter guaka

## Summary

A minimal, interoperable event format for clients to mark NIP-04 (kind 4) encrypted DMs as "read" to prevent duplicate notifications across multiple notification services (email, push, etc.).

## Motivation

- Users receive encrypted DMs via Nostr but may use external notification services (email daemons, push notification services)
- Without read tracking, these services send notifications even after messages are read in a client
- This NIP allows clients to publish read receipts that notification services can monitor

## Specification

### Event Kind

- **30004**: Parameterized Replaceable Event
- Only the most recent receipt per message is kept (prevents spam)

### Event Structure

```json
{
  "kind": 30004,
  "pubkey": "<reader_pubkey>",
  "created_at": <unix_timestamp>,
  "tags": [
    ["d", "<dm_event_id>"],
    ["e", "<dm_event_id>", "<relay_hint>"],
    ["p", "<sender_pubkey>"]
  ],
  "content": "{\"read_at\": <unix_timestamp>}",
  "sig": "<signature>"
}
```

### Tags

- **`d` (required)**: Identifier tag set to the DM event ID (makes this event replaceable per message)
- **`e` (required)**: References the original NIP-04 message event ID, with optional relay hint
- **`p` (recommended)**: Sender's pubkey from the original DM

### Content

- JSON object with `read_at` timestamp: `{"read_at": <unix_timestamp>}`
- Empty string is also acceptable for minimal implementations

### Client Behavior

#### Publishing Receipts

- When a user views/decrypts a NIP-04 message in the client, publish a kind 30004 event
- Only publish once per message (replaceable events naturally deduplicate)
- Publish to the same relays where the original DM was received

#### Consuming Receipts

- Notification services (email daemons, push services) subscribe to kind 30004 events for users they monitor
- When a receipt is found for a DM, mark it as "read" and suppress notifications
- Match receipts using the `e` tag (event ID) and `p` tag (sender pubkey)

#### Privacy Considerations

- Receipts are **public** by design for simplicity
- Anyone can see when you read a message
- Clients MAY allow users to disable read receipt publishing
- Future versions could use NIP-17 gift wrapping for private receipts

### Relay Behavior

- No changes required
- Relays treat this as a standard parameterized replaceable event (NIP-33)
- Older receipts for the same `d` tag are automatically replaced

## Example

### Original DM (kind 4)

```json
{
  "id": "a1b2c3d4e5f6...",
  "kind": 4,
  "pubkey": "sender_pubkey_hex...",
  "created_at": 1697555555,
  "tags": [["p", "recipient_pubkey_hex..."]],
  "content": "<encrypted_content>",
  "sig": "..."
}
```

### Read Receipt (kind 30004)

```json
{
  "id": "x9y8z7w6v5u4...",
  "kind": 30004,
  "pubkey": "recipient_pubkey_hex...",
  "created_at": 1697555600,
  "tags": [
    ["d", "a1b2c3d4e5f6..."],
    ["e", "a1b2c3d4e5f6...", "wss://relay.example.com"],
    ["p", "sender_pubkey_hex..."]
  ],
  "content": "{\"read_at\": 1697555600}",
  "sig": "..."
}
```

## Rationale

### Why kind 30004 (parameterized replaceable)?

- Prevents receipt spam (only one receipt per message)
- Natural deduplication across multiple client sessions
- Efficient for notification services to query

### Why public receipts?

- Simplicity: no encryption overhead
- Interoperability: works with any relay
- Users can opt-out by disabling the feature in their client

### Future Enhancements

- NIP-17 gift-wrapped private receipts for privacy-conscious users
- Support for "delivered" vs "read" vs "deleted" states
- Batch receipts for multiple messages

## Security Considerations

- Receipts are signed by the recipient (proof of authenticity)
- Notification services MUST verify signatures before trusting receipts
- Malicious actors could publish fake receipts, but can't forge signatures

## Backwards Compatibility

- Fully backwards compatible
- Clients that don't support this NIP simply ignore kind 30004 events
- Old notification services continue working (send all notifications)

## Reference Implementation

- **TRipch.at**: Web client that publishes read receipts
- **nostr-email-notification-daemon**: Email service that consumes receipts to suppress notifications

## See Also

- [NIP-04: Encrypted Direct Messages](https://github.com/nostr-protocol/nips/blob/master/04.md)
- [NIP-33: Parameterized Replaceable Events](https://github.com/nostr-protocol/nips/blob/master/33.md)
- [NIP-17: Private Direct Messages](https://github.com/nostr-protocol/nips/blob/master/17.md)

## License

Public Domain

