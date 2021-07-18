authURL = ""
PortalURL = ""
clientID = ""
clientSecret = ""
dbdriverName = "r"
dbuserName = ""
dbPassword = ""
jobInterval = 1
schedulerThreadPoolSize = 10
dbIps = ""
abc =""

main_string = '{ \"PortalConfig\":{\"authURL\":\"'+ \
              authURL +'/oauth/token\",\"PortalURL\":\"'+ PortalURL + \
              '\",\"clientID\":\"' + \
              clientID + '\",\"clientSecret\":\"' + \
              clientSecret + '\"},\"runtimeDbConfig\":{\"dbdriverName\":\"'+ \
              dbdriverName + '\",\"dbIps\":\"' + \
              dbIps + '\",\"dbuserName\":\"' + \
              dbuserName + '\",\"dbPassword\":\"' + \
              dbPassword + '\"},\"jobInterval\":' + \
              str(jobInterval) + ',\"schedulerThreadPoolSize\":' + \
              str(schedulerThreadPoolSize) + '}'


outstr = main_string.replace('"', '\\"').replace('\n', '\\n')
outstr1 = outstr.replace('/', '\/')

print(outstr1)