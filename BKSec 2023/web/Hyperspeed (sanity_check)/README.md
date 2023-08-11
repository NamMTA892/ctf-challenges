# Challenge 1: Multiple Redirects

## Name
Hyperspeed

## Description
This website is a piece of code I wrote when I was high, and I put a secret on it. However, I forgot everything I had done. Can you help me find my secret?

## Flag
BKSEC{93t_h1gH-yeT?}

## Deployment
```bash
docker compose up
```

## Solution
```bash
curl -v -L localhost:xxxx/3cst4sy 2>&1 | grep -i "^< location:"
```
