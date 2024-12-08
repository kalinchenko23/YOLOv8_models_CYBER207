import os 

images_to_delete=[]
for i in os.listdir("/Users/maximkalinchenko/Desktop/Berkeley/Cyber 207/final_project/MIL_IFV/train/labels"):
    with open(os.path.join("/Users/maximkalinchenko/Desktop/Berkeley/Cyber 207/final_project/MIL_IFV/train/labels",i)) as file:
        lines=file.readlines()
        for line in lines:
            if line.split()[0]=='4':
                images_to_delete.append(i)
                break

for image in images_to_delete:
    os.remove(os.path.join("/Users/maximkalinchenko/Desktop/Berkeley/Cyber 207/final_project/MIL_IFV/train/labels",image))
    image=image.replace('.txt', '.jpg')
    os.remove(os.path.join("/Users/maximkalinchenko/Desktop/Berkeley/Cyber 207/final_project/MIL_IFV/train/images",image))
