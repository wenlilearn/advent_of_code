def find_indexes(input)
  first, last = nil, nil
  input.chars.each_with_index do |c, i|
    next unless c =~ /\d/

    first = i if first.nil?
    last = i
  end

  return [first, last]
end

words2digits = {
  'one' => 1,
  'onne' => 1,
  'two' => 2,
  'three' => 3,
  'four' => 4,
  'foour' => 4,
  'five' => 5,
  'six' => 6,
  'seven' => 7,
  'seeveen' => 7,
  'eight' => 8,
  'nine' => 9,
  'ninne' => 9
}

sum = 0
inputs.each do |input|
  input.gsub!('e', 'ee')
  input.gsub!('t', 'tt')
  input.gsub!('n', 'nn')
  input.gsub!('o', 'oo')
  words2digits.each do |word, digit|
    input.gsub!(word, digit.to_s)
  end

  first_index, last_index = find_indexes(input)
  sum += (input[first_index] + input[last_index]).to_i
end
puts sum
