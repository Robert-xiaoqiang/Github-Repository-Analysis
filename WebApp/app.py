from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/introduction/')
def introduction():
	return render_template('introduction.html')

@app.route('/member/')
def member():
	return render_template('member.html')

@app.route('/achievements/')
def achievements():
	return render_template('achievements.html')

if __name__ == '__main__':
	app.run(debug = False)