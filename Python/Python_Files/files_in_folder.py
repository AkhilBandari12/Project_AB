import os

def get_filenames_without_extension(directory):
    filenames_without_extension = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            name, _ = os.path.splitext(filename)
            filenames_without_extension.append(name)
    return filenames_without_extension

# Example usage
directory_path = '/home/buzzadmin/Documents/Apr'
filenames = get_filenames_without_extension(directory_path)

for file in filenames:
    print(file)
