


def search(name):
    sql = f"""
    select * FROM sayt_product sp 
	WHERE lower  ("name") like lower ("%{name}%")


"""