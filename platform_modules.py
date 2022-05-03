import platform
from datetime import datetime
os = platform.system()
processor = platform.processor()
dir  = print(dir(platform))

date = datetime.now()
new_date = date.strftime("%d, %a %B %Y")
print(os, processor)
print(new_date)
