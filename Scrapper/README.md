# Learn how to push files to a GitHub repo

PS C:\Users\tanis\Desktop\Web Scrapper> git init    
Initialized empty Git repository in C:/Users/tanis/Desktop/Web Scrapper/.git/
PS C:\Users\tanis\Desktop\Web Scrapper> git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        main.py
        tempCodeRunnerFile.py

nothing added to commit but untracked files present (use "git add" to track)
PS C:\Users\tanis\Desktop\Web Scrapper> git add . 
PS C:\Users\tanis\Desktop\Web Scrapper> git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   main.py
        new file:   tempCodeRunnerFile.py

PS C:\Users\tanis\Desktop\Web Scrapper> git remote add origin https://github.com/tb-rules10/Scrapper.git    
PS C:\Users\tanis\Desktop\Web Scrapper> git commit -m "first commit"
[master (root-commit) 78dc23c] first commit
 2 files changed, 40 insertions(+)
 create mode 100644 main.py
 create mode 100644 tempCodeRunnerFile.py
PS C:\Users\tanis\Desktop\Web Scrapper> git push -u origin master
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 720 bytes | 360.00 KiB/s, done.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/tb-rules10/Scrapper.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
PS C:\Users\tanis\Desktop\Web Scrapper> 
PS C:\Users\tanis\Desktop\Web Scrapper> git push -u origin master
