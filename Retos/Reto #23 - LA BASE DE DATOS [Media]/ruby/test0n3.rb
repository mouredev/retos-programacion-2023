# frozen_string_literal: true

# to run this app, you require to install mysql2 gem
# gem install mysql2

require 'mysql2'

# class to get db content
class MoureDevDB
  attr_reader :db_host, :db_user, :db_name, :result
  attr_accessor :db_pass

  def initialize
    @db_host = 'mysql-5707.dinaserver.com'
    @db_user = 'mouredev_read'
    @db_name = 'moure_test'
    @db_pass = require_pass
    @result = connect_db
  end

  def access_db
    if @result.nil?
      puts "Can't connect to database"
      return
    end

    puts "id\tname\t\t\tdifficulty\tdate"
    @result.each(as: :array) do |row|
      puts row.join("\t")
    end
  end

  def connect_db
    begin
      connect = Mysql2::Client.new(host: @db_host, username: @db_user, password: @db_pass, database: @db_name)
      query_result = connect.query('SELECT * FROM challenges')
      connect.close
    rescue Mysql2::Error => _e
      query_result = nil
    end
    query_result
  end

  def require_pass
    puts "Type password for #{@db_user}@#{@db_host}: "
    gets.chomp
  end
end

MoureDevDB.new.access_db
