import rpa as r

# Inital test
r.init()
r.url('https://www.google.com')
r.type('//*[@name="q"]', 'decentralization[enter]')
print(r.read('result-stats'))
r.snap('page', 'results.png')
r.close()


"""
# Auto login to discord
r.init()
r.url('https://discord.com/login')
r.type('Email', 'bock.nathaniel@gmail.com')
r.type('Password', '123456[enter]')
r.wait(3)
r.snap('page', 'result.png')
r.close()
"""

"""
# Currently trying to use openCV and Tesseract
r.init(visual_automation = True)
r.url('https://discord.com/login')
# Don't need to login everytime
# Waits for discord to startup
r.wait(5)

# grabs mouse position a few times
for i in range(0, 10):
    print("XY: " + str(r.mouse_xy()))

# Should use openCV to find the jellyfin icon for the discord server
r.click('jellyfin.png')
r.snap('page', 'result.png')
r.close()
"""
