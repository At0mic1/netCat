#! python3

import re, pyperclip

phoneRegex = re.compile(r'''
(
((\d\d\d)|(\(\d\d\d\)))?
(\s|-)
\d\d\d
-
\d\d\d\d
(((ext(\.)?\s)|x)
(\d{2,5}))?
)
''', re.VERBOSE)

# Create a regex for email addresses.
emailRegex = re.compile(r'''

# some.+_thing@,(\d{2,5}))?.com

[a-zA-Z0-9_.+]+   # name part
@                 # @ symbol
[a-zA-Z0-9_.+]+   # domain name part



''', re.VERBOSE)
# Get text from clipboard.
text = pyperclip.paste()

#Extract the email/phone from this text.
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

print(extractedPhone)
print(extractedEmail)

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
