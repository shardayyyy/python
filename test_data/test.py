import string
import random

op_dict = {}
op_dict['colunm_name1'] = 'int'
op_dict['colunm_name2'] = 'varchar'
op_dict['colunm_name3'] = 'boolean'
op_dict['colunm_name4'] = 'number'
op_dict['colunm_name5'] = 'date'

fct_dict = {}
fct_dict['colunm_name1'] = 'int'
fct_dict['colunm_name2'] = 'varchar'
fct_dict['colunm_name3'] = 'boolean'
fct_dict['colunm_name4'] = 'number'
fct_dict['colunm_name5'] = 'date'

et_dict = {}
et_dict['colunm_name1'] = 'int'
et_dict['colunm_name2'] = 'varchar'
et_dict['colunm_name3'] = 'boolean'
et_dict['colunm_name4'] = 'number'
et_dict['colunm_name5'] = 'date'

eu_dict = {}
eu_dict['colunm_name1'] = 'int'
eu_dict['colunm_name2'] = 'varchar'
eu_dict['colunm_name3'] = 'boolean'
eu_dict['colunm_name4'] = 'number'
eu_dict['colunm_name5'] = 'date'

pm_dict = {}
pm_dict['colunm_name1'] = 'int'
pm_dict['colunm_name2'] = 'varchar'
pm_dict['colunm_name3'] = 'boolean'
pm_dict['colunm_name4'] = 'number'
pm_dict['colunm_name5'] = 'date'

cfi_dict = {}
cfi_dict['column_name1'] = 'int'
cfi_dict['column_name2'] = 'varchar'
cfi_dict['column_name3'] = 'boolean'
cfi_dict['column_name4'] = 'number'
cfi_dict['column_name5'] = 'date'

fl_dict = {}
fl_dict['column_name1'] = 'int'
fl_dict['column_name2'] = 'varchar'
fl_dict['column_name3'] = 'boolean'
fl_dict['column_name4'] = 'number'
fl_dict['column_name5'] = 'date'


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def id_generator_int(size=3, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def get_int(size=3, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def get_varchar(size=6, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

def get_number(size=3, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def get_date():
    return '01/01/1900'

def get_boolean():
    return random.choice([True, False])



def generate_OP():
    print 'generating OP'

def generate_FCT():
    print 'generating FCT'

def generate_ET():
    print 'generating ET'

def generate_EU():
    print 'generating EU'

def generate_PM():
    print 'generating PM'

def generate_CFI():
    print 'generating CFI'

def generate_FL():
    print 'generating FL'

# --------------------------------------------------------------------------------

def generate_insert(dict, table_name):
    sql = "INSERT INTO "
    sql += table_name
    sql += "("
    col_names = ""
    for k, v in dict.iteritems():
        col_names += k
        col_names += ', '

    col_names = col_names[:-2]

    sql += col_names
    return sql
    #sql += ") values ("
    #sql_template = sql

    # generate randome values for the column values
    #count = 0
    #while count <= 2:
#        count += 1
#        for item in columns:
#            sql += '"'
#            sql += id_generator()
#            sql += '"'
#            sql += ', '
#            # remove the last 2 character which is a space and comma
#        sql = sql[:-2]
#        sql += ");\n\n"
#        if count <= 2:
#            sql += sql_template
#    print sql

def generate_values(dict):
    #print 'generating VALUES'
    col_values = ") values ("
    for k, v in dict.iteritems():
        if v == 'int':
            col_values += get_int()
            col_values += ', '
        elif v == 'varchar':
            col_values += get_varchar()
            col_values += ', '
        elif v == 'boolean':
            col_values += str(get_boolean())
            col_values += ', '
        elif v == 'number':
            col_values += get_number()
            col_values += ', '
        elif v == 'date':
            col_values += str(get_date())
            col_values += ', '
        else:
            col_values += get_varchar()
            col_values += ', '

    # remove the last 2 character which is a space and comma
    col_values = col_values[:-2]
    col_values += ");\n"
    return col_values


# --------------------------------------
#   MAIN PROGRAM
# --------------------------------------
print generate_insert(op_dict, 'OP_TABLE_NAME'),
print generate_values(op_dict)
