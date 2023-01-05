# community_detection
### DDL: 2023/1/5

參考筆記: https://hackmd.io/0nC3zkwVRDi2cn18jJPA0g

* main1.ipynb 是主要的程式碼
* dataset我沒有放上去，要記得放在同一個資料夾中

2022/11/24(四) 陳學義 
- 目前正在做的是: 視覺化(順便而已)、將 data 處理成可以餵進 GNN 的格式
- 將來要做的是: 訓練 GNN、找 GNN 相關論文、可以看一下 GAN 怎麼做

2022/11/26(六) 
陳學義
1. 搞清楚componet.py後面在做甚麼？  
2. 整理一下 df 整理 column 變成可以訓練，NAN標成一個以外的數字
3. 進行訓練。

盛浩
1. Louvain 算法 - 了解一下，看看能不能實作
2. 針對目前的feature做特徵選擇
3. 蒐集graph資訊，degree、朋友跟朋友的相似度...當成features進行 machine learning
