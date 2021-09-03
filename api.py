import urllib.request
import json
import folium
url = "https://openapi.gg.go.kr/Ggdspsnphstrnfaclt?TYPE=json&KEY=38e39f42cb3941e1a3e46fb13259827f&pSize=1000"
req = urllib.request.urlopen(url)
res = req.readline()
j = json.loads(res)
#REFINE_WGS84_LOGT': '126.7648528', 'REFINE_WGS84_LAT': '37.70312098'}
map_osm = folium.Map(location=[37.566345, 126.977893])
for i in range (0, len (j["Ggdspsnphstrnfaclt"][1]["row"])):
    folium.Marker([j["Ggdspsnphstrnfaclt"][1]["row"][i]["REFINE_WGS84_LAT"],j["Ggdspsnphstrnfaclt"][1]["row"][i]["REFINE_WGS84_LOGT"]],popup=j["Ggdspsnphstrnfaclt"][1]["row"][i]["INST_NM"],icon=folium.Icon(color='blue',icon='info-sign')).add_to(map_osm)
map_osm.save('templates/map.html')
