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
    "Metalymph/valkey": "0.4.1"
  }
}
````

example:

```
import "Metalymph/valkey"

let client =
  @valkey.Client::connect(
    "127.0.0.1",
    6379,
  )

let pong = client.ping()
println(pong)
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