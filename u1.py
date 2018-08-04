fname = 'mbox-short.txt'
fhand = open(fname)
email = dict()
for line in fhand:
    if not line.startswith("From "): continue
    words = line.split()
    if words[1] not in email:
    	email[words[1]] = 1
    else:
        email[words[1]] = email[words[1]] + 1


highest_email = None
highest_count = None
for key, value in email.items():
    if highest_count is None or highest_count < value:
        highest_email = key
        highest_count = value
print(highest_email, highest_count)