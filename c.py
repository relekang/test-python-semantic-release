from git import Repo

repo = Repo('.git')
git = repo.git
git.add('.')
git.commit(m='message')
