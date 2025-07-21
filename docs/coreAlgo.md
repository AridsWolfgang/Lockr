# Lockr Vault - Core Algorithm 

This design assumes:
- Each user has a master password 
- This password derives an encryption key via a Key Deriviation Function (KDF) (e.g., PBKDF2) 
- All passwords and files are encrypted using this derived key 
- Files are stored on disk, metadata in a database (e.g SQLite) 

# Main Features Covered 

1. User Registration/Login 
2. Add/View Passwords 
3. Add/View Encrypted Files 
4. Key handling and secure encryption 

# High-Level Algorithm (Plain English)

```
Start Lockr App 
1. Write out the Banner for CLI
1. Registration and Login Questions 
1. Print out the Main Menu 
1. Pick the Registration function first
1. Ask user to login or register and login functions
2. If register: 
    a. Ask for master password 
    b. Generate salt 
    c. Derive key from password + salt (using KDF) 
    d. Store salt + password hash (not the actual password!)
3. If login: 
    a. Ask for master password 
    b. Retrieve stored salt 
    c. Derive key from password + salt 
    d. Verify hash matches 
4. User is authenticated 
5. Show main menu: 
    - Add Passwords 
    - View Passwords 
    - Add File 
    - View/Export File 
    - Exit 
6. If user adds password: 
    a. Ask for service name + username + password 
    b. Encrypt it using the derived key 
    c. Save to database 
7. If user adds a file: 
    a. Select file from disk 
    b. Encrypt file content using the key 
    c. Save encrypted file to vault folder 
    d. Save metadata in DB 
8. If user views passwords or files: 
    a. Decrypt using derived key 
    b. Display to user 
9. On exit, clear senstive data from memory

```
# Pseudocode 
```Plaintext 
FUNCTION start_app():
    PRINT "Welcom to Lockr"
    choice = INPUT("Login(1) or Register(2): ")
    
    IF choice == 2:
      password = PROMPT_SECRET("Create a Master Password: ")
      salt = GENERATE_RANDOM_SALT() 
      key = KDF(password, salt)
      hashed_pw = HASH(password)
      STORE_USER_CREDENTIALS(salt, hashed_pw)
    ELSE:
      password = PROMPT_SECRET("Enter master password: ")
      salt, stored_hash = LOAD_CREDENTIALS()
      key = KDF(password, salt) 
      
      IF HASH(password) != stored_hash:
        PRINT "Invalid Password"
        RETURN 

    LOOP:
      PRINT_MENU()
      option = INPUT("Choose option: ")

    IF option == "1":                                                 # Add Password
       service = INPUT("Service Name: ")
       username = INPUT("Username: ")
       pw = PROMPT_SECRET("Password: ")
       encrypted = ENCRYPT_JSON({service, username, pw}, key)
       STORE_PASSWORD_ENTRY(encrypted)
    ELIF option == "2":                                               # View Passwords 
       entries = LOAD_PASSWORD_ENTRIES()
       FOR entry IN entries:
          decrypted = DECRYPT(entry.data, key) 
          DISPLAY(decrypted)
    ELIF option == "3":                                               # Add File 
      filepath = SELECT_FILE()
      file_data = READ_FILE(filepath)
      encrypted = ENCRYPT(file_data, key)
      filename = GET_FILENAME(filepath)
      SAVE_FILE_TO_VAULT(encrypted, filename)
      STORE_FILE_METADATA(filename, type, date)
    ELIF option == "4":                                               # View Files 
      files = LIST_FILES()
      FOR file IN files:
        metadata = LOAD_FILE_METADATA(file)
        decrypted = DECRYPT_FILE(file, key)
      OUTPUT_FILE_TO_TEMP(decrypted)
    ELIF option == "5":                                               # Exit 
      PRINT "Goodbye"
      BREAK

END 
```
```
```
