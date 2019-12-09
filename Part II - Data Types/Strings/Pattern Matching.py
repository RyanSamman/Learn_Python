import re
match = re.match('Hello (.*) world','Hello Python world')            # (.*) is the thing that may vary
print("\'"+match.group(1)+"\'")

match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home/lumberjack')
print(match.groups())


