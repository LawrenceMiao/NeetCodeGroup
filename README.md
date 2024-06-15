# NeetCodeGroup

Instead of paying for serverless computing, I utilize Github Actions to benchmark NeetCode solutions.

# Usage

Clone the repo:
```
git clone https://github.com/LawrenceMiao/NeetCodeGroup.git
cd NeetCodeGroup
```

Create and switch to your own personal branch. This is where you will write and upload your solution code:
```
git checkout -b yourBranchName
```

Pull changes from main:
```
git pull orgin main
```
Note: make sure to pull from main whenever a new problem is added.

Implement the method in `solution.py` and push to origin:
```
git add --all
git commit -m "Your commit message
git push origin yourBranchName
```

Github Actions will execute your implementation and send your benchmark to the Discord.
