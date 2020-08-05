import codecs
import os
import glob
import argparse
from collections import defaultdict

f = codecs.open("readme.md", "w", "utf-8")

header = """
# µsini Diagrams
by [µsini](https://twitter/m4dnerd)

✔️ All diagrams are free to use without attribution (Public Domain)   
❌ Diagrams are not up-to-scale   

# 📥 [Download](https://github.com/usini/diagrams/archive/master.zip) 
# ❓ Need a diagram ? --> https://github.com/usini/issues
# [![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/O5O420F33)

# Table of Contents
- [Table of Contents](#table-of-contents)
"""

f.write(header)

folders = [x for x in os.listdir() if not os.path.isfile(x)]

for folder in folders:
    if ".git" in folder:
        continue
    f.write("- [" + folder + "](#" + folder + ")\n")

for folder in folders:
    if ".git" in folder:
        continue
    f.write("# " + folder + "\n")
    print(folder)

    svg_files = [z for z in os.listdir(folder + "/") if z.endswith(".svg")]
    for svg_file in svg_files:
        f.write("### " + svg_file + "\n")
        f.write("![" + svg_file + "](" + folder + "/" + svg_file + ") \n")    

    subfolders = [y for y in os.listdir(folder) if not os.path.isfile(folder + "/" + y)]
    print(subfolders)

    for subfolder in subfolders:
        f.write("## " + folder + "/" + subfolder + "\n")
        print(subfolder)
        svg_files = [z for z in os.listdir(folder + "/" + subfolder + "/") if z.endswith(".svg")]
        print(svg_files)
        for svg_file in svg_files:
            f.write("### " + svg_file + "\n")
            f.write("![" + svg_file + "](" + folder + "/" + subfolder + "/" + svg_file + ") \n")       

    f.write("\n #### [TOP](#table-of-contents) \n")
f.close()





