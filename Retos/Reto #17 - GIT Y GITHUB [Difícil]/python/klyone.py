#!/usr/bin/env python3

## For this code, you need to install gitpython.
## You can do that running: pip install gitpython
import git

if __name__ == "__main__":
    repo = git.Repo("../../..")
    logs_iter = repo.iter_commits("main", max_count=10)
    n_commit = 1

    # For each commit get: commit count | SHA | Author | Message (first line) | Date
    commit_list = []
    for commit in logs_iter:
        commit_list.append({"header" : "Commit {} ".format(n_commit), "sha" : commit.hexsha,
                            "author" : commit.author, "message" : commit.message.splitlines()[0],
                            "date" : commit.committed_datetime})
        n_commit = n_commit + 1

    max_header = max(map(lambda x: len(x["header"]), commit_list))
    max_author = max(map(lambda x: len(format(x["author"])), commit_list))
    max_message = max(map(lambda x: len(format(x["message"])), commit_list))

    for commit in commit_list:
        diff_header = max_header + 1 - len(commit["header"])
        diff_author = max_author + 1 - len(format(commit["author"]))
        diff_message = max_message + 1 - len(format(commit["message"]))
        log_str = "Commit {} {} | {} | {} {} | {} {} | {}".format(commit["header"], " " * (diff_header),
                                                              commit["sha"], commit["author"],
                                                              " " * (diff_author), commit["message"],
                                                              " " * (diff_message), commit["date"])
        print(log_str)
