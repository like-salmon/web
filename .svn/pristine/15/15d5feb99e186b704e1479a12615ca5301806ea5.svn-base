#/usr/bin python
#coding:utf-8

import smtplib,os
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from settings import mailsettings as ms
from email import encoders

__metaclass__= type

class webMail():
    """mail handler"""

    def __init__(self,mto,msub,mfrom = ms["mfrom"]):
        self.msgRoot = MIMEMultipart()
        self.msgRoot["From"] = mfrom
        self.msgRoot["To"] = mto
        self.msgRoot["Pwd"] = ms["mpwd"]
        self.subject = ms["msubj"]
        self.msgRoot['Subject'] = Header(self.subject,'utf-8')
        self.server = ms["mserver"]
        self.template = False#是否开启模板
        self.mail_msg = ''#邮件正文

    def setTemplate(self,msg,imgsrc):
        # MIME内容
        mpath = ms["lmpath"]
        if os.name == "nt":
            mpath = ms["wmpath"]
        with open(mpath,"r") as f:
            msg = f.read()
        self.msgAlternative = MIMEMultipart('alternative')
        self.msgRoot.attach(self.msgAlternative)
        self.mail_msg = msg
        self.msgAlternative.attach(MIMEText(self.mail_msg, 'html', 'utf-8'))
        with open(imgsrc, "rb") as f:
            self.msgImage = MIMEImage(f.read())
            # 定义图片 ID，在 HTML 文本中引用
        self.msgImage.add_header('Content-ID', '<image1>')
        self.msgRoot.attach(self.msgImage)
        self.template = True

    def setAttachment(self,msg,imgs,type="plain"):
        #handler MIMEText
        if type == "plain":
            self.msgRoot.attach(MIMEText(msg, 'plain', 'utf-8'))
        elif type == "html":
            self.msgRoot.attach(MIMEText(msg, 'html', 'utf-8'))
        a,b,c,d = imgs[0],imgs[1],imgs[2],imgs[3]  #4 images body {"imagename":image[body]}
        msg1 = MIMEImage(a[a.keys()[0]], _subtype=a.keys()[0].split(".")[1])
        msg2 = MIMEImage(b[b.keys()[0]], _subtype=b.keys()[0].split(".")[1])
        msg3 = MIMEImage(c[c.keys()[0]], _subtype=c.keys()[0].split(".")[1])
        msg4 = MIMEImage(d[d.keys()[0]], _subtype=d.keys()[0].split(".")[1])
        # Set the filename parameter
        msg1.add_header('Content-Disposition', 'attachment', filename=a.keys()[0])
        msg2.add_header('Content-Disposition', 'attachment', filename=b.keys()[0])
        msg3.add_header('Content-Disposition', 'attachment', filename=c.keys()[0])
        msg4.add_header('Content-Disposition', 'attachment', filename=d.keys()[0])
        self.msgRoot.attach(msg1)
        self.msgRoot.attach(msg2)
        self.msgRoot.attach(msg3)
        self.msgRoot.attach(msg4)
        return 1
        #with open (a,"rb") as f1,open(b,"rb") as f2,open(c,"rb") as f3,open(d,"rb") as f4:

    def sendEmail(self):
        try:
            smtpserver = smtplib.SMTP(self.server,25)
            #如果启用ssl连接,一般修改smtpserver的端口
            #smtpserver.starttls()
            smtpserver.login(self.msgRoot["From"],self.msgRoot["Pwd"])
            smtpserver.sendmail(self.msgRoot["From"],self.msgRoot["To"], self.msgRoot.as_string())
            smtpserver.quit()
            print "mail sent"
        except smtplib.SMTPException:
            print "Error: 无法发送邮件"

if __name__ == "__main__":
    mto = "517908183@qq.com"
    msub = "邮件测试"
    with open("C:\\mywork\zhongjinjujin\\template\\reg_mail.txt","r+") as f:
        msg = f.read()
    imgsrc = "C:\\mywork\\zhongjinjujin\\static\\img\\slide01.jpg"
    mail = webMail(mto,msub,msg,imgsrc)
    mail.sendEmail()






