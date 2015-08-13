__author__ = 'luo.mingnan'
import urllib
import urllib2
import json

# 10.1  user/login
def userLogin(mobile=None, password=None):
    data = {'mobile': mobile, 'password': password}
    data = urllib.urlencode(data)
    req = urllib2.Request(url="http://farseer810.com/user/login", data=data)
    return urllib2.urlopen(req).read()


# response = userLogin("18819451429","123456")#b8e05bb45d071f02c240f42cd0859a58 19----0a84c3b53aa83d3a1bdff55bd7075c00--1
# print response

# 1.6  user/campus/set
def userCampusSet(access_token=None, user_id=None, campus_id=None):
    data = {'access_token': access_token, 'user_id': user_id, 'campus_id': campus_id}
    data = urllib.urlencode(data)
    req = urllib2.Request(url="http://farseer810.com/user/campus/set", data=data)
    return urllib2.urlopen(req).read()


# response = userCampusSet("b8e05bb45d071f02c240f42cd0859a58", 19, 1)
# print response





# response=userLogin("18819451352","123456")#0a84c3b53aa83d3a1bdff55bd7075c00
# print response

# 1.9  password_change
def userPasswordChange(mobile, old_password, new_password):
    data = {'mobile': mobile, 'old_password': old_password, 'new_password': new_password}
    data = urllib.urlencode(data)
    req = urllib2.Request(url="http://localhost:8080/user/password/change", data=data)
    return urllib2.urlopen(req).read()


# response=userPasswordChange("18819410001","100001","100001")
# print response

# 1.10   password/forget
def userPasswordForget(mobile):
    data = {'mobile': mobile}
    data = urllib.urlencode(data)
    req = urllib2.Request(url="http://localhost:8080/user/password/forget", data=data)
    return urllib2.urlopen(req).read()


# response=userPasswordForget("18819410000")
# print response



# 1.11  password_change
def userVerifyPasswordChange(mobile, verify_code, new_password):
    data = {'mobile': mobile, 'verify_code': verify_code, 'new_password': new_password}
    data = urllib.urlencode(data)
    req = urllib2.Request(url="http://localhost:8080/user/password/verify", data=data)
    return urllib2.urlopen(req).read()


# response=userVerifyPasswordChange("18819410000","10000","100000")
# print response

# 1.12---------------------?????????????



# 4.1 campus/login
def campusLogin(login_name, password):
    data = {'login_name': login_name, 'password': password}
    data = urllib.urlencode(data)
    req = urllib2.Request(url="http://localhost:8080/campus/login", data=data)
    return urllib2.urlopen(req).read()


# response=campusLogin("admin1","admin")#db340f93d690a9840df85c24b64d767f
# print response


# 4.2 campus/logout
def campusLogout(access_token):
    data = {'access_token': access_token}
    data = urllib.urlencode(data)
    req = urllib2.Request(url="http://localhost:8080/campus/logout", data=data)
    return urllib2.urlopen(req).read()


# response = campusLogout("")
# print response







# 10.1 /user/post/add                 #OK
def userPostAdd(access_token=None, user_id=None, content=None):
    data = {'access_token': access_token, 'user_id': user_id, 'content': content}
    data = urllib.urlencode(data)
    req = urllib2.Request(url="http://farseer810.com/user/post/add", data=data)
    return urllib2.urlopen(req).read()


# b8e05bb45d071f02c240f42cd0859a58          0a84c3b53aa83d3a1bdff55bd7075c00
# 16 "HelloWorld from user_id 1"   17"HelloWorld from user_id 2"
# response = userPostAdd("0a84c3b53aa83d3a1bdff55bd7075c00",1,"HelloWorld13 from user_id 1")
# print response


# 10.2 /user/post/delete
def userPostDelete(access_token=None, user_id=None, post_id=None):
    data = {'access_token': access_token, 'user_id': user_id, 'post_id': post_id}
    data = urllib.urlencode(data)
    req = urllib2.Request(url="http://farseer810.com/user/post/delete", data=data)
    return urllib2.urlopen(req).read()


# response = userPostDelete("0a84c3b53aa83d3a1bdff55bd7075c00", 1, 10)
# print response


# 10.3 /user/post/comment/add                    #OK
def userPostCommentAdd(access_token=None, user_id=None, post_id=None, content=None, comment_id=None):
    data = {'access_token': access_token, 'user_id': user_id, 'post_id': post_id, 'content': content,
            'comment_id': comment_id}
    data = urllib.urlencode(data)
    req = urllib2.Request(url="http://farseer810.com/user/post/comment/add", data=data)
    return urllib2.urlopen(req).read()


# response = userPostCommentAdd("0a84c3b53aa83d3a1bdff55bd7075c00", 1,30,"comment user_1_2_1 postid_30",9)
# print response


# 10.4 /user/post/comment/delete               #OK
def userPostCommentDelete(access_token=None, user_id=None, comment_id=None):
    data = {'access_token': access_token, 'user_id': user_id, 'comment_id': comment_id}
    data = urllib.urlencode(data)
    req = urllib2.Request(url="http://farseer810.com/user/post/comment/delete", data=data)
    return urllib2.urlopen(req).read()


