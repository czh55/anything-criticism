#!/usr/bin/env python3
"""Regenerate category pages with core criticism veins from video-notes + audio-workshop."""

from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "docs" / "categories"

# Each entry: slug, name, group, ask, questions, thesis, points[(title, body)], fails, bounds, sources[(label, level)]
# level: 富矿 | 有骨架 | 薄 | 待补源

PAGES = [
  {
    "slug": "dishes",
    "name": "饭菜",
    "group": "入口与杯盏",
    "ask": "一道菜好在哪里，差在哪里。",
    "questions": [
      "原料有没有被随便糟蹋，还是被用在它合适的位置。",
      "火候和调味是在成全这道菜，还是在盖住它。",
      "一口里面有没有层次，吃完身体是舒服还是累。",
    ],
    "thesis": "厨艺可拆三层：刀工可练、火候一瞬、调味近艺。验收一顿饭，不看稀缺与排场，看价格是否合理、有没有至少一道印象菜、吃完人累不累。",
    "points": [
      ("先看部位与用途是否匹配", "选错部位再精湛的火候也难救。猪、牛各部位对应嫩度、脂肪与用途；部位错了，口感先翻车。"),
      ("火候与下料时机可核查", "炒菜「水汪汪」常常不是手艺差，而是调料时机反了。美拉德与莱顿弗洛斯特提醒：水分、火力和下料顺序决定焦香还是炖汤感。"),
      ("味型是可命名的结构", "川菜二十四味型延伸百菜百味；意餐道次各有职分（前菜/头道/二道），不是任务清单。好厨用生活意会味型，而不是堆酱料。"),
      ("印象菜验收法", "一顿值得记住的饭：至少一道事后还能复述的印象菜；稀缺菜单与熟客身份不等于更好吃。"),
      ("吃完的身体是裁判", "好饭吃完不累。过咸、过油、过杂、道次失控，都会在离桌时显形。"),
    ],
    "fails": [
      "用「难订」「隐藏菜单」代替味道本身的判断。",
      "调料盖住原料，或部位与菜式错配。",
      "整桌没有印象菜，只剩饱腹与社交。",
    ],
    "bounds": [
      "家庭安慰菜、记忆菜可以不进「印象菜」竞赛。",
      "产业与门店成败（如烘焙关店潮）不等于单道菜的好坏。",
    ],
    "sources": [("audio-workshop", "富矿"), ("video-notes", "有骨架")],
  },
  {
    "slug": "coffee",
    "name": "咖啡",
    "group": "入口与杯盏",
    "ask": "这杯从香气到收尾是否站得住。",
    "questions": [
      "豆子和烘焙说不说得清，香气是干净还是糊。",
      "酸、甜、苦有没有互相撑住，而不是只剩一种刺激。",
      "温度走完之后，杯子里还剩不剩值得记住的味道。",
    ],
    "thesis": "杯内好坏八成在浓缩与奶泡基础，「干净」指风味轮廓清楚、杂味少。杯外还要分清：你买的是效率提神，还是精品风味，还是第三空间。",
    "points": [
      ("基础先于手法", "拉花失败常不是不会摆，而是豆、奶、杯、萃取、打奶任一环掉链子。基础稳了，摆动与回杯才有意义。"),
      ("用可沟通的词说味道", "酸甜苦杂、干净杯、风味轮由中心向外——把感觉换成可对照的词，而不是「挺香」。crema 厚度不等于好喝。"),
      ("热饮有完整风味窗口", "SCA 思路里图案与饮用双轨：好看还要能喝（常见舒适区间约 50–65℃）。放凉后酸苦冲，是场合变了，不是同一标准。"),
      ("先声明场合再比", "效率模式要稳定提神与价；精品模式看豆/烘/冲煮；第三空间看有没有人记得你、气质是否亲近。混场合比较必吵。"),
      ("奖项先问规则", "金奖满天飞时先问「什么奖、怎么评」。奖杯不是风味本身。"),
    ],
    "fails": [
      "只追复杂拉花，液面脏、奶泡厚度错仍硬练手法。",
      "把「110 种香气」当神秘学，不学基础感官词。",
      "用品牌与联名代替杯测判断。",
    ],
    "bounds": [
      "办公室续命咖啡不必按杯测赛标准苛责。",
      "家用器具与咖啡馆设备不在同一条比较线上。",
    ],
    "sources": [("video-notes", "富矿"), ("audio-workshop", "富矿")],
  },
  {
    "slug": "wine",
    "name": "红酒",
    "group": "入口与杯盏",
    "ask": "这瓶在说产地，还是只在说酒精。",
    "questions": [
      "品种和产地还能不能被辨认出来。",
      "酸度和单宁有没有把酒体撑住。",
      "香气干不干净，余味是收回去还是散掉。",
    ],
    "thesis": "品酒走可重复四步：观色→摇杯→闻香→品尝。用香气、酸度、酒体、单宁、回味把感觉说清楚；价格里混着成本、渠道、稀缺与预期，不等于美学。",
    "points": [
      ("感官四步是骨架", "先看颜色与挂杯，再摇杯放香，再闻，再入口。跳步容易只剩「贵不贵」「烈不烈」。"),
      ("术语是翻译器", "香气奔放/内敛、酸度、酒体、单宁、回味悠长或平衡——用来对照，不是用来装。"),
      ("品种是入门地图", "常见品种各有风格与产区倾向；旧世界重风土叙事，新世界常更直给品种特征。"),
      ("醒酒有拐点", "按酒体估时间：充分之后继续醒会走下坡。气泡酒多数不必醒。"),
      ("盲品练的是链条", "口述链尽量落到产区—品种—风格—适饮窗口，而不是形容词堆叠。"),
    ],
    "fails": [
      "把酒标故事、年份神话直接当成好喝。",
      "用酒精刺激感代替结构判断。",
      "醒酒过久仍硬说「开了更好」。",
    ],
    "bounds": [
      "配餐与纯品鉴标准不同：桌上「合适」可以压过「复杂」。",
      "站内材料偏入门碎片，深度产区体系待书籍与更多笔记补。",
    ],
    "sources": [("video-notes", "有骨架"), ("audio-workshop", "薄")],
  },
  {
    "slug": "beer",
    "name": "啤酒",
    "group": "入口与杯盏",
    "ask": "它自称的风格，喝下去是否成立。",
    "questions": [
      "它宣称的风格有没有被做出来。",
      "麦芽、酒花、碳酸和苦度是在配合还是在打架。",
      "喝完是清爽、寡淡，还是腻。",
    ],
    "thesis": "先认宣称的风格（Lager、IPA、Stout…），再查四件是否咬合：麦芽甜感、酒花香苦、碳酸、酒体。风格不成立，形容词再华丽也无效。站内网络笔记几乎空白，此脉络为脚手架，待补源。",
    "points": [
      ("风格是合同", "瓶子上写的风格，是评鉴的第一合同。合同落空，再谈「个性」也是跑题。"),
      ("四件咬合", "麦芽、酒花、碳酸、酒体应互相撑住。香气冲但苦度脏、或碳酸塌掉，都是结构失败。"),
      ("干净与疲劳", "喝完口腔清不清、腻不腻，比「度数高」更能检验。"),
      ("温度与杯型改场合", "过冷压香、过热放异味；换杯等于换场合，标准要跟着改。"),
    ],
    "fails": [
      "用「进口」「精酿」标签代替风格是否成立。",
      "只追苦度数字，不管香气是否干净。",
    ],
    "bounds": [
      "大排档冰镇畅饮与杯测精酿，不是同一套场合。",
      "video-notes / audio-workshop 暂无系统材料，后续优先补源。",
    ],
    "sources": [("video-notes", "待补源"), ("audio-workshop", "待补源")],
  },
  {
    "slug": "interior",
    "name": "装修",
    "group": "空间",
    "ask": "住进去之后，还烦不烦。",
    "questions": [
      "动线顺不顺，常用的事要不要绕路。",
      "光线和材料是否诚实，有没有用装饰盖住使用。",
      "比例和收口经不经得住近看，住三个月后还烦不烦。",
    ],
    "thesis": "显大、显柔、显质感，靠灯光分层、色彩进退与焦点秩序协同。触觉往往先于视觉；全柔软会变成「窗帘城」，需要硬软对比留气口。",
    "points": [
      ("三层照明", "基础 + 功能 + 氛围各有职分；无主灯≠满天筒灯。显色 Ra 高、色温可调，材质才站得住。"),
      ("色彩进退", "膨胀色靠前、收缩色退后；全屋米色会糊。家具与墙面位置反了，小空间更挤。"),
      ("焦点秩序：点线面", "一个主色点、一条导向线、一块中心面。背景只衬托，勿抢戏。"),
      ("弱化边界优于硬扩", "镜条延线、悬浮、开缝比硬拆更安全，但都有剂量：镜勿大面积对人、圆弧勿在小空间乱扩。"),
      ("假色卡要识破", "商业「莫兰迪色」常是提纯滤镜；真层次来自不均匀与关系，不是一整墙同色油漆。"),
    ],
    "fails": [
      "无主灯理解成筒灯阵列，缺功能层与显色。",
      "满墙装饰、背光过亮，细节把墙面堆死。",
      "只追视觉清爽，忽略触感与住三个月后的烦。",
    ],
    "bounds": [
      "样板间拍照好看，不等于动线与收纳成立。",
      "酒店东方美学的「可标准化体面」与住宅长期居住，标准剂量不同。",
    ],
    "sources": [("video-notes", "富矿"), ("audio-workshop", "有骨架")],
  },
  {
    "slug": "architecture",
    "name": "建筑",
    "group": "空间",
    "ask": "怎么进来，光落在哪，让人做什么。",
    "questions": [
      "人怎么进来，在里面被引向哪里。",
      "光从哪落，结构能不能被看见。",
      "它让人做什么、打算让人待多久，空间有没有配合这件事。",
    ],
    "thesis": "建筑先问动线、光与尺度：人如何被引进来、看见什么、被鼓励做什么。好看常可落到重心、材质克制与错落；叙事空间还要警惕「舞台化真实」。",
    "points": [
      ("好看三律（民宅尺度）", "上小下大降重心；外墙材质宜少且色调近；错落感往往比堆符号更像「有设计」。"),
      ("风格是在回答问题", "十种西方风格不是背名字，而是各自在回答「空间应该是什么样」。"),
      ("尺度与路径造体验", "逼仄门槛→开阔、垂直与迷宫、能动机关——路径设计比立面标签更能决定感受。"),
      ("博物馆三问可迁移", "看见了什么 / 看到了什么 / 谁被舞台化。一件展品讲完一个故事，胜过打卡清单。"),
      ("城市更新看手段", "秩序与微更新 vs 全拆；「创造光」比口号更能检验干预是否诚实。"),
    ],
    "fails": [
      "把哥特等风格简化成「黑暗美学」贴纸。",
      "只看立面照片，不问动线与使用。",
      "以为自己看见了真实，其实看见的是灯光与省略排好的舞台。",
    ],
    "bounds": [
      "电影布景魔法感与真实城市更新，评价轴不同。",
      "站内偏案例碎片，结构工程与规范层待补。",
    ],
    "sources": [("video-notes", "有骨架"), ("audio-workshop", "有骨架")],
  },
  {
    "slug": "photo",
    "name": "照片",
    "group": "图像与形体",
    "ask": "取舍有没有主张，技术有没有帮上忙。",
    "questions": [
      "主体清不清楚，多余的东西有没有被拿掉。",
      "光线是在说明一件事，还是只是碰巧亮。",
      "技术是在服务于要说的话，还是在炫耀自己。",
    ],
    "thesis": "审美不是天赋，是「找重点」的能力——帮相机找到那颗黄豆。出片靠找光、定构图、让姿势动起来；AI 时代好照片更要故事与观看理由，而不是精致炫技。",
    "points": [
      ("找重点", "人眼会抓突出物，相机会全收。框架、引导线、负空间、场景元素尽量少，都是在帮相机聚焦。"),
      ("光比与层次", "不高级常因光比：要亮面、暗面与过渡。侧光塑主次；发灰往往是层次不够，不是饱和度不够。"),
      ("姿势是动出来的", "「自然点」最僵；用动作链与连拍选帧。一次只给一个微调指令。"),
      ("调色做减法", "先还原曝光与影调，再分区塑形。减对立色、去灰，比缺色就加色更接近通透。"),
      ("废片是进步证据", "技术废、无意识废、审美过时废——能识别废片，说明标准已升。破趋同：回到 What's your concern。"),
    ],
    "fails": [
      "顶光拍脸、剪刀手空着手、背景杂物无人管。",
      "只堆滤镜与精修，画面仍平、没有观看理由。",
      "复制打卡模板，拍得越多越像别人。",
    ],
    "bounds": [
      "纪实、商业、旅拍目的不同，精致度要求不同。",
      "器材轻熟有出片信心，往往压过「带最好的相机」。",
    ],
    "sources": [("video-notes", "富矿"), ("audio-workshop", "富矿")],
  },
  {
    "slug": "painting",
    "name": "画作",
    "group": "图像与形体",
    "ask": "意图有没有落到看得见的组织上。",
    "questions": [
      "眼睛先看哪里，再被带到哪里。",
      "形和颜色有没有被组织成一个整体。",
      "离开之后还记得哪一块，那一块是不是作者真的下了功夫。",
    ],
    "thesis": "先建立明度秩序与体块结构，再用纯度、冷暖与环境色塑空间；明度≠纯度，远灰近纯，冷暖用面积平衡。技巧永远服从主题；真正的美常源于变化之中的统一。",
    "points": [
      ("两轴分清", "明度问亮暗，纯度问浓淡。混成一条箭头，调色与光感判断会一直错。"),
      ("明度秩序是可读性底座", "去色后仍清晰，说明关键在明度布局。最强明度对比应给发光位。"),
      ("画关系不画孤立色", "让某处更亮，可改周围关系；受光暖、背光冷是常见分工。"),
      ("纯度与冷暖是节奏", "远灰近纯；冷暖靠面积平衡。6:3:1 面积法可跨媒介迁移。"),
      ("先体块后细节", "过早抠细节形不准；临摹找规律（明暗链、色相关系），不是复制完成稿。"),
    ],
    "fails": [
      "只加白提亮，忽视纯度与周围关系。",
      "灰色调无冷暖倾向，高级灰变死灰。",
      "没定主题就套构图技巧。",
      "把商业莫兰迪色卡当成大师的层次。",
    ],
    "bounds": [
      "习作练秩序与创作表达主题，验收标准不同。",
      "站内绘画材料以造型课为主，画史批评仍待书籍补厚。",
    ],
    "sources": [("video-notes", "富矿"), ("audio-workshop", "薄")],
  },
  {
    "slug": "sculpture",
    "name": "雕像",
    "group": "图像与形体",
    "ask": "转一圈之后，轮廓还在不在。",
    "questions": [
      "体量和它周围的空间是否匹配。",
      "换一个角度看，轮廓还成不成立。",
      "材料、受力的方式、近看的手工痕迹是否说得通。",
    ],
    "thesis": "雕塑评鉴先绕圈：体量与空间、轮廓是否在多角度成立、材料与受力是否诚实。站内材料极薄，可先借「体积—主褶—收回」的造型逻辑与博物馆观看法起骨架。",
    "points": [
      ("当体积看，不当贴花看", "大面先立住，再在受力处出主褶/主转折，最后收回小褶——衣服褶皱教学可迁移到形体判断。"),
      ("多角度轮廓", "只在一张照片好看不算；转圈后轮廓散掉，说明体量没有真正组织好。"),
      ("材料与重力", "支撑、悬挑、表面处理要说得通；违背材料脾气的「效果」往往假。"),
      ("观看场合", "展厅灯光与基座会舞台化对象；先问展方让你看见什么，再谈作品本身。"),
    ],
    "fails": [
      "只从前视照片判断「神韵」。",
      "用题材感动代替形体是否成立。",
    ],
    "bounds": [
      "公共纪念碑、架上小雕、装置艺术，评价轴不同。",
      "video-notes / audio-workshop 几乎无雕塑专题，此页待重点补源。",
    ],
    "sources": [("video-notes", "薄"), ("audio-workshop", "待补源")],
  },
  {
    "slug": "calligraphy",
    "name": "书法",
    "group": "图像与形体",
    "ask": "笔势有没有把字立住。",
    "questions": [
      "点画有没有分量，还是只有外形。",
      "整篇气脉通不通，节奏是顺下来的还是断着堆的。",
      "字的姿态和所用书体是否相配，近看经不经得住。",
    ],
    "thesis": "进步靠三件事：看清本质、建立控制、持续校正。线是方向×力度×节奏；结构是重心→主次→空间；章法是行气×留白。评鉴查关系是否可检查，不是描得像不像。",
    "points": [
      ("线的三维", "方向、力度、节奏任缺一维，点画就只剩外形。"),
      ("结构顺序", "先重心稳不稳，再主次笔，再空间分布。顺序反了，单字再工也散。"),
      ("章法是一口气", "行气与留白决定篇；字字漂亮但气断，仍是失败。"),
      ("校正闭环", "临帖与创作都要能指出「错在关系的哪一层」，才能积累判断。"),
    ],
    "fails": [
      "描外形、填格子，忽略力度与节奏。",
      "单字可看、成篇如砌砖。",
    ],
    "bounds": [
      "实用书写与展览创作，场合不同。",
      "站内仅有第一性原理提纲，书体史与碑帖体系待书籍补。",
    ],
    "sources": [("video-notes", "有骨架"), ("audio-workshop", "待补源")],
  },
  {
    "slug": "story",
    "name": "故事",
    "group": "叙事",
    "ask": "谁想要什么，转折是不是挣来的。",
    "questions": [
      "谁想要什么，阻碍是否具体。",
      "转折是情节挣来的，还是作者硬拧的。",
      "结尾有没有把前面用上。",
    ],
    "thesis": "拒绝一句话概括式阅读：追问人物为何这样选。叙事上限在结构与联系——镜头/段落之间是否长出新意思；调色与修辞是加分，救不了空骨架。",
    "points": [
      ("欲望与阻碍要具体", "谁要什么、卡在哪；抽象主题贴标签，人物就不会真的动。"),
      ("转折要挣来", "支点崩塌与重建、希望被踩空，应来自前面埋下的条件，不是作者突然宣布。"),
      ("联系是黏合剂", "色、形、动势、声画关联——相邻单元至少有一条线索，否则只是换场景。"),
      ("结构可先给结果", "倒金字塔：先结果再过程再情绪，适合短叙事；长篇则看单元张力是否反复成立。"),
      ("读对话数情绪层", "对话里有几层情绪、是否只在交换信息；写吃写物常常是在写结构与世界观。"),
    ],
    "fails": [
      "用标签（「苍凉」「温暖」）代替细读选择。",
      "转折靠隐瞒读者，而不是人物行动。",
      "结尾没用上前面铺垫。",
    ],
    "bounds": [
      "商业短视频结构与长篇小说结构，剂量不同。",
      "消费侧「故事溢价」退潮时，仍应用可验证品质另判产品，勿与文学叙事混打。",
    ],
    "sources": [("video-notes", "富矿"), ("audio-workshop", "富矿")],
  },
  {
    "slug": "comic",
    "name": "漫画",
    "group": "叙事",
    "ask": "信息是画出来的，还是注出来的。",
    "questions": [
      "分镜有没有带着人往下读。",
      "角色隔一页还能不能认出来。",
      "信息是画出来的，还是靠旁白注出来的；翻页的节奏紧不紧。",
    ],
    "thesis": "漫画好坏看画是否在叙事：分镜带读、文戏与群像是否立住、伏笔能否事后回收。入坑路径会影响你对「终点」的想象；烂尾标准应看作者是否画完所想、调性是否同频、主角是否崩。",
    "points": [
      ("画出来 vs 注出来", "关键信息若只能靠旁白补，分镜就失职。"),
      ("文戏与群像", "长期连载里，人物关系与文戏往往比战力升级更能决定品质。"),
      ("草蛇灰线", "伏笔应可回收；回收时应让人觉得「早有条件」，不是作者临时发明。"),
      ("翻页节奏", "页末钩子、留白与密度控制阅读呼吸。"),
      ("终点想象要对齐", "你怎么入坑，会影响你觉得什么叫完满；争论前先对齐预期。"),
    ],
    "fails": [
      "只靠战力膨胀续命，人物停在原地。",
      "调性突变、主角崩坏却用「超级展开」掩饰。",
    ],
    "bounds": [
      "短篇一击与超长连载，评价时间尺度不同。",
      "站内深度样本偏《海贼王》圆桌，类型广度待补。",
    ],
    "sources": [("audio-workshop", "有骨架"), ("video-notes", "待补源")],
  },
  {
    "slug": "film",
    "name": "电影",
    "group": "叙事",
    "ask": "场面是否在推进同一件事。",
    "questions": [
      "这个场面有没有把故事往前推。",
      "声音和画面是不是在做同一件事。",
      "人物的选择能不能被看见，时长配不配得上它要的重量。",
    ],
    "thesis": "拉片把情绪与主题翻译成可执行的声画选择。隐喻须成体系；运镜每一下都应有叙事功能。胜利考验能力，回家考验承担——经典会随人生阶段重读。",
    "points": [
      ("每场戏写清感受目标", "本段要让观众感到什么，用了哪两三个声画手段——写不出来，往往就是炫技。"),
      ("隐喻成体系", "意象、机位、轴线、阶梯等应反复呼应同一主题，不能散点贴标签。"),
      ("声音可先行", "听见尚未看见，焦虑与压迫常更强。"),
      ("运镜有职分", "摇交代关系，推放大情绪，拉转向环境；无目的推拉等于噪声。"),
      ("逆向反推学习", "对照花絮与成片差异，还原借位、错位与引导，比背术语更快。"),
    ],
    "fails": [
      "只记名词（长焦/越轴）不问「此刻要观众感受什么」。",
      "把解说观点当剧情事实。",
      "类型错位变成乱炖，而不是服务价值观。",
    ],
    "bounds": [
      "商业类型片的爽感契约与作者电影的主题契约不同。",
      "站内影视视听富、剧作深度样本仍可再补。",
    ],
    "sources": [("video-notes", "富矿"), ("audio-workshop", "薄")],
  },
  {
    "slug": "tv",
    "name": "电视剧",
    "group": "叙事",
    "ask": "集与集之间，人物有没有真的变。",
    "questions": [
      "单集自己有没有形状，而不是只负责拖。",
      "人物随集数有没有变化。",
      "悬念靠的是信息，还是靠不告诉你；世界的规则稳不稳定。",
    ],
    "thesis": "剧集评鉴看三层：单集是否有形状、人物是否随集变化、世界规则是否稳定。好剧常删水、拒廉价大团圆；短剧产业降本后，门槛仍回到 idea、审美与人性理解。",
    "points": [
      ("单集要有形状", "不是流水账切片；本集应有可复述的问题与收束。"),
      ("人物要累计变化", "集数增加若人物零变化，续集只是工期。"),
      ("悬念靠信息设计", "藏信息可以，但规则乱改等于欺骗而非悬念。"),
      ("季与文化剂量", "英剧短季删水是一种品质线索；口碑榜只是候选，仍要按题材与情绪自筛。"),
      ("短剧另开场合", "钩子、反转、付费节点是另一套合同，勿与长剧混用同一刀。"),
    ],
    "fails": [
      "注水集、人物复读、为续订强行开新线。",
      "世界规则随集数漂移，只为制造反转。",
    ],
    "bounds": [
      "日更短剧、美剧长季、英剧短季，结构契约不同。",
      "站内系统拉片少，此脉络偏骨架，待补源。",
    ],
    "sources": [("video-notes", "薄"), ("audio-workshop", "薄")],
  },
  {
    "slug": "game",
    "name": "游戏",
    "group": "叙事",
    "ask": "规则有没有把人带进去。",
    "questions": [
      "规则清不清楚，学起来是在变聪明，还是在背说明书。",
      "每一次选择有没有重量；反馈是及时、可读，还是糊弄。",
      "玩下去是因为想继续，还是因为被拖着；退出之后还记不记得那一局。",
    ],
    "thesis": "游戏评鉴看规则是否教会玩家变聪明、选择是否有重量、反馈是否可读。好玩应是想继续，不是被机制拖着。站内网络笔记几乎空白，此脉络为脚手架。",
    "points": [
      ("规则是教材", "学习曲线应让人变强；纯背说明书是设计失败。"),
      ("选择有代价", "每个有意义的选择应改写局面；伪选择是装饰。"),
      ("反馈可读", "成功/失败信号及时、可理解；糊弄反馈破坏信任。"),
      ("退出后的记忆", "一局之后还记得什么——系统、角色、还是只有肝度。"),
    ],
    "fails": [
      "用数值膨胀与登录奖励代替设计。",
      "叙事与玩法各说各话。",
    ],
    "bounds": [
      "竞技、叙事、放置、社交，合同完全不同。",
      "video-notes / audio-workshop 待补游戏品鉴源。",
    ],
    "sources": [("video-notes", "待补源"), ("audio-workshop", "待补源")],
  },
  {
    "slug": "instrument",
    "name": "乐器",
    "group": "声音",
    "ask": "不同的乐器代表不同的情绪。",
    "questions": [
      "这件乐器天然偏向哪种情绪：明亮、沉、尖、暖，还是空。",
      "音色和技法有没有把那份情绪做出来，还是在硬撑别的气氛。",
      "换一件乐器，同样的旋律还站不站得住；它的不可替代处在哪。",
    ],
    "thesis": "乐器先认音色脾气：明亮、沉、尖、暖、空。技法应把脾气做成可听的情绪；砸键式发力常毁掉层次。换乐器后旋律若完全换味，说明不可替代处正在脾气本身。",
    "points": [
      ("先认脾气", "每件乐器有默认情绪倾向；评鉴先问它擅长什么，再问曲目是否强它所难。"),
      ("发力决定层次", "如钢琴：大臂送力、指尖抓住，旋律才透亮可分层；硬砸则糊。"),
      ("不可替代测试", "同样旋律换乐器——若情绪塌掉，原乐器的价值就在那份脾气。"),
      ("演奏与曲目对齐", "技法炫技若与情绪合同无关，是噪音。"),
    ],
    "fails": [
      "用昂贵品牌代替音色是否合适。",
      "强行让一件乐器演它不擅长的情绪还不改编曲。",
    ],
    "bounds": [
      "教学演示与舞台表现，标准不同。",
      "站内乐器本体材料薄，多落在演奏手感碎片。",
    ],
    "sources": [("video-notes", "薄"), ("audio-workshop", "薄")],
  },
  {
    "slug": "music",
    "name": "音乐",
    "group": "声音",
    "ask": "听完之后，身体还记不记得。",
    "questions": [
      "旋律、和声、节奏有没有各自的职分，还是糊成一团。",
      "情绪是被推着走的，还是被摁着说的；高潮是挣来的还是堆出来的。",
      "听完之后还记得哪一句、哪一声，那一处是不是真的下了功夫。",
    ],
    "thesis": "听音乐先定场合与目的：通勤、反内耗、田野倾听，合同不同。整首/整专通听对抗算法切片；高潮应挣来。人对品味的意志，大于「猜你喜欢」。",
    "points": [
      ("按场合选型", "对事/对人/对环境的内耗，可配不同作品；转移注意力是一种合法用法。"),
      ("通听对抗切片", "听完整首或整张专辑，才听得到结构与演奏家的地图。"),
      ("结构职分", "旋律、和声、节奏各有职分；糊成一团或高潮硬堆，都是结构失败。"),
      ("田野与场域", "不规则细碎声、不插电现场、唱片店偶然性——提醒音乐不止旋律工业。"),
      ("身体记忆验收", "离开后还记得哪一句、哪一声，往往是真下功夫处。"),
    ],
    "fails": [
      "只刷副歌切片，却对「整张很一般」下结论。",
      "用播放量与算法推荐代替自己的听感合同。",
    ],
    "bounds": [
      "流行工业、古典、田野录音、现场限制（如不插电），评价轴不同。",
      "video-notes 偏声画卡点用法；听乐评鉴主要来自 audio-workshop。",
    ],
    "sources": [("audio-workshop", "富矿"), ("video-notes", "薄")],
  },
  {
    "slug": "speech",
    "name": "说话表达",
    "group": "言语",
    "ask": "听的人离开时，带走了哪一句。",
    "questions": [
      "听的人知不知道要带走什么。",
      "句子有没有主次，例子贴不贴着论点。",
      "停顿和语气是在帮忙，还是在填空。",
    ],
    "thesis": "沟通是场域、预期与边界，不是话术万能。职场稀缺的是确定性交付；闲聊先定关系强度与剂量。退出表达竞赛，有时是为了恢复判断力。",
    "points": [
      ("先定场域", "5W1H 结构化常常大于金句；结构性问题用技巧解不了。"),
      ("确定性表达", "复述确认目标与边界；汇报带风险与方案。老板要的是听懂并翻译问题—资源—风险。"),
      ("闲聊看剂量", "地铁、领导一对一、跨语接待，关系强度不同；诉苦易被读成索取。"),
      ("节奏：语速慢、节奏快", "少废话词，用有功能的承接；控场靠动作/眼神/声音/话术倒计时。"),
      ("带走一句", "听者离开时能复述的那句，就是表达是否成立的验收。"),
    ],
    "fails": [
      "自我介绍复述简历；「其实」带纠正味。",
      "拍胸脯给确定性，不打预防针。",
      "在表达竞赛里解释过剩，生活被话术掏空。",
    ],
    "bounds": [
      "演讲、谈判、闲聊、培训，合同不同。",
      "脱口秀场上的冒犯红利，不宜直接搬进职场。",
    ],
    "sources": [("video-notes", "富矿"), ("audio-workshop", "富矿")],
  },
]

