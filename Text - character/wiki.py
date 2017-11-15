import wikipedia as wk
import random as rd
import string as st

with open("wiki.txt",'a') as f:
	pages=[]
	a=1
	while a:
		try:
			char = rd.choice(st.ascii_letters)
			lst = wk.search(char)
			page = lst[rd.randint(0,len(lst))]
			if page not in pages:
				pages.append(page)
			else:
				continue
			con = wk.page(page).content
			print(a,char,page)
			f.write(con)
			a+=1
		except:
			print(char,page,"!!!")