# response = userPostCommentDelete("0a84c3b53aa83d3a1bdff55bd7075c00", 1, 10)
# print response


# 10.5 /user/post/comment/list                 #OK
def userCommentList(access_token=None, user_id=None, post_id=None):
    data = {'access_token': access_token, 'user_id': user_id, 'post_id': post_id}
    data = urllib.urlencode(data)
    req = urllib2.Request(url="http://farseer810.com/user/post/comment/list", data=data)
    return urllib2.urlopen(req).read()


# response = userCommentList("0a84c3b53aa83d3a1bdff55bd7075c00", 1, 18)
# print response




# 10.6 /user/post/favor/add/
def userPostFavorAdd(access_token=None, user_id=None, post_id=None):
    data = {'access_token': access_token, 'user_id': user_id, 'post_id': post_id}
    data = urllib.urlencode(data)
    req = urllib2.Request(url="http://farseer810.com/user/post/favor/add", data=data)
    return urllib2.urlopen(req).read()


# response = userPostFavorAdd("0a84c3b53aa83d3a1bdff55bd7075c00", 1, 10)
# print response


# 10.7 /user/post/favor/delete
def userPostFavorDelete(access_token=None, user_id=None, post_id=None):
    data = {'access_token': access_token, 'user_id': user_id, 'post_id': post_id}
    data = urllib.urlencode(data)
    req = urllib2.Request(url="http://farseer810.com/user/post/favor/delete", data=data)
    return urllib2.urlopen(req).read()


# response = userPostFavorDelete("0a84c3b53aa83d3a1bdff55bd7075c00", 1, 10)
# print response


# 10.8 /user/follow/add
def userFollowAdd(access_token=None, user_id=None, followed_id=None):
    data = {'access_token': access_token, 'user_id': user_id, 'followed_id': followed_id}
    data = urllib.urlencode(data)
    req = urllib2.Request(url="http://farseer810.com/user/follow/add", data=data)
    return urllib2.urlopen(req).read()


# response = userFollowAdd("0a84c3b53aa83d3a1bdff55bd7075c00", 1, 2)
# print response




# 10.9 /user/follow/delete
def userFollowDelete(access_token=None, user_id=None, followed_id=None):
    data = {'access_token': access_token, 'user_id': user_id, 'followed_id': followed_id}
    data = urllib.urlencode(data)
    req = urllib2.Request(url="http://farseer810.com/user/follow/delete", data=data)
    return urllib2.urlopen(req).read()


# response = userFollowDelete("0a84c3b53aa83d3a1bdff55bd7075c00", 1, 2)
# print response


# 10.10/user/follow/list
def userFollowList(access_token=None, user_id=None):
    data = {'access_token': access_token, 'user_id': user_id}
    data = urllib.urlencode(data)
    req = urllib2.Request(url="http://farseer810.com/user/follow/list", data=data)
    return urllib2.urlopen(req).read()


# response = userFollowAdd("0a84c3b53aa83d3a1bdff55bd7075c00", 1)
# print response




# 10.11 /user/post/campus/update
def userCampusUpdate(access_token=None, user_id=None, last_post_id=None):
    data = {'access_token': access_token, 'user_id': user_id, 'last_post_id': last_post_id}
    data = urllib.urlencode(data)
    req = urllib2.Request(url="http://farseer810.com/user/post/campus/update", data=data)
    return urllib2.urlopen(req).read()


# response = userFollowAdd("0a84c3b53aa83d3a1bdff55bd7075c00", 1, 12)
# print response



# 10.12 /user/post/campus/list         #OK
def userPostCampusList(access_token=None, user_id=None, start_post_id=None, start_index=None, post_count=None):
    data = {'access_token': access_token, 'user_id': user_id, 'start_post_id': start_post_id,
            'start_index': start_index, 'post_count': post_count}
    data = urllib.urlencode(data)
    req = urllib2.Request(url="http://farseer810.com/user/post/campus/list", data=data)
    return urllib2.urlopen(req).read()


# response = userPostCampusList("0a84c3b53aa83d3a1bdff55bd7075c00", 1, 17, 0, 3)
# print response


# 10.13 /user/post/follow/update
def userPostFollowUpdate(access_token=None, user_id=None, last_post_id=None):
    data = {'access_token': access_token, 'user_id': user_id, 'last_post_id': last_post_id}
    data = urllib.urlencode(data)
    req = urllib2.Request(url="http://farseer810.com/user/post/follow/update", data=data)
    return urllib2.urlopen(req).read()


# response = userPostFollowUpdate("0a84c3b53aa83d3a1bdff55bd7075c00", 1, 3)
# print response


# 10.14 /user/post/follow/list
def userPostFollowList(access_token=None, user_id=None, start_post_id=None, start_index=None, end_index=None):
    data = {'access_token': access_token, 'user_id': user_id, 'start_post_id': start_post_id,
            'start_index': start_index, 'end_index': end_index}
    data = urllib.urlencode(data)
    req = urllib2.Request(url="http://farseer810.com/user/post/follow/list", data=data)
    return urllib2.urlopen(req).read()

# response = userPostFollowUpdate("0a84c3b53aa83d3a1bdff55bd7075c00", 1, 1, 1, 3)
# print response
