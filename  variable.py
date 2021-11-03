import os

video_name = "video"

img_save_path = 'C:/Users/ygfms/Desktop/최승리/python/test/' + str(video_name) + '/'

for i in range(0, 7):
    globals()[f'img_{i}_F_path'] = img_save_path + f'{i}_F' + '/'
    if not os.path.exists(globals()[f'img_{i}_F_path']):
        os.makedirs(globals()[f'img_{i}_F_path'])
j=2
print(globals()[f'img_{j}_F_path'])

for i in range(0, 7):
    globals()[f'img_{i}_M_path'] = img_save_path + f'{i}_M' + '/'
    if not os.path.exists(globals()[f'img_{i}_M_path']):
        os.makedirs(globals()[f'img_{i}_M_path'])

i=2
print(globals()[f'img_{i}_M_path'])
