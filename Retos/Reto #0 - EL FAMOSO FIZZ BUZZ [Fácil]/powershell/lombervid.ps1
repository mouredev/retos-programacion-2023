#!/usr/bin/env pwsh

for ($i = 1; $i -le 100; $i++) {
    if ($i % 3 -eq 0) {
        Write-Host $(($i % 5 -eq 0) ? "fizzbuzz" : "fizz")
        continue
    }
    Write-Host $(($i % 5 -eq 0) ? "buzz" : $i)
}
