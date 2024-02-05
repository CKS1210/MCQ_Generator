## Workflows

## STEPS:
### 1. Login to the AWS: https://aws.amazon.com/console/
### 2. EC2
### 3. Configure Ubuntu Machine
### 4. Launch the instance
### 5. Update the Machine

```bash
sudo apt update

sudo apt-get update

sudo apt upgrade -y

sudo apt install git curl unzip tar make sudo vim wget -y

git clone "Your-repository"

sudo apt install python3-pip

pip3 install -r requirements.txt

python3 -m streamlit run StreamlitAPP.py
```
### 5. create the .env environment to keep the OpenAI API Key
```bash
touch .env 
```

### 6. checking the existance of this .env file (hidden file)
```bash
ls -a
```

### 7. Insert the OpenAI API Key
```bash
vi .env 
```
```bash
# press insert
```
```bash
copy paste the API key at there
```
```bash
type :wq and hit <enter>
```
