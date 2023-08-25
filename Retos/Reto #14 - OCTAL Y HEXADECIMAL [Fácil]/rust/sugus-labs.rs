fn convert_decimal_to_other_systems(num_dec: u32) -> (String, String) {
        
    fn octal(num_dec: u32) -> String {

        let mut octal_vec: Vec<u32> = vec![];
        let mut quotient: u32 = 1;
        let mut remainder: u32 = 1;
        let mut num_dec = num_dec;
        while quotient != 0 {
            quotient = num_dec / 8;
            remainder = num_dec % 8;
            num_dec = quotient;
            // print(quotient)
            octal_vec.push(remainder);
        }
        octal_vec.reverse();
        let octal_str: String = octal_vec.into_iter().map(|i| i.to_string()).collect::<String>();
        return octal_str
    }

    fn hexa(num_dec: u32) -> String {
        let mut hexa_vec: Vec<String> = vec![];
        let mut quotient: u32 = 1;
        let mut remainder: u32 = 1;
        let mut num_dec = num_dec;
        while quotient != 0 {
            quotient = num_dec / 16;
            remainder = num_dec % 16;
            num_dec = quotient;
            // print(quotient)
            //hexa_vec.push(String::from(std::char::from_u32(remainder).unwrap()));
            hexa_vec.push(remainder.to_string());
        }        
        hexa_vec.reverse();
        let mut hexa_str: Vec<String> = vec![];
        for (num, s) in hexa_vec.iter().enumerate() {
            if *s == String::from("10") {
                hexa_str.push('A'.to_string());
            } else if *s == String::from("11") {
                hexa_str.push('B'.to_string());
            } else if *s == String::from("12") {
                hexa_str.push('C'.to_string());  
            } else if *s == String::from("13") {
                hexa_str.push('D'.to_string());
            } else if *s == String::from("14") {
                hexa_str.push('E'.to_string());    
            } else if *s == String::from("15") {
                hexa_str.push('F'.to_string());            
            } else {
                hexa_str.push((*s.clone()).to_string());
            }
        }
        let hexa_str: String = hexa_str.into_iter().map(|i| i).collect::<String>();
        return hexa_str
    }

    let num_octal = octal(num_dec);
    let num_hexa = hexa(num_dec);
    return (num_octal, num_hexa)

}

fn main() {

    let num_dec: u32 = 1353535;
    //let num_octal: u32;
    //let num_hexa: u32;    
    let result: (String, String) = convert_decimal_to_other_systems(num_dec);
    println!("Decimal number '{}' is:\n - octal: '{}'\n - hexa: '{}'", num_dec, result.0, result.1);
}