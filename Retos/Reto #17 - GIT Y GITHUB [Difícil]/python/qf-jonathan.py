import subprocess
import unittest
from unittest.mock import patch, Mock


def last_commits(n: int):
    cmd = [
        "git",
        "log",
        "-n",
        str(n),
        "--pretty=format:%H|%an|%s|%ad",
        "--date=format:%d/%m/%Y %H:%M:%S",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return list(map(lambda r: r.split("|"), result.stdout.strip().split("\n")))


class LastCommitsTestCase(unittest.TestCase):
    @patch("__main__.subprocess.run")
    def test_get_git_log(self, mock_run):
        # Mocking git result
        mock_response = Mock()
        mock_response.stdout = (
            "hash1|author1|message1|date1\nhash2|author2|message2|date2\n"
        )
        mock_run.return_value = mock_response

        result = last_commits(2)

        # Verify result
        self.assertEqual(
            result,
            [
                ["hash1", "author1", "message1", "date1"],
                ["hash2", "author2", "message2", "date2"],
            ],
        )

        # Check that the command is executed correctly
        mock_run.assert_called_once_with(
            [
                "git",
                "log",
                "-n",
                "2",
                "--pretty=format:%H|%an|%s|%ad",
                "--date=format:%d/%m/%Y %H:%M:%S",
            ],
            capture_output=True,
            text=True,
        )


if __name__ == "__main__":
    print("Example, last 10 commits:")
    last_10_commits = last_commits(10)
    for commit in last_10_commits:
        print(commit)

    print("\nUnit test:")
    unittest.main()
