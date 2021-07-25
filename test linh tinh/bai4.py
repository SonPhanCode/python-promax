"""for num in range(10,20):  #de lap tu 10 toi 20
   for i in range(2,num): #de lap tren cac thua so cua mot so
      if num%i == 0:      #de xac dinh thua so dau tien
         j=num/i          #de uoc luong thua so thu hai
         print ('%d la bang %d * %d' % (num,i,j))
         break #de di chuyen toi so tiep theo, la vong FOR dau tien
   else:                  # else la mot phan cua vong lap
      print (num, 'la so nguyen to')"""
import os,inspect
import pyautogui as pya
from time import sleep
user = "truongjaeee274@gmail.com"
pw = "truongjae27"
string ='''<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE html PUBLIC "-//WAPFORUM//DTD XHTML Mobile 1.0//EN"><html>
    \n<head>
      \n  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        \n<title>Chào mừng bạn đến với Mobi Army 3 - Đăng nhập, Đăng ký</title>
 \n       <link rel="stylesheet" href="http://mobiarmy5.com/forum/app/view/css/template.css" type="text/css" />		
   \n     <link rel="shortcut icon" href='http://dd.mobiarmy5.com/app/view/images/favicon.png' type="image/x-icon" />
	\n	<script type="text/javascript">
	\n	  var _gaq = _gaq || [];
	\n	  _gaq.push(['_setAccount', 'UA-22738816-4']);
	\n	  _gaq.push(['_setDomainName', '.teamobi.com']);
		  _gaq.push(['_trackPageview']);
\n
\n		  (function() {
\n			var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
\n			ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
\n			var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
\n		  })();
\n		</script>
  \n  </head>   
    \n<body>
      \n  <div class="body_body">
        \n    <div class="body-content">
          \n      <div class="a" align="center"><img src="http://mobiarmy5.com/forum/app/view/images/logo.png" /></div>
            \n    <div id="top">
              \n      <div class="link-more">	
                \n        <div class="h" align="center">
                  \n          <!--<div style="color: #032E58;margin-top:-8px;margin-bottom:4px;">
			\n				<center> <b>Mạng xã hội cho điện thoại di động</b></center> 
			\n				</div>-->
			\n				<div class="bg_tree"></div>
			\n				<div class="bg_noel"></div>
                          \n  <div class="menu2" style="background: #561d00;">
				\n				<table width="100%" border="0" cellspacing="4">
				\n					<tr class="menu">
				\n						<td><a href="http://mobiarmy5.com">Trang Chủ</a></td>
				\n						<td><a href="http://mobiarmy5.com/?c=gallery">Giới Thiệu</a></td>
				\n						<td id="selected"><a href="http://mobiarmy5.com/forum/app/?for=forum&do=detail">Diễn Đàn</a></td>
				\n					</tr>
				\n				</table>
				\n			</div>
                                  \n                                                  <div class="bg-content" style="text-align:center">
       \n                     <div style="font-size:10px;">Sử dụng tài khoản Mobi Army 3 để đăng nhập.<br>
	\n						(chú ý: không dùng chung tài khoản mobi army cũ)</div>
          \n                      <center><form action="http://mobiarmy5.com/forum/app/index.php?do=login" method="POST" name="login">
            \n                        <input type="hidden" name="nav" value="" readonly="readonly" />
              \n                      <table>
                \n                        <tr>
                  \n                          <td><label for="user">SĐT / Email:</label></td>
                    \n                        <td><input name="user" type="text" value="'''+user+'''" /></td>
                      \n                  </tr>
                        \n                <tr>
                          \n                  <td><label for="pass">Mật khẩu:</label></td>
                            \n                <td><input name="pass" type="password" value="'''+pw+'''" />
				\n							<input type="hidden" name="checkru" value="7effcea6eaf85c3e20cbfe58bb77d349"/></td>
                                  \n      </tr>
					\n					
                               \n     </table>
                                 \n   <button type="submit" value="Đăng nhập" name="submit">Đăng nhập</button><br />
                                   \n <div style="font-size:10px;">
					\n			Nếu bạn chưa có tài khoản, vui lòng <a href="/app/view/register.php">đăng ký</a>
					\n			<br><a href="http://mobiarmy5.com/matkhau">Quên mật khẩu</a></div>
                               \n </form><br>
				\n				</center>
                  \n          </div>
                    \n    </div>
 \n                       <br>
   \n                 </div>
\n
  \n              </div>
\n
  \n          </div>
\n
  \n        <div class="left_b_bottom"><div class="right_b_bottom"><div class="footer"><div class="left_bottom"></div><div class="right_bottom"></div></div></div></div>
\n <div class="copyright"><h2>Mobi Army 3</h2>
\nBản Quyền thuộc về @TeaMobi - 2014</div>
\n</div>
  \n      </div>
    \n</div>
\n</body>

\n</html>'''
file = open("dangnhapamy.html",mode="w", encoding = "utf8")
file.write(string)
file.close()
nguon=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
#monguon =  str("start "+nguon+"\\"+"dangnhapamy.html")
nguonfile = str(nguon+"\\"+"dangnhapamy.html")
#os.system(monguon)
#os.remove(nguonfile3)
os.startfile(nguonfile)
sleep(1)
pya.hotkey("enter")
