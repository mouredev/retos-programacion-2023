const getLastCommits = async (params: getLastCommitsParams = {}) => {
    const { repositoryName, numberOfCommits } = { repositoryName: 'mouredev/retos-programacion-2023', numberOfCommits: 10, ...params };
    const url = `https://api.github.com/repos/${repositoryName}/commits?per_page=${numberOfCommits}`;
    let commitsApiData: GithubApiCommit[] = await fetch(
        url,
        {
            headers: { 'Accept': 'application/vnd.github.v3+json' },
            method: 'GET'
        }
    )
        .then(response => response.json())
        .catch((error: Error) => console.log(error));
    const commits: CommitsInfo[] = commitsApiData.map(commitInfo => {
        return {
            hash: commitInfo.commit.tree.sha,
            author: commitInfo.commit.author.name,
            message: commitInfo.commit.message,
            date: new Date(commitInfo.commit.author.date).toLocaleString()
        }
    });

    printCommitsInfo(commits);
}

const printCommitsInfo = (commits: CommitsInfo[]) => {
    commits.forEach((commit, index) => {
        console.log(`Commit ${index + 1} | ${commit.hash} | ${commit.author} | ${commit.message} | ${commit.date}`);
        console.log('-------------------------------');
    });
}

getLastCommits();


/** Types */

type CommitsInfo = {
    hash: string,
    author: string,
    message: string,
    date: string
};

type getLastCommitsParams = {
    repositoryName?: string,
    numberOfCommits?: number
};

/** START Types extracted from QuickType */
type GithubApiCommit = {
    sha: string;
    node_id: string;
    commit: Commit;
    url: string;
    html_url: string;
    comments_url: string;
    author: GithubAuthor | null;
    committer: GithubAuthor | null;
    parents: Parent[];
}

type GithubAuthor = {
    login: string;
    id: number;
    node_id: string;
    avatar_url: string;
    gravatar_id: string;
    url: string;
    html_url: string;
    followers_url: string;
    following_url: string;
    gists_url: string;
    starred_url: string;
    subscriptions_url: string;
    organizations_url: string;
    repos_url: string;
    events_url: string;
    received_events_url: string;
    type: Type;
    site_admin: boolean;
}

enum Type {
    User = "User",
}

type Commit = {
    author: CommitAuthor;
    committer: CommitAuthor;
    message: string;
    tree: Tree;
    url: string;
    comment_count: number;
    verification: Verification;
}

type CommitAuthor = {
    name: string;
    email: string;
    date: Date;
}

type Tree = {
    sha: string;
    url: string;
}

type Verification = {
    verified: boolean;
    reason: Reason;
    signature: null | string;
    payload: null | string;
}

enum Reason {
    Unsigned = "unsigned",
    Valid = "valid",
}

type Parent = {
    sha: string;
    url: string;
    html_url: string;
}
/** END Types extracted from QuickType */
