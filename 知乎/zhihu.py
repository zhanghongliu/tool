from zhihu import ZhihuClient

Cookies_File = 'cookies.json'

client = ZhihuClient(Cookies_File)

url = 'http://www.zhihu.com/people/excited-vczh'
author = client.author(url)

print('用户名 %s' % author.name)
print('用户简介 %s' % author.motto)
print('用户关注人数 %d' % author.followee_num)
print('取用户粉丝数 %d' % author.follower_num)
print('用户得到赞同数 %d' % author.upvote_num)
print('用户得到感谢数 %d' % author.thank_num)
print('用户提问数 %d' % author.question_num)
print('用户答题数 %d' % author.answer_num)

print('用户专栏文章数 %d，名称分别为：' % author.post_num)
for column in author.columns:
  print(column.name)
print('用户收藏夹数 %d，名称分别为：' % author.collection_num)
for collection in author.collections:
  print(collection.name)


question = client.question('http://www.zhihu.com/question/28092572')
for answer in question.answers:
   answer.save()