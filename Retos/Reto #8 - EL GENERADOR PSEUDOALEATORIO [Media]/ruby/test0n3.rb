# frozen_string_literal: true

# class random number generator
class RandomNumberGenerator
  def gen_random_with_epoc
    lehmer_generator(Time.now.to_i) % 101
  end

  def lehmer_generator(seed)
    100.times do |_|
      seed = (seed * 48_271) % 2**31 - 1
    end
    seed
  end
end

p "data: #{RandomNumberGenerator.new.gen_random_with_epoc}"
