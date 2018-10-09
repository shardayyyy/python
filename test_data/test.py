import string
import random
import datetime
from collections import OrderedDict

op_dict =OrderedDict()
op_dict['column_name1'] = 'pk'
op_dict['column_name2'] = 'varchar'
op_dict['column_name3'] = 'boolean'
op_dict['column_name4'] = 'number'
op_dict['column_name5'] = 'date'

fct_dict =OrderedDict()
fct_dict['column_name1'] = 'pk'
fct_dict['column_name2'] = 'varchar'
fct_dict['column_name3'] = 'boolean'
fct_dict['column_name4'] = 'number'
fct_dict['column_name5'] = 'date'

et_dict =OrderedDict()
et_dict['column_name1'] = 'pk'
et_dict['column_name2'] = 'varchar'
et_dict['column_name3'] = 'boolean'
et_dict['column_name4'] = 'number'
et_dict['column_name5'] = 'date'

eu_dict =OrderedDict()
eu_dict['column_name1'] = 'pk'
eu_dict['column_name2'] = 'varchar'
eu_dict['column_name3'] = 'boolean'
eu_dict['column_name4'] = 'number'
eu_dict['column_name5'] = 'date'

pm_dict =OrderedDict()
pm_dict['column_name1'] = 'pk'
pm_dict['column_name2'] = 'varchar'
pm_dict['column_name3'] = 'boolean'
pm_dict['column_name4'] = 'number'
pm_dict['column_name5'] = 'date'

cfi_dict =OrderedDict()
cfi_dict['column_name1'] = 'pk'
cfi_dict['column_name2'] = 'varchar'
cfi_dict['column_name3'] = 'boolean'
cfi_dict['column_name4'] = 'number'
cfi_dict['column_name5'] = 'date'

fl_dict =OrderedDict()
fl_dict['column_name1'] = 'pk'
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
    return '"' + ''.join(random.choice(chars) for _ in range(size)) + '"'

def get_number(size=3, chars=string.digits):
    return '"' + ''.join(random.choice(chars) for _ in range(size)) + '"'

def get_date():
    now = datetime.datetime.now()
    return '"' + now.strftime("%Y-%m-%d") + '"'

def get_boolean():
    return random.choice([True, False])



def generate_OP(f, count):
    for i in range(int(count)):
        f.write(generate_insert(op_dict, 'OP_TABLE_NAME'),)
        f.write(generate_values(op_dict, i+1))
        f.write('\n\n')

def generate_FCT(f, count):
    for i in range(int(count)):
        f.write(generate_insert(fct_dict, 'FCT_TABLE_NAME'),)
        f.write(generate_values(fct_dict, i+1))
        f.write('\n\n')

def generate_ET(f, count):
    for i in range(int(count)):
        f.write(generate_insert(et_dict, 'ET_TABLE_NAME'),)
        f.write(generate_values(et_dict, i+1))
        f.write('\n\n')

def generate_EU(f, count):
    for i in range(int(count)):
        f.write(generate_insert(eu_dict, 'EU_TABLE_NAME'),)
        f.write(generate_values(eu_dict, i+1))
        f.write('\n\n')

def generate_PM(f, count):
    for i in range(int(count)):
        f.write(generate_insert(pm_dict, 'PM_TABLE_NAME'),)
        f.write(generate_values(pm_dict, i+1))
        f.write('\n\n')

def generate_CFI(f, count):
    for i in range(int(count)):
        f.write(generate_insert(cfi_dict, 'CFI_TABLE_NAME'),)
        f.write(generate_values(cfi_dict, i+1))
        f.write('\n\n')

def generate_FL(f, count):
    for i in range(int(count)):
        f.write(generate_insert(fl_dict, 'FL_TABLE_NAME'),)
        f.write(generate_values(fl_dict, i+1))
        f.write('\n\n')


# --------------------------------------------------------------------------------

def generate_insert(dict, table_name):
    sql = "INSERT INTO "
    sql += table_name
    sql += "("
    col_names = ""
    for k, v in dict.iteritems():
        col_names += '"' + k + '"'
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

def generate_values(dict, pk):
    #print 'generating VALUES'
    col_values = ") values ("
    for k, v in dict.iteritems():
        if v == 'pk':
            col_values += str(pk)
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
f= open("insert.sql","w+")
generate_OP(f, 10)
generate_FCT(f, 6)
generate_ET(f, 6)
generate_EU(f, 6)
generate_PM(f, 6)
generate_CFI(f, 6)
generate_FL(f, 6)

# Close file when done
f.close()
