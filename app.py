from flask import Flask, request, render_template
app = Flask(__name__)

visit_count = {}
 
@app.route('/')
@app.route('/home')
def hello():
    ip = request.remote_addr
    if ip in visit_count:
        visit_count[ip] += 1
    else:
        visit_count[ip] = 1
    
    total_visits = sum(visit_count.values())
    return render_template('index.html', visits=visit_count[ip], total_visits=total_visits, visit_ip=ip)

if __name__ == '__main__':
    app.run(debug=True)