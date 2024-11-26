import sqlite3

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command (id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null, 'android studio', 'C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe')"
# cursor.execute(query)
# con.commit()

# query = "INSERT INTO sys_command VALUES (null, 'one note', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe')"
# cursor.execute(query)
# con.commit()

# query = "INSERT INTO sys_command VALUES (null, 'browser', 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')"
# cursor.execute(query)
# con.commit()

# query = "INSERT INTO sys_command VALUES (null, 'vs code', 'C:\\Users\\hnban\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')"
# cursor.execute(query)
# con.commit()

# query = "INSERT INTO sys_command VALUES (null, 'discord', 'C:\\Users\\hnban\\AppData\\Local\\Discord\\app-1.0.9168\\Discord.exe')"
# cursor.execute(query)
# con.commit()

# query = "INSERT INTO sys_command VALUES (null, 'spotify', 'C:\\Users\\hnban\\AppData\\Roaming\\Spotify\\Spotify.exe')"
# cursor.execute(query)
# con.commit()

# query = "INSERT INTO sys_command VALUES (null, 'messenger', 'C:\\Program Files\\WindowsApps\\FACEBOOK.317180B0BB486_2150.23.211.0_x64__8xx8rvfyw5nnt\\app\\Messenger.exe')"
# cursor.execute(query)
# con.commit()


#(cách xóa bảng)
# delete_query = "DELETE FROM sys_command WHERE name = 'discord'" 
# cursor.execute(delete_query)
# con.commit()









# query ="CREATE TABLE IF NOT EXISTS web_command (id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null, 'canva', 'https://www.canva.com/')"
# cursor.execute(query)
# con.commit()

# query = "INSERT INTO web_command VALUES (null, 'youtube', 'https://www.youtube.com/')"
# cursor.execute(query)
# con.commit()

# query = "INSERT INTO web_command VALUES (null, 'github', 'https://github.com/')"
# cursor.execute(query)
# con.commit()

# delete_query = "DELETE FROM web_command WHERE name = 'monkeytype'"
# cursor.execute(delete_query)
# con.commit()

# query = "INSERT INTO web_command VALUES (null, 'monkey type', 'https://monkeytype.com/')"
# cursor.execute(query)
# con.commit()

# query = "INSERT INTO web_command VALUES (null, 'facebook', 'https://web.facebook.com/')"
# cursor.execute(query)
# con.commit()
