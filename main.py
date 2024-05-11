import pymysql


if __name__ == "__main__":
    try:
        with pymysql.connect(host="127.0.0.1", port=3306, user="root", password="") as connection:
            print("connected!")
            with connection.cursor() as cursor:
                pass

    except pymysql.Error as error:
        print(error)

