from collections import deque
import dns.resolver


def dnsexists(prefix, name):
    fullname = f"{prefix}{name}".strip(" ")
    print(f"dnsexists: {fullname}")
    try:
        answers = dns.resolver.resolve(f'{fullname}.com', 'SOA')
        print("EXISTS")
        #answers = dns.resolver.resolve('dnspython.org', 'SOA')
    except dns.resolver.LifetimeTimeout:
        print("DNS timed out after 5 seconds")
    except dns.resolver.NoNameservers:
        #Usually if pihole or corporate DNS blocked it
        print("Nameservers failed to answer query")
    except dns.resolver.NoAnswer:
        print("DNS response contain's no answer")
    except dns.resolver.NXDOMAIN:
        print("DNS query name does not exist")
        answers = []
#    print(len(answers))

if __name__ == '__main__':
    ## Need to match on ", n." but print out previous line
    ## Solution here using deque: https://stackoverflow.com/questions/52009831/print-a-number-of-previous-lines-after-matching-string-found-in-line-in-python
    prefix = ""
    line_history = deque(maxlen=1)
    with open('pg29765.txt') as text_file:
    #with open('shorttext.txt') as text_file:
        for line in text_file:
            if ", n." in line:
                ## lines with two or more words are false positives and empty strings as well
                if ((len(line_history.split(" ")) < 2) and (not line_history == "")):
                    #print(len(line_history.split(" ")))
                    print(line_history)
                    dnsexists(prefix, line_history)
            else:
                line_history = line.strip("\n").strip(".")
