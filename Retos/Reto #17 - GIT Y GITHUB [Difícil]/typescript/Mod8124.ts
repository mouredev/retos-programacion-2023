interface IResult {
    sha: string;
    commit: {
      author: {
        name: string;
        date: string;
      };
      message: string;
    };
  }
  
  const getCommits = async (): Promise<void> => {
    try {
      const URL = 'https://api.github.com/repos/mouredev/retos-programacion-2023/commits?per_page=10';
      const req = await fetch(URL);
      const results = await req.json();
      printResult(results);
    } catch (erros) {
      console.log(erros);
    }
  };
  
  const printResult = (results: IResult[]): void => {
    results.forEach(_printResult);
  };
  
  const _printResult = (result: IResult, index: number): void => {
    const hash = result.sha.slice(7);
    const { name, date } = result.commit.author;
    const msg = result.commit.message;
    console.log(
      `Commit ${index + 1} | ${hash} | ${name} | ${msg} | ${new Date(
        date
      ).toLocaleString()} |`
    );
    console.log('-------');
  };
  
  getCommits();
  