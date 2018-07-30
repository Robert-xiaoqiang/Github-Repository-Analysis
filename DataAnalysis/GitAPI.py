import requests
from urllib.request import urlopen
from urllib.request import Request
import json
#a4b3b467a675467a77b449d9ef99e41d8cd56d64
# q=stars:>1&s=stars&type=Repositories
# http://githut.info/


# commit %% add %%
def get_statistics(owner,name,headers):
	url = 'https://api.github.com/repos/{owner}/{name}/commits?page=1&per_page=10'.format(owner=owner, name=name)
	req = Request(url,headers=headers)
	response = urlopen(req).read()
	if len(response)==0: #None
		return response
	else:
		result = json.loads(response.decode())
		return result


def work_decript(repo_dicts, headers):
	res = ''
	for item in repo_dicts:
		try:
			res += item['description']
		except:
			continue
	f = open('decription.txt', 'w')
	print(res, file = f)

#repo_dicts is all 1000 repo
def work_repo(repo_dicts, headers):
	count_language = { }
	count_language_stars = { }
	count_time = { }
	try:
		for item in repo_dicts:
			name = item['name']
			star = item['stargazers_count']
			owner = item['owner']['login']
			language = str('0') 
			user = str('0')
			language = item['language']
			if language in count_language:
				count_language[language] += 1
				count_language_stars[language] += star
			else:
				count_language[language] = 1
				count_language_stars[language] = star		
			commits = get_statistics(owner,name,headers)
			for c in commits:
				#print(c['commit'].keys())
				count_time_key = c['commit']['committer']['date'][10:13]
				if count_time_key in count_time:
					count_time[count_time_key] += 1
				else:
					count_time[count_time_key] = 1
	finally:	
		f1 = open("count_language.txt", "w+")
		f2 = open("count_language_stars.txt", "w+")
		f3 = open("count_time.txt", "w+")
		print(count_language, file = f1)
		print(count_language_stars, file = f2)
		print(count_time, file = f3)
		f1.close()
		f2.close()
		f3.close()

def get_list(url, headers):
	count = int(0)
	is_next = True
	res = [ ] # all repo -> list
	try:
		while is_next:
			print('Requesting...')
			r = requests.get(url, headers = headers)
			print(count, "Status code:", r.status_code)
			response_dict = r.json()
			res += response_dict['items']
			if 'next' in r.links:
				url = r.links['next']['url']
				is_next = True
				count += 1
				if count == 1:
					break
			else:
				is_next = False
	finally:
		return res

def work_tag(tags, headers):
	res = ''
	for i in tags:
		try:
			res += i['short_description']
		except:
			continue
	f = open("tag.txt", "w")
	f.write(res)
	f.close()

def main1():
	headers = {"Authorization": "token a4b3b467a675467a77b449d9ef99e41d8cd56d64",
			   'Accept': 'application/vnd.github.mercy-preview+json'
			  }
	url_repo = 'https://api.github.com/search/repositories?q=stars:>100&sort=stars&type=Repositories?page=10000&per_page=1'
	url_tag = 'https://api.github.com/search/topics?q=Python+is:featured?page=10000&per_page=1'
	l1 = get_list(url_repo, headers)
	work_repo(l1, headers)
	l2 = get_list(url_tag, headers)
	work_tag(l2, headers)

def main2():
	headers = {"Authorization": "token a4b3b467a675467a77b449d9ef99e41d8cd56d64",
		       'Accept': 'application/vnd.github.mercy-preview+json'
		  	  }
	url_repo = 'https://api.github.com/search/repositories?q=stars:>100&sort=stars&type=Repositories?page=10000&per_page=1'
	l = get_list(url_repo, headers)
	work_decript(l, headers)

main2()