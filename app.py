from flask import Flask, render_template, request, redirect
import datetime
import pytz # timezone 
import requests
import os



app = Flask(__name__)

# If user goes to home page
@app.route('/', methods=['GET'])
def home_page():
	return render_template('index.html')


# If name is provided in URL
@app.route('/<name>')
def profile(name):
	return render_template('index.html', name=name)


@app.route('/add_numbers', methods=['GET','POST'])
def add_numbers_post():
	  # --> ['5', '6', '8']
	  # print(type(request.form['text']))
	  if request.method == 'GET':
	  	return render_template('add_numbers.html')
	  elif request.method == 'POST':
  	      print(request.form['text'].split())
  	      total = 0
  	      try:
  	      	for str_num in request.form['text'].split():
  	      		total += int(str_num)
  	      	return render_template('add_numbers.html', result=str(total))
  	      except ValueError:
  	      	return "Easy now! Let's keep it simple! 2 numbers with a space between them please"


@app.route('/shopping_list', methods=['GET','POST'])
def shopping_list_post():
	  # --> ['5', '6', '8']
	  # print(type(request.form['text']))

    if request.method == 'GET':
      return render_template('shopping_list.html')
    elif request.method == 'POST':
          print(request.form['text'].split())
          
          shop_list = []
          try:
            for item in request.form['text'].split():
              
              shop_list.append(item)

              
              
            return render_template('shopping_list.html', result="\n".join([str(item) for item in shop_list]))
          except ValueError:
            return "Easy now! Let's keep it simple! Just words with a space between them"
          
  	      
@app.route('/time', methods=['GET','POST'])
def time_post():
    # --> ['5', '6', '8']
    # print(type(request.form['text']))

    if request.method == 'GET':
      return render_template('time.html')
    elif request.method == 'POST':
          print(request.form['text'].split())
          
          for item in request.form['text'].split():
            answer = (datetime.datetime.now(pytz.timezone("Europe/Dublin")).strftime('Time = ' + '%H:%M:%S' + ' GMT ' + ' Year = ' + '%d-%m-%Y'))
            #answer = datetime.datetime.now().strftime('Time == ' + '%H:%M:%S' + ' Year == ' + '%d-%m-%Y')
            #answer = datetime.datetime.now().strftime('%Y-%m-%d \n %H:%M:%S')

              
              
            return render_template('time.html', result=answer)
	

@app.route('/LOC', methods['GET', 'POST'])
def loc_post():
	#This program solves triangles using the law of cosines
	import math
	if request.method == 'GET':
		return render_template('loc.html')
	elif request.method == 'POST':
		triangle_type = request.form['Do you have an SSS or SAS triangle?'])
		if str(triangle_type) == "SAS":
			A = float(input("Please enter angle A in degrees: "))
			b = float(input("Please enter side b: "))
			c = float(input("Please enter side c: "))

			a = math.sqrt(b**2+c**2-2*b*c*math.cos(math.radians(A)))
			B = math.degrees(math.acos((b**2-a**2-c**2)/(-2*a*c)))
			C = 180 - A - B
			answer = ["Side a is: ", round(a,2),
				  "Angle B is: ", round(B,2),
				  "Angle C is: ", round (C,2)]
			return render_template('loc.html', result=answer)

		elif str(triangle_type) == "SSS":
			a = float(input("Please enter side a: "))
			b = float(input("Please enter side b: "))
			c = float(input("Please enter side c: "))

			A = math.degrees(math.acos((a**2-b**2-c**2)/(-2*b*c)))
			B = math.degrees(math.acos((b**2-a**2-c**2)/(-2*a*c)))
			C = 180 - A - B
			answer = ["Angle A is: ":round(A,2),
				  "Angle B is: ": round(B,2),
				  "Angle C is: ": round(C,2)]
			return render_template('loc.html', result=answer)
		else:
		    print("Sorry, we don't recognize that. Try using capital letters. If this does not work, then your triangle must be solved by other means




@app.route('/python_apps')
def python_apps_page():
	# testing stuff
	return render_template('python_apps.html')


@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/blog', methods=['GET'])
def blog_page():
  return render_template('blog.html')

app.run(host=os.getenv('IP', '0.0.0.0'), port = int(os.getenv('PORT', 8080)))

if __name__ == '__main__':
	app.run(debug=False)
