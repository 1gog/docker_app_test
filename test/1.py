
def run_sql(sql):
	print(sql)

Databases = ('db1', 'db2', 'db3')
for item in Databases:
	sql = "DROP DATABASE {}".format( item )
	run_sql(sql)

