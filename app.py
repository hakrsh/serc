from flask import Flask, render_template, request,redirect
import sqlite3 as sql
app = Flask(__name__)



@app.route('/')
def home():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("SELECT img FROM lab_banner;")
   imgs = cur.fetchall()
   cur.execute("SELECT info FROM about;")
   info = cur.fetchone()
   return render_template("index.html",imgs=imgs,info=info)

@app.route('/Gallery')
def gallery():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("SELECT img FROM lab_banner;")
   imgs = cur.fetchall()
   return render_template("gallery.html",imgs=imgs)

@app.route('/admin-about',methods=['GET', 'POST'])
def admin():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    if request.method == "POST" :
        about = request.form['about']
        con.execute("UPDATE about SET info = ?",(about,))
        con.commit()
        return redirect('/')
    else:
        cur.execute("SELECT info FROM about;")
        about = cur.fetchone()
        return render_template("admin.html",about=about)

@app.route('/admin-news',methods=['GET', 'POST'])
def adminNews():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    if request.method == "POST" :
        news = request.form['news']
        print(news)
        con.execute("UPDATE news SET html = ?",(news,))
        con.commit()
        return redirect('/news')
    else:
        cur.execute("SELECT html FROM news;")
        news = cur.fetchone()
        print(news[0])
        return render_template("admin-news.html",news=news)

@app.route('/admin-focus',methods=['GET', 'POST'])
def adminFocus():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    if request.method == "POST" :
        focus = request.form['focus']
        print(focus)
        con.execute("UPDATE focus SET html = ?",(focus,))
        con.commit()
        return redirect('/focus')
    else:
        cur.execute("SELECT html FROM focus;")
        focus = cur.fetchone()
        # print(focus[0])
        return render_template("admin-focus.html",focus=focus)

@app.route('/admin-posters',methods=['GET', 'POST'])
def adminPosters():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    if request.method == "POST" :
        posters = request.form['posters']
        print(posters)
        con.execute("UPDATE posters SET html = ?",(posters,))
        con.commit()
        return redirect('/showcase')
    else:
        cur.execute("SELECT html FROM posters;")
        posters = cur.fetchone()
        print(posters[0])
        return render_template("admin-posters.html",posters=posters)


@app.route('/projects')
def projects():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT html FROM projects;")
    rows = cur.fetchall()
    print(rows)
    return render_template("projects.html",rows=rows)

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/demos')
def demos():
    return render_template("demos.html")

@app.route('/demo1')
def demo1():
    return render_template("demo1.html")

@app.route('/demo2')
def demo2():
    return render_template("demo2.html")

# @app.route('/focus')
# def focus():
#     return render_template("focus-area.html")

@app.route('/links')
def links():
    return render_template("links.html")

@app.route('/news')
def news():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT html FROM news;")
    content = cur.fetchone()
    print(content[0])
    return render_template("news.html",content=content)


@app.route('/focus')
def focus():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT html FROM focus;")
    content = cur.fetchone()
    # print(content[0])
    return render_template("focus-area.html",content=content)

@app.route('/showcase')
def poster():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT html FROM posters;")
    content = cur.fetchone()
    print(content[0])
    return render_template("posters.html",content=content)

@app.route('/courses')
def courses():
    return render_template("teaching.html")

@app.route('/people')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   cur = con.cursor()

   cur.execute("SELECT l.id as id, t.name as class, l.img as image, l.name as name,t.display_text as post FROM 'lab_peopletype' as t,'lab_people' as l  where t.id=l.list_on_id")
   rows = cur.fetchall()
   
   cur = con.execute("SELECT name as class, display_text FROM lab_peopletype")  
   ids = cur.fetchall()

   return render_template("people.html",rows=rows,ids=ids)

   # return render_template("list.html",rows = rows)

@app.route('/personal/<x>', methods=['GET'])
def personal(x):
    #do your code here
    print(x)
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT id, name, img, email, homepage, phone, short_bio, study_one_line, personal_page, url, display_priority, interest FROM lab_people WHERE id = (?)",(x,))
    row = cur.fetchone()
    name = row[1]

    cur.execute("SELECT lc.name ,published_at, published_year, title, link, conf_type_id, authors_comma_separated, disabled, published_page FROM lab_publication l join lab_conferencetype lc on l.conf_type_id = lc.id WHERE authors_comma_separated LIKE ?",('%'+name+'%',))
    pubs = cur.fetchall()
    pubTypes = set()
    for i in pubs:
        pubTypes.add(i[0])
    return render_template("person.html",row=row,pubs=pubs, pubTypes=pubTypes)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@app.errorhandler(500)
def page_not_found(e):
    return render_template('404.html'), 500
if __name__ == '__main__':
   app.run(debug = True)