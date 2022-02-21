# DNS Registration Lookup

Purpose is to find if specific domain names are registered using a "color-noun" pattern.

Define a color and then interate through all nouns that have the same first letter as that color.

Ex: bluebolt, blueblaze, bluebastion etc...


## Dictionary
https://stackoverflow.com/questions/6441975/where-can-i-download-english-dictionary-database-in-a-text-format
https://www.gutenberg.org/ebooks/29765
https://www.gutenberg.org/cache/epub/29765/pg29765.txt

Use `, n.` to find the noun. Then grab the line above it

## DNS lookup
If a SOA exits then we know it's taken.
```
$ dig +short SOA google.com
ns1.google.com. dns-admin.google.com. 429863821 900 900 1800 60
```

Bash
```bash
function check_tld {
  # $dns is not quoted so it's ignored if empty
  if [ -z "$(dig +short SOA "$1" $dns)" ]; then
    echo "$(tput setaf 2)${1}$(tput sgr0)"
  else
    echo "$(tput setaf 1)${1}$(tput sgr0)" >&2
  fi
}
```
https://github.com/jomo/tld_checker/blob/master/tld_checker.sh#L15-L22


Python
https://pypi.org/project/dnspython/
https://stackoverflow.com/questions/13842116/how-do-we-get-txt-cname-and-soa-records-from-dnspython

```python
answers = dns.resolver.query('google.com', 'SOA')
print 'query qname:', answers.qname, ' num ans.', len(answers)

if len < 1:
    print("Available")
```
