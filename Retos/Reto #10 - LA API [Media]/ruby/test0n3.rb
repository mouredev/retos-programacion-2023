# frozen_string_literal: true

# APIs source: https://github.com/public-apis/public-apis
# source: https://www.twilio.com/blog/5-ways-make-http-requests-ruby

require 'uri'
require 'net/http'

# class GetAPI with random selection of APIs
class GetAPI
  URL = { 0 => { 'title' => 'Cats API', 'url' => 'https://cat-fact.herokuapp.com/facts' },
          1 => { 'title' => 'Fish API', 'url' => 'https://www.fishwatch.gov/api/species' },
          2 => { 'title' => 'Bored API', 'url' => 'https://www.boredapi.com/api/activity/' } }.freeze

  def start
    @selected_api = choose_api
    @selected_url = @selected_api['url']
    @selected_title = @selected_api['title']
    print_api_resp
  end

  def print_api_resp
    # puts "title: #{@selected_title}, url: #{@selected_url}"
    uri = URI(@selected_url)
    res = Net::HTTP.get_response(uri)
    puts "API name #{@selected_title}"
    puts res.body if res.is_a?(Net::HTTPSuccess)
  end

  def choose_api
    URL[URL.keys.sample]
  end
end

GetAPI.new.start
