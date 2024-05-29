a="""
POST /submit
name=lalitha&email=lalithahari2002%40gmail.com&phone=09030391412
Accepted connection from ('127.0.0.1', 60504)
Received request:
GET /favicon.ico HTTP/1.1
Host: 127.0.0.1:8080
Connection: keep-alive
sec-ch-ua: "Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60
sec-ch-ua-platform: "Windows"
Accept: image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: no-cors
Sec-Fetch-Dest: image
Referer: http://127.0.0.1:8080/submit
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9


GET /favicon.ico
"""
b=a.split("/n ")
# print(b)
c=b[0].split("&")
# print("new")
# print(c)
dataname=c[0].split("=")
# print(d)
name= dataname[1]
print(name)
dataemail=c[1].split("=")
email=dataemail[1]
print(email)
datacontact=c[2].split("=")
# print(datacontact)
contactnumber=datacontact[1][1:11]
print(contactnumber)
# contactnumber=datacontact[1].split("\")


