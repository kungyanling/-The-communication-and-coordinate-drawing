# The Inter-Process Communication and Coordinates Plotting (程序間通訊與座標繪圖)
利用 zeroMQ 使 client.c 與用 sever.py 可以相互通訊，client.c 產生緯度，sever.py 產生經度，由 client.c 將座標存入並生成 location.json 檔，再由 sever.py 做後續 json檔的讀取、座標串列切割與繪圖，
而繪圖是利用 folium 模組，可以在世界地圖上繪圖，將隨機生成的座標畫成路線圖並標出座標點
## 使用介紹
在 Ubuntu Terminal 內執行 run.py 檔，即可自動執行 makefile、client.c 與 sever.py。**注意 : 上述四個檔案皆放置在同一資料夾內，才不會出錯!**

執行範例

![image](https://github.com/kungyanling/-The-communication-and-coordinate-drawing/blob/main/%E5%9F%B7%E8%A1%8C%E7%AF%84%E4%BE%8B.png)

成果展示(一) 

![image](https://github.com/kungyanling/The-Inter-Process-Communication-and-Coordinates-Plotting/blob/main/%E6%88%90%E6%9E%9C%E5%B1%95%E7%A4%BA(%E4%B8%80).png)

成果展示(二) **點選其中一個 Marker，即可顯示其座標序及座標值**

![image](https://github.com/kungyanling/The-Inter-Process-Communication-and-Coordinates-Plotting/blob/main/%E6%88%90%E6%9E%9C%E5%B1%95%E7%A4%BA(%E4%BA%8C).png)

## 小小經驗分享
1. 編譯時，記得要在最後方加入指定標頭檔的目錄路徑 " -lzmq -ljson-c"，不然會無法編譯且錯誤訊息顯示 "undefined reference to"
2. 由於 client.c 傳給 sever.py 的整數會變成 bytes，所以要利用 int.from_bytes(bytes, byteorder, *, signed=False) 將其轉換為整數，才能做後續的計算，計算完畢後，要再將其要利用  int.to_bytes(length, byteorder)轉換為 bytes 才能回傳給 client.c

**注意 : 上述 byteorder 在 int.from_bytes 中要用 "big"，而在 int.to_bytes 中要用 "little"，如若用 "big"，則每一個回傳的值皆會變為 0。而上述 length 則是建議 100000，如此才不會因太短而出錯**

## 我的獨到之處

核心程式碼片段(一) client.c

![image](https://github.com/kungyanling/The-Inter-Process-Communication-and-Coordinates-Plotting/blob/main/%E6%A0%B8%E5%BF%83%E7%A8%8B%E5%BC%8F%E7%A2%BC%E7%89%87%E6%AE%B5(%E4%B8%80).png)

1. 利用 srand(time(NULL))，可以使每次產生的亂數都不相同
2. 透過 for 迴圈可以控制產生的座標數，只要更改一個數字即可
3. 在產生完所有的座標後，由於傳送的數字不可能為 0，因此可以利用 client.c 傳送 0，使 sever.py 跳出不停接收訊息的 while 迴圈
4. 傳輸完畢後，即可關閉 socket 與摧毀 context，確保程式能正常運行並做後續 json 檔的操作

核心程式碼片段(二) sever.py

![image](https://github.com/kungyanling/The-Inter-Process-Communication-and-Coordinates-Plotting/blob/main/%E6%A0%B8%E5%BF%83%E7%A8%8B%E5%BC%8F%E7%A2%BC%E7%89%87%E6%AE%B5(%E4%BA%8C).png)

1. 同核心程式碼片段(一)第三點，由於為了做後續計算處理，皆須將收到的 bytes 轉換為整數，因而在轉換後，加上判斷式，當接收到作為結束指令的數字0，即可跳出迴圈做後續的 json 檔處理與座標繪圖
2. time.sleep(1)在此休息一秒是為了等候 client.c 將資料存入json檔並建立 location.json 檔，以免之後讀取時找不到檔案

核心程式碼片段(三) sever.py

![image](https://github.com/kungyanling/The-Inter-Process-Communication-and-Coordinates-Plotting/blob/main/%E6%A0%B8%E5%BF%83%E7%A8%8B%E5%BC%8F%E7%A2%BC%E7%89%87%E6%AE%B5(%E4%B8%89).png)

1. 由於 json 檔資料讀取後，檔案型別為 list 且其中資料並沒有做切割處理，因此利用 result = [] 產生一個空 list，存入切割完的座標們
2. 由於座標皆為兩兩一組，故而利用 n = math.ceil(len(p) / 2) 求出總共要切割出的座標數
3. 再利用 for 迴圈與 list.append()函數將座標們兩個為一組存入 result 中 **注意 : p[idx : idx + 2] 其實只會存取 p[idx] 與 p[idx + 1] 的值**
4. 利用 for 迴圈搭配 folium.Marker，即可在圖上將每一個座標點加上 Marker，並得以顯示其座標序及座標值
