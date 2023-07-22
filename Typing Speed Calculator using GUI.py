words = [&#39;banana&#39;, &#39;guitar&#39;, &#39;elephant&#39;, &#39;puzzle&#39;, &#39;coffee&#39;, &#39;rainbow&#39;, &#39;pencil&#39;, &#39;helicopter&#39;, &#39;butterfly&#39;,
&#39;book&#39;, &#39;microphone&#39;, &#39;ice cream&#39;, &#39;planet&#39;, &#39;sweater&#39;, &#39;cactus&#39;, &#39;clock&#39;, &#39;blanket&#39;, &#39;diamond&#39;,
&#39;popcorn&#39;, &#39;watermelon&#39;, &#39;laptop&#39;, &#39;whistle&#39;, &#39;suitcase&#39;, &#39;flower&#39;, &#39;cookie&#39;, &#39;ladder&#39;, &#39;dolphin&#39;, &#39;sock&#39;,
&#39;kite&#39;, &#39;lipstick&#39;, &#39;pineapple&#39;, &#39;camera&#39;, &#39;sunflower&#39;, &#39;basketball&#39;, &#39;pizza&#39;, &#39;saxophone&#39;, &#39;mushroom&#39;,
&#39;rainbow&#39;, &#39;lemon&#39;, &#39;tree&#39;, &#39;hammer&#39;, &#39;dragonfly&#39;, &#39;hat&#39;, &#39;cheese&#39;, &#39;bicycle&#39;, &#39;lemonade&#39;, &#39;pineapple&#39;,
&#39;toothbrush&#39;, &#39;kangaroo&#39;, &#39;paintbrush&#39;, &#39;drum&#39;, &#39;snowflake&#39;, &#39;calculator&#39;, &#39;mushroom&#39;, &#39;raccoon&#39;,
&#39;bracelet&#39;, &#39;grapefruit&#39;, &#39;camera&#39;, &#39;skateboard&#39;, &#39;octopus&#39;]

def labelSlider():
global count, sliderwords,speed
text = &quot;Welcome to typing Speed Increaser Game&quot;
if (count &gt;= len(text)):
count = 0
sliderwords = &#39;&#39;
sliderwords += text[count]
count += 1
fontLabel.configure(text=sliderwords)
fontLabel.after(150,labelSlider)
def time():
global timeleft, score,miss, speed, total
if(timeleft &gt;= 12):
pass
else:
timeLabelCount.configure(fg=&#39;red&#39;)
if(timeleft&gt;0):
timeleft -= 1
timeLabelCount.configure(text=timeleft)
timeLabelCount.after(1000,time)
if(timeleft==0):
pass
#print(letter)############list to all letter matched
if(timeleft==0):
speed = speed.join(letter)
#print(speed)############### all character matched
#print(len(speed))
total = ((len(speed)) / 60)

7

#print(total)
print(&#39;Typing Speed is &#39;, math.ceil(total),&#39;letter/sec&#39;)

else:
gamePlayDetailLabel.configure(text=&#39;Hit = {} | Miss = {} | Total Score =
{}&#39;.format(score,miss,score-miss))
speedperseclLabel.configure(text=&#39;Typing Speed in letter/sec =
{}&#39;.format(math.ceil(total)))
rr = messagebox.askretrycancel(&#39;Notification&#39;,&#39;Play Again Hit Retry Button&#39;)
if(rr==True):
score = 0
timeleft = 60
miss = 0
timeLabelCount.configure(text=timeleft)
wordLabel.configure(text=words[0])
scoreLabelCount.configure(text=score)

def startGame(event):
global score, miss , speed
if(timeleft == 60):
time()
gamePlayDetailLabel.configure(text=&#39;&#39;)
if(wordEntry.get() == wordLabel[&#39;text&#39;]):
score += 1
scoreLabelCount.configure(text=score)
if(wordEntry.get() == wordLabel[&#39;text&#39;]):
letter.append(wordEntry.get())

else:
miss += 1
random.shuffle(words)
wordLabel.configure(text=words[0])
wordEntry.delete(0,END)
####################################
from tkinter import *
import random
from tkinter import messagebox
import math

8
######################## Root Method
root = Tk()
root.geometry(&quot;800x550+400+100&quot;)
root.configure(bg=&quot;powder blue&quot;)
root.title(&quot;Typing Speed Increser Game&quot;)
##################### Variable Section
score = 0
timeleft = 60
count = 0
sliderwords = &#39;&#39;
miss = 0
letter = []
speed = &#39;&#39;
total = &#39;&#39;

###################### Lable Method
fontLabel = Label(root, text=&quot; &quot;, font=(&quot;airal&quot;,25, &quot;italic bold&quot;),
bg=&quot;powder blue&quot;,fg=&quot;red&quot;,width=40)
fontLabel.place(x=10, y=10)
labelSlider()
random.shuffle(words)
wordLabel = Label(root,text=words[0],font=(&quot;airal&quot;,40, &quot;italic bold&quot;),bg=&#39;powder blue&#39;)
wordLabel.place(x=350, y=200)
scoreLabel = Label(root,text=&quot;Your Score :&quot;,font=(&quot;airal&quot;,25, &quot;italic bold&quot;),bg=&quot;powder blue&quot;)
scoreLabel.place(x=10,y=100)

scoreLabelCount = Label(root,text=score,font=(&quot;airal&quot;,25, &quot;italic bold&quot;),bg=&quot;powder
blue&quot;,fg=&#39;blue&#39;)
scoreLabelCount.place(x=80,y=180)
timerCount = Label(root,text=&quot;Time Left :&quot;,font=(&quot;airal&quot;,25, &quot;italic bold&quot;),bg=&quot;powder blue&quot;)
timerCount.place(x=600,y=100)
timeLabelCount = Label(root,text=timeleft,font=(&quot;airal&quot;,25, &quot;italic bold&quot;),bg=&quot;powder
blue&quot;,fg=&#39;blue&#39;)
timeLabelCount.place(x=680,y=180)

9

gamePlayDetailLabel = Label(root,text=&quot;Type Word and Hit Button&quot;,font=(&quot;airal&quot;,20, &quot;italic
bold&quot;),bg=&quot;powder blue&quot;,fg=&#39;violet red&#39;)
gamePlayDetailLabel.place(x=180,y=450)
speedperseclLabel = Label(root,font=(&quot;airal&quot;,35, &quot;italic bold&quot;),bg=&quot;powder blue&quot;,fg=&#39;red&#39;)
speedperseclLabel.place(x=85,y=480)

####################### Entry Method
wordEntry = Entry(root,font=(&quot;airal&quot;,25, &quot;italic bold&quot;),bd=10,justify=&quot;center&quot;)
wordEntry.place(x=250,y=300)
wordEntry.focus_set()
################################################################

root.bind(&#39;&lt;Return&gt;&#39;,startGame)

root.mainloop()
