10.times do |i|
  begin
    puts "iteration #{i}"
    raise if i>2
  rescue
    retry
  end 
end
