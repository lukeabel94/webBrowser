from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print "start tag:", tag

	def handle_endtag(self, tag):
		print "end tag:", tag

	def handle_data(self, data):
		print "data : ", data

# instantiate parser and feed some html
parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
		'<body><h1>Parse me!</h1></body></html>')
