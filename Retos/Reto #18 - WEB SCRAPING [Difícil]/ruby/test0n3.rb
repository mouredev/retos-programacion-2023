# Ruby app, requires to have installed the following gems:
# - URI
# - net/http
# - nokogiri

# frozen_string_literal: true

require 'uri'
require 'net/http'
require 'nokogiri'

# class GetSchedule, get on date schedule
class ScheduleHolaMundoDay
  HOLAMUNDO_URL = 'https://holamundo.day/'

  def pick_data
    uri = URI(HOLAMUNDO_URL)
    res = Net::HTTP.get_response(uri)
    show_schedule(res.body) if res.is_a?(Net::HTTPSuccess)
  end

  def show_schedule(response)
    doc = Nokogiri::HTML(response)
    schedules = find_schedules(doc)[0]

    clean_html_snip(schedules).drop(8).map(&:content)
  end

  private

  def find_schedules(html_body)
    html_body.css('article.notion-page-content-inner').select do |article|
      article.content.downcase.match?(/(agenda 8 de mayo)/)
    end
  end

  def clean_html_snip(html_snip)
    html_snip.children.select { |elem| elem.name == 'h1' || elem.name == 'blockquote' }
  end
end

puts ScheduleHolaMundoDay.new.pick_data
