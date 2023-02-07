class HelloWorld: Object {
	private uint year = 0;
	
	public HelloWorld () {
	}
	
	public HelloWorld.with_year (int year) {
		if (year>0)
			this.year = year;
	}

	public void greeting () {
		if (year == 0)
			print ("Hello World\n");
		else
			/* Strings prefixed with '@' are string templates. */
			print (@"Hello World, $(this.year)\n"); 
	}
}

void main (string[] args) {
	var helloworld = new HelloWorld.with_year (2021);
	helloworld.greeting ();
}