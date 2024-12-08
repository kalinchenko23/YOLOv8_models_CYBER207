import os 

for i in os.listdir("/Users/maximkalinchenko/Desktop/Berkeley/Cyber 207/final_project/IFV/valid/labels"):
    with open(os.path.join("/Users/maximkalinchenko/Desktop/Berkeley/Cyber 207/final_project/IFV/valid/labels",i),"r", encoding='ISO-8859-1') as file:
        corrected_lines=[]
        lines=file.readlines()
        for line in lines:
            segment=line.split()
            if segment[0]!='23':
                new_line=line.replace(segment[0],"23",1)
                corrected_lines.append(new_line)
            else:
                corrected_lines.append(line)
        with open(os.path.join("/Users/maximkalinchenko/Desktop/Berkeley/Cyber 207/final_project/IFV/valid/labels_corrected",i),"w") as f:
            f.writelines(corrected_lines)
        