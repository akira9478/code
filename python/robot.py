# coding=utf-8
import socket
import sys
import random
host = 'irc.freenode.net'
port= 6667
chan = "#NMG-thu"
robot = "funghi_robot"
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
explore = ['黒より黒く闇より暗き漆黒に我が深紅の混淆を望みたもう。覚醒の時来たれり。無謬の境界に落ちし理。無行の歪みとなりて現出せよ。踊れ踊れ踊れ、我が力の奔流に望は崩壊なり並ぶ者なき崩壊なり。万象等しく灰塵に帰し、深淵より来たれ！エクスプロージョン', '紅き黒炎。万界の王。天地の法を敷衍すれど、我は万象ショウウンの理。崩壊破壊の別名なり。永劫の鉄槌は我が元に下れ！エクスプロージョン！', '光に覆われし漆黒よ。夜をまといし爆炎よ。紅魔の名のもとに原初の崩壊を顕現す。終焉の王国の地に力の根元を隠匿せし者。我が前に統べよ！エクスプロージョン！', '私は爆裂魔法しか愛せない！', '人が深淵を覗くとき、深淵もまた人を覗いているのだ']
ball = ['球','籃框','籃球','鹹酥雞','機器','妹子','運動飲料','球員','球場','球衣','球','球','球','球','球','球']
irc.connect((host,port))
irc.send("USER "+ robot +" "+ robot +" "+ robot +" :This is a fun bot!\n") #user authentication
irc.send("NICK "+ robot +"\n")                            #sets nick
irc.send("PRIVMSG nickserv :iNOOPE\r\n")    #auth
irc.send("JOIN "+ chan +"\n")        #join the chan

while 1:    #puts it in a loop
   data=irc.recv(2048)  #receive the text
   print( data)   #print text to console
   user = data.split(':')[1]
   user = user.split('!')[0]
   if (data.find('PING'))!= -1:                          #check if 'PING' is found
      irc.send('PONG ' + data.split()[1]+'\r\n')
   elif data.find('c8763') !=-1 : #you can change !hi to whatever you want
      irc.send('PRIVMSG '+chan+' : '+ user +' 幫我撐十秒 星爆氣流斬 \r\n')
   elif data.find(':hi') !=-1 : #you can change !hi to whatever you want
      irc.send('PRIVMSG '+chan+' :Hello '+ user +' 今天過得怎麼樣啊 o\'_\'o \r\n')
   elif data.find('megumin') !=-1 : #you can change !hi to whatever you want
      exp = random.choice ( explore )
      irc.send('PRIVMSG '+chan+' : '+exp+'\r\n')
   elif data.find('human') !=-1 : #you can change !hi to whatever you want
      irc.send('PRIVMSG '+chan+' :類類~~ \r\n')
   elif data.find('obov') !=-1 : #you can change !hi to whatever you want
      irc.send('PRIVMSG '+chan+' : 個人認為引戰，等其他版主意見 \r\n')
   elif data.find('戰歌') !=-1 : #you can change !hi to whatever you want
      irc.send('PRIVMSG '+chan+' : (ㄏ￣□￣)ㄏ 喔~~喔喔~~喔喔~~喔喔~~爪爪 \r\n')
   elif data.find('喵電感應') !=-1 : #you can change !hi to whatever you want
      irc.send('PRIVMSG '+chan+' : 大 家 女子 ，莖 天 白勺 口苗 口苗 女子 可 I 口奧 <3 <3  \r\n')
   elif data.find('排骨酥') !=-1 : #you can change !hi to whatever you want
      irc.send('PRIVMSG '+chan+' : 我味增湯 都不放味曾與豆腐 改放菜頭排骨酥用肉燥提味 \r\n')
      irc.send('PRIVMSG '+chan+' : 又清又香 但就略油 壽司改成糯米加香菇肉絲去蒸 \r\n')
      irc.send('PRIVMSG '+chan+' : 這兩個配起來非常棒 最好是加點香菜 \r\n')
      irc.send('PRIVMSG '+chan+' : 不是菜頭湯 這味增湯 喝起來跟排骨酥湯90%口感很像 \r\n')
   elif data.find('野野野野野') !=-1 : #you can change !hi to whatever you want
      irc.send('PRIVMSG '+chan+' : 麻煩這系列的請到政黑或其他地方討論好嗎?這裡是喜 \r\n')
      irc.send('PRIVMSG '+chan+' : 　　　　　　　　　　　　　　　　　　　　　　 仙 \r\n')
      irc.send('PRIVMSG '+chan+' : 　　　　　　　　　　　　　　　　　　　　　　 樂 \r\n')
      irc.send('PRIVMSG '+chan+' : 　　　　　　　　　　　　　　　　　　　　　　 園 \r\n')
   elif data.find('你誰') !=-1 : #you can change !hi to whatever you want
      irc.send('PRIVMSG '+chan+' : 其實全IRC只有我一個人，不信我換個ID推一樣的話給你看 \r\n')
   elif data.find('壞') !=-1 : #you can change !hi to whatever you want
      irc.send('PRIVMSG '+chan+' : 壞了50收 \r\n')
   elif data.find('公海') !=-1 : #you can change !hi to whatever you want
      irc.send('PRIVMSG '+chan+' : 我們現在是在公海，在公海殺人只有這頻道的註冊帳號可以抓我。 \r\n')
      irc.send('PRIVMSG '+chan+' : 我和#NMG-thu的mingyen也有一點交情。 \r\n')
   elif data.find('告你') !=-1 : #you can change !hi to whatever you want
      irc.send('PRIVMSG '+chan+' : 法院認證的'+ user +' \r\n')
   elif data.find('公威阿') !=-1 : #you can change !hi to whatever you want
      irc.send('PRIVMSG '+chan+' : 毫無反應 就只是個機器人 \r\n')
   elif data.find('在哪裡') !=-1 : #you can change !hi to whatever you want
      irc.send('PRIVMSG '+chan+' : 來大都找我吧 我在大都等你 \r\n')
   elif data.find('我難過') !=-1 : #you can change !hi to whatever you want
      irc.send('PRIVMSG '+chan+' : 我難過的是 放棄你 放棄愛 \r\n')
      irc.send('PRIVMSG '+chan+' : 放棄的夢被打碎 \r\n')
      irc.send('PRIVMSG '+chan+' : 忍住悲哀 \r\n')
   elif data.find('啤酒') !=-1 : #you can change !hi to whatever you want
      irc.send('PRIVMSG '+chan+' : 給 '+user+' 一罐啤酒 \r\n')
   elif data.find('打球') !=-1 : #you can change !hi to whatever you want
      exp = random.choice ( ball )
      irc.send('PRIVMSG '+chan+' : '+user+'打球 '+exp+'你帶 \r\n')
   elif data.find('我是人類') !=-1 : #you can change !hi to whatever you want
      irc.send('PRIVMSG '+chan+' : 廢話! \r\n')
   elif data.find('自我介紹') !=-1 : #you can change !hi to whatever you want
      irc.send('PRIVMSG '+chan+' : 我是人類 \r\n')
   elif data.find('老二') !=-1 : #you can change !hi to whatever you want
      irc.send('PRIVMSG '+chan+' : 鄉民都是30CM起跳的 \r\n')
   elif data.find('開戰') !=-1 : #you can change !hi to whatever you want
      irc.send('PRIVMSG '+chan+' : 我雞排已經買好了 \r\n')