# slug -> video-notes note slugs / audio-workshop stems / optional category-summary id
REFS = {
  "dishes": {
    "vn": ["stir-fry-water-mistake", "stir-fry-seasoning-formula", "rest-steak-before-slicing", "pork-cuts-map", "eighty-cooking-tips"],
    "aw": ["lidan-deng-sichuan-chef-50y", "hidden_menu_vip_dining", "italian_food_ordering", "japan_cooking"],
  },
  "coffee": {
    "summary": "coffee",
    "vn": ["latte-details", "sca-latte-art-exam", "foam-thickness", "extraction-latte-impact", "coffee-clean-cup-meaning", "become-coffee-connoisseur-fast", "espresso-crema-thickness-myth"],
    "aw": ["coffee_20years", "iiac_coffee_gold_award"],
  },
  "wine": {
    "vn": ["wine-business-and-aesthetics", "five-wine-tasting-terms", "red-wine-aeration", "decant-wine-two-charts", "six-wine-grapes", "sommelier-blind-tasting-contest"],
    "aw": [],
  },
  "beer": {"vn": [], "aw": []},
  "interior": {
    "summary": "home",
    "vn": ["lighting-texture-layers", "home-color-enlarge", "home-look-bigger-3tips", "home-weaken-boundaries", "home-need-focal-point", "home-soft-curves"],
    "aw": ["ikea_stockholm2025", "quanji_hotel_oriental_aesthetics", "morandi_color_misconception"],
  },
  "architecture": {
    "vn": ["one-house-vs-zijian", "western-architecture-ten-styles", "urban-village-answer"],
    "aw": ["harry_potter_hogwarts_architecture", "museum_staged_reality"],
  },
  "photo": {
    "summary": "photo",
    "vn": ["harmony-shooting", "photo-light-ratio", "photo-refine-trap-ai-era", "photo-framework-visual-lang", "candid-life", "lively-poses", "photo-clarity"],
    "aw": ["feipian_photography", "shemei_qutong", "travel-camera-spring-guide"],
  },
  "painting": {
    "summary": "painting",
    "vn": ["value-order-key", "value-vs-chroma", "paint-relation-not-color", "purity-order-premium", "warm-cool-way", "how-to-match-colors", "negative-space-importance", "klimt-unity-variety"],
    "aw": ["morandi_color_misconception"],
  },
  "sculpture": {
    "vn": ["clothing-folds-from-sculpture"],
    "aw": ["museum_staged_reality"],
  },
  "calligraphy": {
    "vn": ["calligraphy-first-principles"],
    "aw": [],
  },
  "story": {
    "summary": "video",
    "vn": ["2nIYM8mRzxo", "VCTwn3d4Uw", "what-is-montage", "five-common-montages", "how-to-use-transitions"],
    "aw": ["zhang_ailing_analysis", "liuzhenyun_ep01_dialogue"],
  },
  "comic": {
    "vn": [],
    "aw": ["one_piece_finale_roundtable"],
  },
  "film": {
    "summary": "film",
    "vn": ["joker-film-pull-part1", "zhouxingchi-audiovisual", "audiovisual-whitespace-power", "dry-film-pull-technique", "camera-movement-apple"],
    "aw": ["matt-damon-odyssey", "harry_potter_hogwarts_architecture"],
  },
  "tv": {
    "vn": ["us-tv-top10-2026", "top10-british-drama-21c"],
    "aw": ["duanju_chuhai"],
  },
  "game": {"vn": [], "aw": []},
  "instrument": {
    "vn": ["piano-fingertip-catch", "easy-slow-song-entry-beat"],
    "aw": [],
  },
  "music": {
    "vn": ["music-theory-modulation", "zhao-jun-authority"],
    "aw": ["gudian_antineihao_ep11", "gudian_commute_ep3", "tower-records-shibuya", "five_sounds_end_of_world", "taipei-witch-house"],
  },
  "speech": {
    "summary": "workplace",
    "vn": ["wangziru-how-to-improve-eloquence", "work-good-standard", "certainty-boss-wants", "chat-for-feelings-not-facts", "high-eq-no-filler-words", "s-rhythm"],
    "aw": ["jundongkou_communication_ep250", "smalltalk_scenes_art", "exit_expression_contest_daily_life"],
  },
}

