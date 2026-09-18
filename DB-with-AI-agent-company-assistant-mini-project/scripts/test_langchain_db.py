from tools.db_tool import db

print("Tables:")
print(db.get_usable_table_names())


print("\nSchema:")
print(db.get_table_info())