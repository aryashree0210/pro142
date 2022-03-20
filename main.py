from flask import Flask,jsonify,request
import csv
all_article=[] 
with open('articles.csv',encoding='utf-8')as f:
    reader=csv.reader(f)
    data=list(reader)
    all_article=data[1:]
    
liked_article=[]
not_liked_article=[]
did_not_watch=[]
app=Flask(__name__)
@app.route('/get-article')

def get_article():
    return jsonify({
        'data':all_article[0],
        'status':'success',
    })

@app.route('/liked-article',methods=['POST'])
def liked_article():
    article=all_article[0]
    all_article=all_article[1:]
    liked_article.append(article)
    return jsonify({
        'status':'success'
    }),201
  
 
@app.route('/un-liked-article',methods=['POST'])
def un_liked_article():
    article=all_article[0]
    all_article=all_article[1:]
    not_liked_article.append(article)
    return jsonify({
        'status':'success'
    }),201 

    
