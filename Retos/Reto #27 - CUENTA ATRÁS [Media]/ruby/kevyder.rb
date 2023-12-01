# frozen_string_literal: true

def countdown(start, wait)
  return unless start.is_a?(Integer) && wait.is_a?(Integer) && start.positive? && wait.positive?

  (0..start).to_a.reverse_each do |n|
    puts n
    sleep wait
  end
end

countdown(10, 1)
countdown(-1, -1)
countdown('20', '1')
