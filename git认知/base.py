'''
使用git和github
建立本地仓库：mkdir basePython
进入到basePython中，运行git init
如果未设置ssh key，先试用ssh-keygen ，一路enter生成key
使用cat ~/.ssh/id_rsa.pub查看生成的ssh公钥
将生成的ssh公钥写入到github上—settings—ssh and GPG keys
建立github上远程仓库
本地仓库和远程仓库建立关联：git remote add origin git@github.com:ITClubOfBruce/basePython.git
查看本地仓库状态：git status
追踪发生变化的文件：git add .
提交到本地仓库：git commit -m "注释"
提交到远程仓库：git push -u origin maser（第一次提交需要），之后使用git push即可

'''