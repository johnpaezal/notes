# Date & Time API
*java.time – Modern date/time (Java 8+)*

## Core Classes

| Class           | Represents                     |
|-----------------|--------------------------------|
| `LocalDate`     | Date only (year, month, day)   |
| `LocalTime`     | Time only (hour, minute, sec)  |
| `LocalDateTime` | Date + Time (no timezone)      |
| `ZonedDateTime` | Date + Time + timezone         |
| `Instant`       | Point in time (UTC timestamp)  |

---

## LocalDate

```java
// Creation
LocalDate today = LocalDate.now();
LocalDate date = LocalDate.of(2024, 3, 15);        // year, month, day
LocalDate parsed = LocalDate.parse("2024-03-15");  // ISO format

// Read
date.getYear();        // 2024
date.getMonthValue();  // 3
date.getDayOfMonth();  // 15
date.getDayOfWeek();   // FRIDAY
date.getDayOfYear();   // 75

// Manipulate (immutable – returns new instance)
date.plusDays(7);
date.minusMonths(1);
date.plusYears(2);
date.withMonth(6);     // same year/day, month = June

// Compare
date.isBefore(LocalDate.now());
date.isAfter(LocalDate.now());
date.isEqual(LocalDate.now());
```

---

## LocalTime

```java
LocalTime now = LocalTime.now();
LocalTime time = LocalTime.of(14, 30, 0);   // hour, minute, second
LocalTime parsed = LocalTime.parse("14:30:00");

time.getHour();    // 14
time.getMinute();  // 30
time.getSecond();  // 0

time.plusHours(2);
time.minusMinutes(15);
```

---

## LocalDateTime

```java
LocalDateTime now = LocalDateTime.now();
LocalDateTime dt = LocalDateTime.of(2024, 3, 15, 14, 30);
LocalDateTime dt = LocalDateTime.of(date, time);  // combine

dt.toLocalDate();   // extract date
dt.toLocalTime();   // extract time

dt.plusDays(1).minusHours(2);
```

---

## Period & Duration
*Measuring time between dates*

```java
// Period – for dates (years, months, days)
LocalDate start = LocalDate.of(2023, 1, 1);
LocalDate end = LocalDate.of(2024, 6, 15);

Period period = Period.between(start, end);
period.getYears();   // 1
period.getMonths();  // 5
period.getDays();    // 14

// Duration – for times (hours, minutes, seconds)
LocalTime t1 = LocalTime.of(8, 0);
LocalTime t2 = LocalTime.of(17, 30);

Duration duration = Duration.between(t1, t2);
duration.toHours();    // 9
duration.toMinutes();  // 570
```

---

## DateTimeFormatter
*Format and parse dates as strings*

```java
LocalDate date = LocalDate.of(2024, 3, 15);
LocalDateTime dt = LocalDateTime.now();

// Predefined formats
DateTimeFormatter.ISO_LOCAL_DATE;       // "2024-03-15"
DateTimeFormatter.ISO_LOCAL_DATE_TIME;  // "2024-03-15T14:30:00"

// Custom format
DateTimeFormatter fmt = DateTimeFormatter.ofPattern("dd/MM/yyyy");
String formatted = date.format(fmt);   // "15/03/2024"

DateTimeFormatter dtFmt = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm");
String formatted = dt.format(dtFmt);   // "15-03-2024 14:30"

// Parse
LocalDate parsed = LocalDate.parse("15/03/2024", fmt);

// Common pattern tokens
// yyyy  year    MM  month   dd  day
// HH    hour    mm  minute  ss  second
// EEE   day name (Mon)   MMMM  month name (March)
```
