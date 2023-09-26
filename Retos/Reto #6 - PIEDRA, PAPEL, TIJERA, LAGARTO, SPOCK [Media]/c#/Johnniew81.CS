namespace PPRLS
{

  class Program
  {
    public static void Main(string[] args)
    {
      string[] Game1 = { "🖐️", "✌️", "✌️" };
      players player_one = new players(Game1);

      string[] Game2 = { "🖐️", "✌️", "✌️" };
      players player_two = new players(Game2);

      Dictionary<string, (string, string)> rule = new Dictionary<string, (string, string)>()
            {
                { "✌️", ("🖐️","🦎") },
                { "🖐️", ("👊","🖖") },
                { "👊", ("🦎","✌️") },
                { "🦎", ("🖖","🖐️") },
                { "🖖", ("✌️","👊") }
            };
      Console.WriteLine(rock_peper_scissor_lizard_spock(player_one.Game, player_two.Game));

      string rock_peper_scissor_lizard_spock(string[] player_one, string[] player_two)
      {
        int one = 0, two = 0;

        for (int i = 0; i < player_one.Length; i++)
        {
          if (player_one[i] != player_two[i])
          {
            string valor1 = rule[player_one[i]].Item1;
            string valor2 = rule[player_one[i]].Item2;
            one += (comprovacion(valor1, valor2, player_two[i])) ? 1 : 0;
            two += (comprovacion(valor1, valor2, player_two[i])) ? 0 : 1;
          }
        }
        return (one > two) ? "Player 1" : (one < two) ? "Player 2" : "Empate";
      }
      bool comprovacion(string valor1, string valor2, string dato)
      {
        bool result = (dato == valor1 || dato == valor2) ? true : false;
        return result;
      }
    }
  }

  public class players
  {
    public string[] Game { get; set; }

    public players(string[] game)
    {
      Game = game;
    }
  }
}