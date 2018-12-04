import pymysql 
from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open


def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content

#pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")

for i in range(1,126):
	#name="0 ("+str(i)+").pdf"
	#print(name)

	pdfFile = open("pdf/"+"0 ("+str(i)+").pdf","rb")
	outputString = readPDF(pdfFile)
	#print(outputString)
	pdfFile.close()

	str1=outputString.split("\n")


	if str1[36]=='':
		cet_list=[str1[6],str1[8],str1[11],str1[14],str1[35],str1[39],str1[53],str1[55],str1[57],str1[59]]
	else:
		cet_list=[str1[6],str1[8],str1[11],str1[15],str1[36],str1[40],str1[54],str1[56],str1[58],str1[60]]



	#print(cet_list)
	db=pymysql.connect(host="localhost",
	                   user="root",
	                   password="root",
	                   db="test",
	                   port=3306,
	                   charset="utf8"
	                   )                        #创建数据库对象
	 
	cur = db.cursor()
	 
	sql = "INSERT INTO cet (`zkzh`, `name`,`sfzh`,`xuehao`,`time`,`type`,`where`,`kc`,`zw`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	 
	try:
	  cur.execute(sql,(cet_list[0],cet_list[1],cet_list[2],cet_list[3],cet_list[4]+" "+cet_list[5],cet_list[6],cet_list[7],cet_list[8],cet_list[9]))                     #执行sql
	  #cur.execute(sql,('122','1113','2222','3333','444','555','666','777','888','999'))
	  db.commit()                          #提交
	 
	except Exception as e:
	  db.rollback()                       #异常回滚
	 
	finally:
	  db.close()
	  cet_list.clear()
	  str1.clear()







