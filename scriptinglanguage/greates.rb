print "enter the value of x:"
x=gets.to_i
print "enter the value of y:"
y=gets.to_i
print "enter the value of z:"
z = gets.to_i
if x>= y and x>= z
       puts "x = #{x} is the greatest no."
elseif y>=z and y>= x
       puts "y=#{y} is greatest no."
else 
       puts "z is greater"
end