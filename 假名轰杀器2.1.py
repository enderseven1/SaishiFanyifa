# -*- coding:utf-8 -*-
#list1 = "あ ア a  い イ i   う ウ u   え エ e   お オ o か カ ka   き キ ki   く ク ku   け ケ ke   こ コ ko さ サ sa   し シ si/shi   す ス su   せ セ se   そ ソ so た タ ta   ち チ chi   つ ツ tsu   て テ te   と ト to な ナ na   に ニ ni   ぬ ヌ nu   ね ネ ne   の ノ no は ハ ha   ひ ヒ hi   ふ フ fu   へ ヘ he   ほ ホ ho ま マ ma   み ミ mi   む ム mu   め メ me   も モ mo や ヤ ya   ゆ ユ yu   よ ヨ yo ら ラ ra   り リ ri   る ル ru   れ レ re   ろ ロ ro わ ワ wa   を ヲ o/wo ん ン n が ガ ga ぎ ギ gi ぐ グ gu げ ゲ ge ご ゴ go ざ ザ za じ ジ zi/ji ず ズ zu ぜ ゼ ze ぞ ゾ zo だ ダ da ぢ ヂ ji/di づ ヅ zu/du で デ de ど ド do ば バ ba び ビ bi ぶ ブ bu べ ベ be ぼ ボ bo ぱ パ pa ぴ ピ pi ぷ プ pu ぺ ペ pe ぽ ポ po っ ッ xtu"
#lis2t = list1.split()
#print(list2)
import easygui,sys
dict0 = {'危ない':'危', '少ない':'少','必ず':'必', '死ぬ':'死', 'ない':'不','ず':'不', 'ぬ':'不', 'ません':'不','あり':'有','ある':'有','いる':'在',
        #'この':'這','これ':'這','あの':'那','あれ':'那','その他':'他','その':'那','それ':'那','こころ':'心','ここ':'這裏','そこ':'那裏','あそこ':'那裏','こども':'子供'
        'あした':'明日','した':'了','つもり':'打算',
        #'チェック':'検査','セルフ':'自分','ワクチン':'疫苗','ガイド':'指南','はじめに':'前言',
        #'トラブル':'問題','マタニティ':'孕婦','ドクター':'医生','マーカー':'記号筆','チョコレート':'巧克力','':'','':'','':'','':''
        }
list1 = ['あ', 'ア', 'い', 'イ', 'う', 'ウ', 'え', 'エ', 'お', 'オ', 'か', 'カ', 'き', 'キ', 'く', 'ク', 'け', 'ケ', 'こ', 'コ', 'さ', 
        'サ', 'し', 'シ', 'す', 'ス', 'せ', 'セ', 'そ', 'ソ', 'た', 'タ', 'ち', 'チ', 'つ', 'ツ', 'て', 'テ', 'と', 'ト', 'な', 'ナ', 'に', 'ニ', 
        'ぬ', 'ヌ', 'ね', 'ネ', 'の', 'ノ', 'は', 'ハ', 'ひ', 'ヒ', 'ふ', 'フ', 'へ', 'ヘ', 'ほ', 'ホ', 'ま', 'マ', 'み', 'ミ', 'む', 'ム', 'め', 
        'メ', 'も', 'モ', 'や', 'ヤ', 'ゆ', 'ユ', 'よ', 'ヨ', 'ら', 'ラ', 'り', 'リ', 'る', 'ル', 'れ', 'レ', 'ろ', 'ロ', 'わ', 'ワ', 'を', 'ヲ', 
        'ん', 'ン', 'が', 'ガ', 'ぎ', 'ギ', 'ぐ', 'グ', 'げ', 'ゲ', 'ご', 'ゴ', 'ざ', 'ザ', 'じ', 'ジ', 'ず', 'ズ', 'ぜ', 'ゼ', 'ぞ', 'ゾ', 'だ', 
        'ダ', 'ぢ', 'ヂ', 'づ', 'ヅ', 'で', 'デ', 'ど', 'ド', 'ば', 'バ', 'び', 'ビ', 'ぶ', 'ブ', 'べ', 'ベ', 'ぼ', 'ボ', 'ぱ', 'パ', 'ぴ', 'ピ', 
        'ぷ', 'プ', 'ぺ', 'ペ', 'ぽ', 'ポ', 'っ', 'ッ','ぁ','ァ','ィ','ぃ','ぇ','ェ','ぅ','ゥ','ぉ','ォ','ゎ','ヮ','ゃ','ャ','ゅ','ュ','ょ','ョ', 
        'ヶ','ゖ','ー', 'ヵ', 'ｱ', 'ｲ', 'ｴ', 'ｵ', 'ﾅ', 'ﾆ', 'ﾇ', 'ﾈ', 'ﾉ', 'ﾏ', 'ﾐ', 'ﾑ', 'ﾒ', 'ﾓ', 'ﾔ', 'ﾕ', 'ﾖ', 'ﾜ', 'ｦ', 'ﾝ', ' ', 'ﾞ', '゙', 
        '゛', '゚', 'ゑ', 'ゐ','ヴ', 'ヰ', 'ヱ', 'ヸ', 'ヹ', 'ヺ', 'ヷ', 'ヴ']
