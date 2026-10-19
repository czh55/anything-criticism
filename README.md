# 评鉴

把饭菜、咖啡、酒、空间、图像、叙事和说话收成同一件事：判断好坏。静态站放在 `docs/`，用 GitHub Pages 从该目录发布，方式和 [video-notes](https://github.com/czh55/video-notes) 一样。

## 发布

1. 把这个仓库推到 GitHub（例如 `czh55/anything-criticism`）。
2. 仓库 Settings → Pages → Build and deployment → Source 选 **Deploy from a branch**。
3. Branch 选 `main`，文件夹选 **`/docs`**。
4. 站点地址会是 `https://<用户名>.github.io/anything-criticism/`。

## 目录

```
docs/
├── index.html              # 首页：主张 + 十四个类别
├── method.html             # 跨类别的五步
├── categories/*.html       # 各类别占位，之后往里写条目
└── assets/site.css
```

## 之后怎么补

打开对应的 `docs/categories/<id>.html`，在「已记录」一节里按四行加条目：对象、场合、判断、边界。补上第一条后，把首页该卡片的「尚未记录」改成条目数。
