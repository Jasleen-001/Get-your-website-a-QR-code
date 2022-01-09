import qrcode
value=input("Enter a link or text whose qrcode you want to generate: ")
myqr=qrcode.make(value)
print("Qr code for your file is generated and ready to be downloaded! ")
name=input("Enter name for your qrcode image: ")+".png"
myqr.save(name)
