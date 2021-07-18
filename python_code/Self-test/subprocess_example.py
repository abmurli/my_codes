import subprocess
try:
    p = subprocess.Popen(['ls', 'l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()
    print(output)
except Exception as e:
    print(e)
# try:
#     c = subprocess.check_call(['ls', 'l'])
#     print(c)
# except Exception as e:
#     print(e)
