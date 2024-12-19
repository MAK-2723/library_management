from flask import Flask,request,jsonify
from models import init_db
from auth import generate_token,verify_token
from database import execute_query

app=Flask(__name__)

#Middleware for Authentication
@app.before_request
def authenticate():
    exempt_endpoints = ['/login']
    if request.endpoint not in exempt_endpoints:
        token=request.headers.get('Authorization')
        if not token or not verify_token(token):
            return jsonify({"error":"Unauthorized"}), 401
            
#User Login
@app.route('/login',methods=['POST'])
def login():
    data=request.json
    user=execute_query("SELECT id,password FROM members WHERE email=?",(data['email'],),fetchone=True)
    #Check if user exists
    if not user:
        return jsonify({"error":"Invalid email or password"}), 403 
    #Check pass if user found       
    if user[1]==data['password']:
        return jsonify({"token":generate_token(user[0])})
    return jsonify({"error":"Invalid credentials"}), 403

#CRUD for Books
@app.route('/books',methods=['GET','POST'])
def books():
    if request.method=='GET':
        page=int(request.args.get('page',1))
        per_page=5
        offset=(page-1)*per_page
        books=execute_query("SELECT * FROM books LIMIT ? OFFSET ?",(per_page,offset),fetchall=True)
        return jsonify(books)
    
    if request.method=='POST':
        data=request.json
        execute_query("INSERT INTO books (title,author,published_date,pages) VALUES (?,?,?,?)",(data['title'],data['author'],data['published_date'],data['pages']))
        return jsonify({"message":"Book added successfully"}), 201
    
@app.route('/books/<int:book_id>',methods=['PUT','DELETE'])
def manage_book(book_id):
    if request.method=='PUT':
        data=request.json
        execute_query("UPDATE books SET title=? author=? published_date=? pages=? WHERE id=?",(data['title'],data['author'],data['published_date'],data['pages'],book_id))
        return jsonify({"message":"Book updated successfully"})
    
    if request.method=='DELETE':
        execute_query("DELETE FROM books WHERE id ?",(book_id,))
        return jsonify({"message":"Book deleted successfully"})

#CRUD for Members
@app.route('/members',methods=['GET','POST'])
def members():
    if request.method=='GET':
        members=execute_query("SELECT id,name,email FROM members",fetchall=True)
        return jsonify(members)
    if request.method=='POST':
        data=request.json
        execute_query("INSERT INTO members (name,email,password) VALUES (?,?,?)",(data['name'],data['email'],data['password']))
        return jsonify({"message":"Book added successfully"}), 201
    
@app.route('/members/<int:member_id>',methods=['PUT','DELETE'])
def manage_member(member_id):
    if request.method=='PUT':
        data=request.json
        execute_query("UPDATE members SET name=? email=? password=? WHERE id=?",(data['name'],data['email'],data['password'],member_id))
        return jsonify({"message":"Member updated successfully"})
    
    if request.method=='DELETE':
        execute_query("DELETE FROM members WHERE id ?",(member_id,))
        return jsonify({"message":"Member deleted successfully"})

if __name__=="__main__":
    init_db()
    app.run(debug=True)
