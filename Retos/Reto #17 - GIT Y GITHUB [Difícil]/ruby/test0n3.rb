# frozen_string_literal: true

require 'uri'
require 'net/http'
require 'json'
require 'time'

# class GetAPI
class GetAPI
  MOUREDEV_GITHUB = 'https://api.github.com/repos/mouredev/retos-programacion-2023/commits'

  def pick_commits
    uri = URI(MOUREDEV_GITHUB)
    res = Net::HTTP.get_response(uri)
    print_api_resp(JSON.parse(res.body).first(10)) if res.is_a?(Net::HTTPSuccess)
  end

  def print_api_resp(commits)
    commits.map.with_index do |commit, index|
      hash = commit['sha'][0, 6]
      author = commit['author'].nil? ? commit['commit']['author']['name'] : commit['author']['login']
      message = commit['commit']['message'].gsub(/\n\n/, ' - ')
      date = Time.parse(commit['commit']['author']['date']).localtime.strftime('%d/%m/%Y %H:%M:%S')
      "Commit #{index + 1} | #{hash} | #{author} | #{message} | #{date}"
    end
  end
end

puts GetAPI.new.pick_commits
