package com.retos.ej23;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class jorgenavarroenamoradotokio {

	private static final String DB_URL = "jdbc:mysql://mysql-5707.dinaserver.com:3306/moure_test";
	private static final String DB_USER = "mouredev_read";
	private static final String DB_PASSWORD = "mouredev_pass";

	public static void main(String[] args) {
		
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");
			Connection conexion = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);

			String strSql = "SELECT COUNT(*) as total FROM challenges";
			Statement statement = conexion.createStatement();
			ResultSet rs = statement.executeQuery(strSql);

			if (rs.next()) {
				System.out.println(rs.getString("total"));
			}
			
			rs.close();
            statement.close();
            conexion.close();
		} catch (ClassNotFoundException | SQLException e) {
			e.printStackTrace();
		}
	}
}
