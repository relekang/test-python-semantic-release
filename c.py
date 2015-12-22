from git import Repo

repo = Repo('.git')
git = repo.git
git.add('.')
r = git.commit(m='message')
print(r)
print(r.__dict__)
