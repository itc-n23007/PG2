import zipfile, os

def backup_to_zip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zip_filename = f'{os.path.basename(folder)}_{number}.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1

    print(f'Creating {zip_filename}')
    backup_zip = zipfile.ZipFile(zip_filename, 'w')
    
    print('Done')
backup_to_zip(r'C:\delicious')