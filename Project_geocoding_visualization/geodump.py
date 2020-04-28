import sqlite3
import json
import codecs

'''2. This program visualizes the data by reading the database and writing 
the file (where.js) with the location, latitude, and longitude in 
the form of executable JavaScript code.
'''

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

# Read db and write in js file
cur.execute('SELECT * FROM Locations')
fhand = codecs.open('where.js', 'w', "utf-8") 
fhand.write("myData = [\n")
count = 0
for row in cur :
    data = str(row[1].decode())
    try: js = json.loads(str(data))
    except: continue

    if not('status' in js and js['status'] == 'OK') : continue

    # Identify data in json in db
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    if lat == 0 or lng == 0 : continue
    where = js['results'][0]['formatted_address']
    where = where.replace("'", "")
    try :
        print(where, lat, lng)
        # Write data into where.js
        count = count + 1
        if count > 1 : fhand.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(output)
    except:
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")

