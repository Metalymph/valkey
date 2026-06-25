import os
import re

files_to_fix = [
    "valkey/relay/valkey_backend.mbt",
    "valkey/relay/streams.mbt",
    "valkey/relay/redis_wbtest.mbt",
    "valkey/relay/streams_wbtest.mbt"
]

replacements = {
    r"\bMessage\b": "@core.Message",
    r"\bQueueError::OperationFailed\b": "@core.QueueError::OperationFailed",
    r"\bNackResult\b": "@core.NackResult",
    r"\bSentToDlq\b": "@core.SentToDlq",
    r"\bRequeued\b": "@core.Requeued",
    r"\bRelayQueue\b": "@core.RelayQueue",
    r"\bQueueMetrics\b": "@core.QueueMetrics",
    r"\bBackendHealth\b": "@core.BackendHealth",
    r"\bBackendCapabilities\b": "@core.BackendCapabilities",
    r"\bRetryPolicy\b": "@core.RetryPolicy"
}

for filepath in files_to_fix:
    if not os.path.exists(filepath):
        continue
    with open(filepath, "r") as f:
        content = f.read()
    
    for pattern, replacement in replacements.items():
        # Avoid double replacing if it's already @core.Message
        content = re.sub(r"(?<!@core\.)" + pattern, replacement, content)
    
    with open(filepath, "w") as f:
        f.write(content)
