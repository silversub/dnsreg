import dns.resolver

## Need to match on ", n." but print out previous line
## Potential solution here: https://stackoverflow.com/questions/52009831/print-a-number-of-previous-lines-after-matching-string-found-in-line-in-python
count = 0
with open('test.txt') as text_file:
    for linenum, line in enumerate(text_file):
        count += 1
        if ", n." in line:
            print(linenum)
            print(line)
#try:
#    answers = dns.resolver.resolve('google.com', 'SOA')
#    #answers = dns.resolver.resolve('dnspython.org', 'SOA')
#except dns.resolver.NXDOMAIN:
#    print("DNS query name does not exist")
#    answers = []
#print(len(answers))