dict1 = {'結': '结', '収': '收', '賄': '贿', '窮': '穷', '腎': '肾', '虜': '虏', '読': '读', '臨': '临', '貞': '贞', '脈': '脉', '躍': '跃', '組': '组', '薬': '药', '穂': '穗', '戸': '户', 
        '無': '无', '紋': '纹', '彫': '雕', '撮': '摄', '絞': '绞', '畝': '亩', '減': '减', '電': '电', '賭': '赌', '門': '门', '塊': '块', '飼': '饲', '風': '风', '鎮': '镇', '掲': '揭', 
        '緩': '缓', '娯': '娱', '穀': '谷', '黒': '黑', '遊': '游', '複': '复', '弁': '辩', '喪': '丧', '粋': '粹', '詠': '咏', '嵐': '岚', '働': '动', '喩': '喻', '採': '采', '違': '违', 
        '飲': '饮', '価': '价', '輝': '辉', '職': '职', '銀': '银', '須': '须', '絡': '络', '領': '领', '護': '护', '諧': '谐', '衛': '卫', '詐': '诈', '嬢': '娘', '庁': '厅', '賢': '贤', 
        '従': '从', '陥': '陷', '陸': '陆', '許': '许', '則': '则', '渉': '涉', '際': '际', '習': '习', '仏': '佛', '憂': '忧', '繭': '茧', '闇': '暗', '車': '车', '経': '经', '晩': '晚', 
        '紛': '纷', '紡': '纺', '徹': '彻', '頃': '顷', '毀': '毁', '糾': '纠', '両': '两', '宮': '宫', '撃': '击', '圏': '圈', '璽': '玺', '録': '录', '歓': '欢', '脅': '胁', '弾': '弹', 
        '奨': '奖', '塁': '垒', '緒': '绪', '呪': '咒', '観': '观', '払': '拂', '補': '补', '網': '网', '試': '试', '呂': '吕', '緯': '纬', '郵': '邮', '掃': '扫', '訓': '训', '顔': '颜', 
        '動': '动', '優': '优', '侶': '侣', '矯': '矫', '給': '给', '餌': '饵', '頑': '顽', '熱': '热', '軒': '轩', '極': '极', '詮': '诠', '錦': '锦', '雑': '杂', '摯': '挚', '裏': '里', 
        '況': '况', '聖': '圣', '積': '积', '隠': '隐', '妬': '妒', '魚': '鱼', '豊': '丰', '庫': '库', '殻': '壳', '痩': '瘦', '乗': '乘', '転': '转', '適': '适', '貸': '贷', '礎': '础', 
        '摂': '摄', '績': '绩', '綱': '纲', '課': '课', '慄': '栗', '諸': '诸', '養': '养', '郷': '乡', '鉱': '矿', '審': '审', '竜': '龙', '穫': '获', '塗': '涂', '遺': '遗', '詞': '词', 
        '婦': '妇', '舎': '舍', '碁': '棋', '諮': '咨', '責': '责', '児': '儿', '𠮟': '叱', '艦': '舰', '漢': '汉', '節': '节', '稲': '稻', '島': '岛', '憶': '忆', '曽': '曾', '検': '检', 
        '構': '构', '絶': '绝', '計': '计', '憩': '息', '備': '备', '貯': '贮', '館': '馆', '問': '问', '釈': '释', '係': '系', '煙': '烟', '傘': '伞', '嚇': '吓', '謹': '谨', '築': '筑', 
        '顎': '颚', '鑑': '鉴', '遡': '溯', '偉': '伟', '遠': '远', '錠': '锭', '繰': '缲', '併': '并', '証': '证', '諾': '诺', '変': '变', '貿': '贸', '塩': '盐', '験': '验', '浄': '净', 
        '諭': '谕', '橋': '桥', '亀': '龟', '側': '侧', '抜': '拔', '幹': '干', '後': '后', '縁': '缘', '幾': '几', '剤': '剂', '覚': '觉', '視': '视', '艶': '艳', '執': '执', '閣': '阁', 
        '倉': '仓', '偽': '伪', '誕': '诞', '導': '导', '湯': '汤', '枠': '桦', '畳': '叠', '黙': '默', '憤': '愤', '様': '样', '墳': '坟', '強': '强', '遷': '迁', '著': '著', '発': '发', 
        '劇': '剧', '恥': '耻', '麺': '面', '冊': '册', '線': '线', '達': '达', '鉛': '铅', '霊': '灵', '済': '济', '気': '气', '標': '标', '賃': '赁', '継': '继', '暁': '晓', '業': '业', 
        '陽': '阳', '飾': '饰', '斬': '斩', '葉': '叶', '歯': '齿', '慶': '庆', '華': '华', '場': '场', '賞': '赏', '壇': '坛', '拝': '拜', '擁': '拥', '騰': '腾', '飯': '饭', '闘': '斗', 
        '斎': '斋', '仮': '假', '軍': '军', '討': '讨', '誘': '诱', '繕': '缮', '掛': '挂', '缶': '罐', '親': '亲', '暦': '历', '測': '测', '覧': '览', '興': '兴', '揮': '挥', '個': '个', 
        '鬱': '郁', '犠': '牺', '編': '编', '棄': '弃', '跡': '迹', '紳': '绅', '鶏': '鸡', '載': '载', '辺': '边', '猟': '猎', '準': '准', '軟': '软', '診': '诊', '慮': '虑', '剝': '剥', 
        '剰': '剩', '醜': '丑', '弔': '吊', '鋭': '锐', '煩': '烦', '賜': '赐', '酢': '醋', '詣': '诣', '輩': '辈', '織': '织', '麗': '丽', '菓': '果', '図': '图', '訟': '讼', '続': '续', 
        '維': '维', '軽': '轻', '誇': '夸', '詰': '诘', '資': '资', '紀': '纪', '臓': '脏', '桜': '樱', '鮮': '鲜', '長': '长', '沢': '泽', '災': '灾', '湧': '涌', '衆': '众', '銭': '钱', 
        '帯': '带', '亜': '亚', '請': '请', '歴': '历', '謝': '谢', '墾': '垦', '約': '约', '賂': '赂', '圧': '压', '産': '产', '轄': '辖', '負': '负', '孫': '孙', '芸': '艺', '帳': '帐', 
        '栄': '荣', '譜': '谱', '潔': '洁', '欄': '栏', '機': '机', '質': '质', '漁': '渔', '講': '讲', '開': '开', '窯': '窑', '懇': '恳', '題': '题', '噴': '喷', '縄': '绳', '書': '书', 
        '氷': '冰', '獲': '获', '舗': '铺', '聴': '听', '僅': '仅', '異': '异', '謙': '谦', '瘍': '疡', '評': '评', '競': '竞', '飢': '饥', '鋼': '钢', '疎': '疏', '報': '报', '脇': '胁', 
        '環': '环', '歩': '步', '涼': '凉', '餅': '饼', '貧': '贫', '贈': '赠', '愛': '爱', '壌': '壤', '勲': '勋', '鳥': '鸟', '霧': '雾', '鐘': '钟', '傷': '伤', '傾': '倾', '協': '协', 
        '懸': '悬', '焼': '烧', '処': '处', '徴': '征', '尋': '寻', '瑠': '琉', '挿': '插', '談': '谈', '喚': '唤', '還': '还', '買': '买', '荘': '庄', '軌': '轨', '順': '顺', '濃': '浓', 
        '預': '预', '勢': '势', '貨': '货', '売': '卖', '咲': '咲', '絵': '绘', '箋': '笺', '昇': '升', '論': '论', '査': '查', '購': '购', '紺': '绀', '浜': '滨', '術': '术', '醸': '酿', 
        '託': '讬', '誤': '误', '鍛': '锻', '債': '债', '倹': '俭', '貴': '贵', '細': '细', '羨': '羡', '縫': '缝', '階': '阶', '険': '险', '復': '复', '渦': '涡', '納': '纳', '謁': '谒', 
        '陰': '阴', '訴': '诉', '溝': '沟', '応': '应', '営': '营', '製': '制', '賛': '赞', '捜': '搜', '広': '广', '潰': '溃', '決': '决', '並': '并', '別': '别', '譲': '让', '輪': '轮', 
        '園': '园', '東': '东', '対': '对', '償': '偿', '歳': '岁', '単': '单', '為': '为', '襲': '袭', '総': '总', '鎌': '镰', '酔': '醉', '楽': '乐', '戻': '戾', '勧': '劝', '帥': '帅', 
        '儀': '仪', '遅': '迟', '詩': '诗', '層': '层', '純': '纯', '姉': '姊', '鈍': '钝', '樹': '树', '鯨': '鲸', '軸': '轴', '暫': '暂', '鳴': '鸣', '柵': '栅', '揚': '扬', '盤': '盘', 
        '腫': '肿', '毎': '每', '賀': '贺', '詳': '详', '羅': '罗', '倫': '伦', '緊': '紧', '療': '疗', '粛': '肃', '認': '认', '陣': '阵', '拡': '扩', '過': '过', '巻': '卷', '農': '农', 
        '曖': '暧', '張': '张', '絹': '绢', '換': '换', '較': '较', '輸': '输', '専': '专', '勝': '胜', '粧': '妆', '間': '间', '悪': '恶', '餓': '饿', '増': '增', '鎖': '锁', '渇': '渴', 
        '擬': '拟', '択': '择', '謀': '谋', '難': '难', '終': '终', '髪': '发', '誌': '志', '紅': '红', '縮': '缩', '語': '语', '獄': '狱', '確': '确', '敗': '败', '敵': '敌', '説': '说', 
        '設': '设', '現': '现', '勅': '敕', '緑': '绿', '雲': '云', '懐': '怀', '種': '种', '統': '统', '繊': '纤', '腸': '肠', '蓋': '盖', '隻': '只', '針': '针', '薫': '薰', '啓': '启', 
        '務': '务', '韓': '韩', '員': '员', '糧': '粮', '嘆': '叹', '鍵': '键', '額': '额', '挙': '举', '響': '响', '傑': '杰', '時': '时', '態': '太', '窓': '窗', '脳': '脑', '巣': '巢', 
        '聞': '闻', '頰': '颊', '紙': '纸', '訂': '订', '雰': '氛', '驚': '惊', '調': '调', '財': '财', '銘': '铭', '費': '费', '砕': '碎', '猶': '犹', '頼': '赖', '値': '值', '貢': '贡', 
        '齢': '龄', '幣': '币', '渓': '溪', '彙': '汇', '簡': '简', '恵': '汇', '記': '记', '隊': '队', '銃': '铳', '捨': '舍', '桟': '栈', '瀬': '濑', '藍': '蓝', '錯': '错', '締': '缔', 
        '徳': '德', '錬': '炼', '斉': '齐', '運': '运', '義': '义', '訪': '访', '識': '识', '隷': '隶', '薦': '荐', '喫': '吃', '禍': '祸', '岡': '冈', '汚': '污', '拠': '据', '実': '实', 
        '廃': '废', '沈': '沉', '堅': '坚', '見': '见', '駆': '驱', '範': '范', '紹': '绍', '規': '规', '僕': '仆', '籠': '笼', '戯': '戏', '閑': '闲', '剣': '剑', '連': '连', '囲': '围', 
        '渋': '涩', '壊': '坏', '憲': '宪', '円': '圆', '権': '权', '慣': '惯', '欠': '缺', '夢': '梦', '話': '话', '獣': '兽', '閉': '闭', '砲': '炮', '離': '离', '殺': '杀', '鉄': '铁', 
        '謡': '谣', '騎': '骑', '該': '该', '涙': '泪', '進': '进', '億': '亿', '駒': '驹', '縛': '缚', '隣': '邻', '寛': '宽', '綿': '绵', '錮': '锢', '馬': '马', '唄': '呗', '滅': '灭', 
        '陳': '陈', '糸': '丝', '閲': '阅', '罰': '罚', '顕': '显', '縦': '纵', '貝': '贝', '貫': '贯', '厳': '严', '飛': '飞', '韻': '韵', '帰': '归', '師': '师', '週': '周', '鏡': '镜', 
        '蛍': '萤', '衝': '冲', '倣': '仿', '飽': '饱', '級': '级', '筆': '笔', '駅': '驿', '釣': '钓', '顧': '顾', '鈴': '铃', '類': '类', '労': '劳', '漸': '渐', '訳': '译', '練': '练', 
        '剛': '刚', '頭': '头', '項': '项', '誠': '诚', '満': '满', '県': '县', '関': '关', '壱': '壹', '伝': '传', '戦': '战', '撲': '扑', '詔': '诏', '頓': '顿', '乾': '乾', '願': '愿', 
        '銅': '铜', '蔵': '藏', '潤': '润', '騒': '骚', '議': '议', '奮': '奋', '堀': '窟', '濫': '滥', '呉': '吴', '監': '监', '選': '选', '姫': '姬', '坂': '坡', '販': '贩', '膠': '胶', 
        '冨': '富', '悩': '恼', '効': '效', '膚': '肤', '窩': '窝', '損': '损', '篤': '笃', '頻': '频', '１': '1', '２': '2', '３': '3', '４': '4', '５': '5', '６': '6', '７': '7', 
        '８': '8', '９': '9', '０': '0', 'Ａ': 'A', 'Ｂ': 'B', 'Ｃ': 'C', 'Ｄ': 'D', 'Ｅ': 'E', 'Ｆ': 'F', 'Ｇ': 'G', 'Ｈ': 'H', 'Ｉ': 'I', 'Ｊ': 'J', 'Ｋ': 'K', 'Ｌ': 'L', 'Ｍ': 'M', 
        'Ｎ': 'N', 'Ｏ': 'O', 'Ｐ': 'P', 'Ｑ': 'Q', 'Ｒ': 'R', 'Ｓ': 'S', 'Ｔ': 'T', 'Ｕ': 'U', 'Ｖ': 'V', 'Ｗ': 'W', 'Ｘ': 'X', 'Ｙ': 'Y', 'Ｚ': 'Z', 'ａ': 'a', 'ｂ': 'b', 'ｃ': 'c', 
        'ｄ': 'd', 'ｅ': 'e', 'ｆ': 'f', 'ｇ': 'g', 'ｈ': 'h', 'ｉ': 'i', 'ｊ': 'j', 'ｋ': 'k', 'ｌ': 'l', 'ｍ': 'm', 'ｎ': 'n', 'ｏ': 'o', 'ｐ': 'p', 'ｑ': 'q', 'ｒ': 'r', 'ｓ': 's', 
        'ｔ': 't', 'ｕ': 'u', 'ｖ': 'v', 'ｗ': 'w', 'ｘ': 'x', 'ｙ': 'y', 'ｚ': 'z', '、': '，', '・': '、', '「': '“', '『': '‘', '』': '’', '」': '”', '\u3000': ' ', '條': '条',
        '絢': '绚', '澤': '泽', '濁': '浊', '駿': '骏', '綾': '绫', '繚': '缭', '譚': '谭', '龍': '龙', '鷹': '鹰', '蒼': '苍', '鳳': '凤', '“”':'', '磯':'矶', '鬪':'斗', '予':'豫', 
        '懲': '惩', '擾': '扰', '幇': '帮', '顛': '颠', '奪': '夺', '姦': '奸', '頒': '颁', '嘔': '呕', '頚': '颈', '鬆': '松', '誰': '谁', '鶴': '鹤', '糞':'粪'}
