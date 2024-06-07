import qrcode
qr = qrcode.make('https://leetcode.com/u/divyansh7010/')
qr.save('qr.png')
print('Qr code is generated.')