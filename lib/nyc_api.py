import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "https://data.cityofchicago.org/resource/f7f2-ggz5.json"

    response = requests.get(URL)
    return response.content

  def program_agencies(self):
    # we use the JSON library to parse the API response into nicely formatted JSON
        programs_list = []
        programs = json.loads(self.get_programs())
        for program in programs:
            programs_list.append(program["city"])

        return programs_list

#programs = GetPrograms().get_programs()
#print(programs)

programs = GetPrograms()
agencies = programs.program_agencies()

for state in set(agencies):
    print(state)