for ($i=0; $i < 101; $i++) {
    echo (is_int($i/3) && is_int($i/5) && ($i != 0) ? 'fizzbuzz' : (is_int($i/3) && ($i != 0) ? 'fizz' : (is_int($i/5) && ($i != 0) ? 'buzz' : $i))). '</br>';
}
