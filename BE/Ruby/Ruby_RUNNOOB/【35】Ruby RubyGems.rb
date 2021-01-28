
# Ruby RubyGems
# RubyGems 是 Ruby 的一个包管理器，它提供一个分发 Ruby 程序和库的标准格式，还提供一个管理程序包安装的工具。
#
# RubyGems 旨在方便地管理 gem 安装的工具，以及用于分发 gem 的服务器。这类似于 Ubuntu 下的apt-get, Centos 的 yum，Python 的 pip。
#
# RubyGems大约创建于2003年11月，从Ruby 1.9版起成为Ruby标准库的一部分。
#
# 如果你的 Ruby 低于 1.9 版本，也可以通过手动安装:
#
# 首先下载安装包：https://rubygems.org/pages/download。
# 解压并进入目录，执行命令：ruby setup.rb
# 更新 RubyGems 命令：
#
# $ gem update --system          # 需要管理员或root用户
# Gem
# Gem 是 Ruby 模块 (叫做 Gems) 的包管理器。其包含包信息，以及用于安装的文件。
#
# Gem通常是依照".gemspec"文件构建的，包含了有关Gem信息的YAML文件。Ruby代码也可以直接建立Gem，这种情况下通常利用Rake来进行。
#
# gem命令
# gem命令用于构建、上传、下载以及安装Gem包。
#
# gem用法
# RubyGems 在功能上与 apt-get、portage、yum 和 npm 非常相似。
#
# 安装：
#
# gem install mygem
# 卸载：
#
# gem uninstall mygem
# 列出已安装的gem：
#
# gem list --local
# 列出可用的gem，例如：
#
# gem list --remote
# 为所有的gems创建RDoc文档：
#
# gem rdoc --all
# 下载一个gem，但不安装：
#
# gem fetch mygem
# 从可用的gem中搜索，例如：
#
# gem search STRING --remote
# gem 包的构建
# gem命令也被用来构建和维护.gemspec和.gem文件。
#
# 利用.gemspec文件构建.gem：
#
# gem build mygem.gemspec
# 修改国内源
# 由于国内网络原因（你懂的），导致 rubygems.org 存放在 Amazon S3 上面的资源文件间歇性连接失败。
#
# 所以你会与遇到 gem install rack 或 bundle install 的时候半天没有响应，具体可以用 gem install rails -V 来查看执行过程。
#
# 因此我们可以将它修改为国内的下载源: https://gems.ruby-china.com
# 首先，查看当前源：
#
# $ gem sources -l
# *** CURRENT SOURCES ***
#
# https://rubygems.org/
# 接着，移除 https://rubygems.org/，并添加国内下载源 https://gems.ruby-china.com/。
#
# $ gem sources --remove https://rubygems.org/
# $ gem sources -a https://gems.ruby-china.com/
# $ gem sources -l
# *** CURRENT SOURCES ***
#
# https://gems.ruby-china.com/
# # 请确保只有 gems.ruby-china.com
# $ gem install rails
# 如果你使用 Gemfile 和 Bundle (例如：Rails 项目)
# 你可以用bundle的gem源代码镜像命令。
#
# $ bundle config mirror.https://rubygems.org https://gems.ruby-china.com/
# 这样你不用改你的 Gemfile 的 source。
#
# source 'https://rubygems.org/'
# gem 'rails', '4.1.0'
# ...