c = []
d = []
ssss = ''
fd = []
yuan=[]
try:
    while True:
        erttt = input('请输入你要轰杀假名的日语（支持多行直接复制，输入\"smdmzk.start\"即可转换，输入\"smdmzk.delete\"删除上一条：\n')
        if erttt.upper() == 'SMDMZK.START':
            for u,jk in enumerate(c):
                ssss = ''
                fd = []
                for sb in dict0.keys(): #替换
                    jk = jk.replace(sb,dict0[sb])
                for dfg in jk:
                    fd.append(dfg)
                for index,s in enumerate(fd):
                    if s == '々':
                        fd[index] = fd[index-1]
                for sd in fd:
                    ssss += sd
                for i in list1:
                    jk = jk.replace(i,'')
                    ssss = ssss.replace(i,'')
                c[u] = jk
                d.append(ssss)
            print('你要转换的原内容为：')
            for i in yuan:
                print(i)
            print('\n假名轰杀完毕：\n')
            for aaa in c:
                print(aaa)
            print('\n转为简体汉字后：\n')
            for fjk,sbbbb in enumerate(d):
                for e in dict1.keys(): #替换繁体字
                    sbbbb = sbbbb.replace(e,dict1[e])
                d[fjk] = sbbbb
            for bbb in d:
                print(bbb)
            print(c,d,ssss,fd,yuan)
            c = []
            d = []
            ssss = ''
            fd = []
            yuan = []
            u = 0
            jk = ''
            aaa = ''
            fjk = 0
            bbb = ''
            sbbbb = ''
            i = ''
            sd = ''
            s = ''
            index = 0
            erttt = ''
        elif erttt.upper() == 'SMDMZK.DELETE':
            del c[-1]
            del yuan[-1]
            print('已删除')
        if erttt == None or erttt == '':
            c.append('')
            yuan.append('')
        else:
            c.append(erttt)
            yuan.append(erttt)
        print('\n')
except AttributeError:
    sys.exit()

#