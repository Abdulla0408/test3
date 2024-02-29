import sqlite3 as sql

db = sql.connect('FN11.db')

cursor = db.cursor()

cursor.executescript('''
drop table if exists users;
drop table if exists courses;

create table if not exists courses(
    courese_id integer primary key autoincrement,
    course_name varchar(15)
);
               
create table if not exists users(
    user_id integer primary key autoincrement,
    full_name varchar(30),
    course_id integer references courses(course_id)               
);                   

insert into courses(course_name) values ('Python');
insert into users(full_name, course_id) values ('Abdulla Hayitboyev', 1);

''')

full_name = "Abdull Hayitboyev"
course_id = 1

cursor.execute(f'''
insert into users(full_name, course_id) values('{full_name}', {course_id}) 
''')


db.commit()
db.close()
    