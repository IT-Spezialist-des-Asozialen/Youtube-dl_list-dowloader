import os
i=0
links=[]
folder=""
folders=[]
wait = "t"
while wait!="y":
    singleLink=input("Please insert the link to the video: ")
    folder=input("Where should the video be safed? Please insert the complet path. If you insert nothing, the default path is choosen.")
    folders+=[folder]
    links += [singleLink]
    wait=input('If you want to safe all videos, tipe "y". If you want to add others, tipe "Enter".')
    i+=1
print("All videos were safed in the respective folder.")
numbersLinks=len(links)
i=0
while i <numbersLinks:
    os.system('./youtube-dl/youtube-dl '+ links[i]+folders[i])
    i+=1
