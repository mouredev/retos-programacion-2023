#!/bin/sh

url="https://api.github.com/repos/mouredev/retos-programacion-2023/commits"

curl -s $url | jq -n \
    '[inputs | limit(10; .[])] |.[] | {sha: .sha, author_name: .commit.author.name, message: .commit.message,author_date: .commit.author.date}'