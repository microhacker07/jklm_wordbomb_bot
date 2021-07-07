import rpa as r

r.init()
room_code = input("Room code: ")
r.url('https://jklm.fun/' + room_code)
#r.type('//*[@type="text"]', 'nat_bot[enter]')
#r.type('nat_bot[enter]')
r.click('//*[@name="Join game"]')
print(r.read('result-stats'))
r.snap('page', 'results.png')
#r.close()
