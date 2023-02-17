import json

def common_data(list1, list2):
    result = True
    for x in list1:
        for y in list2:
            if x == y:
                result = False
                return result               
    return result

with open("con/heading_info.json", 'r') as f:
    heading_data = json.load(f)

with open("path.json", "r") as f:
    path_data = json.load(f)

GRAPHS = 'connectivity/'

with open(GRAPHS+'scans.txt') as f:
        scans = [scan.strip() for scan in f.readlines()]
        
view_avaiable_dict = {}
human_view_dict = {}
for scan in scans:
    view_avaiable_dict[scan] = []
    human_view_dict[scan] = []
for idx in range(len(path_data)):
    #print(idx)
    if common_data(path_data[idx]['path'], human_view_dict[path_data[idx]['scan']]):
        for path_num in reversed(range(len(path_data[idx]['path']))):
            try:
                heading = heading_data[path_data[idx]['scan']][path_data[idx]['path'][path_num]]
                view_avaiable_dict[path_data[idx]['scan']].append(path_data[idx]['path'][path_num])
            except:
                #1/10 number of total viewpoints max
                #print(path_data[idx]['scan'])
                with open('con/con_info/{}_con_info.json'.format(path_data[idx]['scan']), 'r') as f:
                    con_data = json.load(f)
                if len(human_view_dict[path_data[idx]['scan']]) < int(len(con_data) / 10):
                    human_view_dict[path_data[idx]['scan']].append(path_data[idx]['path'][path_num])
                    #print(path_data[idx]['path'][path_num])
                    break
                

with open('human_view_info.json', 'w') as outfile:
    json.dump(human_view_dict, outfile, indent=3)