VN_BASE = "https://chenzhiheng.cn/video-notes/"
AW_BASE = "https://chenzhiheng.cn/audio-workshop/"
PROJECTS = Path("/Users/chenzhiheng/Projects")

TPL = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name} · 评鉴</title>
  <link rel="stylesheet" href="../assets/site.css">
</head>
<body>
  <div class="wrap page">
    <header class="top">
      <a class="brand" href="../index.html">评鉴</a>
      <nav>
        <a href="../method.html">共同方法</a>
        <a href="../index.html#categories">类别</a>
      </nav>
    </header>
    <p class="crumb"><a href="../index.html">评鉴</a> / {group}</p>
    <h1 class="page-title">{name}</h1>
    <p class="ask">{ask}</p>

    <section class="panel vein">
      <h2>核心脉络</h2>
      <p class="vein-thesis">{thesis}</p>
      <div class="vein-grid">
{points}
      </div>
    </section>

    <section class="panel">
      <h2>典型失败</h2>
      <ul class="fail-list">
{fails}
      </ul>
    </section>

    <section class="panel">
      <h2>边界</h2>
      <ul class="bound-list">
{bounds}
      </ul>
    </section>

    <section class="panel">
      <h2>观察时先问</h2>
      <p class="hint">起步提问，用来对着脉络做现场核对。</p>
      <ol>
{items}
      </ol>
    </section>

    <section class="panel">
      <h2>材料厚度</h2>
      <p class="hint">脉络主要从 video-notes 与 audio-workshop 的总结中收束；厚薄决定后续补源优先级。</p>
      <div class="source-bar">
{sources}
      </div>
    </section>

    <section class="panel">
      <h2>参考资料</h2>
      <p class="hint">下列为站内消化稿标题与链接（可点开）。原平台链接见各总结页内标注。</p>
{refs}
    </section>

    <section class="block">
      <h2>已记录</h2>
      <div class="empty">
        <strong>这里还没有条目。</strong>
        <span>之后每一则都按四行写，方便和别的类别对照。</span>
        <div class="fields">
          <span>对象</span>
          <span>场合</span>
          <span>判断</span>
          <span>边界</span>
        </div>
      </div>
    </section>
    <footer>回到 <a href="../index.html">全部类别</a></footer>
  </div>
