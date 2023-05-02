# frozen_string_literal: true

require 'uri'
require 'net/http'
require 'nokogiri'

# class GetSchedule, get on date schedule
class GetSchedule
  HOLAMUNDO_URL = 'https://holamundo.day/'

  def pick_data
    uri = URI(HOLAMUNDO_URL)
    res = Net::HTTP.get_response(uri)
    print_schedule(res.body) if res.is_a?(Net::HTTPSuccess)
  end

  def print_schedule(response)
    doc = Nokogiri::HTML(response)
    schedule = find_schedules(doc)[0]

    clean_html_snip(schedule).drop(8).map(&:content)
  end

  def find_schedules(html_body)
    html_body.css('article.notion-page-content-inner').select do |article|
      article.content.downcase.match?(/(agenda 8 de mayo)/)
    end
  end

  def clean_html_snip(html_snip)
    html_snip.children.select { |elem| elem.name == 'h1' || elem.name == 'blockquote' }
  end
end

puts GetSchedule.new.pick_data
