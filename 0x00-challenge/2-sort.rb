integers = []
ARGV.each do |arg|
  # skip if not integer
  next unless arg =~ /^-?[0-9]+$/

  # convert to integer and add to the list
  integers << arg.to_i
end

# sort the integers in ascending order
sorted_integers = integers.sort

# print the sorted integers
puts sorted_integers
