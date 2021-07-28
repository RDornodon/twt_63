def filter_db(database, filters):
    filtered_db = database.copy()
    for filter_index, specific_filter in enumerate(filters):
        temp_db = []
        for row in filtered_db:
            if specific_filter in ('?', row[1][filter_index]):
                temp_db += [row]
        filtered_db = temp_db.copy()
    return filtered_db


for _ in range(int(input())):
    stupid_separator = ' || '
    field_separator = ', '
    name_separator = ': '
    N, filters = input().split(stupid_separator)
    filters = filters.split(field_separator)
    database = []
    for R in range(int(N)):
        properties, name = input().split(name_separator)
        properties = properties.split(field_separator)
        database += [[name, properties]]
    filtered_database = filter_db(database, filters)
    suspects = [record[0] for record in filtered_database]
    print(field_separator.join(suspects))
