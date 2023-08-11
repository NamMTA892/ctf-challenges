# Challenge 2: Python LFI (easy)

## Name
Poems

## Description
Cô A đã mở 1 trang web để việc dạy học của mình trở nên hiệu quả hơn. Tuy vậy trang web có 1 bí mật đằng sau. Bạn có thể tìm ra nó?

## Flag
BKSEC{p0em_1s_4_g00d_w4y_t0_s4y_ily}

## Deployment

```bash
docker compose up
```

## Solution
Visit /robots.txt, thấy được file system của challenge.

Hướng exploit sẽ là biến `poem` vừa được eval() mà user lại có thể control được.

Qua BurpSuite: `localhost:9000/poem?baitho=request.data` / phần body của request điền tên của file cần request. 

Truy cập phlag.txt -> được hint là phlag ở mọi nơi
`/proc/self/environ` sẽ là file cần đọc -> get flag.