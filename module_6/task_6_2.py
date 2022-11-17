import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def execute_sql(conn, sql):
    """ Execute sql
    :param conn: Connection object
    :param sql: a SQL script
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

def add_director(conn, director):
    """
    Create a new director into the directors table
    :param conn:
    :param director:
    :return: director id
    """
    sql = 'INSERT INTO directors(name) VALUES(?)'
    cur = conn.cursor()
    cur.execute(sql, director)
    conn.commit()
    return cur.lastrowid

def add_movie(conn, movie):
    """
    Create a new movie into the movies table
    :param conn:
    :param movie:
    :return: movie id
    """
    sql = '''INSERT INTO movies(director_id, title, year, description)
             VALUES(?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, movie)
    conn.commit()
    return cur.lastrowid

def select_all(conn, table):
   """
   Query all rows in the table
   :param conn: the Connection object
   :return:
   """
   cur = conn.cursor()
   cur.execute(f"SELECT * FROM {table}")
   rows = cur.fetchall()

   return rows

def select_where(conn, table, **query):
    """
    Query tasks from table with data from **query dict
    :param conn: the Connection object
    :param table: table name
    :param query: dict of attributes and values
    :return:
    """
    cur = conn.cursor()
    qs = []
    values = ()
    for k, v in query.items():
        qs.append(f"{k}=?")
        values += (v,)
    q = " AND ".join(qs)
    cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
    rows = cur.fetchall()
    return rows

def update(conn, table, id, **kwargs):
    """
    update status, begin_date, and end date of a task
    :param conn:
    :param table: table name
    :param id: row id
    :return:
    """
    parameters = [f"{k} = ?" for k in kwargs]
    parameters = ", ".join(parameters)
    values = tuple(v for v in kwargs.values())
    values += (id, )

    sql = f''' UPDATE {table}
                SET {parameters}
                WHERE id = ?'''
    try:
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        print(f"Update for {id}")
    except sqlite3.OperationalError as e:
        print(e)

def delete_where(conn, table, **kwargs):
    """
    Delete from table where attributes from
    :param conn:  Connection to the SQLite database
    :param table: table name
    :param kwargs: dict of attributes and values
    :return:
    """
    qs = []
    values = tuple()
    for k, v in kwargs.items():
        qs.append(f"{k}=?")
        values += (v,)
    q = " AND ".join(qs)

    sql = f'DELETE FROM {table} WHERE {q}'
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()
    print(f"Deleted row")

def delete_all(conn, table):
    """
    Delete all rows from table
    :param conn: Connection to the SQLite database
    :param table: table name
    :return:
    """
    sql = f'DELETE FROM {table}'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    print(f"Deleted all rows in table {table}")

if __name__ == "__main__":

    create_movies_sql = """
    -- projects table
    CREATE TABLE IF NOT EXISTS movies (
    id integer PRIMARY KEY,
    director_id integer NOT NULL,
    title text NOT NULL,
    year integer NOT NULL,
    description text,
    FOREIGN KEY (director_id) REFERENCES directors (id)
    );
    """

    create_directors_sql = """
    -- zadanie table
    CREATE TABLE IF NOT EXISTS directors (
    id integer PRIMARY KEY,
    name VARCHAR(250) NOT NULL
    );
    """

    db_file = "./module_6/database_movies.db"

    conn = create_connection(db_file)
    if conn is not None:
        print("Create tables")
        execute_sql(conn, create_directors_sql)
        execute_sql(conn, create_movies_sql)
        conn.close()

    director_1 = ["Jon Favreau"]
    director_2 = ["Shane Black"]

    conn = create_connection(db_file)
    if conn is not None:
        all_directors = select_all(conn, "directors")
        print(all_directors)
        director_1_id = add_director(conn, director_1)
        director_2_id = add_director(conn, director_2)

        movie_1 = (
            director_1_id,
            "Iron Man",
            2008,
            "Description 1"
        )
        movie_2 = (
            director_1_id,
            "Iron Man 2",
            2010,
            "Description 2"
        )
        movie_3 = (
            director_2_id,
            "Iron Man 3",
            2013,
            "Description 3"
        )

        movie_1_id = add_movie(conn, movie_1)
        movie_2_id = add_movie(conn, movie_2)
        movie_3_id = add_movie(conn, movie_3)

        conn.commit()
        all_directors = select_all(conn, "directors")
        all_movies = select_all(conn, "movies")
        all_movies_from_director_1 = select_where(conn, "movies", director_id = director_1_id)
        conn.commit()
        print(all_directors)
        print(all_movies)
        print(all_movies_from_director_1)
        update(conn, "movies", movie_2_id, description = "new description")
        all_movies = select_all(conn, "movies")
        conn.commit()
        print(all_movies)
        delete_where(conn, "movies", id = movie_1_id)
        all_movies = select_all(conn, "movies")
        conn.commit()
        print(all_movies)
        delete_all(conn, "movies")
        delete_all(conn, "directors")
        all_directors = select_all(conn, "directors")
        all_movies = select_all(conn, "movies")
        conn.commit()
        print(all_directors)
        print(all_movies)
        conn.close