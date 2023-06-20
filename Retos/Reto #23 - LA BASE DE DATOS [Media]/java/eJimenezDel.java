import java.sql.Connection;
import java.sql.Date;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.text.MessageFormat;
import java.util.ArrayList;
import java.util.List;

public class eJimenezDel {
	
	private final String DB="moure_test";
    private final String URL="jdbc:mysql://mysql-5707.dinaserver.com:3306/"+DB+"?serverTimezone=UTC";
    private final String USER="mouredev_read";
    private final String PASS="mouredev_pass";

	public static void main(String[] args) {
		eJimenezDel reto23eJimenez = new eJimenezDel();		
		
	    reto23eJimenez.printTable(reto23eJimenez.getChallenges());    
                 
		    
    }
	
	private void printTable(List<Challenge>lista) {
		lista.forEach(challenge-> {
			System.out.println(MessageFormat.format("| {0} | {1} | {2} | {3} |", 
					challenge.getId(), challenge.getName(), challenge.getDifficulty(),challenge.getDate()).toString());
			
		});
	}
	
	
    
    public List<Challenge> getChallenges() {       
        
        List<Challenge> challenges = new ArrayList<Challenge>();
        try(Connection connection = DriverManager.getConnection(URL,USER,PASS)){
        	
        	try(Statement statement = connection.createStatement()){
        		
        		try(ResultSet resultSet = statement.executeQuery("SELECT * FROM challenges")){
        			while(resultSet.next()){
        				
                        int id = resultSet.getInt("id");
                        String challengeName = resultSet.getString("name"); 
                        String challengeDifficulty = resultSet.getString("difficulty");
                        Date challengeDate = resultSet.getDate("date");
                        Challenge challenge = new Challenge();
                        challenge.setId(id);
                        challenge.setName(challengeName);
                        challenge.setDifficulty(challengeDifficulty);     
                        challenge.setDate(challengeDate);
                        
						challenges.add(challenge);
                        
                    }        			
        		}        		
        	}           
            
        }catch( SQLException ex){
            System.out.println("error "+ex.getMessage());
            return new ArrayList<Challenge>();
        }
		return challenges;
        
    }    
    
	
}

class Challenge{
	private int id;
	private String name;
	private String difficulty;
	private Date date;
	public String getDifficulty() {
		return difficulty;
	}
	public void setDifficulty(String description) {
		this.difficulty = description;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public Date getDate() {
		return date;
	}
	public void setDate(Date date) {
		this.date = date;
	}
	
}
