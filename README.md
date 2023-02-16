# Test_Task 
Hello everyone! It is my first try to create application that will collect system info(RAM usage, CPU usage) and save it in database(in my case - MongoDB)
So who want to use my application, I wrote this small instruction. Let's start our journay.
## Instruments
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,docker,flask,git,mongodb" />
  </a>
</p>

### Installation
1. Clone code from repository
We will used UNIX-based system(Ubuntu 22.04), so if you have git on your machine, you'll write this commands. 
If you don't have GIT,you should install git [Install Git](https://github.com/git-guides/install-git)
```
cat /etc/os-release
pwd 
mkdir My_APP
cd My_APP
git clone https://github.com/Alkaponees/Test_Flask.git
```
2. Install Python, pip packet manager and flask
Now we will install python on our machine
```
sudo apt update
sudo apt install python3 -y
python3 --version
```
Okay, we installed Python. Then we can install pip and flask for working with app
```
sudo apt update
sudo apt install python3-pip
sudo apt install python3-flask
```
3. Install MongoDb
It's harder part our work. Therefore you should know how to use NoSQL databases. Let's install MongoDB.
I installed MongoDB 6.0 for local machine
3.1 Perform System Update
```
sudo apt update
sudo apt install wget curl gnupg2 software-properties-common apt-transport-https ca-certificates lsb-release -y
```
3.2  Import the public key
```
curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc|sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/mongodb-6.gpg
```
3.3 Configure MongoDB Repo
```
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu $(lsb_release -cs)/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```
3.4 Install MongoDB 6.0 on Ubuntu 22.04
```
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.16_amd64.deb
sudo dpkg -i ./libssl1.1_1.1.1f-1ubuntu2.16_amd64.deb
sudo apt update
sudo apt install mongodb-org -y
```
After successful installation, start and enable MongoDB:
```
sudo systemctl enable --now mongod
```
3.5 Using MongoDB 6.0 Database
```
mongosh
```
Detail info about install MongoDB on Ubuntu, you can read here --> [Install MongoDB](https://techviewleo.com/install-mongodb-on-ubuntu-linux/)
Congratulation, we installed all dependences for running our app

