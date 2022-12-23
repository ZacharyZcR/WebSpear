import sqlite3

class SQLite3Handle:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def insert(self, table_name, data):
        """
        插入数据
        :param table_name: 表名
        :param data: 数据字典，键是列名，值是列值
        """
        # 检查表是否存在
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        if not self.cursor.fetchone():
            # 如果表不存在，则创建表
            print('1')
            columns = ", ".join(data.keys())
            placeholders = ", ".join(["?"] * len(data))
            sql = f"CREATE TABLE {table_name} ({columns})"
            self.execute(sql)
            print('2')

        # 插入数据
        print('3')
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?"] * len(data))
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.execute(sql, tuple(data.values()))

    def execute(self, sql, params=()):
        self.cursor.execute(sql, params)
        self.conn.commit()

    def fetchall(self, sql, params=()):
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()

    def fetchone(self, sql, params=()):
        self.cursor.execute(sql, params)
        return self.cursor.fetchone()

    def create_table(self, table_name, columns):
        """
        创建表
        :param table_name: 表名
        :param columns: 列的列表，每一项是一个元组，包含列名和列类型
        """
        column_defs = ", ".join([f"{column[0]} {column[1]}" for column in columns])
        sql = f"CREATE TABLE {table_name} ({column_defs})"
        self.execute(sql)

    def query(self, table_name):
        """
        执行查询
        :param table_name: 表名
        :return: 查询结果的列表，每一项是一个元组
        """
        sql = f"SELECT * FROM {table_name}"
        self.cursor.execute(sql)
        return self.cursor.fetchall()



if __name__ == '__main__':
    helper = SQLite3Handle("mydatabase.db")
    helper.connect()
    print(helper.query('scan'))