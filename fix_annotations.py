import os

path = "./data/labels"
filenames = []
counter = 0

# I do this in two steps, but technically you could just do it in one step rather than creating the list then processing
# the files.  This way, if there is any problem with gathering the filenames it fails without partially processing
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".txt"):
            filenames.append(os.path.join(root, file))
            counter += 1
print(f'Found {counter} annotation (*.txt) files')
counter = 0
for filename in filenames:
    with open(filename, 'r') as fobj:
        annotations = [[float(num) for num in line.split()] for line in fobj]
    print(annotations)
    for index, annotation in enumerate(annotations):
        x = (annotation[3] + annotation[1])/2
        y = (annotation[4] + annotation[2])/2
        width = (annotation[3] - annotation[1])
        height = (annotation[4] - annotation[2])
        annotations[index][1]=x
        annotations[index][2]=y
        annotations[index][3]=width
        annotations[index][4]=height

    with open(filename, 'w') as f:
        for annotation in annotations:
            for value in annotation:
                f.write(f"{value} ")
            f.write("\n")
            counter += 1
print(f'Processed {counter} annotations')



