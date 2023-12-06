import org.eclipse.jgit.api.Git;
import org.eclipse.jgit.api.errors.GitAPIException;
import org.eclipse.jgit.revwalk.RevCommit;
import org.eclipse.jgit.storage.file.FileRepositoryBuilder;
import org.ietf.jgss.GSSException;

import java.io.File;
import java.io.IOException;

public class Qv1ko {

    public static void main(String[] args) {
        lastCommits();
    }// main

    private static void lastCommits() {
        String repoPath = ".";
        Git git = new Git(new FileRepositoryBuilder().setGitDir(new File(repoPath)).readEnvironment().findGitDir().build());
        int num = 1;
        for (RevCommit commit : git.log().setMaxCount(10).call()) {
            System.out.println("Commit " + num + " | " + commit.getName() + " | " + commit.getAuthorIdent().getName() + " | " + commit.getFullMessage() + " | " + commit.getAuthorIdent().getWhen());
        }
    }

}// class
