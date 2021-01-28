
# 创建 Ruby 线程
# 要启动一个新的线程，只需要调用 Thread.new 即可:
#
# # 线程 #1 代码部分
# Thread.new {
#   # 线程 #2 执行代码
# }
# # 线程 #1 执行代码
#
#!/usr/bin/ruby

def func1
  i=0
  while i<=2
    puts "func1 at: #{Time.now}"
    sleep(2)
    i=i+1
  end
end

def func2
  j=0
  while j<=2
    puts "func2 at: #{Time.now}"
    sleep(1)
    j=j+1
  end
end

puts "Started At #{Time.now}"
t1=Thread.new{func1()}
t2=Thread.new{func2()}
t1.join
t2.join
puts "End at #{Time.now}"
sleep 1

# TODO 通过Mutex类实现线程同步
require "thread"
puts "Synchronize Thread"

@num=200
@mutex=Mutex.new

def buyTicket(num)
  @mutex.lock
  if @num>=num
    @num=@num-num
    puts "you have successfully bought #{num} tickets"
  else
    puts "sorry,no enough tickets"
  end
  @mutex.unlock
end

ticket1=Thread.new 10 do
  10.times do |value|
    ticketNum=15
    buyTicket(ticketNum)
    sleep 0.01
  end
end

ticket2=Thread.new 10 do
  10.times do |value|
    ticketNum=20
    buyTicket(ticketNum)
    sleep 0.01
  end
end

sleep 1
ticket1.join
ticket2.join
sleep 2

# TODO 监管数据交接的Queue类实现线程同步
# Queue类就是表示一个支持线程的队列，能够同步对队列末尾进行访问。不同的线程可以使用统一个对类，但是不用担心这个队列中的数据是否能够同步，另外使用SizedQueue类能够限制队列的长度
# SizedQueue类能够非常便捷的帮助我们开发线程同步的应用程序，应为只要加入到这个队列中，就不用关心线程的同步问题。
# 经典的生产者消费者问题：
puts "SizedQuee Test"

queue = Queue.new

producer = Thread.new do
  10.times do |i|
    sleep rand(i) # 让线程睡眠一段时间
    queue << i
    puts "#{i} produced"
  end
end

consumer = Thread.new do
  10.times do |i|
    value = queue.pop
    sleep rand(i/2)
    puts "consumed #{value}"
  end
end

consumer.join
sleep 1

# TODO 线程变量
# 线程可以有其私有变量，线程的私有变量在线程创建的时候写入线程。可以被线程范围内使用，但是不能被线程外部进行共享。
# 但是有时候，线程的局部变量需要别别的线程或者主线程访问怎么办？ruby当中提供了允许通过名字来创建线程变量，类似的把线程看做hash式的散列表。
# 通过[]=写入并通过[]读出数据。我们来看一下下面的代码：
count = 0
arr = []

10.times do |i|
  arr[i] = Thread.new {
    sleep(rand(0)/10.0)
    Thread.current["mycount"] = count
    count += 1
  }
end

arr.each {|t| t.join; print t["mycount"], ", " }
puts "count = #{count}"



# TODO 线程互斥
# Mutex(Mutal Exclusion = 互斥锁)是一种用于多线程编程中，防止两条线程同时对同一公共资源（比如全局变量）进行读写的机制。
# TODO 不互斥
count1 = count2 = 0
difference = 0
counter = Thread.new do
  loop do
    count1 += 1
    count2 += 1
  end
end
spy = Thread.new do
  loop do
    difference += (count1 - count2).abs
  end
end
sleep 1
puts "count1 :  #{count1}"
puts "count2 :  #{count2}"
puts "difference : #{difference}"
# 以上实例运行输出结果为：
#
# count1 :  9712487
# count2 :  12501239
# difference : 0

# TODO 使用 mutex 的实例
mutex = Mutex.new

count1 = count2 = 0
difference = 0
counter = Thread.new do
  loop do
    mutex.synchronize do
      count1 += 1
      count2 += 1
    end
  end
end
spy = Thread.new do
  loop do
    mutex.synchronize do
      difference += (count1 - count2).abs
    end
  end
end
sleep 1
mutex.lock
puts "count1 :  #{count1}"
puts "count2 :  #{count2}"
puts "difference : #{difference}"
# 以上实例运行输出结果为：
#
# count1 :  1336406
# count2 :  1336406
# difference : 0

# TODO 死锁
# 两个以上的运算单元，双方都在等待对方停止运行，以获取系统资源，但是没有一方提前退出时，这种状况，就称为死锁。
# 例如，一个进程 p1占用了显示器，同时又必须使用打印机，而打印机被进程p2占用，p2又必须使用显示器，这样就形成了死锁。
# 当我们在使用 Mutex 对象时需要注意线程死锁。
mutex = Mutex.new

cv = ConditionVariable.new
a = Thread.new {
  mutex.synchronize {
    puts "A: I have critical section, but will wait for cv"
    cv.wait(mutex)
    puts "A: I have critical section again! I rule!"
  }
}

puts "(Later, back at the ranch...)"

b = Thread.new {
  mutex.synchronize {
    puts "B: Now I am critical, but am done with cv"
    cv.signal
    puts "B: I am still critical, finishing up"
  }
}
a.join
b.join
# 以上实例输出结果为：
#
# A: I have critical section, but will wait for cv
# (Later, back at the ranch...)
# B: Now I am critical, but am done with cv
# B: I am still critical, finishing up
# A: I have critical section again! I rule!
