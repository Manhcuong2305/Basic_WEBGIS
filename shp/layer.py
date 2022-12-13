from .models import gsLayer


from geo.Geoserver import Geoserver

geo = Geoserver('http://127.0.0.1:8080/geoserver', username='admin', password='geoserver')


workspaces= geo.get_workspaces()
workspace_names= []

geos= geo.get_datastores()
geo_names= []

layers = geo.get_layers()
name_of_all_layers= []
#dict_of_layer = {}


for keys, values in workspaces.items():
    for key, value in values.items():
        for i in range(len(value)):
            #for names, hrefs in value[i].items():
            workspace_names.append(value[i]['name'])




for key, value in layers.items():
    for ke, val in value.items():
        for i in range(0, len(val)):
            name_of_all_layers.append((val[i]['name']))
            #name_of_all_layers.append((val[i]['name'].split(":")[-1]))

# for name in name_of_all_layers:
#     na_of_layer = name.split(':')[-1]
#     ws_of_layer = name.split(':')[0]
#     hf_of_layer = name
#     gsLayer.objects.create(name= na_of_layer, workspace= ws_of_layer, href= hf_of_layer)

# {'layers': {'layer': [{'name': 'geoapp:HienTrangBenhVien', 'href': 'http://127.0.0.1:8080/geoserver/rest/layers/geoapp%3AHienTrangBenhVien.json'}, {'name': 'geoapp:dem_bien', 'href': 'http://127.0.0.1:8080/geoserver/rest/layers/geoapp%3Adem_bien.json'}, {'name': 'geoapp:jb_demo', 'href': 'http://127.0.0.1:8080/geoserver/rest/layers/geoapp%3Ajb_demo.json'}, {'name': 'demo:HienTrangMangLuoiDuongBo', 'href': 'http://127.0.0.1:8080/geoserver/rest/layers/demo%3AHienTrangMangLuoiDuongBo.json'}, {'name': 'demo:HienTrangMatDoDanSo_CapHuyen', 'href': 'http://127.0.0.1:8080/geoserver/rest/layers/demo%3AHienTrangMatDoDanSo_CapHuyen.json'}, {'name': 'demo:sea_dem_gevco', 'href': 'http://127.0.0.1:8080/geoserver/rest/layers/demo%3Asea_dem_gevco.json'}]}}