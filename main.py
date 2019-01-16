from api import getAllRating, getRating
import json

id = 192003
data = getAllRating(id)

output = json.dumps(data, indent=2)

file = open("data-" + str(id) + ".json", "w")
file.write(output)
file.close()
