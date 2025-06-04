from datetime import datetime, timezone
import secrets

def gen_benchmark_id():
    timestamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')
    random_suffix = secrets.token_hex(3).upper()
    return f"{timestamp}_{random_suffix}"