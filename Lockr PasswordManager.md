# Password Manager

## Objectives

To research, design, and build a cross-platform password manager in Python, starting with simple and evolving into a secure, full-featured product with CLI, GUI, Web and Mobile interfaces.

### Phase 1: Research and Planning

#### Key Research Areas

1. What a Password Manager Does:
   1. Store and retrieve passwords securely
   2. Generate strong passwords
   3. Encrypt Data
   4. Sync Across Devices (Optional)
   5. Autofill login forms (Advanced)
2. Core Concepts:
   1. Encryption (AES, Fernet, Key Derivation with PBKDF2 or bcrypt)
   2. Secure storage (SQLite, JSON, or file-based initially)
   3. Master password (never stored, used to unlock vault)
   4. Zero-Knowledge design (no one else can see passwords)
3. Python Libraries:
   1. cryptography - for encryption
   2. sqlite3 - for storage
   3. argparse, click or typer - for CLI
   4. tkinter or PyQt - for GUI
   5. Flask or FastAPI - for web backend
   6. Kivy or BeeWare - for mobile apps (using python)

### Phase 2: Minimal CLI Password Manager (MVP)

#### Features

1. Initialize a password vault (with master password)
2. Add, retrieve, delete credentials
3. Encrypt and Decrypt passwords
4. Local storage in encrypted form

#### Tech Stack

1. `Python` + `cryptography` + `sqlite3`
2. CLI using `argparse` or `typer`

### Phase 3: Extend to GUI

#### Features

1. Simple GUI interface for existing CLI features
2. Optional Password Generator

#### Tech Stack

1. `tkinter` (built-in) or `PyQt5`(More advanced)

### Phase 4: Web Interface

#### Features

1. Flask/FastAPI server with user authentication 
2. REST API for vault operations
3. Frontend with basic HTML/CSS/JS or a frontend framework like React

#### Security Additions

1. HTTPS
2. JWT tokens for session management
3. Server-side encryption with user's master password

### Phase 5: Mobile Interface

#### Approaches

1. `Kivy` - pure python cross platform
2. `BeeWare/Toga` - python to native mobile apps
3. Use Rest API from Phase 4 - mobile fronted in Flutter or React Native

## Future Features (Post MVP)

1. Biometric authentication (figerprint/face)
2. Auto-fill browser extension
3. Cloud Sync with encryption
4. Password health audit (weak/reused)
5. Two-Factor Authentication (2FA)
6. Offline mode with sync later

## Security Considerations

1. Always hash master passwords (e.g., bcrypt)
2. Use encryption (e.g AES-256 with derived key)
3. Salt + iterations to prevent brute-force attacks
4. Lockout after multiple failed logins
5. Don't log sensitive data

## Documentation & Testing

1. Write docstrings and usage guides
2. Unit tests with unittest or pytest
3. Store code in GitHub (private if sensitive)