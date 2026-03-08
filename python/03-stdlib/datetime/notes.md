# Python Datetime

## Core Types
*Represent dates, times, and durations*

**`date`** – Year, month, day only
**`time`** – Hour, minute, second only
**`datetime`** – Date + time combined
**`timedelta`** – Duration or difference between two points
**`timezone`** – Timezone info (UTC offset)

```python
from datetime import date, time, datetime, timedelta, timezone

today    = date.today()               # 2024-03-07
now      = datetime.now()             # 2024-03-07 14:30:00.123456
utc_now  = datetime.now(timezone.utc) # timezone-aware
delta    = timedelta(days=7, hours=3)
```

---

## Creating Dates & Times
*Construct from values or strings*

```python
from datetime import date, datetime

# From values
d = date(2024, 3, 7)            # date(year, month, day)
dt = datetime(2024, 3, 7, 14, 30, 0)

# From string (strptime)
dt = datetime.strptime("2024-03-07 14:30", "%Y-%m-%d %H:%M")
d  = date.fromisoformat("2024-03-07")

# From timestamp (Unix)
dt = datetime.fromtimestamp(1709817000)
dt = datetime.fromtimestamp(1709817000, tz=timezone.utc)
```

---

## Formatting
*Convert to strings*

```python
from datetime import datetime

now = datetime(2024, 3, 7, 14, 30, 0)

now.strftime("%Y-%m-%d")           # "2024-03-07"
now.strftime("%d/%m/%Y %H:%M")    # "07/03/2024 14:30"
now.isoformat()                    # "2024-03-07T14:30:00"
```

### Format Codes
*Common strftime / strptime codes*

| Code | Meaning | Example |
|------|---------|---------|
| `%Y` | 4-digit year | `2024` |
| `%m` | Month (01–12) | `03` |
| `%d` | Day (01–31) | `07` |
| `%H` | Hour 24h (00–23) | `14` |
| `%M` | Minute (00–59) | `30` |
| `%S` | Second (00–59) | `00` |
| `%A` | Weekday name | `Thursday` |

---

## Arithmetic
*Add, subtract, and compare dates*

```python
from datetime import datetime, timedelta

now = datetime.now()

tomorrow    = now + timedelta(days=1)
last_week   = now - timedelta(weeks=1)
in_90_days  = now + timedelta(days=90)

# Difference between two datetimes
end   = datetime(2024, 12, 31)
start = datetime(2024, 1, 1)
delta = end - start           # timedelta object
delta.days                    # 365
```

---

## Timezones
*Work with aware datetimes*

```python
from datetime import datetime, timezone, timedelta
import zoneinfo   # Python 3.9+

# UTC
utc_now = datetime.now(timezone.utc)

# Named timezone
from zoneinfo import ZoneInfo
ny_time  = datetime.now(ZoneInfo("America/New_York"))
bog_time = datetime.now(ZoneInfo("America/Bogota"))

# Convert between timezones
utc_dt = datetime.now(timezone.utc)
local  = utc_dt.astimezone(ZoneInfo("America/Bogota"))
```

---

## Useful Properties
*Access date/time components*

```python
from datetime import datetime

dt = datetime(2024, 3, 7, 14, 30, 45)

dt.year        # 2024
dt.month       # 3
dt.day         # 7
dt.hour        # 14
dt.minute      # 30
dt.second      # 45
dt.weekday()   # 3  (0=Monday, 6=Sunday)
dt.date()      # date(2024, 3, 7)
dt.time()      # time(14, 30, 45)
```

---

## Best Practices

**Always store UTC** – Save as UTC in DB; convert to local only for display  
**Aware vs naive** – Always use timezone-aware datetimes in production  
**`zoneinfo`** – Prefer over `pytz` (built-in since Python 3.9)  
**`isoformat()`** – Use for serialization; unambiguous and parseable  
**`timedelta`** – Use for date arithmetic; never do it manually with raw ints  
