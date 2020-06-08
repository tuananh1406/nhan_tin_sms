# coding: utf-8
from ipaddress import IPv4Address
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService


# Lấy IP của điện thoại, cần cài pyairmore trên điện thoại trước
ip = input('Nhập IP của điện thoại: ')
ip_dien_thoai = IPv4Address(ip)
# Bắt đầu 1 session
session = AirmoreSession(ip_dien_thoai)
# Khởi tạo 1 dịch vụ quản lý tin nhắn
tin_nhan = MessagingService(session)
# Lấy lịch sử tin nhắn
ds_tin_nhan = tin_nhan.fetch_message_history()
# Gửi tin nhắn đến 1 số điện thoại
so_dien_thoai = input('Nhập số điện thoại: ')
noi_dung = input('Nhập nội dung tin nhắn: ')
tin_nhan.send_message(so_dien_thoai, noi_dung)
print('Đã gửi tin nhắn')
