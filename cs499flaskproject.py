from flask import Flask


def say_hello(username = "Everyone"):
    return '<p>Hello %s!</p>\n' % username


header_text = '''
    <html>\n<head> <title>CS499 Flask Project </title> </head>\n<body>'''
instructions = '''
    <p><em>Mission Statement</em>: CS499 Python web application using flask framework</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'


application = Flask(__name__)


application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))


application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))


if __name__ == "__main__":

    application.debug = True
    application.run()
