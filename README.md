# Valkey

Native async Valkey/Redis client for MoonBit.

Valkey provides a lightweight RESP implementation, TCP networking support, typed Redis helpers, Redis Streams support, and Consumer Group operations.

Built on top of the `moonbitlang/async` runtime.

---

## Features

- Native RESP protocol implementation
- Async TCP client
- Typed Redis/Valkey commands
- Redis Streams support
- Consumer Groups
- Pending message inspection
- Message recovery helpers
- MoonBit-native APIs

---

## Installation

```json
{
  "deps": {
    "Metalymph/valkey": "0.5.0"
  }
}
```

example `moon.pkg`:
```json
{
  "import": [
    "Metalymph/valkey"
  ]
}
```

```moonbit
let client =
  @valkey.Client::connect(
    "127.0.0.1",
    6379,
  )

let pong = client.ping()
println(pong)
```

---

## Relay Adapter

This package also provides a backend adapter for [Metalymph/relay](https://github.com/Metalymph/relay).

Add the dependency to your `moon.pkg`:
```json
{
  "import": [
    "Metalymph/relay/core",
    "Metalymph/valkey/relay"
  ]
}
```

Usage:
```moonbit
let backend = @relay.ValkeyStreamBackend::new(client, "my_stream", "my_group", "consumer_1")
let queue = backend.to_relay_queue()
```

Supported Features

Core Commands

* GET
* SET
* DEL
* EXISTS
* INCR
* DECR
* EXPIRE
* TTL
* PING

Streams

* XADD
* XGROUP CREATE
* XREADGROUP
* XACK
* XPENDING
* XAUTOCLAIM