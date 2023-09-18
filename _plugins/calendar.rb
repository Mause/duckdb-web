# frozen_string_literal: true

require 'json'
require 'jekyll'
require 'net/http'
require 'time'

DAY_IN_SECONDS = 60 * 60 * 24

def format_time(event)
  start = event['start']['date']
  end_date = event['end']['date']

  if Time.parse(end_date) == (Time.parse(start) + DAY_IN_SECONDS)
    start
  else
    "#{start} - #{end_date}"
  end
end


module Jekyll
  class CalendarTag < Liquid::Tag
    def initialize(tag_name, text, tokens)
      @historical = eval text
      super
    end

    def render(context)
      site = context.registers[:site]
      page = context.registers[:page]
      @converter = site.find_converter_instance(::Jekyll::Converters::Markdown)

      uri = URI('https://clients6.google.com/calendar/v3/calendars/c_rqj60henfnuin5klbati6g9kfg@group.calendar.google.com/events')
      params = {
        :calendarId => 'c_rqj60henfnuin5klbati6g9kfg@group.calendar.google.com',
        :singleEvents => true,
        :timeZone => 'Europe/Amsterdam',
        :sanitizeHtml => true,
        :key => 'AIzaSyBNlYH01_9Hc5S1J9vuFmu2nUqBZJNAXxs'
      }
      params[:timeMin] = Time.now.iso8601 unless @historical

      uri.query = URI.encode_www_form(params)
      cal = JSON.parse Net::HTTP.get(uri)

      puts "items: historical: #{@historical}"

      items = cal['items'].reverse.map do |item|
        "<li>#{format_time(item)} - #{item['summary']}</li>"
      end.join("")

      "<ul>#{items}</ul>"
    end
  end
end

Liquid::Template.register_tag('calendar', Jekyll::CalendarTag)
