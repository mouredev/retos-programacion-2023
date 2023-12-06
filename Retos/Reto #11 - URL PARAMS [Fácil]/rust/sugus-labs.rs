fn extract_params(url: &str) -> (Vec<String>, Vec<(String, String)>) {
    
    let mut params_vec: Vec<(String, String)> = vec![];
    let mut values_vec: Vec<String> = vec![];
    let mut param_name: String = String::from(" ");
    let mut param_value: String = String::from(" ");
    let mut tup: (String, String);

    let mixed_params = url.split("?");
    for (num, param) in mixed_params.enumerate() {
        if num == 1 {
            let mixed_params_sep = param.split("&");
            for param_sep in mixed_params_sep {
                let param_vals = param_sep.split("=");
                for (num, elem) in param_vals.enumerate() {
                    if num == 0 {
                        param_name = elem.to_string();
                    } else {
                        param_value = elem.to_string();   
                    }
                }
                values_vec.push(param_value.clone());
                tup = (param_name.clone(), param_value.clone());
                params_vec.push(tup);
            }  
        }
    }

    return (values_vec, params_vec)
}

fn main() {

    let url: String = String::from("https://retosdeprogramacion.com?year=2023&challenge=0");
    let result = extract_params(&url);
//    params_values = list(params_dict.values())
    println!("{:?}", result.1);
    println!("{:?}", result.0);
//    print(params_values)    

}