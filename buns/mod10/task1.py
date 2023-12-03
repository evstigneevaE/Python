import requests
import json


data = json.loads(requests.get('https://swapi.dev/api/starships/10').text)


pilots = []


for pilot in data['pilots']:
 
    pilot_info_all = json.loads(requests.get(pilot).text)
 
    
    pilot_info = {'name': pilot_info_all['name'],               
                  'height':pilot_info_all['height'],           
                  'mass': pilot_info_all['mass'],              
                  'homeworld': json.loads(requests.get(pilot_info_all['homeworld']).text)['name'], 
                  'homeworld_url': pilot_info_all['homeworld']} 
   
    pilots.append(pilot_info)
    

new_data = {'name': data['name'],                                      
            'max_atmosphering_speed': data['max_atmosphering_speed'],  
            'starship_class': data['starship_class'],                  
            'pilots': pilots}                                        


with open('info_starship.json', 'w') as file:
    
    json.dump(new_data, file, indent=4)


print(json.dumps(new_data, indent=4))




"""
вывод:

{
    "name": "Millennium Falcon",
    "max_atmosphering_speed": "1050",
    "starship_class": "Light freighter",
    "pilots": [
        {
            "name": "Chewbacca",
            "height": "228",
            "mass": "112",
            "homeworld": "Kashyyyk",
            "homeworld_url": "https://swapi.dev/api/planets/14/"
        },
        {
            "name": "Han Solo",
            "height": "180",
            "mass": "80",
            "homeworld": "Corellia",
            "homeworld_url": "https://swapi.dev/api/planets/22/"
        },
        {
            "name": "Lando Calrissian",
            "height": "177",
            "mass": "79",
            "homeworld": "Socorro",
            "homeworld_url": "https://swapi.dev/api/planets/30/"
        },
        {
            "name": "Nien Nunb",
            "height": "160",
            "mass": "68",
            "homeworld": "Sullust",
            "homeworld_url": "https://swapi.dev/api/planets/33/"
        }
    ]
}

Process finished with exit code 0


"""
