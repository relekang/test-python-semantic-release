from git import Repo

repo = Repo('.git')
git = repo.git
git.add('.')
r = git.commit(m='comitted by c.py')
print(r)
git.push('origin', 'master')
