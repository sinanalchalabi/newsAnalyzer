##Log Analyzer
This is a tool use to analysis a database for a news site
and print back reports about it, including:
**.**Top three Articles.
**.**Top Authors.
**.**Dates with error percent higher than 1%

###Requirement
This code run under Terminal using Vagrant
with virtual machine with Postgresql.

####Terminal
If you are using a Mac or Linux system,
your regular terminal program will do just fine. 
On Windows, we recommend using the Git Bash
terminal that comes with the Git software. 
If you don't already have Git installed,
download Git from git-scm.com.

####Installing the Virtual Machine
We'll use a virtual machine (VM)
to run an SQL database server and a web app that uses it. 
The VM is a Linux server system that runs on top of your own computer. 
You can share files easily between your computer and the VM; 
and you'll be running a web service inside the VM
which you'll be able to access from your regular browser.
We're using tools called Vagrant and VirtualBox to install and manage the VM.

####Install VirtualBox
VirtualBox is the software that actually runs the virtual machine.
You can download it from virtualbox.org.
Install the platform package for your operating system.
You do not need the extension pack or the SDK. 
You do not need to launch VirtualBox after installing it;
Vagrant will do that.

####Install Vagrant
Vagrant is the software that configures the VM and lets you share files
between your host computer and the VM's filesystem.
Download it from vagrantup.com. 
Install the version for your operating system.
Windows users: The Installer may ask you to grant network permissions
to Vagrant or make a firewall exception. Be sure to allow this.

####Download the VM configuration
There are a couple of different ways you can download the VM configuration.
You can download and unzip this file: FSND-Virtual-Machine.zip 
This will give you a directory called FSND-Virtual-Machine.
It may be located inside your Downloads folder.
Alternately, you can use Github to fork and clone the repository:
https://github.com/udacity/fullstack-nanodegree-vm.
Either way, you will end up with a new directory containing the VM files.
Change to this directory in your terminal with cd.
Inside, you will find another directory called vagrant.
Change directory to the vagrant directory.

#####Start the virtual machine
From your terminal, inside the vagrant subdirectory,
run the command vagrant up.
This will cause Vagrant to download the 
Linux operating system and install it.
This may take quite a while (many minutes)
depending on how fast your Internet connection is.
When vagrant up is finished running, you will get your shell prompt back.
At this point, you can run vagrant ssh to log in
to your newly installed Linux VM

####Download the data
Next, download the data from:
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
You will need to unzip this file after downloading it.
The file inside is called newsdata.sql.
Put this file into the vagrant directory,
which is shared with your virtual machine.
To load the data, cd into the vagrant directory
and use the command `psql -d news -f newsdata.sql`.
Here's what this command does:
psql — the PostgreSQL command line program
-d news — connect to the database named news which has been set up for you
-f newsdata.sql — run the SQL statements in the file newsdata.sql
Running this command will connect to your installed database server and
execute the SQL commands in the downloaded file,
creating tables and populating them with data.

####Creating required Views
Some Views are created to help this tool
so this need to be installed before using the tool
**.**Popular Articles View to collect most populer articles using this query:
`create view populararticle as \
 select articles.slug,count(log.path) as num \
 from articles,log \
 where log.path = concat ('/article/',articles.slug) \
 group by articles.slug \
 order by num desc;`
**.**WrongPages to calculate error requestes per day using this query:
`create view wrongpage as \
 select time::DATE,count(time::DATE) as num \
 from log \
 where status!='200 OK' \
 group by time::DATE \
 order by time::DATE;`
**.**Totalpage to calculate total requestes per day using this query:
`create view totalpage as \
 select time::DATE,count(time::DATE) as num \
 from log \
 group by time::DATE \
 order by time::DATE;`
**You can easily create these Views by running the code:
 file in terminal:`python view.py`**

###Usage
After compeleting the requirements,
you can easily run the code in new terminal:
`python news.py`
to get the required results.

###Deployment
This work is done using Python DB-API
Firstly connect to the database then apply the required queries
for each question and fetch the results and print it out.
each query use different clues to reach the results,
also some views are used to get the results.
###Author
**Sinan AlChalabi** - IT Manager - AlMadar ISP

###License
It is a free to use and redistribute.