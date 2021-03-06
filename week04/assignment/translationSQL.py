import pandas as pd
import pymysql

# connection = pymysql.connect(host='localhost',
#                         user='root',
#                         password='a123456',
#                         db='maoyan',
#                         charset='utf8mb4',
#                         port= 3306)

# 请将以下的 SQL 语句翻译成 pandas 语句：

# 1. SELECT * FROM data;
# sql = 'SELECT * FROM movies'
# cur = connection.cursor()
# cur.execute(sql)
# result = cur.fetchall()
# print(result)

df = pd.read_sql(sql, connection)

# 2. SELECT * FROM data LIMIT 10;
df.loc[:10]

# 3. SELECT id FROM data;  //id 是 data 表的特定一列
df['id']

# 4. SELECT COUNT(id) FROM data;
len(df)

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
df.loc[(df['id'] >= 1000) & (df['age'] <= 30)]

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
df.groupby('id')['order_id'].nunique()

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
pd.merge(t1, t2, how='inner', on=['id', 'id'])

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
pd.concat([df1, df2]).drop_duplicates()

# 9. DELETE FROM table1 WHERE id=10;
delete_row = df[df["id"]==10].index
df.drop(delete_row)

# 10. ALTER TABLE table1 DROP COLUMN column_name;
df.drop(columns=['column_name'])

# cur.close()
# connection.close()
