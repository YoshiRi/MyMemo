import json

sdic=[]
with open("slam_hub_twint.json", 'r',encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        sdic.append(data)


tweets = []
ids = []

for dic in sdic:
    # if there are already same tweets ids
    if dic['conversation_id'] in ids:
        indx = ids.index(dic['conversation_id'])
        tweets[indx]
        
        # add txt
        tweets[indx]['text'].append(dic['tweet'])
        # add url
        for url in dic['urls']:
            tweets[indx]['urls'].append(url)
         # add photo url
        if dic['photos']:
            for photo in dic['photos']:
                tweets[indx]["photos"].append(photo)           
    # New id 
    else:
        ids.append(dic['conversation_id'])
        newtweet = {}
        newtweet['text'] = []
        newtweet['urls'] = []
        newtweet['photos'] = []
        
        newtweet['conversation_id'] = dic['conversation_id']
        # add txt
        newtweet['text'].append(dic['tweet'])
        # add url
        for url in dic['urls']:
            newtweet['urls'].append(url)
        # add photo url
        if dic['photos']:
            for photo in dic['photos']:
                newtweet["photos"].append(photo)
        tweets.append(newtweet)

import subprocess
import arxiv

docdics = []
counts = 0

for dics in tweets:
# 途中からやったときの名残
# for i in range(117,len(tweets)):
#dics = tweets[i]
    print( counts,"of",len(tweets),flush=True)
    counts += 1
    
    ddic = {}
    title = ""
    youtubetitle = ""
    arxivtitle = ""
    imgurl = ""
    
    # url が空の場合はスキップ
    if not dics["urls"] and not dics["photos"]:
        print("skip",flush=True)
        continue
        
    # arxivのリンク情報を埋める
    for url in dics["urls"]:
        # Arxivだった場合
        if 'arxiv' in url:
            arxivid_ = url.split('/')[-1]
            ids = [s for s in arxivid_.split('.') if s[0].isdigit()]

            arxivid__=""
            for i in range(len(ids)):
                arxivid__ += ids[i]+"."
            arxivid = arxivid__[:-1]
            arxivtitle = arxiv.query(id_list=[arxivid])[0]['title']

        # Youtubeの場合
        if 'youtu' in url: # if it is youtube link
            imgurl = subprocess.check_output("youtube-dl --get-thumbnail \""+url +"\"", shell=True)
            youtubetitle = subprocess.check_output("youtube-dl --get-title \""+ url +"\"", shell=True)
            # solve decode problem
            if type(imgurl) == bytes:
                imgurl = imgurl.decode("utf-8", "ignore")
            if type(youtubetitle) == bytes:
                youtubetitle = youtubetitle.decode("utf-8", "ignore")
            
    
    # photosの画像があるならそちらを優先
    if dics["photos"]:
        imgurl = dics["photos"][0]
    
    
    # arxivやYoutubeにないときはスキップ
    if arxivtitle:
        title = arxivtitle
    else:
        if youtubetitle:
            title = youtubetitle
        else:
            # arxivやYoutubeにもないとき画像があるなら 最後のツイートの最初の行をタイトルとする
            if imgurl:
                title = dics["text"][0].split("\n")[0]
            # 画像もタイトルもない場合はスキップ
            else:
                print(dics["text"])
                continue

        
        
    ddic['id'] = dics['conversation_id']
    ddic['title'] = title
    ddic['imgurl'] = imgurl
    ddic['text'] = dics['text']
    docdics.append(ddic)

createddate = sdic[0]["date"]

preamble = "---\nmarp: true\nheader: 'from @slam_hub'\nfooter: '@ossyaritoori'\nsize: 16:9\npaginate: true\n---\n \n# SLAM_HUB Twitter 情報まとめ \n" + "Created on " + createddate +"\n"

mkdocfile = open("survey_twint.md","w+",encoding='utf-8')

#Write Preamble
mkdocfile.write(preamble)

for mkdics in docdics:
    imgurl=mkdics["imgurl"]
    # URLが改行で終わっている場合これを解除
    if imgurl:
        if imgurl[-1] == "\n":
            imgurl = imgurl[:-1]
    # 要約となるtextはだいたい最初のツイート
    abstract = mkdics["text"][-1]
    onepagestring = "\n---\n"+"## " + mkdics["title"]    + "\n" + abstract    + "\n ![bg right:40% fit]("+imgurl+")\n"
    mkdocfile.write(onepagestring)
    
mkdocfile.close()