</body>
</html>
"""


def load_indexes():
    import json

    vn_list = json.loads((PROJECTS / "video-notes/docs/index.json").read_text(encoding="utf-8"))
    aw_list = json.loads((PROJECTS / "audio-workshop/docs/index.json").read_text(encoding="utf-8"))
    vn = {x["slug"]: x for x in vn_list}
    aw = {}
    for x in aw_list:
        fn = x.get("filename") or ""
        stem = fn.replace("-总结.svg", "").replace("-总结.html", "")
        if stem:
            aw[stem] = x
    return vn, aw


def resolve_refs(slug: str, vn: dict, aw: dict) -> str:
    cfg = REFS.get(slug) or {}
    items = []
    summary = cfg.get("summary")
    if summary:
        items.append(
            (
                "video-notes · 类目总结",
                f"{VN_BASE}category-summaries/{summary}-总结.html",
                {"coffee": "咖啡手作", "photo": "摄影拍摄", "painting": "绘画造型", "film": "影视视听", "home": "家装空间", "workplace": "职场表达", "video": "视频制作"}.get(summary, summary)
                + " · 核心观点",
            )
        )
    for s in cfg.get("vn") or []:
        it = vn.get(s)
        if not it:
            print(f"  warn missing vn:{s}")
            continue
        html = (it.get("outputs") or {}).get("html") or f"{s}-图文实录.html"
        items.append(("video-notes", f"{VN_BASE}{html}", it["title"]))
    for stem in cfg.get("aw") or []:
        it = aw.get(stem)
        if not it:
            print(f"  warn missing aw:{stem}")
            continue
        html = (it.get("filename") or f"{stem}-总结.svg").replace("-总结.svg", "-总结.html")
        items.append(("audio-workshop", f"{AW_BASE}{html}", it["title"]))

    if not items:
        return '      <p class="hint">暂无站内对应条目，脉络为脚手架，待补源。</p>'

    lis = "\n".join(
        f'        <li><span class="ref-src">{src}</span><a href="{href}" target="_blank" rel="noopener">{title}</a></li>'
        for src, href, title in items
    )
    return f'      <ul class="ref-list">\n{lis}\n      </ul>'


def render(page: dict, vn: dict, aw: dict) -> str:
    points = "\n".join(
        f"""        <article class="vein-item">
          <b>{i:02d}</b>
          <div>
            <h3>{title}</h3>
            <p>{body}</p>
          </div>
        </article>"""
        for i, (title, body) in enumerate(page["points"], 1)
    )
    fails = "\n".join(f"        <li>{x}</li>" for x in page["fails"])
    bounds = "\n".join(f"        <li>{x}</li>" for x in page["bounds"])
    items = "\n".join(f"        <li>{q}</li>" for q in page["questions"])
    sources = "\n".join(
        f'        <span class="source-pill{" thin" if level in ("薄", "待补源") else ""}"><strong>{label}</strong>{level}</span>'
        for label, level in page["sources"]
    )
    return TPL.format(
        name=page["name"],
        group=page["group"],
        ask=page["ask"],
        thesis=page["thesis"],
        points=points,
        fails=fails,
        bounds=bounds,
        items=items,
        sources=sources,
        refs=resolve_refs(page["slug"], vn, aw),
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    vn, aw = load_indexes()
    for page in PAGES:
        path = OUT / f"{page['slug']}.html"
        path.write_text(render(page, vn, aw), encoding="utf-8")
        print("wrote", path.name)
    print("total", len(PAGES))


if __name__ == "__main__":
    main()
