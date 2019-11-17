from mechanize import *
br = Browser()
br.open('https://www.brainscape.com/subjects/aws-s3')
html = br.response().readlines()
for line in html:
  print(line)
