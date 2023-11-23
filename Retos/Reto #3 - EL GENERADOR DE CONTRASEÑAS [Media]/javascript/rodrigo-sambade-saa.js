function generatePassword(length, includeUppercase, includeNumbers, includeSymbols) {
    if (length < 8 || length > 16) {
        throw new Error('Invalid password length ' + length);
    }

    const lowercaseChars = 'abcdefghijklmnopqrstuvwxyz';
    const uppercaseChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const numberChars = '0123456789';
    const symbolChars = '!@#$%^&*()_+[]{}|;:,.<>?';
  
    let validChars = lowercaseChars;
  
    if (includeUppercase) {
      validChars += uppercaseChars;
    }
  
    if (includeNumbers) {
      validChars += numberChars;
    }
  
    if (includeSymbols) {
      validChars += symbolChars;
    }
  
    let password = '';
  
    for (let i = 0; i < length; i++) {
      const randomIndex = Math.floor(Math.random() * validChars.length);
      password += validChars[randomIndex];
    }
  
    return password;
  }
  
  const newPassword = generatePassword(16, true, true, true);
  console.log(newPassword);
  