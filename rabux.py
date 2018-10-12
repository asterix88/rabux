# -*- coding:utf-8 -*-
# Coded by : Asterix

import os
import sys
from time import sleep

if sys.platform == "linux2":
	os.system("clear")
elif sys.platform == "win32":
	os.system("cls")
else:
	os.system("clear")
print "\033[1;31m+-----------------------------------------+"

print """               _                  
              ( )                 
  _ __    _ _ | |_    _   _       
 ( '__) /'_` )| '_`\ ( ) ( )(`\/')
 | |   ( (_| || |_) )| (_) | >  < 
 (_)   `\__,_)(_,__/'`\___/'(_/\_)  V.1.0                   

 """    
print "\033[0mAuthor: Asterix | 11-04-2018 (09.30)"
print "\033[1;31mTeam  : BlackHole Security         "
print "\033[0mDeface Simple Script Maker  "
print "\033[1;31m+-----------------------------------------+"
print
print "\033[1;33mSelect:"
print
print "\033[1;32m[1] Script"
print "\033[1;32m[2] About"
print "\033[1;32m[q] Exit"
print "\n"

menu = raw_input("\033[1;31mrabux_>\033[1;32m")


if menu == '1':
    print " [1] Script 1"
    print " [2] Script 2"
    print " [3] Script 3"
    print " [4] Script 4"
    print " [q] exit"
	
    nc = raw_input("\033[1;31mrabux_>\033[1;32m")
    if nc == '1':
        try: 
            file = open("script1.html" , 'w')
        except(IOError):
            print ("ERROR")
            sys.exit()
		
        print "\033[1;33m\nScript Theme 1\033[1;32m"
        print 
        name_style=raw_input("Enter your name: ")
        team_style=raw_input("Enter your team name: ")
        greetz_style=raw_input("Greetz to: ")
        sleep(1)
        print " [+] Success !"
        print " [+] Script save as script1.html"
		
        file.write("""
<html>""")
        file.write("""
<head><meta http-equiv="Content-Language" content="en-us"> """)
        file.write('\n')
        file.write(""" 
<meta content="HACKED" name="description"/>
<meta content="HACKED" name="keywords"/>
<meta content="HACKED" name="Abstract"/>
<meta name="HACKED"/> """)

        file.write('\n')
    
        file.write("""
<link rel="icon" href="hackerraun.jpg"> """)
        file.write("""
<title>Hacked By """+name_style+"""</title> """)

        file.write('\n')
        
        file.write(""" 
<style type="text/css"> """)
        file.write("""
h1 {color: #333;font-size: 100px;margin: 1px auto;text-align:center; font-family:Orbitron;}
.neon {color: #FFFFFF;text-shadow: 0 0 5px #1ab4e7, 0 0 10px #1ab4e7, 0 0 30px #18a2d0, 0 0 45px #18a2d0, 0 0 60px #18a2d0;}
h2 {color: #333;font-size: 50px;margin: 1px auto;text-align:center;text-transform:uppercase; font-family:Audiowide;}
.neon {color: #FFFFFF;text-shadow: 0 0 5px #1ab4e7, 0 0 10px #1ab4e7, 0 0 30px #18a2d0, 0 0 45px #18a2d0, 0 0 60px #18a2d0;}
h3 {color: #333;font-size: 50px;margin: 1px auto;text-align:center;text-transform:uppercase; font-family:Audiowide;}
.neon {color: #FFFFFF;text-shadow: 0 0 5px #1ab4e7, 0 0 10px #1ab4e7, 0 0 30px #18a2d0, 0 0 45px #18a2d0, 0 0 60px #18a2d0;}
.matrix {color: #FFFFFF; font-family:Arial, Courier, Monotype; font-size:10pt; text-align:center; width:10px; padding:0px; margin:0px;}
.jokitz1{
    text-align : center;
    }
.jokitz2{
	text-align : center;
	font-family : Courier;
	}
	
</style>
</head> """)

        file.write("""
<body bgcolor=black lang=EN-US style='tab-interval:36.0pt; text-align:center'> <onload=type_text() onclick='alert("Zuahahaha")'> """)
        file.write('\n')
        
        file.write("""
<style>body{cursor:url("http://www.madleets.com/elhacker.cur"),auto;}html{display:table;height:100%;width:100%;}body{display:table-row;}body{display:table-cell;vertical-align:middle;text-align:center;}a:link{text-decoration:none;}</style>""")
        file.write('\n')
        file.write("""
<link href='http://fonts.googleapis.com/css?family=Iceland' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Orbitron:700' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Audiowide' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Iceland' rel='stylesheet' type='text/css'>

<p align="center" dir="ltr"></p>

<script type="text/javascript">

<!--   """)
        file.write("""
var message="Sorry, right-click has been disabled"; """)

        file.write(""" 
function clickIE() {if (document.all) {(message);return false;}}

function clickNS(e) {if

(document.layers||(document.getElementById&&!document.all)) {

if (e.which==2||e.which==3) {(message);return false;}}}

if (document.layers)

{document.captureEvents(Event.MOUSEDOWN);document.onmousedown=clickNS;}

else{document.onmouseup=clickNS;document.oncontextmenu=clickIE;}

document.oncontextmenu=new Function("return false")

 // -->

</script>

<!-- <script language="JavaScript1.2" type="text/javascript">

function ClearError() {return true;}

window.onerror = ClearError;

</script> -->  """)
        file.write('\n')
        
        file.write("""
<script type="text/javascript" language="javascript">



<!--

var rows=1; // must be an odd number

var speed=10; // lower is faster

var reveal=2; // between 0 and 2 only. The higher, the faster the word appears

var effectalign="center" //enter "center" to center it.



/***********************************************

* The Matrix Text Effect- by Richard Womersley (http://www.mf2fm.co.uk/rv)

* This notice must stay intact for use

* Visit http://www.dynamicdrive.com/ for full source code

***********************************************/

         """)
        file.write('\n')
         
        file.write(""" 
var w3c=document.getElementById && !window.opera;;

var ie45=document.all && !window.opera;

var ma_tab, matemp, ma_bod, ma_row, x, y, columns, ma_txt, ma_cho;

var m_coch=new Array();

var m_copo=new Array();

window.onload=function() { """)
        file.write('\n')
        
        file.write("""
    if (!w3c && !ie45) return """)
        file.write("""
  var matrix=(w3c)?document.getElementById("matrix"):document.all["matrix"];

  ma_txt=(w3c)?matrix.firstChild.nodeValue:matrix.innerHTML;

 ma_txt=" "+ma_txt+" ";

 columns=ma_txt.length;

 if (w3c) { """)
        file.write("""
    while (matrix.childNodes.length) matrix.removeChild(matrix.childNodes[0]);

    ma_tab=document.createElement("table");

    ma_tab.setAttribute("border", 0);

    ma_tab.setAttribute("align", effectalign);

    ma_tab.style.backgroundColor="#000000";

    ma_bod=document.createElement("tbody");

    for (x=0; x<rows; x++) { """)

        file.write("""
      ma_row=document.createElement("tr");

      for (y=0; y<columns; y++) { """)
        file.write(""" 
          matemp=document.createElement("td");

          matemp.setAttribute("id", "Mx"+x+"y"+y);

         matemp.className="matrix";

          matemp.appendChild(document.createTextNode(String.fromCharCode(160)));

          ma_row.appendChild(matemp);
          
        }
        ma_bod.appendChild(ma_row);

      }
      ma_tab.appendChild(ma_bod);

      matrix.appendChild(ma_tab);
         
    } else {
            
      ma_tab='<ta'+'ble align="'+effectalign+'" border="0" style="background-color:#000000">';

      for (var x=0; x<rows; x++) {
      
        ma_tab+='<t'+'r>';

        for (var y=0; y<columns; y++) {
        
        ma_tab+='<t'+'d class="matrix" id="Mx'+x+'y'+y+'"> </'+'td>';
      }
      
      ma_tab+='</'+'tr>';
      
    }
    
    ma_tab+='</'+'table>';
    
    matrix.innerHTML=ma_tab;
  }
  
  ma_cho=ma_txt;

  for (x=0; x<columns; x++) {
  
    ma_cho+=String.fromCharCode(32+Math.floor(Math.random()*94));

    m_copo[x]=0;
  }
  
  ma_bod=setInterval("mytricks()", speed);
}


function mytricks() {

  x=0;

  for (y=0; y<columns; y++) {
  
    x=x+(m_copo[y]==100);

    ma_row=m_copo[y]%100;

    if (ma_row && m_copo[y]<100) {
    
      if (ma_row<rows+1) {
      
        if (w3c) {
        
          matemp=document.getElementById("Mx"+(ma_row-1)+"y"+y);

          matemp.firstChild.nodeValue=m_coch[y];
        }
        
        else {
        
          matemp=document.all["Mx"+(ma_row-1)+"y"+y];

          matemp.innerHTML=m_coch[y];
          
        }
        
        matemp.style.color="#81F2FF";

        matemp.style.fontWeight="bold";
        
      }
      
      if (ma_row>1 && ma_row<rows+2) {
      
        matemp=(w3c)?document.getElementById("Mx"+(ma_row-2)+"y"+y):document.all["Mx"+(ma_row-2)+"y"+y];

        matemp.style.fontWeight="normal";

        matemp.style.color="#00BBFF";
      }
      
      if (ma_row>2) {

        matemp=(w3c)?document.getElementById("Mx"+(ma_row-3)+"y"+y):document.all["Mx"+(ma_row-3)+"y"+y];

        matemp.style.color="#20FFDA";
      }
              
      if (ma_row<Math.floor(rows/2)+1) m_copo[y]++;

      else if (ma_row==Math.floor(rows/2)+1 && m_coch[y]==ma_txt.charAt(y)) zoomer(y);

      else if (ma_row<rows+2) m_copo[y]++;

      else if (m_copo[y]<100) m_copo[y]=0;
    }
            
    else if (Math.random()>0.9 && m_copo[y]<100) {
        m_coch[y]=ma_cho.charAt(Math.floor(Math.random()*ma_cho.length));

        m_copo[y]++;
        
      }
    }
          
    if (x==columns) clearInterval(ma_bod);
    
}

function zoomer(ycol) {

  var mtmp, mtem, ytmp;

  if (m_copo[ycol]==Math.floor(rows/2)+1) {
  
    for (ytmp=0; ytmp<rows; ytmp++) {
              
      if (w3c) {
                
        mtmp=document.getElementById("Mx"+ytmp+"y"+ycol);

        mtmp.firstChild.nodeValue=m_coch[ycol];
      }
      
      else {
        mtmp=document.all["Mx"+ytmp+"y"+ycol];

        mtmp.innerHTML=m_coch[ycol];
      }
              
      mtmp.style.color="#5BEEFF";

      mtmp.style.fontWeight="bold";
      
    }
            
    if (Math.random()<reveal) {
      mtmp=ma_cho.indexOf(ma_txt.charAt(ycol));

      ma_cho=ma_cho.substring(0, mtmp)+ma_cho.substring(mtmp+1, ma_cho.length);
                
    }
              
    if (Math.random()<reveal-1) ma_cho=ma_cho.substring(0, ma_cho.length-1);

    m_copo[ycol]+=199;

    setTimeout("zoomer("+ycol+")", speed);
              
  }
  
  else if (m_copo[ycol]>200) {
              
    if (w3c) {
    
      mtmp=document.getElementById("Mx"+(m_copo[ycol]-201)+"y"+ycol);

      mtem=document.getElementById("Mx"+(200+rows-m_copo[ycol]--)+"y"+ycol);
    }
    
    else {
                  
      mtmp=document.all["Mx"+(m_copo[ycol]-201)+"y"+ycol];

      mtem=document.all["Mx"+(200+rows-m_copo[ycol]--)+"y"+ycol];
    }
    mtmp.style.fontWeight="normal";

    mtem.style.fontWeight="normal";

    setTimeout("zoomer("+ycol+")", speed);
  }
  else if (m_copo[ycol]==200) m_copo[ycol]=100+Math.floor(rows/2);

  if (m_copo[ycol]>100 && m_copo[ycol]<200) {
                  
    if (w3c) {
                      
      mtmp=document.getElementById("Mx"+(m_copo[ycol]-101)+"y"+ycol);

      mtmp.firstChild.nodeValue=String.fromCharCode(160);

      mtem=document.getElementById("Mx"+(100+rows-m_copo[ycol]--)+"y"+ycol);

      mtem.firstChild.nodeValue=String.fromCharCode(160);
    }
    
    else {
                      
      mtmp=document.all["Mx"+(m_copo[ycol]-101)+"y"+ycol];

      mtmp.innerHTML=String.fromCharCode(160);

      mtem=document.all["Mx"+(100+rows-m_copo[ycol]--)+"y"+ycol];

      mtem.innerHTML=String.fromCharCode(160);
                      
    }
                     
   setTimeout("zoomer("+ycol+")", speed);
                     
 } """)
 
        file.write('\n')
        
        file.write("""
var h1 = document.getElementsByTagName("h1")[0],

text = h1.innerText || h1.textContent,

split = [], i, lit = 0, timer = null;

for(i = 0; i < text.length; ++i) {

split.push("<span>" + text[i] + "</span>");

}

h1.innerHTML = split.join("");

split = h1.childNodes;



var flicker = function() {

lit += 0.01;

if(lit >= 1) {

clearInterval(timer);

}


for(i = 0; i < split.length; ++i) {

if(Math.random() < lit) {

split[i].className = "neon";


} else {

split[i].className = "";

}

}

}

setInterval(flicker, 100);



}

//strat sec 



// end  -->

</script> """)
        
        file.write('\n')
        
        file.write("""
<body style="color: #FFFFFF; background-color: #000000">

<img src="https://scontent.fsub5-1.fna.fbcdn.net/v/t1.0-1/p160x160/18700043_261442954329212_6270640292972818895_n.jpg?oh=674e5b3fab52074398d9e4532ffd6b63&oe=59D9D762"></center><br>

<center><img src="http://www6.0zz0.com/2011/03/14/06/269205957.gif"></center><br> """)
        file.write('\n')
        
        
        file.write("""
<h1> ..:: """+name_style+""" ::..</h1>""")
        file.write('\n')
        file.write("""
<h3>"""+team_style+"""</h3>""")
        
        file.write('\n')
        
        file.write("""

<center><img src="http://www6.0zz0.com/2011/03/14/06/269205957.gif"></center><br>

<center><div style="width:250px;height:50px;border:6px ridge orange;"> """)
        file.write("""
<font face="Iceland" style="color:#00FFFF;text-shadow:0px 1px 5px #000;font-size:20px">YOUR FACE STATUS:</font>
<font face="Iceland" style="color:Red;text-shadow:0px 1px 5px #000;font-size:20px">LULZ !</font><br>
<font face="Iceland" style="color:#00FFFF;text-shadow:0px 1px 5px #000;font-size:20px">YOUR SITE STATUS:</font>
<font face="Iceland" style="color:Red;text-shadow:0px 1px 5px #000;font-size:20px">LOSE !</font><br></div></center><br>


""")
        file.write('\n')
        
        file.write("""
  
<font face="Iceland" style="color:#00FCFF;text-shadow:0px 1px 5px #000;font-size:50px"><br>
<div id="matrix" class="auto-style8" font-size="100px"> Greetz To :"""+greetz_style+""" </div></font><br>

</body>
</html> """)
        sys.exit()
        
    	
		
		
    if nc == '2':
		try: 
			file = open("script2.html" , 'w')
		except(IOError):
			print ("ERROR")
			sys.exit()
			
		print "\033[1;33m\nScript Theme 2 \033[1;32m"
		print 
		name_style = raw_input("Enter your name: ")
		message = raw_input("Enter your message: ")
		picture_style = raw_input("Enter your picture: ")
		sleep(1)
		print "[+] Success"
		print "[+] Script is save as script2.html"
	
		
		file.write("""
<html>   
    <head>
        <title>Hacked By """+name_style+"""</title>
		<link href="http://fonts.googleapis.com/css?family=Orbitron" rel="stylesheet" type="text/css" />

		<script>alert("Got Hacked?");</script>
		<style type="text/css"> """)
		file.write('\n')
		
		file.write("""
#container {
  width:97vw;
  margin:2vw auto;
}
font{
  font-familly:Orbitron;
  text-align:center;
  letter-spacing:1px;
  color:white;
  /*Create overlap*/
  
  margin:0;
  line-height:0;
  /*Animation*/
  
  -webkit-animation: glitch1 2.5s infinite;
  
          animation: glitch1 2.5s infinite;
}
font:nth-child(2) {
  color: #67f3da;
  -webkit-animation: glitch2 2.5s infinite;
          animation: glitch2 2.5s infinite;
}
font:nth-child(3) {
  color: #f16f6f;
  -webkit-animation: glitch3 2.5s infinite;
          animation: glitch3 2.5s infinite;
}
/*Keyframes*/
@-webkit-keyframes glitch1 {
  0% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  7% {
    -webkit-transform: skew(-0.5deg, -0.9deg);
            transform: skew(-0.5deg, -0.9deg);
    opacity: 0.75;
  }
  10% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  27% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  30% {
    -webkit-transform: skew(0.8deg, -0.1deg);
            transform: skew(0.8deg, -0.1deg);
    opacity: 0.75;
  }
  35% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  52% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  55% {
    -webkit-transform: skew(-1deg, 0.2deg);
            transform: skew(-1deg, 0.2deg);
    opacity: 0.75;
  }
  50% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  72% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  75% {
    -webkit-transform: skew(0.4deg, 1deg);
            transform: skew(0.4deg, 1deg);
    opacity: 0.75;
  }
  80% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  100% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
}
@keyframes glitch1 {
  0% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  7% {
    -webkit-transform: skew(-0.5deg, -0.9deg);
            transform: skew(-0.5deg, -0.9deg);
    opacity: 0.75;
  }
  10% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  27% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  30% {
    -webkit-transform: skew(0.8deg, -0.1deg);
            transform: skew(0.8deg, -0.1deg);
    opacity: 0.75;
  }
  35% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  52% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  55% {
    -webkit-transform: skew(-1deg, 0.2deg);
            transform: skew(-1deg, 0.2deg);
    opacity: 0.75;
  }
  50% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  72% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  75% {
    -webkit-transform: skew(0.4deg, 1deg);
            transform: skew(0.4deg, 1deg);
    opacity: 0.75;
  }
  80% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  100% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
}
@-webkit-keyframes glitch2 {
  0% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  7% {
    -webkit-transform: translate(-2px, -3px);
            transform: translate(-2px, -3px);
    opacity: 0.5;
  }
  10% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  27% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  30% {
    -webkit-transform: translate(-5px, -2px);
            transform: translate(-5px, -2px);
    opacity: 0.5;
  }
  35% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  52% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  55% {
    -webkit-transform: translate(-5px, -1px);
            transform: translate(-5px, -1px);
    opacity: 0.5;
  }
  50% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  72% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  75% {
    -webkit-transform: translate(-2px, -6px);
            transform: translate(-2px, -6px);
    opacity: 0.5;
  }
  80% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  100% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
}
@keyframes glitch2 {
  0% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  7% {
    -webkit-transform: translate(-2px, -3px);
            transform: translate(-2px, -3px);
    opacity: 0.5;
  }
  10% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  27% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  30% {
    -webkit-transform: translate(-5px, -2px);
            transform: translate(-5px, -2px);
    opacity: 0.5;
  }
  35% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  52% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  55% {
    -webkit-transform: translate(-5px, -1px);
            transform: translate(-5px, -1px);
    opacity: 0.5;
  }
  50% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  72% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  75% {
    -webkit-transform: translate(-2px, -6px);
            transform: translate(-2px, -6px);
    opacity: 0.5;
  }
  80% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  100% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
}
mm
@-webkit-keyframes glitch3 {
  0% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  7% {
    -webkit-transform: translate(2px, 3px);
            transform: translate(2px, 3px);
    opacity: 0.5;
  }
  10% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  27% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  30% {
    -webkit-transform: translate(5px, 2px);
            transform: translate(5px, 2px);
    opacity: 0.5;
  }
  35% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  52% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  55% {
    -webkit-transform: translate(5px, 1px);
            transform: translate(5px, 1px);
    opacity: 0.5;
  }
  50% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  72% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  75% {
    -webkit-transform: translate(2px, 6px);
            transform: translate(2px, 6px);
    opacity: 0.5;
  }
  80% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  100% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
}
@keyframes glitch3 {
  0% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  7% {
    -webkit-transform: translate(2px, 3px);
            transform: translate(2px, 3px);
    opacity: 0.5;
  }
  10% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  27% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  30% {
    -webkit-transform: translate(5px, 2px);
            transform: translate(5px, 2px);
    opacity: 0.5;
  }
  35% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  52% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  55% {
    -webkit-transform: translate(5px, 1px);
            transform: translate(5px, 1px);
    opacity: 0.5;
  }
  50% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  72% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  75% {
    -webkit-transform: translate(2px, 6px);
            transform: translate(2px, 6px);
    opacity: 0.5;
  }
  80% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  100% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
}
		</style>
	</head>
	</head>
	<body bgcolor="black" oncontextmenu="return false;" onkeydown="return false;" onmousedown="return false;" ondragstart="return false" onselectstart="return false">
		<iframe width="0" height="0" scrolling="yes" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/403414851&amp;auto_play=true&amp;hide_related=false&amp;show_comments=false&amp;show_user=true&amp;show_reposts=false&amp;visual=false"></iframe>
		<center>
			<br />

			<br />

			<br />

			<br />

			<br />
			<div id="container">
			    <img src=" """+picture_style+""" " title="Hacked" />
			    <br />

				<br />

				<font face="Orbitron" size="7">Hacked By """+name_style+"""</font>
				<br />

				<br />

				<br />

				<font face="Orbitron" size="5">"""+message+"""</font>
			</div>
		</center>
		<script type="text/javascript">
var snowmax=30
var snowcolor=new Array("white","yellow","red","aqua")
var snowtype=new Array("Arial Narrow","Times","Comic Sans MS")
var snowletter="."
var sinkspeed=0.6
var snowmaxsize=30
var snowminsize=10
var snowingzone=1
var snow=new Array()
var marginbottom
var marginright
var timer
var i_snow=0
var x_mv=new Array();
var crds=new Array();
var lftrght=new Array();
var browserinfos=navigator.userAgent 
var ie5=document.all&&document.getElementById&&!browserinfos.match(/Opera/)
var ns6=document.getElementById&&!document.all
var opera=browserinfos.match(/Opera/)  
var browserok=ie5||ns6||opera
function randommaker(range) {  
 rand=Math.floor(range*Math.random())
    return rand
}
function initsnow() {
 if (ie5 || opera) {
  marginbottom = document.body.clientHeight
  marginright = document.body.clientWidth
 }
 else if (ns6) {
  marginbottom = window.innerHeight
  marginright = window.innerWidth
 }
 var snowsizerange=snowmaxsize-snowminsize
 for (i=0;i<=snowmax;i++) {
  crds[i] = 0;                      
     lftrght[i] = Math.random()*15;         
     x_mv[i] = 0.03 + Math.random()/10;
  snow[i]=document.getElementById("s"+i)
  snow[i].style.fontFamily=snowtype[randommaker(snowtype.length)]
  snow[i].size=randommaker(snowsizerange)+snowminsize
  snow[i].style.fontSize=snow[i].size
  snow[i].style.color=snowcolor[randommaker(snowcolor.length)]
  snow[i].sink=sinkspeed*snow[i].size/5
  if (snowingzone==1) {snow[i].posx=randommaker(marginright-snow[i].size)}
  if (snowingzone==2) {snow[i].posx=randommaker(marginright/2-snow[i].size)}
  if (snowingzone==3) {snow[i].posx=randommaker(marginright/2-snow[i].size)+marginright/4}
  if (snowingzone==4) {snow[i].posx=randommaker(marginright/2-snow[i].size)+marginright/2}
  snow[i].posy=randommaker(2*marginbottom-marginbottom-2*snow[i].size)
  snow[i].style.left=snow[i].posx
  snow[i].style.top=snow[i].posy
 }
 movesnow()
}
function movesnow() {
 for (i=0;i<=snowmax;i++) {
  crds[i] += x_mv[i];
  snow[i].posy+=snow[i].sink
  snow[i].style.left=snow[i].posx+lftrght[i]*Math.sin(crds[i]);
  snow[i].style.top=snow[i].posy 
  if (snow[i].posy>=marginbottom-2*snow[i].size || parseInt(snow[i].style.left)>(marginright-3*lftrght[i])){
   if (snowingzone==1) {snow[i].posx=randommaker(marginright-snow[i].size)}
   if (snowingzone==2) {snow[i].posx=randommaker(marginright/2-snow[i].size)}
   if (snowingzone==3) {snow[i].posx=randommaker(marginright/2-snow[i].size)+marginright/4}
   if (snowingzone==4) {snow[i].posx=randommaker(marginright/2-snow[i].size)+marginright/2}
   snow[i].posy=0
  }
 }
 var timer=setTimeout("movesnow()",50)
}
for (i=0;i<=snowmax;i++) {
 document.write("<span id='s"+i+"' style='position:absolute;top:-"+snowmaxsize+"'>"+snowletter+"</span>")
}
if (browserok) {
 window.onload=initsnow
}
		</script>
		<script type="text/javascript">
//<![CDATA[
shortcut={all_shortcuts:{},add:function(a,b,c){var
d={type:"keydown",propagate:!1,disable_in_input:!1,target:document,keycode:!1};if(c)for(var
e in d)"undefined"==typeof c[e]&&(c[e]=d[e]);else
c=d;d=c.target,"string"==typeof
c.target&&(d=document.getElementById(c.target)),a=a.toLowerCase(),e=function(d){d=d||window.event;if(c.disable_in_input){var
e;d.target?e=d.target:d.srcElement&&(e=d.srcElement),3==e.nodeType&&(e=e.parentNode);if("INPUT"==e.tagName||"TEXTAREA"==e.tagName)return}d.keyCode?code=d.keyCode:d.which&&(code=d.which),e=String.fromCharCode(code).toLowerCase(),188==code&&(e=","),190==code&&(e=".");var
f=a.split("+"),g=0,h={"`":"~",1:"!",2:"@",3:"#",4:"$",5:"%",6:"^",7:"&",8:"*",9:"(",0:")","-":"_","=":"+",";":":","'":'"',",":"<",".":">","/":"?","\\":"|"},i={esc:27,escape:27,tab:9,space:32,"return":13,enter:13,backspace:8,scrolllock:145,scroll_lock:145,scroll:145,capslock:20,caps_lock:20,caps:20,numlock:144,num_lock:144,num:144,pause:19,"break":19,insert:45,home:36,"delete":46,end:35,pageup:33,page_up:33,pu:33,pagedown:34,page_down:34,pd:34,left:37,up:38,right:39,down:40,f1:112,f2:113,f3:114,f4:115,f5:116,f6:117,f7:118,f8:119,f9:120,f10:121,f11:122,f12:123},j=!1,l=!1,m=!1,n=!1,o=!1,p=!1,q=!1,r=!1;d.ctrlKey&&(n=!0),d.shiftKey&&(l=!0),d.altKey&&(p=!0),d.metaKey&&(r=!0);for(var
s=0;k=f[s],s<f.length;s++)"ctrl"==k||"control"==k?(g++,m=!0):"shift"==k?(g++,j=!0):"alt"==k?(g++,o=!0):"meta"==k?(g++,q=!0):1<k.length?i[k]==code&&g++:c.keycode?c.keycode==code&&g++:e==k?g++:h[e]&&d.shiftKey&&(e=h[e],e==k&&g++);if(g==f.length&&n==m&&l==j&&p==o&&r==q&&(b(d),!c.propagate))return
d.cancelBubble=!0,d.returnValue=!1,d.stopPropagation&&(d.stopPropagation(),d.preventDefault()),!1},this.all_shortcuts[a]={callback:e,target:d,event:c.type},d.addEventListener?d.addEventListener(c.type,e,!1):d.attachEvent?d.attachEvent("on"+c.type,e):d["on"+c.type]=e},remove:function(a){var
a=a.toLowerCase(),b=this.all_shortcuts[a];delete
this.all_shortcuts[a];if(b){var
a=b.event,c=b.target,b=b.callback;c.detachEvent?c.detachEvent("on"+a,b):c.removeEventListener?c.removeEventListener(a,b,!1):c["on"+a]=!1}}},shortcut.add("Ctrl+U",function(){top.location.href="http://www.shafou.com"});
//]]>  
		</script>
	</body>
</html> """)

		
    if nc == '3':
		try:
			file = open("scirpt3.html", 'w')
		except(IOError):
			print ("ERORR")
			sys.exit()
		
		
		print "\033[1;33m\nScript Theme 3\033[1;32m"
		print 
		name_style = raw_input("Enter your name: ")
		team_style = raw_input("Enter your team name: ")
		greetz_style = raw_input("Greetz to: ")
		sleep(1)
		print "[+] Success"
		print "[+] Script save as script3.html"
		
		file.write("""
<html>
<head>
<title>"""+name_style+"""</title>
	<style>

@import url(http://fonts.googleapis.com/css?family=Gilda+Display);

html {
  background-color:black;
  color: white;
  overflow: hidden;
  height: 100%;
  -webkit-user-select: none;
     -moz-user-select: none;
      -ms-user-select: none;
          user-select: none;
		  font-size: medium;
}

.error {
  text-align: center;
  font-family: 'Gilda Display', serif;
  
  text-align: center;
  width: 100%;
  height: 120px;
  margin: auto;
  position: absolute;
  top: 0;
  bottom: 0;
  left: -60px;
  right: 0;
  -webkit-animation: noise-3 1s linear infinite;
          animation: noise-3 1s linear infinite;
  overflow: default;
}

body:after {
  content:' """ +name_style+""" ';
  font-family: OCR-A;
  font-size: 70px;
  
  text-align: center;
  width: 550px;
  margin: auto;
  position: absolute;
  top: 25%;
  bottom: 0;
  left: 0;
  right: 35%;
  opacity: 0;
  color: red;
  -webkit-animation: noise-1 .2s linear infinite;
          animation: noise-1 .2s linear infinite;
}
body:before {
  content: ' """+name_style+""" ';
  font-family: OCR-A;
  font-size: 75px;
  
  text-align: center;
  width: 550px;
  margin: auto;
  position: absolute;
  top: 25%;
  bottom: 0;
  left: 0;
  right: 35%;
  opacity: 0;
  color: green;
  -webkit-animation: noise-2 .2s linear infinite;
          animation: noise-2 .2s linear infinite;
}

.info {
  text-align: center;
  width: 200px;
  height: 60px;
  margin: auto;
  position: absolute;
  top: 280px;
  bottom: 0;
  left: 20px;
  right: 0;
  -webkit-animation: noise-3 1s linear infinite;
          animation: noise-3 1s linear infinite;
}

.info:before {
  content: ' """+team_style+""" ';
  font-family: OCR-A;
  font-size: 50px;
  text-align: center;
  width: 800px; 
  margin: auto;
  position: absolute;
  top: 20px;
  bottom: 0;
  left: 40px;
  right: 100px;
  opacity: 0;
  color: red;
  -webkit-animation: noise-2 .2s linear infinite;
          animation: noise-2 .2s linear infinite;
}

.info:after {
  content: ' """+team_style+""" ';
  font-family: OCR-A;
  font-size: 50px;
  text-align: center;
  width: 800px;
  margin: auto;
  position: absolute;
  top: 20px;
  bottom: 0;
  left: 40px;
  right: 0;
  opacity: 0;
  color: blue;
  -webkit-animation: noise-1 .2s linear infinite;
          animation: noise-1 .2s linear infinite;
}

@-webkit-keyframes noise-1 {
  0%, 20%, 40%, 60%, 70%, 90% {opacity: 0;}
  10% {opacity: .1;}
  50% {opacity: .5; left: -6px;}
  80% {opacity: .3;}
  100% {opacity: .6; left: 2px;}
}

@keyframes noise-1 {
  0%, 20%, 40%, 60%, 70%, 90% {opacity: 0;}
  10% {opacity: .1;}
  50% {opacity: .5; left: -6px;}
  80% {opacity: .3;}
  100% {opacity: .6; left: 2px;}
}

@-webkit-keyframes noise-2 {
  0%, 20%, 40%, 60%, 70%, 90% {opacity: 0;}
  10% {opacity: .1;}
  50% {opacity: .5; left: 6px;}
  80% {opacity: .3;}
  100% {opacity: .6; left: -2px;}
}

@keyframes noise-2 {
  0%, 20%, 40%, 60%, 70%, 90% {opacity: 0;}
  10% {opacity: .1;}
  50% {opacity: .5; left: 6px;}
  80% {opacity: .3;}
  100% {opacity: .6; left: -2px;}
}

@-webkit-keyframes noise {
  0%, 3%, 5%, 42%, 44%, 100% {opacity: 1; -webkit-transform: scaleY(1); transform: scaleY(1);}  
  4.3% {opacity: 1; -webkit-transform: scaleY(1.7); transform: scaleY(1.7);}
  43% {opacity: 1; -webkit-transform: scaleX(1.5); transform: scaleX(1.5);}
}

@keyframes noise {
  0%, 3%, 5%, 42%, 44%, 100% {opacity: 1; -webkit-transform: scaleY(1); transform: scaleY(1);}  
  4.3% {opacity: 1; -webkit-transform: scaleY(1.7); transform: scaleY(1.7);}
  43% {opacity: 1; -webkit-transform: scaleX(1.5); transform: scaleX(1.5);}
}

@-webkit-keyframes noise-3 {
  0%,3%,5%,42%,44%,100% {opacity: 1; -webkit-transform: scaleY(1); transform: scaleY(1);}
  4.3% {opacity: 1; -webkit-transform: scaleY(4); transform: scaleY(4);}
  43% {opacity: 1; -webkit-transform: scaleX(10) rotate(60deg); transform: scaleX(10) rotate(60deg);}
}

@keyframes noise-3 {
  0%,3%,5%,42%,44%,100% {opacity: 1; -webkit-transform: scaleY(1); transform: scaleY(1);}
  4.3% {opacity: 1; -webkit-transform: scaleY(4); transform: scaleY(4);}
  43% {opacity: 1; -webkit-transform: scaleX(10) rotate(60deg); transform: scaleX(10) rotate(60deg);}
}

.wrap {
  top: 30%;
  left: 25%;
  
  height: 200px;
  
  margin-top: -100px;
  position: absolute;
}
code {
  color: white;
}
span.blue {
  color: #48beef;
}
span.comment {
  color: #7f8c8d;
}
span.orange {
  color: #f39c12;
}
span.green {
  color: #33cc33;
}

.viewFull {
  font-family:OCR-A;
  color:orange;
  text-decoration:;
}

	
}

 @media only screen and (min-height: 500px) {

.viewFull{
  display:none; 	
	}

}
	</style>
</head>
<body>



<div class="error">

<div class="wrap">
  <div class="404">
    <pre><code>
	 <span class="green">&lt;!</span><span></span><span class="green">!&gt;</span>
<span class="orange">&lt;html&gt;</span>
    <span class="orange">&lt;style&gt;</span>
 * {
	<span class="green">your_system</span>:<span class="blue">lulz!</span>;
}
     <span class="orange">&lt;/style&gt;</span>
 <span class="orange">&lt;body&gt;</span> 
          Hacked by """+name_style+"""
      Greetz To :
	<span class="comment">&lt;!--""" +greetz_style+ """
we just tested your system 
fix your website bug :) --&gt;
		</span>
		</span>
    <span class="orange"></span> 
			  

</div>
<br />
<span class="info">
<br />

			<span class="orange">&nbsp;&lt;/body&gt;</span>

<br/>
      				<span class="orange">&lt;/html&gt;</span>
    	</code></pre>
  </div>
</div>

</span>
</body>
</html> """)
    
		
    if nc == '4':
		try:
			file = open("Script4.html", 'w')
		except(IOError):
			print "ERROR"
			sys.exit()
			
		print "\033[1;33m\nScript Theme4\033[1;32m"
		print 
		name_style = raw_input("Enter your name: ")
		team_style = raw_input("Enter your team name: ")
		picture_style= raw_input("Your picture: ")
		message= raw_input("Enter your message: ")
		greetz_style = raw_input("Greetz to: ")
		sleep(1)
		print "[+] Success"
		print "[+] Script is save as script4.html"
		
		file.write("""


<html> 
<head> 
<title>Hacked | """+team_style+"""</title>
 </head> 

<link rel="shortcut icon" href=" """+picture_style+""" ">
<link href='http://fonts.googleapis.com/css?family=Jolly+Lodger' rel='stylesheet' type='text/css'>
<body oncontextmenu="return false;" onkeydown="return false;" onmousedown="return false;" type="text/css" bgcolor="#010101"><style type="text/css">body { font-family: 'Jolly Lodger'; color: white; padding: 0; margin: 0; background-image: url(''); background-repeat:no-repeat; background-position:center; background-size: 100% 100%;}.ALXploits_Blink {-webkit-animation-name: blinker;-webkit-animation-duration: 2s;-webkit-animation-timing-function: linear;-webkit-animation-iteration-count: infinite;-moz-animation-name: blinker;-moz-animation-duration: 1s;-moz-animation-timing-function: linear;-moz-animation-iteration-count: infinite; animation-name: blinker; animation-duration: 1s; animation-timing-function: linear; animation-iteration-count: infinite; color: red;}.name { text-decoration: none;}@-moz-keyframes roll { 100% { -moz-transform: rotate(360deg); } }@-o-keyframes roll { 100% { -o-transform: rotate(360deg); } }@-webkit-keyframes roll { 100% { -webkit-transform: rotate(360deg); } }img { opacity: 0.8; } img { animation-name: rotate ; animation-duration: 5s; animation-play-state: running; animation-timing-function: linear; animation-iteration-count: infinite; opacity: 1.0; filter: alpha(opacity=50);} img:hover {opacity: 1.0;filter: alpha(opacity=100);} @keyframes rotate{ 10% {transform:rotateY(36deg)} 20% {transform:rotateY(72deg)} 30% {transform:rotateY(108deg)} 40% {transform:rotateY(144deg)} 50% {transform:rotateY(180deg)} 60% {transform:rotateY(216deg)} 70% {transform:rotateY(252deg)} 80% {transform:rotateY(288deg)} 90% {transform:rotateY(324deg)} 100% {transform:rotateY(360deg)} }</style><script type="text/javascript">TypingText = function(element, interval, cursor, finishedCallback) {  if((typeof document.getElementById == "undefined") || (typeof element.innerHTML == "undefined")) {    this.running = true;// Never run.    return;  }  this.element = element;  this.finishedCallback = (finishedCallback ? finishedCallback : function() { return; });  this.interval = (typeof interval == "undefined" ? 30 : interval);  this.origText = this.element.innerHTML;  this.unparsedOrigText = this.origText;  this.cursor = (cursor ? cursor : "");  this.currentText = "";  this.currentChar = 0;  this.element.typingText = this;  if(this.element.id == "") this.element.id = "typingtext" + TypingText.currentIndex++;  TypingText.all.push(this);  this.running = false;  this.inTag = false;  this.tagBuffer = "";  this.inHTMLEntity = false;  this.HTMLEntityBuffer = "";}TypingText.all = new Array();TypingText.currentIndex = 0;TypingText.runAll = function() {  for(var i = 0; i < TypingText.all.length; i++) TypingText.all[i].run();}TypingText.prototype.run = function() {  if(this.running) return;  if(typeof this.origText == "undefined") {    setTimeout("document.getElementById('" + this.element.id + "').typingText.run()", this.interval);// We haven't finished loading yet.  Have patience.    return;  }  if(this.currentText == "") this.element.innerHTML = "";  if(this.currentChar < this.origText.length) {    if(this.origText.charAt(this.currentChar) == "<" && !this.inTag) {      this.tagBuffer = "<";      this.inTag = true;      this.currentChar++;      this.run();      return;    } else if(this.origText.charAt(this.currentChar) == ">" && this.inTag) {      this.tagBuffer += ">";      this.inTag = false;      this.currentText += this.tagBuffer;      this.currentChar++;      this.run();      return;    } else if(this.inTag) {      this.tagBuffer += this.origText.charAt(this.currentChar);      this.currentChar++;      this.run();      return;    } else if(this.origText.charAt(this.currentChar) == "&" && !this.inHTMLEntity) {      this.HTMLEntityBuffer = "&";      this.inHTMLEntity = true;      this.currentChar++;      this.run();      return;    } else if(this.origText.charAt(this.currentChar) == ";" && this.inHTMLEntity) {      this.HTMLEntityBuffer += ";";      this.inHTMLEntity = false;      this.currentText += this.HTMLEntityBuffer;      this.currentChar++;      this.run();      return;    } else if(this.inHTMLEntity) {      this.HTMLEntityBuffer += this.origText.charAt(this.currentChar);      this.currentChar++;      this.run();      return;    } else {      this.currentText += this.origText.charAt(this.currentChar);    }    this.element.innerHTML = this.currentText;    this.element.innerHTML += (this.currentChar < this.origText.length - 1 ? (typeof this.cursor == "function" ? this.cursor(this.currentText) : this.cursor) : "");    this.currentChar++;    setTimeout("document.getElementById('" + this.element.id + "').typingText.run()", this.interval);  } else {this.currentText = "_";this.currentChar = 0;        this.running = false;        this.finishedCallback();  }}</script> </head><br>
<p>
<center> <font color="silver" family="Orbitron" size="200"> Hacked by """+name_style+"""</font></center>

 <br><center><img src=" """+picture_style+""" " width="450" height="450">
<br>
<!--Tulisan Pertama--><center><font size="5" color="silver" face="courier new"> """+greetz_style+"""</font>
<br><br>
<!-- Tulisan Kedua--><center><div id="foter" class="foter" style="position: center; width: 600px; height: 28px; margin: 0px; padding: 10px; font-size: 24px; text-align: center; color: rgb(255, 255, 255); font-family: &quot;trebuchet ms&quot;, Courier new, courier new, sans-serif; transform: transform-origin: 50% 0px 0px; background-color: rgb(0, 0, 0); border: 1px solid rgb(170, 170, 170); opacity: 0.5; ">
<font face="courier new"><marquee color="white" behavior="Flip" scrollamount="6" width="85%" style="width: 50%;">"""+message+"""</marquee></font></div></span><!--Tengah--><br><br><br>
<b>__________________________________________________________________________________________</b></marquee><div style="text-shadow: 0px 0px 8px Black;"> <center><blink><font face="Orbitron" size="8" color="silver"><b>We Are</b> </font> <font face="Orbitron" size="8" color="White"><b>"""+team_style+"""</b></font></blink><br><center><marquee direction="right" loop="true" scrollamount="300"><b>__________________________________________________________________________________________</marquee>
</font></b> <br>
<style>body{overflow:hidden;background-color:black}#q{font:50px impact;color:white;position:absolute;left:0;right:0;top:45%} </div>

</html>
<center> """)

		
		
		
		
    if nc == 'q':
		print "Exiting..."
		sleep(1)
		sys.exit()
	
		
			
			
			
			
        
if menu == '2':
    	print "\n Rabux V.1.0 this file is the same type with Scriptux\n"
        print " It let you create deface page with simple  and free"
        print " This tool is for education only"
        print "\n"
        print " Greetz To: "
        print " [+] DedSecTL\t[+] Cvar1984"
        print " [+] TenSwapper07[+] Djosec12"
        print " [+] MR.RM\t[+] F4KS3C"
        print " [+] 3RROR_TMX\t[+] NO7_4LON3"
        print " [+] GTN\t[+] MR.K3N"
        print " [+] Scarl37\t[+] Troubelmaker97"
        print " [+] L_viole\t[+] de@hdies"
        print " [+] X1423N6\t[+] MR.R45K1N"
        print " [+] BLrose.20.10[+] idanovita"
        print " [+] Kerens.id\t[+] lord.zephyrus"
        print " [-] All member of BlackHole Sec "
                     
                      
        
if menu == 'q':
    	print "Exiting..."
        sleep(1)
        sys.exit()


      



