
import psycopg

conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="python_fast_api",
    user="postgres",
    password="balamurugan"
)

cursor = conn.cursor()
try:
    # create_table_query = """
    #     CREATE TABLE IF NOT EXISTS users (
    #         id SERIAL PRIMARY KEY,
    #         name VARCHAR(100) NOT NULL,
    #         age INT NOT NULL,
    #         place VARCHAR(100) NOT NULL
    #     )
    # """
    # cursor.execute(create_table_query)
    # conn.commit()
    # print("Table created successfully!")

    # name = input("Enter your name: ")
    # age = int(input("Enter your age: "))
    # place = input("Enter your place: ")

    # query = """
    #     INSERT INTO users (name, age, place)
    #     VALUES (%s, %s, %s)
    # """
    # cursor.execute(query, (name, age, place))
    # conn.commit()
    # print("User saved successfully!")
    # cursor.close()
    # conn.close()

    select_query = "SELECT * FROM users"
    cursor = conn.cursor()
    cursor.execute(select_query)
    result = cursor.fetchall()
    for row in result:
        print(row)

        with open("users.txt", "a") as file:
            for row in result:
                file.write(f"{row}\n")
except Exception as e:
    print("Error creating table:", e)
finally:
    cursor.close()
    conn.close()