# 高中英语维克多词汇电子版

蓝奏云：<https://zhiyuyu.lanzout.com/b098xjaid> 密码:6mnk

维词（20220402）.zip 为最新版导出

.db 文件为提取的文件 （使用sqlite可用）

victory.zip为旧版

网页版 <https://1299172402.github.io/weici/>

## 维词数据库文件分析

### apk 解包后的 .db 文件

| 类型   | db文件位置           | 通过 sqlite 读取                     |
| ------ | -------------------- | ------------------------------------ |
| 学生版 | /assets/ext.db       | 不可以（之前是可以的，看来被修改了） |
| 教师版 | /assets/weici_ext.db | 可以                                 |

### 学生版app 运行后的数据（需要root环境）

- 位置：/data/data/com.android.weici.senior.student/databases

  | 名称            | 备注                                                         |
  | --------------- | ------------------------------------------------------------ |
  | ext369.db       | 学生版apk解压后的ext.db为同一文件（哈希值相同）              |
  | ext_plain369.db | 可以直接打开，但与同为369版本的教师端apk内的 .db 文件哈希值不同 |

  注：369 应该指得是当前学生端app的版本号（通常教师端与学生端版本号同步）

- 位置：/data/data/com.android.weici.senior.student/media

  维词APP - 我的 - 音频下载 - 下载语音包后的文件

  内部的 sound 文件夹为空

  应该是以压缩包形式下载的，然后自动解压了

## 表中 detail 的各个属性

| 是否需要 | 属性                 | 释义         | 备注                                                 |
| -------- | -------------------- | ------------ | ---------------------------------------------------- |
| 0        | id                   | 词id         | 数据库中的词汇id                                     |
| 1        | word                 | 单词/词组    |                                                      |
| 1        | part_of_speech       | 词性         | 如 adj，n                                            |
| 1        | en_phonetic_symbols  | 英音英标     |                                                      |
| 1        | en_file              | 英音发音文件 |                                                      |
| 1        | usa_phonetic_symbols | 美音音标     |                                                      |
| 1        | usa_file             | 美音发音文件 |                                                      |
| 0        | speech               |              | 未知的音频文件（不在下载里面）                       |
| 1        | lv_speak             | 口语         |                                                      |
| 1        | lv_write             | 书面         |                                                      |
| 1        | lv_read              | 阅读         |                                                      |
| 1        | lv_frequency         | 词频         |                                                      |
| 1        | point                |              | 是否为重难点词汇，类型int                            |
| 0        | point_name           |              | 0：否；1：是                                         |
| 0        | not_use              |              | 未知                                                 |
| 0        | not_use_name         |              | 未知                                                 |
| 0        | outpoint             |              | 是否为额外词汇，类型int                              |
| 0        | outpoint_name        |              | 0：无；1：课标外词汇；2：课标派词汇                  |
| 1        | use_method           | 用法点拨     |                                                      |
| 1        | antonym              | 反义词       |                                                      |
| 1        | synonyms             | 近义词       |                                                      |
| 1        | family_word          | 词族         |                                                      |
| 0        | family_word_image    |              |                                                      |
| 0        | rate                 |              | 未知，类型int，从0开始，测试到24仍有，有部分数字没有 |
| -1       | area                 | 地区         | 如 苏、津                                            |
| -1       | book                 |              | 类型int                                              |
| -1       | book_name            |              | 类型str，如"Book 1"                                  |
| -1       | unit                 |              | 类型int                                              |
| -1       | unit_name            |              | 类型str，如"Unit 2"                                  |
| -1       | fixed_id             |              | 似乎全部为0                                          |
| -1       | simple               |              | 如"B1U2"                                             |
| -1       | follow_word          |              | 感觉就是当前词                                       |
|          | new_attribute        |              | 未知                                                 |
| 1        | gy_paraphrase        | 英文释义     |                                                      |
| 1        | gy_fixed_collocation | 固定搭配     |                                                      |
| 1        | gy_derivative        | 派生词汇     |                                                      |
| 1        | gy_exam_link         | 真题解析     |                                                      |
|          | gy_word_expand       |              |                                                      |

是否需要中：

| 值   | 释义       |
| ---- | ---------- |
| -1   | 完全不需要 |
| 0    | 不太需要   |
| 1    | 需要       |
