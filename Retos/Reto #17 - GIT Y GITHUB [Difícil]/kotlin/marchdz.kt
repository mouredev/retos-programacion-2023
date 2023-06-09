import com.github.syari.kgit.KGit
import org.eclipse.jgit.api.Git
import org.eclipse.jgit.revwalk.RevCommit
import org.eclipse.jgit.storage.file.FileRepositoryBuilder
import org.eclipse.jgit.util.GitDateFormatter
import java.io.File
import java.time.LocalDate
import java.time.format.DateTimeFormatter


fun main() {
    val url = "https://github.com/mouredev/retos-programacion-2023"
    cloneRepository(url)
    retrieveDataAndPrint()
    deleteRepository(url)
}

fun cloneRepository(url: String) {
    KGit.cloneRepository {
        setDirectory(File("RepositorioDescargado"))
        setURI(url)
        setTimeout(60)
        println("Repositorio $url descargado al disco.\n")
    }
}

fun retrieveDataAndPrint() {
    val existingRepository = FileRepositoryBuilder()
        .setGitDir(File("RepositorioDescargado/.git"))
        .build()
    val log: Iterable<RevCommit> = Git(existingRepository).log().setMaxCount(10)
        .call()
    for ((index, commit) in log.withIndex()) {
        val hash = commit.name.subSequence(0, 7)
        val name = commit.authorIdent.name
        val message = commit.shortMessage
        val unformattedDate = LocalDate.parse(GitDateFormatter(GitDateFormatter
            .Format.SHORT).formatDate(commit.authorIdent))
        val dateFormatterPattern = DateTimeFormatter.ofPattern("dd/MM/yyyy")
        val formattedDate = unformattedDate.format(dateFormatterPattern)
        val formattedTime = GitDateFormatter(GitDateFormatter.Format.LOCAL)
            .formatDate(commit.authorIdent).split(" ")[3].subSequence(0, 5)
        println("Commit ${index + 1} | $hash | $name | $message " +
                "| $formattedDate $formattedTime")
    }
}

fun deleteRepository(url: String) {
    val file = File("RepositorioDescargado")
    file.deleteRecursively()
    println("\nRepositorio $url borrado del disco.")
}
