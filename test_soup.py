from bs4 import BeautifulSoup

HTML="""
<html>
<title>
	Welcome Page
</title>
<body>
	<p1> This is first paragraph </p1>
	<p2> This is first paragraph </p2>
	<p3> This is first paragraph </p3>
	<h1> This is heading1 </h1>
	<h2> This is heading2 </h2>
	<h3> This is heading3 </h3>
	<h4> This is heading4 </h4>
	<h5> This is heading5 </h5>
	<h6> This is heading6 </h6>
	<li> Ansible </li>
	<li> Dockers </li> 
	<li> kubernetes </li>		
</body>
</html>

"""
soup=BeautifulSoup(HTML,'html.parser')
#print(type(soup))
print(soup.find('title'))
print(soup.find('title').text)
print(soup.find('title').string)
print(soup.findAll('li'))
print("Technologies....")
for skills in soup.findAll('li'):
    print(skills.text)

