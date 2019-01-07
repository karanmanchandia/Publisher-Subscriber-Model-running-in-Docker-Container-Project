from flask import Flask, request
import os
import sys
from io import StringIO
import contextlib

@contextlib.contextmanager
def stdoutIO(stdout=None):
	old = sys.stdout
	if stdout is None:
		stdout = StringIO()
	sys.stdout = stdout
	yield stdout
	sys.stdout = old

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def hello():
	output = ""

	if request.form:

		text_in = request.form['test']
		
		ok = False

		with stdoutIO() as s:
			try:
				exec(text_in)
				ok = True
			except Exception as e:
				output = str(e)
			
		if ok:
			output = s.getvalue()

	html = '<h1 align="center" style="background-color:DodgerBlue;">Distributed Systems Project 2</h1><h3 align="center" style="background-color:DodgerBlue;">Phase 1</h3><h6 align="right";">Developed By Karan Manchandia (karanman)<br/> Sai Saket Regulapati (saisaket)</h6><h4 align="center" >Type your Python code here</h4><form method="POST" action="/"><center><textarea name="test"style="margin: 0px; width: 561px; height: 320px;"></textarea></center><br/><center><input type="submit" value="Debug and Run"></center></form><h4 align="center" >Output:</h4><center><h3>{output}</h3></center>'

	return html.format(output=output)

def execute(code_string):
	os.mkdir("Temp")



if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8888)


