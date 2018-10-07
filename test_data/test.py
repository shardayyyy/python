import string
import random
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def id_generator_int(size=3, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


columns = ['"column1"','"column2"','"column3"','"column4"','"column5"','"column6"','"column7"','"column8"','"column9"','"column10"']

table_name = '"TABLE_NAME"'

sql = "insert into "
sql += table_name
sql += "("


col_names = ""
for col in columns:
    col_names += col
    col_names += ', '

col_names = col_names[:-2]

sql += col_names
sql += ") values ("
sql_template = sql

# generate randome values for the column values
count = 0
while count <= 2:
    count += 1
    for item in columns:
        sql += '"'
        sql += id_generator()
        sql += '"'
        sql += ', '
        # remove the last 2 character which is a space and comma
    sql = sql[:-2]
    sql += ");\n\n"
    if count <= 2:
        sql += sql_template
print sql
