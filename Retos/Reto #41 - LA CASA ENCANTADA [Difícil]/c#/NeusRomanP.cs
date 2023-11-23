namespace NeusRomanP
{
  public class NeusRomanP
  {

    Question q1 = new Question(
      "This Pokemon wears his mother's skull over his face:",
      new Option("Rampardos", false),
      new Option("Cubeone", true),
      new Option("Duskull", false),
      new Option("Yamask", false)
    );
    Question q2 = new Question(
      "Who's the Pokemon that is said to steals children away taking them to the world of the dead?",
      new Option("Drifloon", true),
      new Option("Gengar", false),
      new Option("Hypno", false),
      new Option("Giratina", false)
    );

    Question q3 = new Question(
      "This Pokemon is controlled by the mushroom on his head:",
      new Option("Foongus", false),
      new Option("Amoonguss", false),
      new Option("Hypno", false),
      new Option("Parasect", true)
    );

    Question q4 = new Question(
      "It chokes its prey while singing because it's so overjoyed with the suffering inflicted on its victims:",
      new Option("Jigglypuff", false),
      new Option("Gengar", false),
      new Option("Gourgeist", true),
      new Option("Phantump", false)
    );

    Question q5 = new Question(
      "Its true form is so terrifying that anyone unfortunate enough to catch a glimpse has met a mysterious and swift end. It also wears a Pikachu disguise made out of rags in hopes it will be mistaken for the much-beloved Pokemon:",
      new Option("Raichu", false),
      new Option("Mimikyu", true),
      new Option("Emolga", false),
      new Option("Phantump", false)
    );

    Question q6 = new Question(
      "Is said to be an abandoned toy who came to life, fueled by its hatred after being cast off, to haunt his owner:",
      new Option("Claydol", false),
      new Option("Baltoy", false),
      new Option("Bannette", true),
      new Option("Mimikyu", false)
    );

    Question q7 = new Question(
      "When it finds humans or Pokemon it likes, it freezes them and takes them to its chilly den, where they become decorations:",
      new Option("Misdreavus", false),
      new Option("Mouredev", false),
      new Option("Regice", false),
      new Option("Froslass", true)
    );

    Question q8 = new Question(
      "This Pokemon poses as your shadow, then curses you and steals your life:",
      new Option("Gengar", true),
      new Option("Sableye", false),
      new Option("Trevenant", false),
      new Option("Mismagius", false)
    );

    Question q9 = new Question(
      "His candle purpose id to lure people in, pretending to be a guiding light, only to absorb their life force:",
      new Option("Litten", false),
      new Option("Gastly", false),
      new Option("Giratina", false),
      new Option("Litwick", true)
    );

    Question q10 = new Question(
      "This Pokemon has mind-controlled its victims and played a role in “history-changing events”:",
      new Option("Psyduck", false),
      new Option("Malamar", true),
      new Option("Rotom", false),
      new Option("Mewtwo", false)
    );

    Question q11 = new Question(
      "This Pokemon are rotten tree stumps possessed by the spirits of lost children who died in the forest. Their cries sound like “eerie screams” and they can mimic the voice of a child:",
      new Option("Phantump", true),
      new Option("Sudowoodo", false),
      new Option("Treecko", false),
      new Option("Gothita", false)
    );

    Question q12 = new Question(
      "It pulls its prey down into the sand by controlling the sand itself, and then it sucks out their souls:",
      new Option("Palossand", true),
      new Option("Duskull", false),
      new Option("Chandelure", false),
      new Option("Diglett", false)
    );

    Question q13 = new Question(
      "Each of them carries a mask that used to be its face when it was human. Sometimes they look at it and cry:",
      new Option("Meowscarada", false),
      new Option("Yamask", true),
      new Option("Marowak", false),
      new Option("Duskull", false)
    );

    Question q14 = new Question(
      "Its evolved form gathers bones, which they essentially wear as a diaper “to guard their posteriors”, according to multiple Pokedex entries:",
      new Option("Cubone", false),
      new Option("Vullaby", true),
      new Option("Rufflet", false),
      new Option("Riolu", false)
    );



    Question[] questions = new Question[14];

    string[,] rooms = {
      {"⬜️", "⬜️", "⬜️", "⬜️"},
      {"⬜️", "⬜️", "⬜️", "⬜️"},
      {"⬜️", "⬜️", "⬜️", "⬜️"},
      {"⬜️", "⬜️", "⬜️", "⬜️"}
    };

    bool endGame = false;

    int[] currentPosition = {0, 0};
    int[] startPosition = {0, 0};
    int[] exitPosition = {0, 0};

    static void Main(string[] args)
    {

      var thisClass = new NeusRomanP();

      thisClass.questions = new Question[] {thisClass.q1, thisClass.q2, thisClass.q3, thisClass.q4, thisClass.q5, thisClass.q6,
                                            thisClass.q7, thisClass.q8, thisClass.q9, thisClass.q10, thisClass.q11, thisClass.q12,
                                            thisClass.q13, thisClass.q14};

      thisClass.SetStartAndExit();
      thisClass.PrintRooms();

      while(!thisClass.endGame){
        thisClass.AskForDirection();
      }
      Console.WriteLine("Congratulations! You found the candy room and exited the house!");
    }

    private void AskForDirection(){
      Console.WriteLine("Chose the direction you want to move:");
      List<string> directonsList = ShowOptionsToMove();

      string direction = Console.ReadLine() ?? " ";

      bool correctInput = directonsList.Contains(direction);
      
      while(!correctInput){
        Console.WriteLine("Enter a valid direction:");
        directonsList = ShowOptionsToMove();

        direction = Console.ReadLine() ?? " ";

        correctInput = directonsList.Contains(direction);
      }

      //If question answered correctly move
      if(CheckIfNextRoomIsExit(direction) || CheckIfNextRoomIsStart(direction)){
        MovePosition(direction);
      }else{
        if(CheckGhost()){
          Console.WriteLine("👻 BOO! A ghost appeared! You need to answer 2 questions!");
          if(AskQuestion() && AskQuestion()){
            MovePosition(direction);
          }
        }else{
          if(AskQuestion()){
            MovePosition(direction);
          }
        }
      }
      

      PrintRooms();
    }

    private bool CheckIfNextRoomIsExit(string direction){
      if(direction == "L"){
        return exitPosition[1] == (currentPosition[1] - 1) && exitPosition[0] == currentPosition[0]; 
      }

      if(direction == "R"){
        return exitPosition[1] == (currentPosition[1] + 1) && exitPosition[0] == currentPosition[0]; 
      }

      if(direction == "U"){
        return exitPosition[1] == currentPosition[1] && exitPosition[0] == (currentPosition[0] - 1); 
      }

      if(direction == "D"){
        return exitPosition[1] == currentPosition[1] && exitPosition[0] == (currentPosition[0] + 1); 
      }

      return false;
    }

    private bool CheckIfNextRoomIsStart(string direction){
      if(direction == "L"){
        return startPosition[1] == (currentPosition[1] - 1) && startPosition[0] == currentPosition[0]; 
      }

      if(direction == "R"){
        return startPosition[1] == (currentPosition[1] + 1) && startPosition[0] == currentPosition[0]; 
      }

      if(direction == "U"){
        return startPosition[1] == currentPosition[1] && startPosition[0] == (currentPosition[0] - 1); 
      }

      if(direction == "D"){
        return startPosition[1] == currentPosition[1] && startPosition[0] == (currentPosition[0] + 1); 
      }

      return false;
    }

    private List<string> ShowOptionsToMove(){

      List<string> directionsList = new List<string>();

      if(currentPosition[1] != 0){
        directionsList.Add("L");
        Console.WriteLine("[L] Left");
      }
      if(currentPosition[1] != 3){
        directionsList.Add("R");
        Console.WriteLine("[R] Right");
      }
      if(currentPosition[0] != 0){
        directionsList.Add("U");
        Console.WriteLine("[U] Up");
      }
      if(currentPosition[0] != 3){
        directionsList.Add("D");
        Console.WriteLine("[D] Down");
      }

      return directionsList;
    }

    private void MovePosition(string direction){

      if(startPosition[0] == currentPosition[0] && startPosition[1] == currentPosition[1]){
        this.rooms[currentPosition[0], currentPosition[1]] = "🚪";
      }else{
        this.rooms[currentPosition[0], currentPosition[1]] = "⬛";
      }
      

      if(direction == "L"){
        currentPosition[1]--;
      }
      if(direction == "R"){
        currentPosition[1]++;
      }
      if(direction == "U"){
        currentPosition[0]--;
      }
      if(direction == "D"){
        currentPosition[0]++;
      }

      if (currentPosition[0] == exitPosition[0] && currentPosition[1] == exitPosition[1]){
        this.rooms[exitPosition[0], exitPosition[1]] = "🍭";
        endGame = true;
      }

      if(!(exitPosition[0] == currentPosition[0] && exitPosition[1] == currentPosition[1])){
        this.rooms[currentPosition[0], currentPosition[1]] = "🧑";
      }
    }

    private bool AskQuestion(){
      Random random = new Random();
      int questionNumber = random.Next(0, questions.GetLength(0));
      Question question = questions[questionNumber];
      ShowQuestionOptions(question);

      string response = Console.ReadLine() ?? " ";
      while(response != "1" && response != "2" && response != "3" && response != "4"){
        Console.WriteLine("Choose a valid response!");
        ShowQuestionOptions(question);
        response = Console.ReadLine() ?? " ";
      }

      if(question.options[Int32.Parse(response) - 1].isCorrect){
        Console.WriteLine("Correct!");
      }else{
        Console.WriteLine("You failed!");
      }

      return question.options[Int32.Parse(response) - 1].isCorrect;
    }

    public void ShowQuestionOptions(Question question){
      Console.WriteLine(question.title);
      Console.WriteLine("[1]" + question.option1.title);
      Console.WriteLine("[2]" + question.option2.title);
      Console.WriteLine("[3]" + question.option3.title);
      Console.WriteLine("[4]" + question.option4.title);
    }

    public bool CheckGhost(){
      Random random = new Random();
      int ghostNumber = random.Next(0, 10);

      if(ghostNumber == 0){
        return true;
      }
      
      return false;
    }

    private void PrintRooms(){
      for (int i = 0; i < this.rooms.GetLength(0); i++){
        for (int j = 0; j < this.rooms.GetLength(1); j++){
          Console.Write(this.rooms[i, j]);
        }
        Console.Write("\n");
      }
    }

    private void SetStartAndExit(){
      Random random = new Random();
      int startX = random.Next(0, 4);
      int startY = random.Next(0, 4);

      startPosition[0] = startX;
      startPosition[1] = startY;

      currentPosition[0] = startX;
      currentPosition[1] = startY;

      int exitX = startX;
      int exitY = startY;

      //Avoid Start and Exit at the same room
      while(exitX == startX && exitY == startY){
        exitX = random.Next(0, 4);
        exitY = random.Next(0, 4);
      }

      exitPosition[0] = exitX;
      exitPosition[1] = exitY;

      this.rooms[startX, startY] = "🚪";
    }
  }
}

public class Question{
  public string title;
  public Option option1;
  public Option option2;
  public Option option3;
  public Option option4;

  public Option[] options;

  public Question(string questionTitle, Option questionOption1, Option questionOption2, Option questionOption3, Option questionOption4){
    title = questionTitle;
    option1 = questionOption1;
    option2 = questionOption2;
    option3 = questionOption3;
    option4 = questionOption4;

    options = new Option[]{option1, option2, option3, option4};
  }

}

public class Option{
  public string title;
  public bool isCorrect;

  public Option(string optionTitle, bool isCorrectOption){
    title = optionTitle;
    isCorrect = isCorrectOption;
  }
}
