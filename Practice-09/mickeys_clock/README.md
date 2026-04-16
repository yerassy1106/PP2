### 2. README для Mickey's Clock (`mickeys_clock/README.md`)

```markdown
# Mickey's Clock Application

A real-time clock application where Mickey Mouse's hands indicate the current system time.

## Features
- **Right Hand**: Indicates minutes.
- **Left Hand**: Indicates seconds.
- **Sync**: Automatically synchronizes with the system clock.

## How to Run
From the root directory:
```bash
python mickeys_clock/main.py
Implementation DetailsUses pygame.transform.rotate for hand movements.Calculating rotation angles: $Angle = -(units \times 6) + 90^\circ$.