# 评鉴

把饭菜、咖啡、酒、空间、图像、叙事、声音和说话收成同一件事：判断好坏。静态站放在 `docs/`，用 GitHub Pages 从该目录发布，方式和 [video-notes](https://github.com/czh55/video-notes) 一样。

## 发布

1. 把这个仓库推到 GitHub（例如 `czh55/anything-criticism`）。
2. 仓库 Settings → Pages → Build and deployment → Source 选 **Deploy from a branch**。
3. Branch 选 `main`，文件夹选 **`/docs`**。
4. 站点地址会是 `https://<用户名>.github.io/anything-criticism/`。

## 目录

```
docs/
├── index.html              # 首页：主张 + 十八个类别
├── method.html             # 跨类别的五步
├── categories/*.html       # 各类别占位，之后往里写条目
└── assets/site.css
```

## 核心脉络从哪来

各类别页的「核心脉络 / 典型失败 / 边界」主要从两个网络知识库收束：

- [video-notes](https://github.com/czh55/video-notes)：咖啡、摄影、绘画、影视、家装、职场表达等
- [audio-workshop](https://github.com/czh55/audio-workshop)：饭菜、摄影审美、古典聆听、沟通、叙事细读等

厚度写在各类别页底部。啤酒、游戏、雕塑等标注「待补源」的，只立了脚手架。

重生成类别页：

```bash
python3 scripts/build_category_veins.py
```

## 之后怎么补

打开对应的 `docs/categories/<id>.html`，在「已记录」一节里按四行加条目：对象、场合、判断、边界。补上第一条后，把首页该卡片的「脉络已立」改成条目数。
