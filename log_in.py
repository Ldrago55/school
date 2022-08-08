<form name="loginform" method="post" action="userinfo.php">
import requests
url = 'http://example.com/userinfo.php'
values = {'username': 'user',
          'password': 'pass'}

r = requests.post(url, data=values)
# print r.content


from webbot import Browser 
web = Browser()
web.go_to('google.com') 
web.click('Sign in')
web.type('mymail@gmail.com' , into='Email')
web.click('NEXT' , tag='span')
web.type('mypassword' , into='Password' , id='passwordFieldId') # specific selection
web.click('NEXT' , tag='span') # you are logged in ^_^