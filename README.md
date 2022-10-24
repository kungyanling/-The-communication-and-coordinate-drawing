# The Inter-Process Communication and Coordinates Plotting (程序間通訊與座標繪圖)
利用zeroMQ使client.c與用sever.py可以相互通訊，client.c產生緯度，sever.py產生經度，由client.c將座標存入並生成location.json檔，再由sever.py做後續json檔的讀取、座標串列切割與繪圖，
而繪圖是利用folium模組，可以在世界地圖上繪圖，將隨機生成的座標畫成路線圖並標出座標點
## 使用介紹
在Ubuntu Terminal內執行run.py檔，即可自動執行makefile、client.c與sever.py。**注意 : 將上述四個檔案皆放置在同一資料夾內，才不會出錯!**

執行範例

![image](https://github.com/kungyanling/-The-communication-and-coordinate-drawing/blob/main/%E5%9F%B7%E8%A1%8C%E7%AF%84%E4%BE%8B.png)

成果展示(一) 

![image](https://github.com/kungyanling/The-Inter-Process-Communication-and-Coordinates-Plotting/blob/main/%E6%88%90%E6%9E%9C%E5%B1%95%E7%A4%BA(%E4%B8%80).png)

成果展示(二) **點選其中一個Marker，即可顯示其座標序及座標值**

![image](https://github.com/kungyanling/The-Inter-Process-Communication-and-Coordinates-Plotting/blob/main/%E6%88%90%E6%9E%9C%E5%B1%95%E7%A4%BA(%E4%BA%8C).png)
