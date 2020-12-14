import requests
from bs4 import BeautifulSoup
import pandas as pd

class HDUOJ:

	def __init__(self):
		self.URL = 'http://acm.hdu.edu.cn/userstatus.php'
		self.userlist = ['successzjl23', 'nbbtxdy', 'zzp123456','yutudaoyao2','Liquor1201','wenyay123','hansiqi1','skyzo123','2274527696','qcydm1','huoyufei','housiqi','SE9MW35', 'jsdhwdmaX20wyk','czyorange','fificici0721','saber009',
						 '2020012124']
		self.namelist = ['周佳璐','杨顺昌','左泽平','宋怡诺','王婧磊','陈雅文','韩思琪','郭宇天','王欣雨','齐超元','郭泽坤','侯思琪','施景','王雨珂','程子蕴','袁彤菲','李元浩', '黄家豪']
		# 伪装请求头
		self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60'}

	def get_problem(self):
		l = []
		for i in range(len(self.namelist)):
			tmp = []
			html = requests.get(self.URL, params={'user': self.userlist[i]}, headers=self.header)
			soup = BeautifulSoup(html.text, "html.parser")
			name = soup.select('body > table >  tr:nth-child(6) > td > table >  tr > td > h1')
			rank = soup.select('body > table >  tr:nth-child(6) > td > table >  tr > td > table >  tr:nth-child(2) > td:nth-child(2)')
			Problems_Submitted = soup.select('body > table > tr:nth-child(6) > td > table >  tr > td > table >  tr:nth-child(3) > td:nth-child(2)')
			Problems_Solved = soup.select('body > table > tr:nth-child(6) > td > table >  tr > td > table >  tr:nth-child(4) > td:nth-child(2)')
			Submissions =soup.select('body > table > tr:nth-child(6) > td > table >  tr > td > table >  tr:nth-child(5) > td:nth-child(2)')
			Accepted = soup.select('body > table > tr:nth-child(6) > td > table >  tr > td > table >  tr:nth-child(6) > td:nth-child(2)')
			temp = self.userlist[i], self.namelist[i], int(rank[0].get_text()),Problems_Submitted[0].get_text(), Problems_Solved[0].get_text(), Submissions[0].get_text(), Accepted[0].get_text()
			l.append(temp)
		l.sort(key=lambda x: x[2])
		print(l)
		df = pd.DataFrame(l, columns=['user', 'name', 'rank', 'Problems_Submitted',
								'Problems_Solved', 'Submissions', 'Accepted'])
		df.to_csv('d:\\problem.csv', encoding="utf_8_sig")
		print('done')


if __name__ == '__main__':
	cls = HDUOJ()
	cls.get_problem()

#  pip install numpy -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

