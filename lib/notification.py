#/usr/bin/python3
'''
Created on 2023/08/24

@author: ZL Chen
@title: Notification
'''

from requests import post

class line(object):
	def send_message(self, message):
		headers = {
			'Authorization': 'Bearer ' + '77Zfj9AKBfazjmzYA6BkvpcC8ukQOdTBd1Vj7W4K7sa', # Quick Test Group Notification
			'Content-Type': 'application/x-www-form-urlencoded'
		}
		params = {
			'message': message
		}
		r = post('https://notify-api.line.me/api/notify', headers=headers, params=params)
		print('Status code number:', r.status_code)  #200