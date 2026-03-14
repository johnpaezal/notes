# Regex
*Pattern matching for strings*

## Quick Reference

```java
// Test if whole string matches
"hello123".matches("[a-z]+\\d+");   // true
"Hello".matches("[a-z]+");          // false (uppercase)

// Common patterns
"[a-z]"       // one lowercase letter
"[A-Z]"       // one uppercase letter
"[0-9]" / "\\d"   // one digit
"\\w"         // word character [a-zA-Z0-9_]
"\\s"         // whitespace (space, tab, newline)
"."           // any character
"+"           // one or more
"*"           // zero or more
"?"           // zero or one
"{3}"         // exactly 3
"{2,5}"       // between 2 and 5
"^"           // start of string
"$"           // end of string
```

---

## Pattern & Matcher

```java
import java.util.regex.*;

String text = "Email: alice@example.com and bob@test.org";
Pattern pattern = Pattern.compile("[\\w.]+@[\\w.]+\\.[a-z]{2,}");
Matcher matcher = pattern.matcher(text);

// Find all matches
while (matcher.find()) {
    System.out.println(matcher.group());  // "alice@example.com", "bob@test.org"
    matcher.start();  // start index
    matcher.end();    // end index
}

// Check if entire string matches
matcher.matches();

// Check if string contains a match
matcher.find();
```

---

## String Methods with Regex

```java
String s = "hello world foo bar";

// Split
s.split("\\s+");           // ["hello", "world", "foo", "bar"]
s.split(" ", 2);           // ["hello", "world foo bar"] (limit)

// Replace
s.replaceAll("\\s+", "-"); // "hello-world-foo-bar"
s.replaceFirst("o", "0");  // "hell0 world foo bar"

// Check
s.matches(".*world.*");    // true (matches whole string)
```

---

## Capture Groups

```java
String date = "2024-03-15";
Pattern p = Pattern.compile("(\\d{4})-(\\d{2})-(\\d{2})");
Matcher m = p.matcher(date);

if (m.matches()) {
    m.group(0);  // "2024-03-15" (full match)
    m.group(1);  // "2024" (year)
    m.group(2);  // "03"   (month)
    m.group(3);  // "15"   (day)
}

// Named groups
Pattern p = Pattern.compile("(?<year>\\d{4})-(?<month>\\d{2})-(?<day>\\d{2})");
Matcher m = p.matcher("2024-03-15");
if (m.matches()) {
    m.group("year");   // "2024"
    m.group("month");  // "03"
}
```

---

## Common Patterns

```java
// Email (basic)
"[\\w._%+-]+@[\\w.-]+\\.[a-zA-Z]{2,}"

// Phone (digits only, 10)
"\\d{10}"

// URL (basic)
"https?://[\\w./-]+"

// Only digits
"\\d+"

// Only letters
"[a-zA-Z]+"

// Alphanumeric
"[a-zA-Z0-9]+"

// Whitespace cleanup
text.replaceAll("\\s+", " ").trim()
```
