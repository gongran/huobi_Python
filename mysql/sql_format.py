def format_sql(table, obj: dict) -> str:
    cols = ','.join(obj.keys())
    values = ','.join(obj.values())
    sql = "insert into {table} ({cols}) values ({values})".format(table=table, cols=cols, values=values)
    return


def format_sqls(table, objs: list) -> str:
    obj = objs.__getitem__(0)
    cols = ','.join(obj.keys())
    values = get_values_str(objs)
    sql = "insert into {table} ({cols}) values {values}".format(table=table, cols=cols, values=values)
    return sql


def get_values_str(objs: list):
    values = []
    for obj in objs:
        values.append("({sqlValue})".format(sqlValue=','.join("'%s'" % o for o in obj.values())))
    return ",".join(values)

# format_sqls("coin", [{"a": "1", "b": "2"}, {"a": "3", "b": "4"}])
